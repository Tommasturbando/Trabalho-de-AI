import random
# Dicionário de camisolas de futebol na loja
camisolas_futebol = {
        "Camisola Barcelona 23/24": {
        "preco": 100.00,
        "quantidade": random.randint(10,100),
        "tamanhos": ["S", "M", "L", "XL"],
        
    },
        "Camisola Real Madrid 23/24": {
        "preco": 100.00,
        "quantidade":random.randint(10,100),
        "tamanhos": ["M", "L", "XL"],
     },
        "Camisola Paris Saint-Germain 23/24": {
        "preco": 100.00,
        "quantidade": random.randint(10,100),
        "tamanhos": ["S"],

    },
    "Camisola Manchester United 20/21": {
        "preco": 59.99,
        "quantidade": random.randint(10,100),
        "tamanhos": ["XXL"],
    },
    "Camisola Juventus 18/19": {
        "preco": 30.00,
        "quantidade": random.randint(10,100),
        "tamanhos": ["S"],
    },
    "Camisola Bayern Munique 23/24": {
        "preco": 100.00,
        "quantidade": random.randint(10,100),
        "tamanhos": ["M", "L"],
    },
    "Camisola Sporting 23/24": {
        "preco": 100.00,
        "quantidade": random.randint(10,100),
        "tamanhos": ["S", "M", "L"],
    }
}

def print_loja():
    # Exibindo as camisolas e suas informações
    print("Camisas de Futebol disponíveis na loja:\n")
    for camisola, detalhes in camisolas_futebol.items():
        print(f"Produto: {camisola}")
        print(f"Preço: ${detalhes['preco']:.2f}")
        print(f"Quantidade em estoque: {detalhes['quantidade']}")
        print(f"Tamanhos disponíveis: {', '.join(detalhes['tamanhos'])}")
        print("-" * 40)  # Linha separadora
    print()
    print()
    print()

print_loja()


#Update camisolas de futebol na loja
def update_quantidade_camisolas(camisola, nova_quantidade):
    camisola_update = camisolas_futebol[camisola]
    quantidade = camisola_update['quantidade']
    camisola_update['quantidade'] = nova_quantidade
    camisolas_futebol[camisola]=camisola_update

update_quantidade_camisolas("Camisola Manchester United 20/21", random.randint(10,100))
update_quantidade_camisolas("Camisola Sporting 23/24", random.randint(10,100))
update_quantidade_camisolas("Camisola Real Madrid 23/24", 0) 

# Função principal da loja
def loja():
    while True:
        print("\nOpções:")
        print("1. Adicionar nova Camisola")
        print("2. Remover Camisola")
        print("3. Ver detalhes de todas as camisolas")
        print("4. Sair da loja")

        escolha = input("Escolha uma operação (1-4): ")

        if escolha == "1":
            nome = input("Digite o nome da camisola: ")
            preco = float(input("Digite o preço da camisola: "))
            quantidade = int(input("Digite a quantidade em estoque: "))
            tamanhos = input("Digite os tamanhos disponíveis (separados por vírgula): ").split(",")
            
            camisolas_futebol[nome] = {
                "preco": preco,
                "quantidade": quantidade,
                "tamanhos": [tam.strip() for tam in tamanhos]
            }
            print(f"\nCamisola '{nome}' adicionada com sucesso!")

        elif escolha == "2":
            nome = input("Digite o nome da camisola que deseja remover: ")
            if nome in camisolas_futebol:
                del camisolas_futebol[nome]
                print(f"\nCamisola '{nome}' removida com sucesso!")
            else:
                print("\nCamisola não encontrada!")

        elif escolha == "3":
            print_loja()

        elif escolha == "4":
            print("\nSaindo da loja. Até logo!")
            break

        else:
            print("\nOpção inválida! Tente novamente.")

# Chamar a função principal para iniciar a loja
loja()

print_loja()


