# Função para exibir o histórico
def exibir_historico(historico):
    if not historico:
        print("Histórico vazio.")
    else:
        print("Histórico:")
        for i, entrada in enumerate(historico, 1):
            print(f"{i}. {entrada}")

# Função principal da calculadora
def calculadora():
    historico = []  # Lista para guardar o histórico das operações

    while True:
        print("\nOpções:")
        print("1. Somar")
        print("2. Subtrair")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Ver histórico")
        print("6. Sair")

        escolha = input("Escolha uma operação (1-6): ")
        if escolha == "6":
            print("A sair da calculadora.")
            break
        elif escolha == "5":
            exibir_historico(historico)
        elif escolha in ["1", "2", "3", "4"]:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
