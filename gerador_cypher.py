def escrever_estado(arq_gerar, var_estado, var_regiao, uf, uf_code, name, no_accents, gentilic, gentilic_alternative, website, timezone, flag_image):
    linha = f'CREATE ({var_estado}:Estado {{cod_uf: "{uf}", sigla: "{uf_code}", nome: "{name}", sem_acento: "{no_accents}", gentilico: "{gentilic}", gent_altern: "{gentilic_alternative}", url_site: "{website}", timezone: "{timezone}", url_band: "{flag_image}"}})-[:PERTENCE_A]->({var_regiao})\n'

    if var_estado == 'e27':
        linha += '\n'

    with open(arq_gerar, 'a', encoding='utf-8') as txt_file:
        txt_file.write(linha)
        txt_file.close()


def escrever_cidade(arq_gerar, var_cidade, var_estado, name, no_accents, alternative_names, is_capital, lon, lat):
    linha = f'CREATE ({var_cidade}:Cidade {{nome: "{name}", sem_acento: "{no_accents}", nome_altern: "{alternative_names}", is_capital: "{is_capital}", long: "{lon}", latit: "{lat}"}})-[:PERTENCE_A]->({var_estado})\n'

    if "'" in linha:
        linha = linha.replace("'", '’')

    with open(arq_gerar, 'a', encoding='utf-8') as txt_file:
        txt_file.write(linha)
        txt_file.close()


print('--------------------------------------Bem-vindo(a)!--------------------------------------\n')
arq_gerar = str(input('Qual o nome do arquivo a se gerar? (arquivo .txt, insira apenas o nome)\n > ')) + '.txt'
arq_recebe1 = str(input('Qual o nome do arquivo a se ler as UFs/Estados? (arquivo .csv, insira apenas o nome)\n > ')) + '.csv'
arq_recebe2 = str(input('Qual o nome do arquivo a se ler as Cidades? (arquivo .csv, insira apenas o nome)\n > ')) + '.csv'

txt_file = open(arq_gerar, 'w+')
txt_file.write('''CREATE (p1:Pais {nome: 'Brasil'})\n
CREATE (r1:Macroregiao {nome: 'Norte'})-[:PERTENCE_A]->(p1)
CREATE (r2:Macroregiao {nome: 'Nordeste'})-[:PERTENCE_A]->(p1)
CREATE (r3:Macroregiao {nome: 'Centro-Oeste'})-[:PERTENCE_A]->(p1)
CREATE (r4:Macroregiao {nome: 'Sudeste'})-[:PERTENCE_A]->(p1)
CREATE (r5:Macroregiao {nome: 'Sul'})-[:PERTENCE_A]->(p1)\n\n''')
txt_file.close()
vars_regioes = {'Norte': 'r1', 'Nordeste': 'r2', 'Centro-Oeste': 'r3', 'Sudeste': 'r4', 'Sul': 'r5'}

from csv import DictReader
cont_est = 0
vars_estados = dict()

with open(arq_recebe1, 'r', encoding='utf-8') as csv_file:
    leitor_csv = DictReader(csv_file)
    # Itera sobre as linhas do arquivo CSV
    for linha_csv in leitor_csv:
        uf = linha_csv['uf']
        uf_code = linha_csv['uf_code']
        name = linha_csv['name']
        no_accents = linha_csv['no_accents']
        gentilic = linha_csv['gentilic']
        gentilic_alternative = linha_csv['gentilic_alternative']
        website = linha_csv['website']
        timezone = linha_csv['timezone']
        flag_image = linha_csv['flag_image']
        macroregion = linha_csv['macroregion']
        # Atualiza os contadores e monta as variáveis de id
        cont_est += 1
        var_estado = 'e' + str(cont_est)
        vars_estados[uf_code] = var_estado
        # Chama a função para escrever a linha no arquivo TXT
        escrever_estado(arq_gerar, var_estado, vars_regioes[macroregion], uf, uf_code, name, no_accents, gentilic, gentilic_alternative, website, timezone, flag_image)
csv_file.close()


cont_cid = 0

with open(arq_recebe2, 'r', encoding='utf-8') as arquivo_csv:
    leitor_csv = DictReader(arquivo_csv)

    # Itera sobre as linhas do arquivo CSV
    for linha_csv in leitor_csv:

        municipio = linha_csv['municipio']
        uf = linha_csv['uf']
        uf_code = linha_csv['uf_code']
        name = linha_csv['name']
        mesoregion = linha_csv['mesoregion']
        microregion = linha_csv['microregion']
        rgint = linha_csv['rgint']
        rgi = linha_csv['rgi']
        osm_relation_id = linha_csv['osm_relation_id']
        wikidata_id = linha_csv['wikidata_id']

        if linha_csv['is_capital'] == '':
            is_capital = 'False'
        else:
            is_capital = linha_csv['is_capital']

        wikipedia_pt = linha_csv['wikipedia_pt']
        lon = linha_csv['lon']
        lat = linha_csv['lat']
        no_accents = linha_csv['no_accents']
        slug_name = linha_csv['slug_name']
        alternative_names = linha_csv['alternative_names']
        pop_21 = linha_csv['pop_21']

        cont_cid += 1
        var_cidade = 'c' + str(cont_cid)
        var_estado = vars_estados[uf_code]

        # Chama a função para escrever a linha no arquivo TXT
        escrever_cidade(arq_gerar, var_cidade, var_estado, name, no_accents, alternative_names, is_capital, lon, lat)
arquivo_csv.close()

print('-----------------------------------------------------------------------------------------')
print('                     Processo encerrado. Arquivo criado com sucesso!                     ')
print('                    Obrigado por usar um algoritmo de antthLuca. (^-^)                   ')
