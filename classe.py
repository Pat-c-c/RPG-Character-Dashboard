import pandas as pd

def create_class_dataframe():
    data = {
        "Classe": [
            "Patrulheiro",
            "Paladina",
            "Berserker",
            "Bruxo",
            "Bardo",
            "Feiticeiro"
        ],
        "Descrição da Classe": [
            "Especialistas em rastrear e se mover silenciosamente pela natureza. Ágeis, habilidosos com arcos e sempre prontos para proteger os inocentes das ameaças naturais.",
            "Guerreiras devotas, com grande habilidade em combate e proteção. Sua fé as fortalece, e sua missão é lutar pela justiça e defender os necessitados.",
            "Guerreiros destemidos, conhecidos por sua força bruta e fúria incontrolável. Quando em batalha, sua resistência os torna temíveis, mas sua falta de controle emocional pode ser um risco.",
            "Mestres das artes mágicas, capazes de manipular a realidade com suas magias. Sua busca pelo conhecimento os torna poderosos, mas também isolados do resto do mundo.",
            "Artistas e mestres das palavras. Suas músicas e histórias encantam os outros e podem mudar o curso das situações, usando carisma e magia para influenciar os aliados.",
            "Especialistas em magia arcana e ocultismo. Seu vasto conhecimento sobre as artes místicas os torna poderosos, mas sua busca pelo poder pode levá-los ao isolamento."
        ]
    }
    df = pd.DataFrame(data)
    return df

if __name__ == "__main__":
    df = create_class_dataframe()
    print(df)
    df.to_csv("classes_data.csv", index=False)
