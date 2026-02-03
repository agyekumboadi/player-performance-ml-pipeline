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
| Cross-sport testing | Transfer evaluation | **Partial generalisation** | Requires context-aware feature adjustments |

---

## Evidence gallery (selected outputs)

### Model performance comparison
![Final model performance comparison](outputs/analysis/final_model_performance_comparison.png)

### Model test evaluation (summary)

| Dataset | Accuracy | F1-score | ROC AUC | Report |
|--------|---------:|---------:|--------:|--------|
| Basketball | (value) | (value) | (value) | [View](outputs/analysis/basketball_model_evaluation.txt) |
| Cross-sport | (value) | (value) | (value) | [View](outputs/analysis/crosssport_model_evaluation.txt) |

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
