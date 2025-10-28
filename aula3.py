Início

    // Criar uma fila vazia
    Fila ← fila_vazia()

    // Inserir 3 pacientes na fila
    Para i de 1 até 3 faça
        Escreva("Digite o nome do paciente ", i, ": ")
        Leia(nome)
        
        Escreva("Digite o CPF do paciente ", i, ": ")
        Leia(cpf)
        
        paciente ← (nome, cpf)
        Enfileirar(Fila, paciente)
    FimPara

    // Remover o primeiro paciente da fila (atendimento)
    paciente_atendido ← Desenfileirar(Fila)
    Escreva("Paciente atendido: ", paciente_atendido.nome, " - CPF: ", paciente_atendido.cpf)

    // Mostrar pacientes restantes na fila
    Escreva("Pacientes ainda na fila:")
    Para cada paciente em Fila faça
        Escreva("Nome: ", paciente.nome, " - CPF: ", paciente.cpf)
    FimPara

Fim

    