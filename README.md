# Blackjack Multiplayer em Python

## Descrição
Este projeto é uma implementação simples de um jogo de **Blackjack** multiplayer utilizando **Python** e **sockets TCP** para conexão entre servidor e clientes. Dois jogadores podem se conectar ao servidor, fazer apostas e jogar contra o dealer.

## Tecnologias Utilizadas
- **Python**
- **Sockets TCP/IP**
- **Programação Orientada a Eventos**

## Como Funciona
- O servidor aguarda conexão de dois jogadores.
- Cada jogador começa com um saldo inicial de **100**.
- Os jogadores fazem suas apostas antes de cada rodada.
- O jogo segue as regras padrão do Blackjack:
  - Cartas de **2 a 10** valem seu próprio número.
  - **J, Q, K** valem **10** pontos.
  - **A (As)** vale **11**, mas pode ser **1** se o jogador estourar 21.
- Os jogadores decidem se pedem mais cartas (**hit**) ou se mantêm a mão (**stand**).
- O dealer segue as regras padrão e joga após os jogadores.
- O saldo é atualizado conforme o resultado da rodada.
- Os jogadores podem decidir se querem continuar jogando ou sair.

## Estrutura do Projeto
O projeto está dividido em dois arquivos principais:
- **servidor.py**: Responsável por gerenciar as conexões e a lógica do jogo.
- **cliente.py**: Interface do jogador para interagir com o servidor.

## Como Executar
1. Clone este repositório:
   ```sh
   git clone https://github.com/Pglopess/blackjack-multiplayer.git
   cd blackjack-multiplayer
   ```
2. Execute o servidor primeiro:
   ```sh
   python servidor.py
   ```
3. Em outra janela de terminal, execute dois clientes:
   ```sh
   python cliente.py
   ```
   E repita para um segundo cliente.
4. Siga as instruções no terminal para jogar.

## Melhorias Futuras
- Adicionar uma interface gráfica (GUI) para melhor experiência do jogador.
- Implementar mais regras do jogo para torná-lo mais realista.
- Permitir mais de dois jogadores por partida.

## Contribuição
Sinta-se à vontade para sugerir melhorias ou fazer um **fork** do repositório. Feedbacks são sempre bem-vindos! :smiley:

## Autor
[Pedro Gustavo Thomas](https://www.linkedin.com/in/pedro-gustavo-thomas-5935392b7)

