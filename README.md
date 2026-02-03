# Player Performance Analytics – Reproducible ML Pipeline (Multi-Sport)

This repository documents my research project: **Player Performance Analysis in Sports Using Data Analytics**.  
It delivers an **end-to-end, reproducible machine learning pipeline** for forecasting and interpreting player performance using **football**, then validating generalisability using **basketball** and **cross-sport** datasets.

**Core focus:** building models that are not only accurate, but also **auditable and explainable** (PCA + SHAP), with outputs presented in decision-ready form.

---

## Why this project matters (UK Digital Technology relevance)

Sports and performance-driven sectors increasingly rely on analytics to improve decision-making, recruitment, training, and risk management. This work demonstrates my ability to:
- design a **structured ML workflow** from raw data to validated outputs,
- apply **responsible modelling practices** (evaluation discipline, leakage awareness, explainability),
- and communicate findings through **clear evidence artefacts** (saved visuals, metrics, and interpretation plots).

---

## What this repository contains

This repo shares:
- reproducible source code (Python + Notebook),
- workflow diagrams,
- evaluation outputs (metrics + plots),
- SHAP explainability visuals.

**Note:** raw datasets and trained model files are excluded for size, licensing, and academic integrity reasons. The repository remains a transparent technical record of *methods, outputs, and evidence*.

---

## Technical objectives

1. Analyse multi-sport performance datasets (Football, Basketball, Cross-Sport)  
2. Engineer and select features using correlation checks and **PCA**  
3. Train and compare predictive models: **Logistic Regression**, **Random Forest**, **SVM**  
4. Evaluate using standard metrics: Accuracy, Precision, Recall, F1-score, **ROC AUC**  
5. Improve transparency using **SHAP** (global + individual interpretability)  
6. Test model adaptability across non-football datasets (generalisability)

---

## Pipeline summary (high level)

1. **Data understanding & cleaning**  
   - basic validation, missing-value handling, standardisation, and EDA

2. **Feature engineering & selection**  
   - composite KPIs and distribution checks  
   - correlation-based screening  
   - dimensionality reduction via **PCA** where appropriate

3. **Modelling**  
   - Logistic Regression baseline  
   - Random Forest for non-linear relationships  
   - SVM as a benchmark model

4. **Evaluation & testing**  
   - comparison across models and feature sets  
   - cross-sport validation to test transferability

5. **Explainability**  
   - SHAP summary plots (global importance)  
   - SHAP waterfall plots (individual prediction reasoning)

---

## Results at a glance

| Model | Feature strategy | Key metric (ROC AUC) | Interpretation |
|------|------------------|---------------------:|---------------|
| Random Forest | Top features | **0.8719** | Best balance of performance + interpretability |
| Logistic Regression | PCA-based | **0.88–0.89 (approx.)** | Strong baseline, stable behaviour |
| Cross-sport testing | Transfer evaluation | **Partial generalisation (ROC AUC: 0.5007)** | Requires context-aware feature adjustments |

---

## Model performance (confirmed scores)

### Football – core modelling results (ROC AUC)
| Model | Feature strategy | ROC AUC | Notes |
|------|------------------|--------:|------|
| Random Forest | PCA feature space | **0.8889** | Strong non-linear performance on reduced dimensions |
| Random Forest | Top 10 feature subset | **0.8906** | Best overall trade-off between performance and interpretability |

### Football – baseline comparison (Full Features)
| Model | ROC AUC |
|------|--------:|
| Logistic Regression | **0.8946** |
| Random Forest | **0.8906** |
| SVM | **0.8719** |

### Cross-sport testing – generalisability (Random Forest + SMOTE)
| Dataset | Accuracy | F1-score (weighted) | ROC AUC | Report |
|--------|---------:|--------------------:|--------:|--------|
| Basketball | **0.93** | **0.93** | **0.9719** | [View](outputs/analysis/basketball_model_evaluation.txt) |
| Cross-sport (running/rowing/cycling) | **0.59** | **0.57** | **0.5007** | [View](outputs/analysis/crosssport_model_evaluation.txt) |

## Evidence gallery (selected outputs)

### Workflow Diagram
![workflow diagram of dataset inputs across training and testing stages](outputs/eda_visuals/datasets_pipeline_diagram.png)

### Selected Exploratory Data Analysis Visuals ([view all](outputs/eda_visuals))
![top 15 correlated features](outputs/eda_visuals/top15_correlated_features.png)
![injury vs. minutes played](outputs/eda_visuals/logistic_injury_vs_minutes_played.png)
![goal contribution distribution (goals + assist)](outputs/eda_visuals/goal_contribution_distribution.png)
![filtered correlation matrix](outputs/eda_visuals/filtered_correlation_matrix.png)

### Confusion matrix (basketball test)
![Basketball confusion matrix](outputs/analysis/basketball_confusion_matrix_roc9719.png)

### Explainability (SHAP)
![SHAP summary – cross-sport](outputs/shap_plots/shap_summary_crosssport.png)

![SHAP summary – class 1](outputs/shap_plots/shap_summary_class1.png)

### PCA diagnostics
![PCA explained variance](outputs/plots/pca_explained_variance_cleaned.png)

---

## Key findings (evidence-led)

- Offensive performance indicators (e.g., goal contribution, goals, assists, shot-based measures) showed strong association with high performance outcomes.  
- Random Forest using a selected feature subset delivered strong predictive capability while remaining interpretable through SHAP.  
- SHAP explainability improved trust by showing **which features drive predictions** and how they interact.  
- Cross-sport testing showed that the modelling approach is **transferable in principle**, but performance domains require tailored feature interpretation.

---

## Repository structure

```text
MyResearchProject/
└── Player_Performance_Analysis_in_Sports/
    ├── docs/
    │   └── flowchart/                 # Project workflow diagram(s)
    │
    ├── outputs/
    │   ├── analysis/                  # Model evaluation PNGs + text outputs
    │   ├── eda_visuals/               # Exploratory analysis visuals
    │   ├── plots/                     # PCA and other plots
    │   └── shap_plots/                # SHAP explainability visuals
    │
    ├── src/
    │   ├── samuel_agyekum_research_project_player_performance_analysis.py
    │   └── Sports_Performance_Analysis_Model.ipynb
    │
    ├── .gitattributes
    ├── .gitignore
    ├── LICENSE
    ├── README.md
    └── requirements.txt 
```
---
## Author

**Samuel Boadi Agyekum**  
Data Analytics & IT Security Management (MSc) - UK  

- GitHub: https://github.com/agyekumboadi  
- LinkedIn: https://www.linkedin.com/in/samuel-agyekum-388a82150/  
- Email: agyekumowuraku@outlook.com  

**Focus areas:** Applied machine learning, reproducible analytics pipelines, explainable AI (SHAP), performance evaluation, and data governance.

**Role in this project:** Sole developer and researcher who designed the pipeline, implemented modelling (Logistic Regression, Random Forest, SVM), ran cross-sport testing, produced evaluation artefacts (metrics, confusion matrices, ROC AUC comparisons), and generated explainability outputs (SHAP).

This repository is presented as a transparent technical evidence pack: it documents methodology, implementation decisions, and reproducible outputs used to evaluate model reliability and transferability across datasets.


