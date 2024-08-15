def escrever_estado(txt_file, var_estado, var_regiao, uf, uf_code, name, no_accents, gentilic, gentilic_alternative,
                    website, timezone, flag_image):
    linha = f"INSERT INTO UF (regiao_id, nome, sigla) VALUES ({var_regiao}, '{name}', '{uf_code}');\n"

    if var_estado == 'e27':
        linha += '\n'

    txt_file.write(linha)


def escrever_cidade(txt_file, var_cidade, var_estado, name, no_accents, alternative_names, is_capital, lon, lat):
    if "'" in name:
        name = name.replace("'", '’')

    linha = f"INSERT INTO Cidade (uf_id, nome) VALUES ('{var_estado}', '{name}');\n"

    txt_file.write(linha)


def main():
    # Menu
    print('--------------------------------------Bem-vindo(a)!--------------------------------------\n')
    arq_gerar = str(input('Qual o nome do arquivo a se gerar? (arquivo .txt, insira apenas o nome)\n > ')) + '.txt'
    arq_recebe1 = str(
        input('Qual o nome do arquivo a se ler as UFs/Estados? (arquivo .csv, insira apenas o nome)\n > ')) + '.csv'
    arq_recebe2 = str(
        input('Qual o nome do arquivo a se ler as Cidades? (arquivo .csv, insira apenas o nome)\n > ')) + '.csv'

    # Inicializa o arquivo TXT
    with open(arq_gerar, 'w+', encoding='utf-8') as txt_file:
        txt_file.write('''-- Tabela Macroregião\n
                        CREATE TABLE Macroregiao (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nome TEXT NOT NULL
                        );

                        INSERT INTO Macroregiao (nome) VALUES ('Norte');
                        INSERT INTO Macroregiao (nome) VALUES ('Nordeste');
                        INSERT INTO Macroregiao (nome) VALUES ('Centro-Oeste');
                        INSERT INTO Macroregiao (nome) VALUES ('Sudeste');
                        INSERT INTO Macroregiao (nome) VALUES ('Sul');

                        -- Tabela UF
                        CREATE TABLE UF (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            regiao_id INTEGER NOT NULL,
                            nome TEXT NOT NULL,
                            sigla TEXT NOT NULL,
                            FOREIGN KEY (regiao_id) REFERENCES Macroregiao(id)
                        );

                        -- Tabela Cidade
                        CREATE TABLE Cidade (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            uf_id INTEGER NOT NULL,
                            nome TEXT NOT NULL,
                            FOREIGN KEY (uf_id) REFERENCES UF(id)
                        );\n\n''')

        # Registra as variáveis das regiões
        vars_regioes = {'Norte': 1, 'Nordeste': 2, 'Centro-Oeste': 3, 'Sudeste': 4, 'Sul': 5}

        # Preparando a importação, contador e as variáveis dos estados
        from csv import DictReader
        cont_est = 0
        vars_estados = dict()

        # Abre o primeiro CSV
        with open(arq_recebe1, 'r', encoding='utf-8') as csv_file:
            leitor_csv = DictReader(csv_file)
            # Itera sobre as linhas do arquivo CSV. MODIFIQUE AQUI AS COLUNAS DO SEU ARQUIVO CSV!!!
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
                vars_estados[uf_code] = cont_est

                # Chama a função para escrever a linha no arquivo TXT
                escrever_estado(txt_file, var_estado, vars_regioes[macroregion], uf, uf_code, name, no_accents,
                                gentilic, gentilic_alternative, website, timezone, flag_image)

        # Define um novo contador, de cidades
        cont_cid = 0

        # Abre o segundo CSV
        with open(arq_recebe2, 'r', encoding='utf-8') as arquivo_csv:
            leitor_csv = DictReader(arquivo_csv)
            # Itera sobre as linhas do arquivo CSV. MODIFIQUE AQUI AS COLUNAS DO SEU ARQUIVO CSV!!!
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
                # Frescura minha, no arquivo CSV quando uma cidade não é capital, vem null. Eu optei por substituir por "False"
                if linha_csv['is_capital'] == '':
                    is_capital = 'False'
                else:
                    is_capital = linha_csv['is_capital']
                # Continuação
                wikipedia_pt = linha_csv['wikipedia_pt']
                lon = linha_csv['lon']
                lat = linha_csv['lat']
                no_accents = linha_csv['no_accents']
                slug_name = linha_csv['slug_name']
                alternative_names = linha_csv['alternative_names']
                pop_21 = linha_csv['pop_21']

                # Atualiza os contadores e monta as variáveis de id
                cont_cid += 1
                var_cidade = 'c' + str(cont_cid)
                var_estado = vars_estados[uf_code]

                # Chama a função para escrever a linha no arquivo TXT
                escrever_cidade(txt_file, var_cidade, var_estado, name, no_accents, alternative_names, is_capital, lon,
                                lat)

    print('-----------------------------------------------------------------------------------------')
    print('                     Processo encerrado. Arquivo criado com sucesso!                     ')
    print('                    Obrigado por usar um algoritmo de antthLuca. (^-^)                   ')


if __name__ == "__main__":
    main()
