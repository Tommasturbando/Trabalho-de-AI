# Dicionário de camisolas de futebol na loja
camisolas_futebol = {
        "Camisola Barcelona 23/24": {
        "preco": 100.00,
        "quantidade": 10,
        "tamanhos": ["S", "M", "L", "XL"],
        
    },
        "Camisola Real Madrid 23/24": {
        "preco": 100.00,
        "quantidade":5,
        "tamanhos": ["M", "L", "XL"],
     },
        "Camisola Paris Saint-Germain 23/24": {
        "preco": 100.00,
        "quantidade": 2,
        "tamanhos": ["S"],

    },
    "Camisola Manchester United 20/21": {
        "preco": 59.99,
        "quantidade": 4,
        "tamanhos": ["XXL"],
    },
    "Camisola Juventus 18/19": {
        "preco": 30.00,
        "quantidade": 2,
        "tamanhos": ["S"],
    },
    "Camisola Bayern Munique 23/24": {
        "preco": 100.00,
        "quantidade": 12,
        "tamanhos": ["M", "L"],
    },
    "Camisola Sporting 23/24": {
        "preco": 100.00,
        "quantidade": 7,
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
