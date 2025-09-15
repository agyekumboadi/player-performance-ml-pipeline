# Player Performance Analysis in Sports
------------------------------------------------------------------------------------------------------------------------
This repository contains the source code, workflow diagrams, and analysis outputs from my research project:  
**"Player Performance Analysis in Sports Using Data Analytics"**  

The project applies *machine learning models* to forecast player performance across multiple sports, using a reproducible data pipeline and interpretable models.

## Project Overview

The project investigates how data-driven methods can enhance the assessment of players performance in sports.
By combining statistical analysis, feature engineering, and predictive modelling, it identifies the Key Performance Indicators (KPIs) most strongly associated with high-performing players.

### Key Objectives
* Analyse large-scale multi-sport datasets (Football, Basketball, and Cross-Sport).
* Engineer and select features using statistical correlation and *Principal Component Analysis (PCA)*.
* Apply *Logistic Regression*, *Random Forest*, and *Support Vector Machine (SVM)* for performance prediction.
* Use *SHapley Additive exPlanations (SHAP)* to explain model predictions.
* Evaluate model generalisability across sports.


## Folder Structure

The repository is organised as follows:

MyResearchProject/  
└── Player_Performance_Analysis_in_Sports/  
    ├── docs/  
    │   └── flowchart/                   # Project workflow diagram(s)  
    │
    ├── outputs/  
    │   ├── analysis/                 # Model evaluation PNGs and text files  
    │   │   ├── *.png  
    │   │   ├── basketball_model_evaluation.txt  
    │   │   └── crosssport_model_evaluation.txt  
    │   │  
    │   ├── eda_visuals/               # Exploratory Data Analysis visuals  
    │   │   └── *.png  
    │   │
    │   ├── plots/                      # PCA and other plots  
    │   │   └── pca_explained_variance_cleaned.png  
    │   │
    │   └── shap_plots/                 # SHAP summary and interpretation visuals  
    │       └── shap_summary_crosssport.png  
    │
    ├── src/  
    │   ├── samuel_agyekum_research_project_player_performance_analysis.py   # Python source file  
    │   └── Sports_Performance_Analysis_Model.ipynb                     # Jupyter Notebook source file  
    │
    ├── .attributes  
    ├── .gitignore  
    ├── LICENSE  
    ├── README.md  
    └── requirements.txt  


**Note:**  
All datasets and trained model files (*.joblib*, *.pkl*, *.csv*, Excel outputs) are excluded for privacy, academic integrity, and size limitations.  
Only processed outputs, analysis visuals, and non-sensitive code are shared.

---

## Methodology

The project follows the **CRISP-DM framework**:

1. **Business Understanding**  
   Define research objectives and KPI requirements.

2. **Data Understanding**  
   Perform exploratory data analysis (EDA) and data cleaning.

3. **Data Preparation**  
   * Feature engineering (composite KPIs, standardised formats)  
   * Handling missing values  
   * Dimensionality reduction using PCA  

4. **Modelling**  
   * Logistic Regression (linear baseline)  
   * Random Forest (ensemble model)  
   * SVM (non-linear benchmark)  

5. **Evaluation**  
   * Metrics: Accuracy, Precision, Recall, F1-score, ROC AUC  
   * Cross-sport generalisability tests  

6. **Explainability**  
   * SHAP summary plots for feature importance  
   * SHAP waterfall plots for individual prediction interpretation  


## Technologies Used

* **Python 3.x**
* pandas, NumPy – Data manipulation
* scikit-learn – Machine learning models
* SHAP – Explainability
* Matplotlib, Seaborn – Visualisations
* Jupyter Notebook – Interactive development


## Key Findings

* Offensive metrics (goal contribution, goals total, assists, shot accuracy) were the strongest predictors of high player performance.  
* Random Forest (Top 10 features) achieved the best trade-off between accuracy and interpretability (ROC AUC: 0.8719).  
* SHAP analysis improved transparency and model trust by quantifying feature influence.  
* Cross-sport testing confirmed partial generalisability, though context-specific adjustments are required.


## Data and Privacy

* Raw datasets are **not** included to prevent unauthorised reuse.
* All personal or identifiable player information is not included.
* Only aggregated visuals and processed results are shared.


## Installation and Usage

### Prerequisites
* Python 3.9+
* Git
* Jupyter Notebook

### Steps
1. Clone the repository
git clone https://github.com/agyekumboadi/MyResearchProject.git

2. Navigate into the folder
cd MyResearchProject/Player_Performance_Analysis_in_Sports

3. Install dependencies
pip install -r requirements.txt 

4. Open the Jupyter Notebook
jupyter notebook src/Sports_Performance_Analysis_Model.ipynb


### Privacy and Academic Integrity

This repository excludes:

- Raw datasets (.csv, Excel)
- Trained model files (.joblib, .pkl)
- Confidential or proprietary outputs

This ensures:

1. Data confidentiality
2. Prevention of academic misconduct
3. Compliance with research policies

License

This project is the intellectual property of Samuel Boadi Agyekum and is licensed under the
Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License:

1. Free to view and share with attribution.
2. Not for commercial use.
3. No modifications or derivative works allowed.


# Contact Author

Author: Samuel Boadi Agyekum  
Email: agyekumowuraku@outlook.com  
LinkedIn: http://linkedin.com/in/samuelbagyekum  
