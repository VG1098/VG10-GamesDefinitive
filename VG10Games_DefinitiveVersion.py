import datetime

data = datetime.date(2024,12,18)
print(type(data))

dia = data.day
mes = data.month
ano = data.year

print(dia,mes,ano)

def mostrar_menu_principal():
    """
    Exibe as opções do menu principal e retorna a escolha do usuário.
    """
    print("""
Olá caro cliente, seja bem-vindo a VG10 Games!
Antes de prosseguirmos, gostaríamos de saber qual serviço você procura:

Escolha a opção desejada (DIGITE APENAS O NÚMERO):

[1] LAN HOUSE
[2] ALUGAR JOGOS
[3] INSCRIÇÕES PARA CAMPEONATOS (E-SPORTS)
[4] EXPERIÊNCIA VR
[5] SIMULADOR DE CORRIDA
[0] SAIR
    """)
    opcao = input("Digite sua opção: ")
    return opcao

def solicitar_opcao(mensagem):
    """
    Solicita que o usuário faça uma escolha com base em uma mensagem personalizada.
    """
    print(mensagem)
    while True:
        escolha = input("Digite sua escolha: ")
        if escolha in ['1', '2']:
            return escolha
        print("Entrada inválida! Por favor, escolha 1 ou 2.")

def lan_house():
    """
    Lida com as interações relacionadas à LAN HOUSE.
    """
    print("\n***** Você escolheu a opção LAN HOUSE! *****\n")

    print("Abaixo você pode conferir as plataformas disponíveis para se divertir na nossa Lan House:")
    print("""
    [1] PS4
    [2] PS5
    [3] XBOX SERIES S
    [4] XBOX SERIES X
    [5] PC
    """)

    # Perguntar sobre o cadastro
    cadastro = solicitar_opcao("""
Agora gostaríamos de saber se você já possui cadastro: (DIGITE APENAS O NÚMERO)

[1] SIM
[2] NÃO
    """)

    if cadastro == '1':  # Possui cadastro
        print('Muito obrigado pela confirmação!')

        cadastro_existente()
        escolhas_usuario()
        comecar_tempo()
        opcoes_usuario()


    if cadastro == '2':  # O usuário não tem cadastro
        print('Ok então iremos criar um cadastro inicial para você, para isso basta seguir as orientações a seguir:')
        print('Neste momento vamos precisar de algumas informações para efetivar o seu cadastro:')

        criar_cadastro()
        escolhas_usuario()
        comecar_tempo()
        opcoes_usuario()

pass

def cadastro_existente():
    """
    Lida com a utlização de um cadastro existente.
    """
    print('Muito obrigado pela confirmação!')
    cadastro_existe = solicitar_opcao("""
Agora por favor escolha uma das opções a seguir (DIGITE APENAS O NÚMERO):

[1] SEGUIR COM CADASTRO EXISTENTE
[2] DESEJO FAZER ALTERAÇÕES NO MEU CADASTRO
        """)

    if cadastro_existe == '1':  # Seguir com cadastro existente
            print('Ok, então você deseja se logar com o seu cadastro existente! ')
            validacao_cpf()
    if cadastro_existe == '2':
        print('Você escolheu fazer alterações no cadastro')
        print( 'Aviso Importante!!! Ao fazer alterações no cadastro, como por exemplo a alteração do nome de usuário existente será cobrado um valor adicional de R$10,00 ')

        alterar_cadastro()


        # Perguntar sobre créditos disponíveis
    credito_disponivel = solicitar_opcao("""
Você gostaria de consultar se há créditos disponíveis para o seu cadastro? (DIGITE APENAS O NÚMERO)

[1] SIM
[2] NÃO
        """)

    if credito_disponivel == '1':
            credito = 120  # Exemplo fictício de créditos
            print(f"Ok jogador, seu crédito disponível é de {credito} minutos!")
            print("Lembrete importante: Utilize seus créditos disponíveis se forem maiores ou iguais a 60 minutos!")
    if credito_disponivel == '2':
            print('Ok, você optou por não consultar os créditos disponiveis!')

pass

def criar_cadastro():
    """
    Lida com a criação de um novo cadastro.
    """
    print("\n***** Você escolheu a opção CRIAR CADASTRO! *****\n")
    nome = input('Digite seu nome completo: ')
    while True:
        cpf = input(
            'Caro cliente, você poderia por favor nos informar o seu CPF? ').replace('-', '')
        caracteres = len(cpf)
        if caracteres != 11:
            print('CPF inválido! Por favor, digite novamente: ')
            continue
        else:
            print(f'Obrigado pela confirmação! ')
            break
    validacao_email()
    print('Por favor nos confirme os dados do seu endereço!')
    rua = input('Digite o nome da rua: ')
    numero = input('Digite o número: ')
    complemento = input('Digite o complemento: ')
    bairro = input('Digite o bairro: ')
    cep = input('Caro cliente, você poderia por favor nos informar o seu CEP? ').replace('-', '').strip()
    while len(cep) != 8 or not cep.isdigit():
            print('CEP inválido! Por favor, digite novamente.')
            cep = input('Caro cliente, você poderia por favor nos informar o seu CEP? ').replace('-', '').strip()
    cidade = input('Digite a cidade: ')
    estado = input('Digite o estado: ')

    dicionario = {
        'nome': nome,
        'cpf': cpf,
        'rua': rua,
        'numero': numero,
        'complemento': complemento,
        'bairro': bairro,
        'cep': cep,
        'cidade': cidade,
        'estado': estado,
    }

    ficha = [dicionario]

    print()
    print( f"\033[40m{'Nome'.center(30)} {'CPF'.center(20)} {'Rua'.center(12)} {'Número'.center(15)} {'Complemento'.center(13)} {'Bairro'.center(17)} {'CEP'.center(25)} {'Cidade'.center(15)} {'Estado'.center(18)}\033[0m")
    print( f"\033[40m{nome:<30} {cpf:>15} {rua:>15} {numero:>11} {complemento:<13} {bairro:>25} {cep:>14} {cidade:>24} {estado:>18}\033[0m")

    confirmar_dados()

    print('Agora você poderá criar um usuário!')
    print('Por favor nos confirme seu ano de nascimento')

    anoAtual = 2024
    anoNascimento = int(input("Digite seu ano de nascimento: "))
    idade = anoAtual - anoNascimento

    if idade <= 9:
        print("\nVOCÊ É UM GAMER MIRIM")
    elif idade <= 14:
        print("\n VOCÊ É UM GAMER INFANTIL")
    elif idade <= 19:
        print("\n VOCÊ É GAMER JÚNIOR")
    elif idade <= 30:
        print("\nVOCÊ É UM GAMER SÊNIOR")
    else:
        print("\n VOCÊ É UM GAMER MASTER")

    texto1 = 'Sim'.lower()
    texto2 = 'Não'.lower()
    usuario_nao_identificado = 'USUÁRIO NÃO IDENTIFICADO'

    usuario = input('Você gostaria de criar um nome de usuário? (sim/não) ').strip().lower()
    if texto1 in usuario:
        nome_usuario = f'Seu nome de usuário é: {nome} {cpf} '
        usuarioPadrao = nome_usuario.split()
        print(nome_usuario)
        trocarUsuario = input('Você gostaria de trocar o nome de usuário? ').strip().lower()
        if texto2 in trocarUsuario:
            print('Você não alterou seu nome de usuário e está acessando o sistema como',usuarioPadrao,'!')
        if texto1 in trocarUsuario:
            criarUsuario = input('Por favor Digite o nome de usuário desejado:')
            print('Seu novo nome de usuário é:', criarUsuario, )

    elif texto2 in usuario:
        print('Você não criou um usuário e está acessando o sistema como:', usuario_nao_identificado)
        print('Aviso Importante!!! Ao acessar o sistema como usuário não identificado você não pode guardar ou acumular créditos! ')

    if texto2 in usuario:
        criarUsuarioIdentificado = input("""
Essa é a sua última chance para criar um usuário: Você realmnete deseja seguir como um USUÁRIO NÃO IDENTIFICADO? (DIGITE APENAS O NÚMERO)

[OPÇÃO 1] SIM
[OPÇÃO 2] NÃO

""")
        match criarUsuarioIdentificado:
            case '1':
                    print('Ok, você realmente seguirá como um USUÁRIO NÃO IDENTIFICADO!')
                    usuario_nao_autenticado()
                    exit()
            case '2':
                usuarioIdentificado = input('Por favor digite o nome de usário desejado:')
                print('Seu nome de usuário é,',usuarioIdentificado,'!')
                print( 'Agora que você criou um usuário, você pode guardar os créditos, consultar os créditos disponíveis, colocar créditos e reservar um horário!!!')

pass

def alterar_cadastro():
    """
        Lida com a alteração de dados cadastrais como endereço e nome de usuário.
        """
    print('Você escolheu fazer alterações no cadastro')
    print('Aviso Importante!!! Ao fazer alterações no cadastro, como por exemplo a alteração do nome de usuário existente será cobrado um valor adicional de R$10,00 ')

    alteracao = input("""
Por favor nos informe qual alteração você deseja fazer: (DIGITE APENAS O NÚMERO)

[OPÇÃO 1] ALTERAR O ENDEREÇO
[OPÇÃO 2] ALTERAR O NOME DE USUÁRIO
[OPÇÃO 3] ALTERAR EMAIL CADASTRADO


                                    """)
    match alteracao:
        case '1':
            print('Por favor nos informe o endereço completo atualizado')
            preencher_endereco()

        case '2':
            print('Ok, você deseja alterar o sue nome de usuário!')
            validacao_cpf()
            usuario = input('Por favor digite o seu nome de usuário já cadastrado:')
            print('Ok, já localizamos o seu nome de usuário!')
            trocarUsuario = input('Agora por favor digite o nome de usuário desejado: ')
            print('Ok seu novo nome de usuário é', trocarUsuario, 'Para confirmar a alteração por gentileza pague a taxa de alteração no valor de R$10,00 comparecendo ao caixa da loja! ')

        case '3':
            validacao_email()

        case _:
            print('Opção inválida, por favor escolha entre 1 ou 2.')


pass

def confirmar_dados():
    dados = input("""
Você poderia nos confirmar se as informações inseridas na sua ficha estão corretas (DIGITE APENAS O NÚMERO):

[OPÇÃO 1] SIM
[OPÇÃO 2] NÃO, EU DESEJO FAZER CORREÇÕES
                            """)

    match dados.strip():  # Remove espaços extras ao redor da resposta
        case '1':  # Se o usuário digitar 1
            print('Ok, muito obrigado pela confirmação! ')

        case '2':  # Se o usuário digitar 2
            print('Ok, então por favor digite novamente as informações solicitadas! ')
            validar_dados() # Chama a função para corrigir o cadastro
            print('Ok, as informações foram corrigidas!')
        case _:  # Para qualquer entrada inválida
            print('Opção inválida! Por favor, escolha 1 ou 2.')
            confirmar_dados()  # Repete a pergunta para corrigir o erro
pass

def validar_dados():
    nome = input('Digite seu nome completo: ')
    while True:
        cpf = input(
            'Caro cliente, você poderia por favor nos informar o seu CPF? ').replace('-', '')
        caracteres = len(cpf)
        if caracteres != 11:
            print('CPF inválido! Por favor, digite novamente: ')
            continue
        else:
            print(f'Obrigado pela confirmação! ')
            break
    validacao_email()
    print('Por favor nos confirme os dados do seu endereço!')
    rua = input('Digite o nome da rua: ')
    numero = input('Digite o número: ')
    complemento = input('Digite o complemento: ')
    bairro = input('Digite o bairro: ')
    cep = input('Caro cliente, você poderia por favor nos informar o seu CEP? ').replace('-', '').strip()
    while len(cep) != 8 or not cep.isdigit():
        print('CEP inválido! Por favor, digite novamente.')
        cep = input('Caro cliente, você poderia por favor nos informar o seu CEP? ').replace('-', '').strip()
    cidade = input('Digite a cidade: ')
    estado = input('Digite o estado: ')

    dicionario = {
        'nome': nome,
        'cpf': cpf,
        'rua': rua,
        'numero': numero,
        'complemento': complemento,
        'bairro': bairro,
        'cep': cep,
        'cidade': cidade,
        'estado': estado,
    }

    ficha = [dicionario]

    print()
    print(
        f"\033[40m{'Nome'.center(30)} {'CPF'.center(20)} {'Rua'.center(12)} {'Número'.center(15)} {'Complemento'.center(13)} {'Bairro'.center(17)} {'CEP'.center(25)} {'Cidade'.center(15)} {'Estado'.center(18)}\033[0m")
    print(
        f"\033[40m{nome:<30} {cpf:>15} {rua:>15} {numero:>11} {complemento:<13} {bairro:>25} {cep:>14} {cidade:>24} {estado:>18}\033[0m")

pass

def escolhas_usuario():
    """
        Lida com as escolhas do usuário do usuário.
        """
    jogo = input('Agora digite o jogo  que você deseja jogar: ')
    print('Obrigado jogador você selecionou o jogo', jogo, '!')
    plataformas = input('Selecione a plataforma: ')
    plataforma1 = 'PS4'
    plataforma2 = 'PS5'
    plataforma3 = 'XBOX SERIES S'
    plataforma4 = 'XBOX SERIES X'
    plataforma5 = 'PC'
    acessorios1 = 'COMBO (HEADSET E CONTROLE ELITE)'

    experienciaDefinitiva = input("""
Você deseja utilizar acessórios Premium para aprimorar ainda mais a sua experiência? (DIGITE APENAS O NÚMERO)

[OPÇÃO 1] SIM
[OPÇÃO 2] NÃO
                                                                                """)

    if experienciaDefinitiva == '1':
        acessorios = input("""
ESCOLHA OS ACESSÓRIOS PARA APRIMORAR A SUA EXPERIÊNCIA (DIGITE APENAS O NÚMERO)

[OPÇÃO 1] COMBO (HEADSET E CONTROLE ELITE)
                                                                                    """)

        if acessorios == '1':
            print('Ok, você escolheu a opção', acessorios1,'e será cobrada uma taxa adicional de R$10,00 no (Valor da hora)!')

        else:
            print('Opção inválida de acessórios.')
    elif experienciaDefinitiva == '2':


            print('Ok, você não deseja ter uma experiência definitiva!')
    else:
            print('Opção inválida para experiência definitiva.')

    if plataforma1 in plataformas:
        print('\033[40m', jogo.center(40, '#'), "\033[0m\n")
        print('PS4'.ljust(34, '.'), "R$8,00 (Valor da hora)")
        tempo = int(input('Quantas horas você deseja jogar? '))
        valor1 = 8.00
        print(f'O valor cobrado será {tempo * valor1:,.2f}')

    if plataforma1 in plataformas:
        maquina = input("""
Escolha uma máquina de acordo com a plataforma escolhida (DIGITE APENAS O NÚMERO):

[MÁQUINA 1] PS4
[MÁQUINA 2] PS4
[MÁQUINA 3] PS4
[MÁQUINA 4] PS4
[MÁQUINA 5] PS4
                                                                                                        """)

        match maquina:
            case '1' | '2' | '3' | '4' | '5':
                print('Ok você selecionou a maquina', maquina, 'dirija-se até ela! ')
            case _:
                print('Por favor selecione uma opção válida')


    if plataforma2 in plataformas:
        print('\033[40m', jogo.center(40, '#'), "\033[0m\n")
        print('PS5'.ljust(34, '.'), "R$10,00 (Valor da hora)")
        tempo = int(input('Quantas horas você deseja jogar? '))
        valor2 = 10.00
        print(f'O valor cobrado será de R$ {tempo * valor2:,.2f}')

    if plataforma2 in plataformas:
        maquina = input("""
Escolha uma máquina de acordo com a plataforma escolhida (DIGITE APENAS O NÚMERO):

[MÁQUINA 6] PS5
[MÁQUINA 7] PS5
[MÁQUINA 8] PS5
[MÁQUINA 9] PS5
[MÁQUINA 10] PS5
                                                                                                            """)

        match maquina:
            case '6' | '7' | '8' | '9' | '10':
                print('Ok você selecionou a maquina', maquina, 'dirija-se até ela! ')
            case _:
                print('Por favor selecione uma opção válida')

    if plataforma3 in plataformas:
        print('\033[40m', jogo.center(40, '#'), "\033[0m\n")
        print('XBOX SERIES S'.ljust(34, '.'), "R$9,00 (Valor da hora)")
        tempo = int(input('Quantas horas você deseja jogar? '))
        valor3 = 9.00
        print(f'O valor cobrado será de R$ {tempo * valor3:,.2f}')

    if plataforma3 in plataformas:
        maquina = input("""
Escolha uma máquina de acordo com a plataforma escolhida (DIGITE APENAS O NÚMERO):

[MÁQUINA 11] XBOX SERIES S
[MÁQUINA 12] XBOX SERIES S
[MÁQUINA 13] XBOX SERIES S

                                                                                                            """)

        match maquina:
            case '11' | '12' | '13':
                print('Ok você selecionou a maquina', maquina, 'dirija-se até ela! ')
            case _:
                print('Por favor selecione uma opção válida')

        if plataforma4 in plataformas:
            print('\033[40m', jogo.center(40, '#'), "\033[0m\n")
            print('XBOX SERIES X'.ljust(34, '.'), "R$10,00 (Valor da hora)")
            tempo = int(input('Quantas horas você deseja jogar? '))
            valor4 = 10.00
            print(f'O valor cobrado será de R$ {tempo * valor4:,.2f}')

        if plataforma4 in plataformas:
            maquina = input("""
Escolha uma máquina de acordo com a plataforma escolhida (DIGITE APENAS O NÚMERO):

[MÁQUINA 14] XBOX SERIES X
[MÁQUINA 15] XBOX SERIES X
[MÁQUINA 16] XBOX SERIES X

                                                                                                            """)
            match maquina:
                case '14' | '15' | '16':
                    print('Ok você selecionou a maquina', maquina, 'dirija-se até ela! ')
                case _:
                    print('Por favor selecione uma opção válida')

        if plataforma5 in plataformas:
            print('\033[40m', jogo.center(40, '#'), "\033[0m\n")
            print('PC'.ljust(34, '.'), "R$5,00 (Valor da hora)")
            tempo = int(input('Quantas horas você deseja jogar? '))
            valor5 = 5.00
            print(f'O valor cobrado será de R$ {tempo * valor5:,.2f}')

        if plataforma5 in plataformas:
            maquina = input("""
Escolha uma máquina de acordo com a plataforma escolhida (DIGITE APENAS O NÚMERO):

[MÁQUINA 17] PC
[MÁQUINA 18] PC
[MÁQUINA 19] PC
[MÁQUINA 20] PC

                                                                                                            """)
            match maquina:
                case '17' | '18' | '19' | '20':
                    print('Ok você selecionou a maquina', maquina, 'dirija-se até ela! ')
                case _:
                    print('Por favor selecione uma opção válida')

pass



def comecar_tempo():
    """
            Lida com o registro de tempo.
            """
    start = input(
        'Você está pronto para começar a jogar? Lembre-se que ao avançar nessa opção seu tempo irá começar a contar! Digite (C) para continuar: ').strip().upper()
    if start == 'C':
        print("\nCronômetro iniciado...\n")
        print('A VG10 Games lhe deseja muita diversão!')

pass

def opcoes_usuario():
    """
        Lida com as opções diponíveis do usuário cadastrado.
        """
    global dia
    guardarCredito = input("""
Você gostaria de guardar o tempo restante? (DIGITE APENAS O NÚMERO)

[OPÇÃO 1] SIM
[OPÇÃO 2] NÃO
                                                                                                                            """)
    match guardarCredito:
                                    case '1':
                                        print('Ok você optou por guardar o tempo restante! ')
                                    case '2':
                                        print('Ok você optou por NÃO guardar o tempo restante! ')

    regras_creditos()

    colocarCreditos = input("""
Você deseja colocar créditos (DIGITE APENAS O NÚMERO)

[OPÇÃO 1] SIM
[OPÇÃO 2] NÃO
                                                                                                                            """)

    match colocarCreditos:
                                    case '1': dia = input("""
Você optou por colocar créditos, você deseja fazer uma reserva para um dia especifico da semana (DIGITE APENAS O NÚMERO)

[OPÇÃO 1] SIM
[OPÇÃO 2] NÃO

                                                                                        """)


    match dia:
        case '1':
            print('Você optou por reservar um dia especifico da semana!')
            reservaDia = input("""
Escolha um dia da semana (DIGITE APENAS O NÚMERO):

[1] DOMINGO
[2] SEGUNDA FEIRA
[3] TERÇA FEIRA
[4] QUARTA FEIRA
[5] QUINTA FEIRA
[6] SEXTA FEIRA
[7] SÁBADO
                                                                                                """)


            dia1 = 'Domingo'
            dia2 = 'Segunda-Feira'
            dia3 = 'Terça-Feira'
            dia4 = 'Quarta-Feira'
            dia5 = 'Quinta-Feira'
            dia6 = 'Sexta-Feira'
            dia7 = 'Sábado'

            match reservaDia:
                case '1':
                    print('Ok jogador você selecionou', dia1,'!')
                    print('Agora consulte o calendário abaixo, e de acordo com o dia reservado digite o dia do mês!')
                    print((calendario()))
                    dia_Mes = int(input('Digite o dia do mês :'))
                    print('Ok jogador você selecionou', dia1,'dia',dia_Mes, 'de dezembro de 2024')
                case '2':
                    print('Ok jogador você selecionou', dia2,'agora por favor nos confirme o horário! ')
                    print('Agora consulte o calendário abaixo, e de acordo com o dia reservado digite o dia do mês!')
                    print((calendario()))
                    dia_Mes = int(input('Digite o dia do mês :'))
                    print('Ok jogador você selecionou', dia1, 'dia', dia_Mes, 'de dezembro de 2024')
                case '3':
                    print('Ok jogador você selecionou', dia3,'agora por favor nos confirme o horário! ')
                    print('Agora consulte o calendário abaixo, e de acordo com o dia reservado digite o dia do mês!')
                    print((calendario()))
                    dia_Mes = int(input('Digite o dia do mês :'))
                    print('Ok jogador você selecionou', dia1, 'dia', dia_Mes, 'de dezembro de 2024')
                case '4':
                    print('Ok jogador você selecionou', dia4, 'agora por favor nos confirme o horário! ')
                    print('Agora consulte o calendário abaixo, e de acordo com o dia reservado digite o dia do mês!')
                    print((calendario()))
                    dia_Mes = int(input('Digite o dia do mês :'))
                    print('Ok jogador você selecionou', dia1, 'dia', dia_Mes, 'de dezembro de 2024')
                case '5':
                    print('Ok jogador você selecionou', dia5, 'agora por favor nos confirme o horário! ')
                    print('Agora consulte o calendário abaixo, e de acordo com o dia reservado digite o dia do mês!')
                    print((calendario()))
                    dia_Mes = int(input('Digite o dia do mês :'))
                    print('Ok jogador você selecionou', dia1, 'dia', dia_Mes, 'de dezembro de 2024')
                case '6':
                    print('Ok jogador você selecionou', dia6, 'agora por favor nos confirme o horário! ')
                    print('Agora consulte o calendário abaixo, e de acordo com o dia reservado digite o dia do mês!')
                    print((calendario()))
                    dia_Mes = int(input('Digite o dia do mês :'))
                    print('Ok jogador você selecionou', dia1, 'dia', dia_Mes, 'de dezembro de 2024')
                case '7':
                    print('Ok jogador você selecionou', dia7, 'agora por favor nos confirme o horário! ')
                    print('Agora consulte o calendário abaixo, e de acordo com o dia reservado digite o dia do mês!')
                    print((calendario()))
                    dia_Mes = int(input('Digite o dia do mês :'))
                    print('Ok jogador você selecionou', dia1, 'dia', dia_Mes, 'de dezembro de 2024')
                case _:
                    print('Seleção inválida, por favor escolha um número entre 1 e 7.')
            reservaHorario = input("""
Agora por favor escolha o horário:(DIGITE APENAS O NÚMERO)
[1] 09:00
[2] 10:00
[3] 11:00
[4] 12:00
[5] 13:00
[6] 14:00
[7] 15:00
[8] 16:00
[9] 17:00
[10] 18:00
[11] 19:00


                                                                                                                          """)
            match reservaHorario:
                case '1':
                    print('Ok jogador você selecionou o horário 09:00! ')
                case '2':
                    print('Ok jogador você selecionou o horário 10:00! ')
                case '3':
                    print('Ok jogador você selecionou o horário 11:00! ')
                case '4':
                    print('Ok jogador você selecionou o horário 12:00! ')
                case '5':
                    print('Ok jogador você selecionou o horário 13:00! ')
                case '6':
                    print('Ok jogador você selecionou o horário 14:00! ')
                case '7':
                    print('Ok jogador você selecionou o horário 15:00! ')
                case '8':
                    print('Ok jogador você selecionou o horário 16:00! ')
                case '9':
                    print('Ok jogador você selecionou o horário 17:00! ')
                case '10':
                    print('Ok jogador você selecionou o horário 18:00! ')
                case '11':
                    print('Ok jogador você selecionou o horário 19:00! ')
                case _:
                    print('Por favor selecione uma opção válida')

            enviar_reserva()

            print('Aviso importante! Não serão tolerados atrasos, em caso de imprevistos por favor nos comunique com antecedência ')

            plataformaparaReserva = input('Agora por favor nos confirme a plataforma: ')

            plataforma1 = 'PS4'
            plataforma2 = 'PS5'
            plataforma3 = 'XBOX SERIES S'
            plataforma4 = 'XBOX SERIES X'
            plataforma5 = 'PC'

            if plataforma1 in plataformaparaReserva:
                print('PS4'.ljust(34, '.'), "R$8,00 (Valor da hora)")
                tempo = int(input('Quantas horas você deseja jogar? '))
                valor1 = 8.00
                print(f'O valor cobrado será {tempo * valor1:,.2f}')
                print('Caro jogador por favor compareça ao caixa da loja para pagar o valor informado e garantir a sua reserva! ')

            if plataforma2 in plataformaparaReserva:
                print('PS5'.ljust(34, '.'), "R$10,00 (Valor da hora)")
                tempo = int(input('Quantas horas você deseja jogar? '))
                valor2 = 10.00
                print(f'O valor cobrado será de R$ {tempo * valor2:,.2f}')
                print('Caro jogador por favor compareça ao caixa da loja para pagar o valor informado e garantir a sua reserva! ')

            if plataforma3 in plataformaparaReserva:
                print('XBOX SERIES S'.ljust(34, '.'), "R$9,00 (Valor da hora)")
                tempo = int(input('Quantas horas você deseja jogar? '))
                valor3 = 9.00
                print(f'O valor cobrado será de R$ {tempo * valor3:,.2f}')
                print( 'Caro jogador por favor compareça ao caixa da loja para pagar o valor informado e garantir a sua reserva! ')

            if plataforma4 in plataformaparaReserva:
                print('XBOX SERIES X'.ljust(34, '.'), "R$10,00 (Valor da hora)")
                tempo = int(input('Quantas horas você deseja jogar? '))
                valor4 = 10.00
                print(f'O valor cobrado será de R$ {tempo * valor4:,.2f}')
                print(  'Caro jogador por favor compareça ao caixa da loja para pagar o valor informado e garantir a sua reserva! ')

            if plataforma5 in plataformaparaReserva:
                print('PC'.ljust(34, '.'), "R$5,00 (Valor da hora)")
                tempo = int(input('Quantas horas você deseja jogar? '))
                valor5 = 5.00
                print(f'O valor cobrado será de R$ {tempo * valor5:,.2f}')
                print('Caro jogador por favor compareça ao caixa da loja para pagar o valor informado e garantir a sua reserva! ')

            nota = int(input("Digite sua nota de 1 a 10 para avaliar o nosso atendimento: "))
            match nota:
                case _ if nota < 0:
                    print(f"\nNota inválida")
                case _ if nota <= 4:
                    print(f"\nPéssimo atendimento: {nota}")
                case _ if nota <= 7:
                    print(f"\nAtendimento pode melhorar: {nota}")
                case _ if nota <= 9:
                    print(f"\nÓtimo atendimento: {nota}")
                case _ if nota <= 10:
                    print(f"\nExcelente atendimento: {nota}")
                case _:
                    print(f"\nNota inválida")

        case '2':
            print('Você optou por não reservar um dia especifico da semana!')
            print('Atenção! Dessa forma você poderá comparecer no dia que quiser na loja, obviamente sem ter reservado um horário você somente terá acesso a máquina, se a mesma estiver disponível! ')

            plataformaparaReserva = input('Agora por favor nos confirme a plataforma: ')

            plataforma1 = 'PS4'
            plataforma2 = 'PS5'
            plataforma3 = 'XBOX SERIES S'
            plataforma4 = 'XBOX SERIES X'
            plataforma5 = 'PC'

            if plataforma1 in plataformaparaReserva:
                print('PS4'.ljust(34, '.'), "R$8,00 (Valor da hora)")
                tempo = int(input('Quantas horas você deseja jogar? '))
                valor1 = 8.00
                print(f'O valor cobrado será {tempo * valor1:,.2f}')
                print('Caro jogador por favor compareça ao caixa da loja para pagar o valor informado e garantir a sua reserva! ')

            if plataforma2 in plataformaparaReserva:
                print('PS5'.ljust(34, '.'), "R$10,00 (Valor da hora)")
                tempo = int(input('Quantas horas você deseja jogar? '))
                valor2 = 10.00
                print(f'O valor cobrado será de R$ {tempo * valor2:,.2f}')
                print('Caro jogador por favor compareça ao caixa da loja para pagar o valor informado e garantir a sua reserva! ')

            if plataforma3 in plataformaparaReserva:
                print('XBOX SERIES S'.ljust(34, '.'), "R$9,00 (Valor da hora)")
                tempo = int(input('Quantas horas você deseja jogar? '))
                valor3 = 9.00
                print(f'O valor cobrado será de R$ {tempo * valor3:,.2f}')
                print( 'Caro jogador por favor compareça ao caixa da loja para pagar o valor informado e garantir a sua reserva! ')

            if plataforma4 in plataformaparaReserva:
                print('XBOX SERIES X'.ljust(34, '.'), "R$10,00 (Valor da hora)")
                tempo = int(input('Quantas horas você deseja jogar? '))
                valor4 = 10.00
                print(f'O valor cobrado será de R$ {tempo * valor4:,.2f}')
                print(  'Caro jogador por favor compareça ao caixa da loja para pagar o valor informado e garantir a sua reserva! ')

            if plataforma5 in plataformaparaReserva:
                print('PC'.ljust(34, '.'), "R$5,00 (Valor da hora)")
                tempo = int(input('Quantas horas você deseja jogar? '))
                valor5 = 5.00
                print(f'O valor cobrado será de R$ {tempo * valor5:,.2f}')
                print('Caro jogador por favor compareça ao caixa da loja para pagar o valor informado e garantir a sua reserva! ')

                pesquisa_satisfacao()



pass

def usuario_nao_autenticado():
    """
        Lida com a opção de usuário não identificado.
        """
    escolhas_usuario()
    comecar_tempo()
    pesquisa_satisfacao()

pass


def preencher_endereco():
    """
        Lida com o preenchimento dos dados de endereço por parte do usuário.
        """
    rua = input("Digite o nome da rua: ")
    numero = int(input('Digite o número: '))
    complemento = input('Digite o complemento: ')
    bairro = input('Digite o bairro: ')
    while True:
        cep = input('Caro cliente, você poderia por favor nos informar o seu CEP? ').replace('-', '')
        caracteres = len(cep)
        if caracteres != 8:
            print('CEP inválido! Por favor, digite novamente: ')
            continue
        else:
            print(f'Obrigado pela confirmação! ')
            break
    cidade = input('Digite a cidade: ')
    estado = input('Digite o estado: ')
    print('Obrigado, os seus dados de endereço foram atualizados!')

pass

def regras_creditos():
    # Exibir as regras para créditos disponíveis
    regras_creditos = solicitar_opcao("""
Você deseja ler nossas regras para a utilização de créditos disponíveis? (DIGITE APENAS O NÚMERO)

[1] SIM
[2] NÃO
            """)

    if regras_creditos == '1':
        print("""
Para utilizar créditos disponíveis:
- O tempo mínimo é de 60 minutos.
- Créditos não utilizados expiram após 90 dias.
- Consulte nossa política completa em nosso site.
Boa diversão! :-)
                """)
    else:
        print('Ok, você optou por não ler as regras de créditos disponíveis.')
pass

def calendario():
    import calendar
    from datetime import datetime

    # Capturar o ano e o mês atual
    hoje = datetime.now()
    ano_atual = hoje.year
    mes_atual = hoje.month

    # Gerar o calendário do mês atual
    calendario = calendar.month(ano_atual, mes_atual)
    print(calendario)

pass

def validacao_cpf():
    """
            Lida com a validação do CPF.
            """
    while True:
        cpf = input(
            'Caro cliente, você poderia por favor nos informar o seu CPF? ').replace('-', '')
        caracteres = len(cpf)
        if caracteres != 11:
            print('CPF inválido! Por favor, digite novamente: ')
            continue
        else:
            print(f'Obrigado pela confirmação, já localizamos o seu cadastro! ')
            break
pass

def validacao_email():
    """
                Lida com a validação do EMAIL.
                """
    email = input('Digite seu email: ')
    while '@' not in email:
        print('E-mail inválido! Por favor, digite novamente.')
        email = input('Digite seu email: ')
pass

def enviar_reserva():
    """
                   Lida com confrimação do envio por email das infromações sobre a reserva.
                   """
    enviar_confirmacao = input("""
Você deseja que as informações da sua reserva sejam enviadas por Email?(DIGITE APENAS O NÚMERO)

[OPÇÃO 1] SIM
[OPÇÃO 2] NÃO

                                                                """)
    match enviar_confirmacao:
        case '1':
            print('Ok, você deseja o envio das informações da sua reserva por Email!')
            validacao_email()
            print('As informações foram enviadas por Email!')
        case '2':
            print('Ok, as informações da sua reserva não serão enviadas por Email! ')

pass

def pesquisa_satisfacao():

    nota = int(input("Digite sua nota de 1 a 10 para avaliar o nosso atendimento: "))
    match nota:
        case _ if nota < 0:
            print(f"\nNota inválida")
        case _ if nota <= 4:
            print(f"\nPéssimo atendimento: {nota}")
        case _ if nota <= 7:
            print(f"\nAtendimento pode melhorar: {nota}")
        case _ if nota <= 9:
            print(f"\nÓtimo atendimento: {nota}")
        case _ if nota <= 10:
            print(f"\nExcelente atendimento: {nota}")
        case _:
            print(f"\nNota inválida")

pass

def alugar_jogos():
    """
    Lida com as interações relacionadas ao aluguel de jogos.
    """
    print("\n***** Você escolheu a opção ALUGAR JOGOS! *****\n")
    # Aqui você adicionaria a lógica para alugar jogos
pass

def inscricoes_campeonatos():
    """
    Lida com inscrições de campeonatos.
    """
    print("\n***** Você escolheu a opção INSCRIÇÕES PARA CAMPEONATOS! *****\n")
    # Lógica específica para inscrições de campeonatos
pass


def experiencia_vr():
    """
    Lida com a experiência de Realidade Virtual (VR).
    """
    print("\n***** Você escolheu a opção EXPERIÊNCIA VR! *****\n")
    # Lógica para VR
pass


def simulador_corrida():
    """
    Lida com interações relacionadas ao simulador de corrida.
    """
    print("\n***** Você escolheu a opção SIMULADOR DE CORRIDA! *****\n")
    # Lógica para o simulador de corrida
pass


def executar_sistema():
    """
    Função principal que gerencia o fluxo do sistema com base na opção do menu principal.
    """
    while True:
        opcao = mostrar_menu_principal()

        if opcao == "1":
            lan_house()
        elif opcao == "2":
            alugar_jogos()
        elif opcao == "3":
            inscricoes_campeonatos()
        elif opcao == "4":
            experiencia_vr()
        elif opcao == "5":
            simulador_corrida()
        elif opcao == "0":
            print("\nObrigado por visitar a VG10 Games! Até breve!")
            break
        else:
            print("\nOpção inválida! Por favor, escolha um número do menu.")




# Testando o sistema
executar_sistema()





