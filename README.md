# MiniCRA-PCN
O MiniCRA-PCN é um modelo de reconstrução de PointNets inspirado na arquitetura da CRA-PCN.

O modelo foi desenvolvido e executado em um ambiente Colab, com uma H100 em 12 horas.

### Estrutura do projeto:
- MiniCRA-PCN.ipynb: Notebook com scripts de treinamento e inferência.
- ./input/download.py: Script de download do dataset. Necessário porque é grande demais para subir pro Github.
- ./input/: Diretório contendo o dataset. (necessário executar o script download.py e descomprimir)
- ./output/logs/train.log: Log de treinamento.
- ./output/model/: Diretório contendo o modelo treinado. (necessário descomprimir)
- ./output/predictions/: Diretório contendo as predições do modelo treinado. (necessário descomprimir)
- ./analysis/: Diretório contendo os gráficos de análise dos resultados do modelo.