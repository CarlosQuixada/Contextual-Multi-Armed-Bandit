# MAB vs CMAB para Envio de E-mails

Este projeto demonstra como algoritmos de **Multi-Armed Bandit (MAB)** e **Contextual Multi-Armed Bandit (CMAB)** podem ser usados para otimizar o envio de e-mails com base na taxa de cliques, comparando abordagens **com** e **sem contexto**.

## Objetivo

Comparar a performance de:
- **Epsilon-Greedy** (sem contexto)
- **LinGreedy** (com contexto)

na tarefa de escolher o **melhor período do dia** (manhã, tarde, noite) para enviar e-mails e maximizar a recompensa (clique).

## Simulação

Foi criado um **dataset sintético realista**, contendo:
- Período de 3 meses
- Entre 500 e 10.000 clientes por dia
- Variáveis de perfil: `segmento`, `qtd_cliques_30d`, `tempo_cliente`, `usou_app_hoje`, `dia_semana`, `dias_desde_ultimo_clique`

A recompensa (`reward`) é simulada com base nessas variáveis, representando a chance de clique de um cliente.

## Métricas Avaliadas

- Recompensa acumulada por algoritmo
- Taxa de sucesso por interação
- Comparação com baseline

## Lógica do Baseline

Para comparação justa, foi implementado um baseline que escolhe horários com base na taxa de clique média histórica de cada período.

## Resultados

- CMAB com **contexto** (LinGreedy) obteve performance **superior** ao MAB e ao baseline.
- Contexto permitiu decisões **mais personalizadas** e **melhor aproveitamento** das informações de cada cliente.

## Organização do Projeto

```
📦 CONTEXTUAL_MULTI_ARMED_BANDIT
├── 📁 dataset
│   ├── 📁 raw
│   │   └── dataset.csv                  # Dataset (simulado)
│   └── 📁 processed
│       ├── features_importantes.pkl    # Lista de features selecionadas
│       └── preprocessor.pkl            # Pipeline de transformação (OneHot, Scaling, etc.)
│
├── 📁 notebook
│   ├── 00_Create_Dataset.ipynb         # Geração do dataset sintético
│   ├── 01_Analise_Processamento.ipynb  # Exploração e tratamento das variáveis
│   └── 02_Simulacao_CMAB.ipynb         # Simulação dos modelos MAB/CMAB
│
├── README.md                           # Este arquivo
├── teste.py                            # Script auxiliar
├── poetry.lock                         # Lockfile do ambiente Python
├── pyproject.toml                      # Configuração de dependências com Poetry
└── .gitignore                          # Arquivos a ignorar no versionamento
```

## Referências

- [Mabwiser – Multi-Armed Bandits for Python](https://github.com/fidelity/mabwiser)
- [An Overview of Contextual Bandits](https://towardsdatascience.com/an-overview-of-contextual-bandits-53ac3aa45034/)

## Autor

Carlos Quixadá  
LinkedIn: [linkedin.com/in/carlosquixada](https://linkedin.com/in/carlosquixada)
