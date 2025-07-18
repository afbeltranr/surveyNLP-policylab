from modeling import train_topic_model
from post_process_topic_model import extract_topic_info, assign_topics_to_docs, summarize_topics
import pandas as pd
import os

def main():
    try:
        # Create output directory
        os.makedirs("outputs", exist_ok=True)

        # Read the synthetic survey data
        print("Loading data...")
        df = pd.read_csv("data/raw/survey_data.csv")
        
        # Train the topic model
        print("Training topic model...")
        topic_model, topics, probs = train_topic_model(df["response"].tolist())

        # Get labeled data
        print("Processing results...")
        df_with_topics = assign_topics_to_docs(df, topics, probs)

        # Extract topic-word mappings
        topic_info = extract_topic_info(topic_model)

        # Create basic summaries
        topic_summaries = summarize_topics(df_with_topics)

        # Save results
        print("Saving results...")
        topic_info.to_csv("outputs/topic_info.csv", index=False)
        df_with_topics.to_csv("outputs/df_with_topics.csv", index=False)
        topic_summaries.to_csv("outputs/topic_summaries.csv", index=False)
        
        print("✅ Topic modeling completed successfully!")
        
    except FileNotFoundError as e:
        print(f"❌ Error: Input file not found - {e}")
    except Exception as e:
        print(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    main()
