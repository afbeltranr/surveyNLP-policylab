import pandas as pd
import os
from bertopic import BERTopic
from sentence_transformers import SentenceTransformer

def load_data(path="data/processed/survey_clean.csv"):
    df = pd.read_csv(path)
    return df["response_clean"].tolist(), df

def train_topic_model(docs, model_name="all-MiniLM-L6-v2"):
    embedding_model = SentenceTransformer(model_name)
    topic_model = BERTopic(embedding_model=embedding_model, verbose=False)
    topics, probs = topic_model.fit_transform(docs)
    return topic_model, topics, probs

def save_topic_info(topic_model, df, topics, out_path="outputs/topics.csv"):
    df["topic"] = topics
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    df.to_csv(out_path, index=False)
    topic_model.save("outputs/bertopic_model")
    print(f"✅ Topics and model saved to {out_path} and outputs/bertopic_model/")

def run_modeling_pipeline():
    docs, df = load_data()
    topic_model, topics, probs = train_topic_model(docs)
    save_topic_info(topic_model, df, topics)

if __name__ == "__main__":
    run_modeling_pipeline()
