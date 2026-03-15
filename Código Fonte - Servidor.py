import socket
import random

# Função que gera cartas aleatórias (apenas os valores numéricos)
def gerar_carta():
    carta = random.randint(1, 13)
    return 10 if carta > 10 else (11 if carta == 1 else carta)

# Função que calcula o valor total das cartas dos jogadores (com a mecânica do Ás)
def calcular_total(cartas):
    total = sum(cartas)
    num_ases = cartas.count(11)
    
    while total > 21 and num_ases > 0:
        total -= 10  # Converte um Ás de 11 para 1
        num_ases -= 1

    return total

# Configuração do servidor
host = '127.0.0.1'  
port = 12345  

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((host, port))
servidor.listen(2)

print("Aguardando dois jogadores...")

# Aceitando a conexão dos jogadores
cliente1, addr1 = servidor.accept()
print(f"Jogador 1 conectado: {addr1}")

cliente2, addr2 = servidor.accept()
print(f"Jogador 2 conectado: {addr2}")

# Saldo inicial dos jogadores
saldos = {cliente1: 100, cliente2: 100}

def enviar_para_ambos(mensagem):
    cliente1.send(mensagem.encode())
    cliente2.send(mensagem.encode())

def jogar_como_dealer():
    cartas = [gerar_carta(), gerar_carta()]
    while calcular_total(cartas) < 17:
        cartas.append(gerar_carta())
    return cartas, calcular_total(cartas)

def rodada_jogador(cliente):
    cartas = [gerar_carta(), gerar_carta()]
    cliente.send(f"Suas cartas iniciais: {cartas}, total: {calcular_total(cartas)}\n".encode())
    
    while calcular_total(cartas) < 21:
        cliente.send("Deseja pedir mais uma carta (h) ou parar (s)?\n".encode())
        resposta = cliente.recv(1024).decode().strip().lower()

        if resposta == 'h':
            cartas.append(gerar_carta())
            total = calcular_total(cartas)
            cliente.send(f"Suas cartas: {cartas}, total: {total}\n".encode())

            if total > 21:
                cliente.send("Você estourou!\n".encode())
                break
        else:
            break

    return cartas, calcular_total(cartas)

while True:
    enviar_para_ambos("\n=== Nova rodada de Blackjack ===\n")

    for cliente in [cliente1, cliente2]:
        cliente.send(f"Seu saldo: {saldos[cliente]}\n".encode())
        cliente.send("Quanto deseja apostar?\n".encode())
        aposta = int(cliente.recv(1024).decode().strip())
        if aposta > saldos[cliente]:
            aposta = saldos[cliente]  # Garante que o jogador não aposte mais do que tem
        saldos[cliente] -= aposta

    cartas_dealer, total_dealer = jogar_como_dealer()
    enviar_para_ambos(f"Dealer mostra: {cartas_dealer[0]}\n")

    resultados = []
    for cliente in [cliente1, cliente2]:
        cartas, total = rodada_jogador(cliente)
        resultados.append((cliente, cartas, total))

    enviar_para_ambos(f"\nCartas do Dealer: {cartas_dealer}, total: {total_dealer}\n")

    for cliente, cartas, total in resultados:
        if total > 21:
            cliente.send("Você perdeu!\n".encode())
        elif total_dealer > 21 or total > total_dealer:
            ganho = aposta * 2
            saldos[cliente] += ganho
            cliente.send(f"Você venceu! Ganhou {ganho}.\n".encode())
        else:
            cliente.send("Você perdeu para o Dealer.\n".encode())

    enviar_para_ambos("Desejam continuar jogando? (s/n)\n")
    if cliente1.recv(1024).decode().strip().lower() != 's' or cliente2.recv(1024).decode().strip().lower() != 's':
        break

cliente1.close()
cliente2.close()
servidor.close()
