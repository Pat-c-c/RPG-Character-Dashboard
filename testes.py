import pandas as pd

def create_mission_dataframe():
    data = {
        "Missão": [
            "Escalar uma parede ou superfície íngreme",
            "Desarmar uma armadilha",
            "Persuadir um NPC",
            "Identificar uma criatura mágica ou encantada",
            "Lidar com um animal selvagem ou domar uma criatura",
            "Resistir ao medo ou manipulação mental",
            "Escalar uma parede ou superfície íngreme",
            "Desarmar uma armadilha",
            "Persuadir um NPC",
            "Identificar uma criatura mágica ou encantada",
            "Lidar com um animal selvagem ou domar uma criatura",
            "Resistir ao medo ou manipulação mental",
            "Escalar uma parede ou superfície íngreme",
            "Desarmar uma armadilha",
            "Persuadir um NPC",
            "Identificar uma criatura mágica ou encantada",
            "Lidar com um animal selvagem ou domar uma criatura",
            "Resistir ao medo ou manipulação mental",
            "Escalar uma parede ou superfície íngreme",
            "Desarmar uma armadilha",
            "Persuadir um NPC",
            "Identificar uma criatura mágica ou encantada",
            "Lidar com um animal selvagem ou domar uma criatura",
            "Resistir ao medo ou manipulação mental",
            "Escalar uma parede ou superfície íngreme",
            "Desarmar uma armadilha",
            "Persuadir um NPC",
            "Identificar uma criatura mágica ou encantada",
            "Lidar com um animal selvagem ou domar uma criatura",
            "Resistir ao medo ou manipulação mental",
            "Escalar uma parede ou superfície íngreme",
            "Desarmar uma armadilha",
            "Persuadir um NPC",
            "Identificar uma criatura mágica ou encantada",
            "Lidar com um animal selvagem ou domar uma criatura",
            "Resistir ao medo ou manipulação mental"
        ],
        "Classe": [
            "Patrulheiro", "Patrulheiro", "Patrulheiro", "Patrulheiro", "Patrulheiro", "Patrulheiro",
            "Paladina", "Paladina", "Paladina", "Paladina", "Paladina", "Paladina",
            "Berserker", "Berserker", "Berserker", "Berserker", "Berserker", "Berserker",
            "Bruxo", "Bruxo", "Bruxo", "Bruxo", "Bruxo", "Bruxo",
            "Bardo", "Bardo", "Bardo", "Bardo", "Bardo", "Bardo",
            "Feiticeiro", "Feiticeiro", "Feiticeiro", "Feiticeiro", "Feiticeiro", "Feiticeiro"
        ],
        "Pontos": [
            5, 8, -2, -2, 8, 2,
            -2, -3, 7, -2, 2, 8,
            -5, -4, -5, -3, 4, 5,
            -4, 6, 6, 8, -2, 6,
            -3, 4, 8, 5, 6, 4,
            -3, -3, 5, 7, -3, 7
        ]
    }
    df = pd.DataFrame(data)
    return df

if __name__ == "__main__":
    df = create_mission_dataframe()
    print(df)
    df.to_csv("missions_data.csv", index=False)
