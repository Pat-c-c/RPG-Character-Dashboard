import pandas as pd

def create_weapon_dataframe():
    data = {
        "Classe": [
            "Patrulheiro",
            "Paladina",
            "Berserker",
            "Bruxo",
            "Bardo",
            "Feiticeiro"
        ],
        "Arma": [
            "Arco Longo",
            "Espada Longa",
            "Machado Grande",
            "Livro de Magias",
            "Lira",
            "Cajado de Cristal"
        ],
        "Tipo de Dano": [
            "Perfurante",
            "Cortante",
            "Cortante",
            "-",
            "-",
            "Contundente"
        ],
        "describe_weapon": [
            "Uma arma de longo alcance, perfeita para ataques a distância.",
            "Uma espada versátil usada por cavaleiros e paladinos.",
            "Uma arma pesada e potente, ideal para ataques devastadores.",
            "Utilizado por bruxos, é um foco para a realização de feitiços.",
            "Uma ferramenta musical que também pode ser usada para controle de multidões.",
            "Usado para canalizar magias poderosas e efeitos arcânicos."
        ]
    }
    df = pd.DataFrame(data)
    return df

if __name__ == "__main__":
    df = create_weapon_dataframe()
    print(df)
    df.to_csv("weapons_data.csv", index=False)
