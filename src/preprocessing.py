import pandas as pd
import re
import os

# Define basic cleaning function
def clean_response(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)  # remove punctuation
    noise_patterns = [
        r"\bsegun mi experiencia\b",
        r"\ben mi comunidad\b",
        r"\bpersonalmente hablando\b"
    ]
    for pattern in noise_patterns:
        text = re.sub(pattern, "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

def preprocess_dataset(input_path="data/raw/survey_data.csv", output_path="data/processed/survey_clean.csv"):
    df = pd.read_csv(input_path)
    df["response_clean"] = df["response"].apply(clean_response)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"✅ Preprocessed data saved to {output_path}")

if __name__ == "__main__":
    preprocess_dataset()
