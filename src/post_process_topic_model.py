# src/postprocess_topic_model.py

import pandas as pd

def extract_topic_info(topic_model, top_n_words: int = 5) -> pd.DataFrame:
    """
    Extracts topic info with top_n_words per topic.
    """
    # Get basic topic info
    topic_info = topic_model.get_topic_info()
    topic_info = topic_info[topic_info.Topic != -1]  # exclude outliers
    
    # Extract words for each topic
    topic_words = {}
    for topic in topic_info["Topic"]:
        words = topic_model.get_topic(topic)
        if words:  # Skip empty topics
            words = [word for word, _ in words[:top_n_words]]
            topic_words[topic] = ", ".join(words)
    
    # Add words to dataframe
    topic_info["Top_Words"] = topic_info["Topic"].map(topic_words)
    
    return topic_info[["Topic", "Top_Words", "Count"]]

def assign_topics_to_docs(df: pd.DataFrame, topics: list, probs: list) -> pd.DataFrame:
    """
    Adds topic and probability to each document in the DataFrame.
    """
    df = df.copy()
    df["Topic"] = topics
    df["Topic_Probability"] = probs
    return df

def summarize_topics(df_with_topics: pd.DataFrame) -> pd.DataFrame:
    """
    Simple summarization: top 3 documents by confidence per topic.
    """
    summaries = []
    for topic_id in df_with_topics["Topic"].unique():
        if topic_id == -1:
            continue
        topic_df = df_with_topics[df_with_topics["Topic"] == topic_id]
        top_docs = topic_df.sort_values("Topic_Probability", ascending=False).head(3)
        summary = " | ".join(top_docs["response"].values)
        summaries.append({"Topic": topic_id, "Summary": summary})
    return pd.DataFrame(summaries)
