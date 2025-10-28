from collections import deque

# 1. Definição da estrutura de paciente
class Paciente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

# 2. Criar a fila (FIFO)
fila = deque()

# 3. Inserir 3 pacientes na fila
for i in range(1, 4):
    print(f"Digite os dados do paciente {i}:")
    nome = input("Nome: ")
    cpf = input("CPF: ")
    paciente = Paciente(nome, cpf)
    fila.append(paciente)  # Enfileirar

# 4. Remover o primeiro paciente da fila (atendimento)
if fila:
    paciente_atendido = fila.popleft()  # Desenfileirar
    print(f"\nPaciente atendido: {paciente_atendido.nome} - CPF: {paciente_atendido.cpf}")
else:
    print("\nA fila está vazia. Ninguém para atender.")

# 5. Mostrar quem ainda está na fila
print("\nPacientes ainda na fila:")
if fila:
    for paciente in fila:
        print(f"Nome: {paciente.nome} - CPF: {paciente.cpf}")
else:
    print("Nenhum paciente na fila.")