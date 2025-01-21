import pandas as pd

def create_character_dataframe():
    data = {
        "Nome": [
            "Leonidas",
            "Joana D'Arc",
            "AlexandreGrande",
            "Merlin",
            "Fantasma da Ópera",
            "Rasputin"
        ],
        "Classe": [
            "Patrulheiro",
            "Paladina",
            "Berserker",
            "Bruxo",
            "Bardo",
            "Feiticeiro"
        ],
        "Nível": [15, 12, 20, 18, 16, 14],
        "Força": [12, 10, 18, 8, 6, 8],
        "Inteligencia": [9, 15, 10, 20, 16, 18],
        "Destreza": [13, 8, 14, 10, 8, 10],
        "Vida": [14, 12, 20, 12, 10, 14],
        "Ouro": [40, 25, 30, 35, 25, 30],
        "Velocidade": [11, 8, 10, 10, 12, 11],
        "Resistência": [10, 10, 14, 8, 6, 9],
        "Mana": [7, 15, 5, 20, 18, 22],
        "Carisma": [7, 14, 10, 18, 20, 16]
    }
    df = pd.DataFrame(data)
    return df

if __name__ == "__main__":
    df = create_character_dataframe()
    print(df)
    df.to_csv("characters_data.csv", index=False)
