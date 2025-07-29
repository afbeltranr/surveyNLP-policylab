import pandas as pd
import re
import os

from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt')

# Spanish stop words to exclude from removal
KEEP_WORDS = {'no', 'hay', 'sin', 'sobre', 'muy', 'mucho', 'muchos', 'mucha', 'muchas'}

# Define Spanish stop words (excluding KEEP_WORDS)
STOP_WORDS = {
    'mi', 'segun', 'personalmente', 'hablando', 'la', 'el', 'en', 'y', 'a', 'los', 'del',
    'se', 'las', 'por', 'un', 'para', 'con', 'una', 'su', 'al', 'lo', 'como',
    'mas', 'pero', 'sus', 'le', 'ya', 'o', 'este', 'si', 'porque', 'esta',
    'entre', 'cuando', 'este', 'esto', 'esta', 'estos', 'estas'
} - KEEP_WORDS

def clean_response(text: str) -> str:
    # Convert to lowercase
    text = text.lower()
    
    # Remove noise patterns
    noise_patterns = [
        r"\bsegun mi experiencia\b",
        r"\ben mi comunidad\b",
        r"\bpersonalmente hablando\b"
    ]
    for pattern in noise_patterns:
        text = re.sub(pattern, "", text)
    
    # Tokenize and remove stop words while keeping important negations and descriptors
    tokens = word_tokenize(text)
    tokens = [token for token in tokens if token not in STOP_WORDS]
    
    # Rejoin tokens and standardize spacing
    text = " ".join(tokens)
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
