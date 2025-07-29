import pandas as pd
import os
import spacy
from bertopic import BERTopic
from sentence_transformers import SentenceTransformer
from sklearn.feature_extraction.text import CountVectorizer

# Load Spanish language model
nlp = spacy.load('es_core_news_sm')

# Custom stop words to keep
KEEP_WORDS = {
    'no', 'hay', 'sin', 'falta', 'cerca', 'lejos',
    'mal', 'bien', 'mejor', 'peor', 'mucho', 'poco'
}

def preprocess_text(text):
    """Process text using spaCy's Spanish model."""
    doc = nlp(text.lower())
    # Keep content words, numbers, and specific keep words
    tokens = [
        token.lemma_ for token in doc
        if (not token.is_stop or token.text in KEEP_WORDS) and
           (token.is_alpha or token.is_digit) and
           len(token.text) > 1
    ]
    return " ".join(tokens)

def load_data(path="data/processed/survey_clean.csv"):
    df = pd.read_csv(path)
    # Apply spaCy preprocessing
    texts = [preprocess_text(text) for text in df["response_clean"]]
    return texts, df

def train_topic_model(docs, model_name="all-MiniLM-L6-v2", language="spanish"):
    # Initialize sentence transformer for embeddings
    embedding_model = SentenceTransformer(model_name)
    
    # Define Spanish stop words
    spanish_stop_words = [
        'el', 'la', 'los', 'las', 'un', 'una', 'unos', 'unas', 'y', 'o', 'pero', 'si',
        'de', 'del', 'a', 'en', 'para', 'por', 'con', 'mi', 'tu', 'su', 'este',
        'esta', 'ese', 'esa', 'aquel', 'aquella', 'que', 'quien', 'cual', 'cuando',
        'donde', 'porque', 'como', 'segun', 'personalmente', 'hablando', 'experiencia'
    ]
    
    # Create custom vectorizer
    vectorizer_model = CountVectorizer(
        stop_words=spanish_stop_words,
        min_df=2,
        max_df=0.95,
        token_pattern=r'(?u)\b[a-záéíóúñ][a-záéíóúñ]+\b'
    )
    
    # Initialize BERTopic with minimal settings
    topic_model = BERTopic(
        embedding_model=embedding_model,
        vectorizer_model=vectorizer_model,
        language=language,
        min_topic_size=5,
        verbose=True
    )
    
    # Fit the model and transform documents
    topics = topic_model.fit_transform(docs)
    
    # Get the topic assignments (first element of tuple)
    if isinstance(topics, tuple):
        topics = topics[0]
    
    return topic_model, topics, None  # probabilities handled differently in newer versions

def save_topic_info(topic_model, df, topics, out_path="outputs/topics.csv"):
    # Save document-topic assignments
    df["Topic"] = topics
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    df.to_csv(out_path, index=False)
    
    # Get and save topic words
    topic_words = {}
    for topic_id in set(topics):
        topic_docs = df[df["Topic"] == topic_id]["response_clean"]
        # Use spaCy to extract key terms
        doc = nlp(" ".join(topic_docs))
        # Get most common content words
        word_freq = {}
        for token in doc:
            if token.is_alpha and not token.is_stop:
                word_freq[token.text] = word_freq.get(token.text, 0) + 1
        # Sort by frequency
        sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
        topic_words[topic_id] = [word for word, _ in sorted_words[:10]]
    
    # Create topic info DataFrame
    topic_info = pd.DataFrame({
        'Topic': topic_words.keys(),
        'Top_Words': [', '.join(words) for words in topic_words.values()],
        'Count': df['Topic'].value_counts()
    })
    
    # Save outputs
    os.makedirs("outputs", exist_ok=True)
    topic_info.to_csv("outputs/topic_info.csv", index=False)
    
    # Save model
    topic_model.save("outputs/bertopic_model")
    print(f"✅ Topics and model saved to outputs/")
    
    return topic_info

def run_modeling_pipeline():
    docs, df = load_data()
    topic_model, topics, probs = train_topic_model(docs)
    save_topic_info(topic_model, df, topics)

if __name__ == "__main__":
    run_modeling_pipeline()
