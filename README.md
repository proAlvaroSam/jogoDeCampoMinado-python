# 💣 Campo Minado

Este projeto em Python implementa um jogo de Campo Minado. O objetivo do jogo é revelar todas as células seguras sem acertar as minas espalhadas pelo campo.

## 🚀 Funcionalidades

### Criação do Campo
- O campo de jogo é criado com um tamanho específico e um número determinado de minas.
- As minas são posicionadas aleatoriamente no campo.
- As células adjacentes às minas são atualizadas com números que indicam a quantidade de minas nas proximidades.

### Exibição do Campo
- O campo é exibido de forma que apenas as células reveladas pelo jogador sejam visíveis.
- As células não reveladas são representadas por um ponto (".").
- As minas são representadas por um asterisco ("*") quando reveladas.

### Revelação de Células
- O jogador pode escolher revelar uma célula específica no campo.
- Se a célula escolhida for uma mina, o jogo termina com "Game Over".
- Se a célula escolhida for vazia (0), todas as células adjacentes vazias também são reveladas automaticamente.
- Se a célula escolhida contiver um número, apenas essa célula é revelada.

### Condição de Vitória
- O jogador vence o jogo se todas as células seguras forem reveladas sem acertar nenhuma mina.

### Ainda tenho muito o que melhorar nesse código

