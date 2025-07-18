import pandas as pd
import pytest
from src.post_process_topic_model import extract_topic_info, assign_topics_to_docs, summarize_topics

def test_assign_topics_to_docs():
    # Create dummy data
    df = pd.DataFrame({
        "response": ["text1", "text2"],
        "region": ["reg1", "reg2"]
    })
    topics = [0, 1]
    probs = [0.8, 0.9]
    
    result = assign_topics_to_docs(df, topics, probs)
    
    assert "Topic" in result.columns
    assert "Topic_Probability" in result.columns
    assert len(result) == 2
    assert list(result["Topic"]) == topics
    assert list(result["Topic_Probability"]) == probs

def test_summarize_topics():
    # Create dummy data with topics
    df = pd.DataFrame({
        "response": ["text1", "text2", "text3"],
        "Topic": [0, 0, 1],
        "Topic_Probability": [0.8, 0.7, 0.9]
    })
    
    result = summarize_topics(df)
    
    assert isinstance(result, pd.DataFrame)
    assert "Topic" in result.columns
    assert "Summary" in result.columns
    assert len(result) == len(df["Topic"].unique())  # No need to subtract 1 since we don't have topic -1 in test data
