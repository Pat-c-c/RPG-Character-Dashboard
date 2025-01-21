import pandas as pd

def create_character_description_dataframe():
    data = {
        "Personagem": [
            "Leonidas",
            "Joana D'Arc",
            "AlexandreGrande",
            "Merlin",
            "Fantasma da Ópera",
            "Rasputin"
        ],
        "Descrição do Personagem": [
            "É um mestre na arte de caçar e rastrear, sempre à frente nas batalhas contra as forças naturais. Prefere a solidão e tem grande habilidade de se mover silenciosamente, embora suas interações sociais sejam limitadas.",
            "Uma líder devota com uma fé inabalável. Luta pela justiça e proteção dos inocentes, sendo uma guerreira corajosa, embora mais focada em combate e defesa do que em magia.",
            "Movido pela fúria e força bruta. Quando em batalha, sua resistência física e impetuosidade o tornam imbatível, mas sua falta de controle emocional o coloca em risco.",
            "Mago profundo, especialista em magia e controle mental. Sua busca por conhecimento mágico o torna distante, mas suas habilidades em manipular a realidade são incomparáveis.",
            "Artista talentoso cujas músicas influenciam as emoções dos outros. Sua habilidade de encantar e persuadir o torna valioso, mas seu passado sombrio o faz difícil de entender.",
            "Mestre das artes ocultas. Seu foco é obter poder a qualquer custo, manipulando forças mágicas para controlar o mundo ao seu redor, mas sua busca incessante por poder o torna impiedoso."
        ]
    }
    df = pd.DataFrame(data)
    return df

if __name__ == "__main__":
    df = create_character_description_dataframe()
    print(df)
    df.to_csv("character_descriptions.csv", index=False)
