import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict

def analyze_regional_distribution(df):
    """Create a heatmap of topic distribution across regions."""
    # Create pivot table of topic counts by region
    topic_region = pd.crosstab(df['region'], df['Topic'])
    
    # Normalize by region
    topic_region_norm = topic_region.div(topic_region.sum(axis=1), axis=0)
    
    # Create heatmap
    plt.figure(figsize=(15, 8))
    sns.heatmap(topic_region_norm, cmap='YlOrRd', annot=True, fmt='.2f')
    plt.title('Topic Distribution Across Regions')
    plt.xlabel('Topic ID')
    plt.ylabel('Region')
    plt.tight_layout()
    plt.savefig('visuals/topic_region_distribution.png')
    plt.close()
    
    return topic_region_norm

def evaluate_topic_quality(df):
    """Evaluate topic coherence using probability scores and topic size."""
    topic_metrics = {}
    
    # Calculate average probability by topic
    avg_probs = df.groupby('Topic')['Topic_Probability'].mean()
    
    # Calculate topic sizes
    topic_sizes = df['Topic'].value_counts()
    
    # Calculate topic diversity (unique responses per topic)
    topic_diversity = df.groupby('Topic')['response'].nunique() / topic_sizes
    
    # Combine metrics
    topic_metrics = pd.DataFrame({
        'avg_probability': avg_probs,
        'size': topic_sizes,
        'diversity': topic_diversity
    }).round(3)
    
    # Visualize metrics
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))
    
    # Plot average probabilities
    topic_metrics['avg_probability'].plot(kind='bar', ax=axes[0], color='skyblue')
    axes[0].set_title('Average Topic Assignment Probability')
    axes[0].set_xlabel('Topic ID')
    
    # Plot topic sizes
    topic_metrics['size'].plot(kind='bar', ax=axes[1], color='lightgreen')
    axes[1].set_title('Topic Sizes')
    axes[1].set_xlabel('Topic ID')
    
    # Plot topic diversity
    topic_metrics['diversity'].plot(kind='bar', ax=axes[2], color='salmon')
    axes[2].set_title('Topic Response Diversity')
    axes[2].set_xlabel('Topic ID')
    
    plt.tight_layout()
    plt.savefig('visuals/topic_quality_metrics.png')
    plt.close()
    
    return topic_metrics

def get_representative_responses(df, top_n=3):
    """Get most representative responses for each topic based on probability."""
    representative_responses = {}
    
    for topic in df['Topic'].unique():
        # Get responses for this topic, sorted by probability
        topic_responses = df[df['Topic'] == topic].sort_values(
            'Topic_Probability', ascending=False
        )[['response', 'Topic_Probability']].head(top_n)
        
        representative_responses[topic] = topic_responses
    
    # Save to CSV
    result_rows = []
    for topic, responses in representative_responses.items():
        for _, row in responses.iterrows():
            result_rows.append({
                'Topic': topic,
                'Response': row['response'],
                'Probability': row['Topic_Probability']
            })
    
    rep_df = pd.DataFrame(result_rows)
    rep_df.to_csv('outputs/representative_responses.csv', index=False)
    return representative_responses

def run_analysis(input_path='outputs/df_with_topics.csv'):
    """Run all analyses and generate visualizations."""
    print("Loading data...")
    df = pd.read_csv(input_path)
    
    print("Analyzing regional distribution...")
    region_dist = analyze_regional_distribution(df)
    
    print("Evaluating topic quality...")
    topic_metrics = evaluate_topic_quality(df)
    
    print("Finding representative responses...")
    rep_responses = get_representative_responses(df)
    
    print("✅ Analysis complete! Check visuals/ and outputs/ directories for results.")
