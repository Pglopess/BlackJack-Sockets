# Blackjack Multiplayer via Sockets

Jogo de Blackjack para dois jogadores em rede, com comunicação via sockets TCP em Python.

## Sobre

O servidor gerencia a lógica do jogo e se comunica com dois clientes conectados simultaneamente. Cada jogador recebe cartas, decide suas jogadas e aposta parte do saldo. O dealer joga automaticamente seguindo a regra de parar em 17 ou mais.

## Funcionalidades

- Partida entre dois jogadores conectados via rede
- Dealer automático (para em 17+)
- Mecânica do Ás (vale 11 ou 1, conforme necessário)
- Sistema de apostas com saldo inicial de 100 fichas
- Rodadas contínuas até os jogadores decidirem sair

## Tecnologias

- Python (socket, random)

## Como executar

**1. Inicie o servidor:**
```bash
python servidor.py
```

**2. Em dois terminais diferentes, conecte os clientes:**
```bash
python cliente.py
```

O servidor aguarda os dois clientes antes de iniciar o jogo.

## Estrutura do projeto

```
├── servidor.py   # Lógica do jogo, dealer e comunicação com os clientes
└── cliente.py    # Interface do jogador via terminal
```

## Conceitos praticados

- Comunicação em rede com sockets TCP
- Arquitetura cliente-servidor
- Lógica de jogo (Blackjack)
- Programação com múltiplas conexões simultâneas
