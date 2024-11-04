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
