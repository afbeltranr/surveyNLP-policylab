def test_bertopic_runs():
    from src.modeling import load_data, train_topic_model
    docs, _ = load_data("data/processed/survey_clean.csv")
    docs = docs[:20]  # use a small sample to keep test fast
    model, topics, probs = train_topic_model(docs)
    
    assert len(topics) == len(docs), "Topic assignment failed"
    assert hasattr(model, "get_topic_info"), "BERTopic model object is invalid"
