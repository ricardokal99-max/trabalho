# Bem-vindo à Maquina de Venda Automatica de Ingressos de Cinema!

# Solicitar a idade do cliente 
idade = int(input("Por favor, digite sua idade: "))

# Verificar a idade para sugestão de filmes
if idade < 12:
    print("Recomendamos o Filme up altas aventura.")
elif 12 <= idade < 18: 
    print("Recomendamos o Filme avatar.") 
else:
    print("Recomendamos o Fime bacural.")

# Verificar a disponibilidade  de ingressos 
quantidade_ingressos = 10 # suponha que haja 10 ingressos disponiveis
if quantidade_ingressos > 10:
    print("ingressos estão disponiveis. Divirta-se no cinema!")

elif quantidade_ingressos == 10:

else:
     print("Desculpe, todos os ingressos estão esgotados para hoje.")

