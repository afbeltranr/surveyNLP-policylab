# 🔍 SurveyNLP Pipeline
> Automated Topic Analysis for Territorial Survey Data

[![CI Status](https://github.com/afbeltranr/surveyNLP-policylab/actions/workflows/ci_pipeline.yaml/badge.svg)](https://github.com/afbeltranr/surveyNLP-policylab/actions)
[![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/)
[![BERTopic](https://img.shields.io/badge/NLP-BERTopic-orange.svg)](https://maartengr.github.io/BERTopic/)

A modular NLP system that processes qualitative survey responses to extract structured insights for evidence-based policy making. Built with modern NLP techniques and continuous integration practices.

## 🎯 Overview

```mermaid
flowchart LR
    subgraph Input[Data Sources]
        A1[Survey Responses] 
        A2[Demographic Data]
    end
    
    subgraph Process[NLP Pipeline]
        B[Text Processing]
        C[Topic Modeling]
        D[Analysis]
    end
    
    subgraph Output[Insights]
        E1[Regional Maps]
        E2[Topic Clusters]
        E3[Group Analysis]
    end
    
    Input --> Process
    Process --> Output
```

## 📊 Key Insights

### Regional Topic Distribution
![Regional Topic Heatmap](visuals/region_topic_heatmap.png)

### Population Group Analysis
![Group Topic Distribution](visuals/group_topic_distribution.png)

### Topic Clusters
![Topic Distribution](visuals/topic_distribution.png)

### Key Terms by Topic
<details>
<summary>Click to expand topic wordclouds</summary>

#### Topic 0
![Topic 0 Wordcloud](visuals/wordcloud_topic_0.png)

#### Topic 1  
![Topic 1 Wordcloud](visuals/wordcloud_topic_1.png)

#### Topic 2
![Topic 2 Wordcloud](visuals/wordcloud_topic_2.png)

#### Topic 3
![Topic 3 Wordcloud](visuals/wordcloud_topic_3.png)

[... and more topics]
</details>

## 🛠 Technical Architecture

```mermaid
graph TD
    A[Raw Survey Data] --> B[Data Preprocessing]
    B --> C[Text Cleaning]
    C --> D[BERTopic Modeling]
    D --> E[Topic Extraction]
    E --> F1[Regional Analysis]
    E --> F2[Group Analysis]
    E --> F3[Topic Distribution]
    F1 & F2 & F3 --> G[Visualization Generation]
    G --> H[Insight Reports]
```

## 🔄 Pipeline Components

1. **Data Generation & Preprocessing**
   - Synthetic survey data generation
   - Text cleaning and standardization

2. **Topic Analysis**
   - BERTopic modeling
   - Semantic clustering
   - Topic labeling

3. **Insight Generation**
   - Regional distributions
   - Population group patterns
   - Topic summaries

4. **Quality Assurance**
   - Continuous Integration
   - Automated testing
   - Validation checkpoints

## 🚀 Quick Start

```bash
# Clone repository
git clone https://github.com/afbeltranr/surveyNLP-policylab.git

# Install dependencies
pip install -r requirements.txt

# Run pipeline
python main.py
```

## 📈 Results

Key topics identified from the survey responses:

1. 🏥 **Healthcare Access**
   - Mental health services are underserved (Topic 13)
   - Limited access to medical facilities (Topic 14)
   - Essential medication shortages (Topic 2)
   - Long appointment wait times (Topic 4)

2. 🏗 **Infrastructure Issues**
   - Frequent power outages (Topic 10)
   - Limited access to clean water (Topic 12)
   - Poor waste management (Topic 11)
   - Housing conditions need improvement (Topic 7)

3. 💼 **Economic Challenges**
   - Limited local employment opportunities (Topic 0)
   - Youth migration due to lack of opportunities (Topic 5)
   - Insufficient support for entrepreneurship (Topic 6)

4. 🤝 **Social Cohesion**
   - Low community participation (Topic 1)
   - Feelings of abandonment (Topic 3)
   - Lack of trust in institutions (Topic 9)

These insights suggest a need for:
- Improved healthcare infrastructure and access
- Infrastructure maintenance and development
- Economic development initiatives
- Community engagement programs 🇨🇴  
> Modular & Continuously Delivered NLP System for Qualitative Survey Analysis

This project simulates an automated NLP system that processes and summarizes qualitative territorial survey responses to support human-centered policy development. It emphasizes **flexible automation**, **human-in-the-loop validation**, and **modular CI/CD**, powered by **synthetic data** and scalable Python code.

---

### 📌 Key Features
- ✅ End-to-end ETL pipeline with continuous retraining
- 🧠 Topic modeling, clustering, and LLM-assisted classification
- ⚙️ TabM-style adapter ensemble experimentation
- 📊 Visual dashboards + policy-ready narratives
- 🔄 CI/CD with GitHub Actions (Bayesian-style update loop)

---

## 🧱 Project Structure

```
.
├── data/              # Synthetic raw and processed text
├── notebooks/         # Prototyping and EDA
├── src/               # Modular Python code (ETL, modeling, viz)
├── tests/             # CI/CD tests
├── .github/workflows/ # GitHub Actions workflows
└── main.py            # Entrypoint to run the full pipeline
```

---

## 🚧 Project Stages

> Each stage will include visuals and automation scripts. Status will update as we go!

### ✅ Stage 1: Corpus Creation & Taxonomy Design  
![Stage](https://img.shields.io/badge/status-in_progress-yellow)
- Generate synthetic survey responses across diverse regions and groups
- Build initial taxonomic categories based on public policy themes  
<-- explain how categories and subcategories were selected from real-world policies -->

---

### ✅ Stage 2: Topic Modeling & Representation Learning  
![Stage](https://img.shields.io/badge/status-not_started-lightgrey)
- Use BERTopic, UMAP + HDBSCAN
- Embed TabM-style representation adapters (optional innovation layer)  
<-- explain adapter ensemble idea and why it's innovative for tabular NLP -->

---

### ✅ Stage 3: LLM-assisted Classification  
![Stage](https://img.shields.io/badge/status-not_started-lightgrey)
- GPT-based codification using few-shot prompts
- Validate vs. manual labels (simulation of expert input)  
<-- explain the importance of classification assist for edge cases -->

---

### ✅ Stage 4: Dashboards & Policy Narratives  
![Stage](https://img.shields.io/badge/status-not_started-lightgrey)
- Generate visuals by region, population group, and topic
- Summarize with quote banks and key insights  
<-- describe impact: how these visuals help decision makers -->

---

### ✅ Stage 5: CI/CD for Continuous Learning  
![Stage](https://img.shields.io/badge/status-not_started-lightgrey)
- GitHub Actions run tests + retrain model weekly or on new data
- Output updated reports + flag shifts in discourse  
<-- show automation diagram, link YAML workflow, explain Bayesian retraining metaphor -->

---

## 🛠 Tech Stack

- Python, pandas, spaCy
- BERTopic, SentenceTransformers
- GitHub Codespaces, GitHub Actions
- Dash / Plotly
- Optionally: OpenAI / GPT4All / TabM adapter module

---

## 🧪 Tests & Continuous Delivery

- `test_modeling.py` includes dummy tests for pipeline stability
- GitHub Actions in `.github/workflows/ci.yml` handles:
  - Install dependencies
  - Run tests
  - Retrain models
  - Save results to `outputs/` or trigger cloud export

---

## 📊 Diagrams (coming soon)

We'll include:
- End-to-end ETL Pipeline
- Human-in-the-loop Validation Flow
- GitHub Automation & Continuous Learning  
(*Use this space to embed PNGs or Mermaid diagrams*)

---

## 🧠 Why This Project Matters

This simulation reflects real-world NLP applications in public services, especially where **qualitative understanding** matters more than raw numbers. It merges **data science, automation, and social context**, preparing analysts to think beyond dashboards.

---

*📝 This README will evolve as stages progress and diagrams are created. All data is synthetic and used for educational purposes only.*
