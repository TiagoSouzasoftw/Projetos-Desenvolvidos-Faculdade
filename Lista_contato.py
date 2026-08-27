print('Bem-vindo à Lista de Contatos')
print('-' * 64)

lista_contatos = []  # Lista vazia para armazenar os dicionários de contatos
id_global = 000000  # RU inicial que será iterado a cada contato incluído


def cadastrar_contato(id):
    """Cadastra um novo contato com ID, nome, atividade e telefone."""
    print('-' * 64)
    print('-' * 20 + ' MENU CADASTRAR CONTATO ' + '-' * 20)
    print(f'Id do Contato: {id}')
    nome = input('Por favor entre com o nome do Contato: ')
    atividade = input('Por favor entre com a Atividade do contato: ')
    telefone = input('Por favor entre com o telefone do contato: ')

    contato_dicionario = {
        'id': id,
        'nome': nome,
        'atividade': atividade,
        'telefone': telefone
    }

    # Adiciona uma cópia do dicionário para evitar mutabilidade indesejada
    lista_contatos.append(contato_dicionario.copy())
    print('Contato cadastrado com sucesso!\n')


def consultar_contatos(id_global):
    """Oferece sub-opções para consultar todos os contatos, por ID ou por atividade."""
    while True:
        print('-' * 64)
        print('-' * 20 + ' MENU CONSULTAR CONTATO ' + '-' * 20)
        op_consultar = input(
            'Escolha a opção desejada:\n'
            '1. Consultar Todos\n'
            '2. Consultar por ID\n'
            '3. Consultar por atividade\n'
            '4. Retornar ao Menu\n'
            '>> '
        )

        if op_consultar == '1':
            print('-' * 15)
            if not lista_contatos:
                print('Nenhum contato cadastrado.')
            for contato in lista_contatos:
                for chave, valor in contato.items():
                    print(f'{chave}: {valor}')
                print('-' * 15)

        elif op_consultar == '2':
            try:
                id_selecionado = int(input('Digite o id do contato: '))
                encontrado = False
                for contato in lista_contatos:
                    if contato['id'] == id_selecionado:
                        print('-' * 15)
                        for chave, valor in contato.items():
                            print(f'{chave}: {valor}')
                        print('-' * 15)
                        encontrado = True
                        break
                if not encontrado:
                    print('Id não encontrado.')
            except ValueError:
                print('Por favor, digite apenas números válidos para o ID.')

        elif op_consultar == '3':
            atividade_selecionada = input('Digite a atividade: ')
            print('-' * 15)
            encontrado = False
            for contato in lista_contatos:
                if contato['atividade'].lower() == atividade_selecionada.lower():
                    for chave, valor in contato.items():
                        print(f'{chave}: {valor}')
                    print('-' * 15)
                    encontrado = True
            if not encontrado:
                print('Nenhum contato encontrado com essa atividade.')

        elif op_consultar == '4':
            return
        else:
            print('Opção inválida.')


def remover_contato():
    """Remove um contato da lista com base no ID informado."""
    while True:
        print('-' * 64)
        print('-' * 20 + ' MENU REMOVER CONTATO ' + '-' * 20)
        try:
            id_remover = int(input('Digite o id do contato a ser removido: '))
            encontrado = False
            for contato in lista_contatos:
                if contato['id'] == id_remover:
                    lista_contatos.remove(contato)
                    print('Contato removido com sucesso.')
                    encontrado = True
                    return
            if not encontrado:
                print('Id inválido ou não encontrado.')
        except ValueError:
            print('Por favor, utilize apenas valores numéricos.')


# Menu principal do sistema
while True:
    print('-' * 25 + ' MENU PRINCIPAL ' + '-' * 25)
    menu = input(
        'Escolha a opção desejada:\n'
        '1. Cadastrar Contato\n'
        '2. Consultar Contato\n'
        '3. Remover Contato\n'
        '4. Encerrar o programa\n'
        '>> '
    )

    if menu == '1':
        cadastrar_contato(id_global)
        id_global += 1  # Incrementa o RU para o próximo contato
    elif menu == '2':
        consultar_contatos(id_global)
    elif menu == '3':
        remover_contato()
    elif menu == '4':
        print('Encerrando o programa...')
        break
    else:
        print('Opção inválida. Tente novamente.\n')