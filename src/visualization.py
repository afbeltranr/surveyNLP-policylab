import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import os
from topic_labels import get_topic_label, get_topic_category, get_category_color
import numpy as np

class InsightVisualizer:
    def __init__(self, output_dir="visuals"):
        """Initialize with output directory for saving plots."""
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
        # Set style for all plots
        plt.style.use('seaborn-v0_8')
        
    def _save_plot(self, name):
        """Helper to save plots with consistent styling."""
        plt.tight_layout()
        path = os.path.join(self.output_dir, f"{name}.png")
        plt.savefig(path, dpi=300, bbox_inches='tight')
        plt.close()
        return path

    def plot_topic_distribution(self, df):
        """Create bar plot of topic distribution with labels."""
        plt.figure(figsize=(15, 8))
        
        # Get topic counts and create DataFrame with labels
        topic_counts = df['Topic'].value_counts().sort_index()
        plot_data = pd.DataFrame({
            'Topic': topic_counts.index,
            'Count': topic_counts.values,
            'Label': [get_topic_label(t) for t in topic_counts.index],
            'Category': [get_topic_category(t) for t in topic_counts.index]
        })
        
        # Sort by category and count
        plot_data = plot_data.sort_values(['Category', 'Count'], ascending=[True, False])
        
        # Create color palette based on categories
        colors = [get_category_color(cat) for cat in plot_data['Category']]
        
        # Create bar plot
        bars = plt.bar(range(len(plot_data)), plot_data['Count'], color=colors)
        
        # Customize the plot
        plt.title('Distribution of Topics Across All Responses', pad=20, size=14)
        plt.xlabel('Topics by Category', size=12)
        plt.ylabel('Number of Responses', size=12)
        
        # Set x-axis labels
        plt.xticks(range(len(plot_data)), plot_data['Label'], rotation=45, ha='right')
        
        # Add legend for categories
        handles = [plt.Rectangle((0,0),1,1, color=get_category_color(cat)) 
                  for cat in sorted(set(plot_data['Category']))]
        plt.legend(handles, sorted(set(plot_data['Category'])), 
                  title='Categories', loc='upper right')
        
        # Adjust layout
        plt.tight_layout()
        return self._save_plot('topic_distribution')

    def plot_region_topic_heatmap(self, df):
        """Create heatmap of topics by region with labeled topics."""
        plt.figure(figsize=(15, 10))
        
        # Create pivot table of regions and topics
        topic_by_region = pd.crosstab(df['region'], df['Topic'])
        
        # Rename columns with topic labels
        topic_by_region.columns = [get_topic_label(t) for t in topic_by_region.columns]
        
        # Normalize by region
        topic_by_region_norm = topic_by_region.div(topic_by_region.sum(axis=1), axis=0)
        
        # Create heatmap with better formatting
        sns.heatmap(topic_by_region_norm, 
                   annot=True, 
                   fmt='.2f', 
                   cmap='YlOrRd',
                   cbar_kws={'label': 'Proportion of Responses'},
                   linewidths=0.5)
        
        plt.title('Topic Distribution by Region', pad=20, size=14)
        plt.xlabel('Topics', size=12)
        plt.ylabel('Region', size=12)
        
        # Rotate x-axis labels for better readability
        plt.xticks(rotation=45, ha='right')
        plt.yticks(rotation=0)
        
        return self._save_plot('region_topic_heatmap')

    def plot_group_insights(self, df):
        """Create grouped bar plot of topics by population group."""
        plt.figure(figsize=(15, 6))
        group_topic = pd.crosstab(df['group'], df['Topic'])
        group_topic_norm = group_topic.div(group_topic.sum(axis=1), axis=0)
        
        group_topic_norm.plot(kind='bar', stacked=True)
        plt.title('Topic Distribution by Population Group')
        plt.xlabel('Population Group')
        plt.ylabel('Proportion of Responses')
        plt.legend(title='Topic', bbox_to_anchor=(1.05, 1))
        return self._save_plot('group_topic_distribution')

    def generate_wordclouds(self, df, topic_words):
        """Generate wordcloud for each topic."""
        for topic_id, words in topic_words.items():
            if topic_id == -1:  # Skip outlier topic if present
                continue
                
            wordcloud = WordCloud(
                width=800, 
                height=400,
                background_color='white'
            ).generate_from_frequencies(dict(words))
            
            plt.figure(figsize=(10, 5))
            plt.imshow(wordcloud, interpolation='bilinear')
            plt.axis('off')
            plt.title(f'Topic {topic_id} Key Terms')
            self._save_plot(f'wordcloud_topic_{topic_id}')

def create_all_visualizations(df_path="outputs/df_with_topics.csv", 
                            topic_info_path="outputs/topic_info.csv"):
    """Main function to create all visualizations."""
    # Load data
    df = pd.read_csv(df_path)
    topic_info = pd.read_csv(topic_info_path)
    
    # Initialize visualizer
    viz = InsightVisualizer()
    
    # Generate all plots
    viz.plot_topic_distribution(df)
    viz.plot_region_topic_heatmap(df)
    viz.plot_group_insights(df)
    
    # For word clouds, we need to process topic info
    # Convert comma-separated words into frequency dictionaries
    topic_words = {}
    for _, row in topic_info.iterrows():
        words = row['Top_Words'].split(', ')
        # Create a simple frequency dict (all words equal weight for now)
        topic_words[row['Topic']] = {word: 1 for word in words}
    viz.generate_wordclouds(df, topic_words)
    
    print("✅ All visualizations saved in /visuals directory")

if __name__ == "__main__":
    create_all_visualizations()
