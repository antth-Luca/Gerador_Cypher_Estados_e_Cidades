# Gerador Cypher de Estados e Cidades

**Síntese:** Este é um algoritmo Python para gerar um arquivo txt com query Cypher dos Estados e Cidades brasileiros para ser ultilizada no Neo4j.

**Processo:** O algoritmo recebe dois arquivos CSV com os estados e cidades brasileiros, respectivamente. E cria um arquivo TXT com as querys Cypher prontas para serem usadas no Neo4j e serem criados os nós e relações do País, Macroregiões, Estados e Cidades brasileiros.

#### Os nós e relações são criados da seguinte forma:
```(Cidade) -[:PERTENCE_A]-> (Estado) -[:PERTENCE_A]-> (Macroregião) -[:PERTENCE_A]-> (País)```
<div style="display: flex; justify-itens: center;">
  <img src="https://github.com/antth-Luca/Gerador_Cypher_Estados_e_Cidades/blob/main/exemplo_nos.png">
</div>


#### Estarei deixando os seguintes arquivos:
* [gerador_cypher.py](https://github.com/antth-Luca/Gerador_Cypher_Estados_e_Cidades/blob/main/gerador_cypher.py) - o arquivo Python que se deve executar;
* [query_cypher.txt](https://github.com/antth-Luca/Gerador_Cypher_Estados_e_Cidades/blob/main/query_cypher.txt) - a query que eu gerei para o meu projeto;
* [ufs.csv](https://github.com/antth-Luca/Gerador_Cypher_Estados_e_Cidades/blob/main/ufs.csv) e [municipios.csv](https://github.com/antth-Luca/Gerador_Cypher_Estados_e_Cidades/blob/main/municipios.csv) - arquivos CSV que eu usei, [disponível no repositório "municipios-br"](https://github.com/mapaslivres/municipios-br)

### ATENÇÃO! Dados de 2021.