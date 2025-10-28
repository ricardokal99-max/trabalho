# Lista para armazenar os pacientes
pacientes = []

def cadastrar_paciente():
    nome = input("Nome do paciente: ").strip()
    idade = int(input("Idade do paciente: "))
    telefone = input("Telefone do paciente: ").strip()
    pacientes.append({"nome": nome, "idade": idade, "telefone": telefone})
    print("Paciente cadastrado com sucesso!\n")

def exibir_estatisticas():
    if not pacientes:
        print("Nenhum paciente cadastrado.\n")
        return

    total = len(pacientes)
    idades = [p["idade"] for p in pacientes]
    media_idade = sum(idades) / total

    mais_novo = min(pacientes, key=lambda p: p["idade"])
    mais_velho = max(pacientes, key=lambda p: p["idade"])

    print(f"\nNúmero total de pacientes: {total}")
    print(f"Idade média dos pacientes: {media_idade:.2f}")
    print(f"Paciente mais novo: {mais_novo['nome']} ({mais_novo['idade']} anos)")
    print(f"Paciente mais velho: {mais_velho['nome']} ({mais_velho['idade']} anos)\n")

def buscar_paciente():
    nome_busca = input("Digite o nome do paciente que deseja buscar: ").strip().lower()
    encontrados = [p for p in pacientes if nome_busca in p["nome"].lower()]

    if encontrados:
        print("\nPacientes encontrados:")
        for p in encontrados:
            print(f"Nome: {p['nome']}, Idade: {p['idade']}, Telefone: {p['telefone']}")
        print()
    else:
        print("Paciente não encontrado.\n")

def menu():
    while True:
        print("=== Sistema da Clínica ===")
        print("1. Cadastrar paciente")
        print("2. Ver estatísticas")
        print("3. Buscar paciente")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_paciente()
        elif opcao == '2':
            exibir_estatisticas()
        elif opcao == '3':
            buscar_paciente()
        elif opcao == '4':
            print("Saindo do sistema. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

# Iniciar o programa
menu()
