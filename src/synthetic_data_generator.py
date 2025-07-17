import pandas as pd
import random
import os

# Define possible responses and metadata
regions = ['Pacifico', 'Amazonas', 'Andina', 'Orinoquia', 'Caribe']
groups = ['Mujeres', 'Jovenes', 'Afrocolombianos', 'Pueblos Indigenas', 'Personas Mayores']
questions = [
    "Que necesidades prioritarias existen en su comunidad?",
    "Como evalua la atencion en salud mental en su zona?",
    "Que propuestas ha escuchado dentro de la comunidad?",
    "Que problemas enfrenta con el acceso a servicios publicos?"
]

# Template answer banks
answers_by_theme = {
    "Condiciones de vida": [
        "Falta de acceso al agua potable",
        "Viviendas en mal estado",
        "Cortes de luz frecuentes",
        "No hay recoleccion de basuras"
    ],
    "Salud": [
        "No hay atencion medica cerca",
        "La salud mental es ignorada",
        "Faltan medicamentos esenciales",
        "Hay demoras en las citas"
    ],
    "Trabajo e ingresos": [
        "No hay empleo local",
        "Los jovenes migran por falta de oportunidades",
        "No hay apoyo a emprendimientos",
        "La economia informal domina"
    ],
    "Relacion comunidad-Estado": [
        "Falta de confianza en las instituciones",
        "No hay participacion comunitaria",
        "Nadie responde a nuestras solicitudes",
        "Nos sentimos abandonados"
    ]
}

def generate_response():
    theme = random.choice(list(answers_by_theme.keys()))
    phrase = random.choice(answers_by_theme[theme])
    noise = random.choice(["", "", " (segun mi experiencia)", " en mi comunidad", " personalmente hablando"])
    return f"{phrase}{noise}"

def generate_dataset(n=200):
    data = []
    for _ in range(n):
        region = random.choice(regions)
        group = random.choice(groups)
        question = random.choice(questions)
        response = generate_response()
        data.append({
            "region": region,
            "group": group,
            "question": question,
            "response": response
        })
    return pd.DataFrame(data)

def save_dataset(df, out_path="data/raw/survey_data.csv"):
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    df.to_csv(out_path, index=False)
    print(f"✅ Synthetic data saved to {out_path}")

if __name__ == "__main__":
    df = generate_dataset(n=300)
    save_dataset(df)
