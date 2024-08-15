# Gerador de Estados e Cidades

**Síntese:** Este projeto contém algoritmos Python para gerar query de Estados e Cidades brasileiros para ser ultilizada em bancos de dados. Estes algoritmos podem gerar Cypher e SQLite.

**Processo:** O algoritmo recebe dois arquivos CSV com os estados e cidades brasileiros, respectivamente. E cria um arquivo TXT com as querys prontas para serem usadas no seu BD.

## Cypher - Neo4j
#### Os nós e relações são criados da seguinte forma:
```(Cidade) -[:PERTENCE_A]-> (Estado) -[:PERTENCE_A]-> (Macroregião) -[:PERTENCE_A]-> (País)```
<div style="display: flex; justify-itens: center;">
  <img src="https://github.com/antth-Luca/Gerador_Cypher_Estados_e_Cidades/blob/main/exemplo_nos.png">
</div>

## SQLite
#### Prévia das telas:
```[Cidade] <-- [UF] <-- [Macroregião]```
<div style="display: flex; justify-itens: center;">
  <img src="https://github.com/antth-Luca/Gerador_Cypher_Estados_e_Cidades/blob/main/table_cidade.png">
  <img src="https://github.com/antth-Luca/Gerador_Cypher_Estados_e_Cidades/blob/main/table_uf.png">
  <img src="https://github.com/antth-Luca/Gerador_Cypher_Estados_e_Cidades/blob/main/table_regiao.png">
</div>

---

### Avisos:
* Sinta-se à vontade para modificar o .py e adequar ao seu CSV;
* Os dados dos CSVs usados são de 2021.

### Autor:
* Luca Anthony - [antthLuca](https://github.com/antth-Luca)

### Anexos:
#### Estarei anexando os arquivos CSV usados:
* [ufs.csv](https://github.com/mapaslivres/municipios-br/blob/main/tabelas/ufs.csv);
* [municipios.csv](https://github.com/mapaslivres/municipios-br/blob/main/tabelas/municipios.csv);
* Disponível no [repositório "municipios-br"](https://github.com/mapaslivres/municipios-br).
