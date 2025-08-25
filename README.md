# Projeto de Integração e Interpolação Numérica

Este projeto calcula a área de uma região definida por pontos usando interpolação linear e integração numérica pelo método de Simpson. Os pontos são lidos de um arquivo CSV e a área calculada é comparada com o valor fornecido pelo Google Maps.

## Estrutura do Projeto

- `main.py`: Script principal que realiza a leitura dos pontos, interpolação, integração e exibe os resultados.
- `points.csv`: Arquivo contendo os pontos (x, y) delimitando a região.

## Como Executar

1. Certifique-se de ter o Python 3 e o pacote `numpy` instalado.
2. Execute o script principal:

```sh
python main.py
```

## Funcionamento

- Os pontos do arquivo `points.csv` são lidos e usados para interpolar segmentos de reta.
- Cada segmento é integrado numericamente usando o método de Simpson.
- A soma das áreas dos segmentos fornece a área total aproximada.
- O resultado é comparado com a área real fornecida pelo Google Maps.

## Saída Esperada

O programa imprime:

- Área total calculada
- Área real do Google Maps
- Erro relativo entre os valores

## Dependências

- Python 3
- numpy

## Licença

Este projeto é apenas para fins educacionais.
