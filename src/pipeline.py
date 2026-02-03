
# samuel_agyekum_research_project_player_performance_analysis.py
# Saving & Loading Script for my Research Project
# Author Samuel Boadi Agyekum
# Project Title: Player Performance Analysis in Sports Using Data Analytics
# Updated: 3rd May 2025

import os
import pandas as pd
import joblib
import pickle


# ============================================================================================================================================
#                                           Defining base and subfolder paths
# ============================================================================================================================================

base_path = r"C:\Users\agyek\OneDrive\Data_Analytics_and_IT_Security_Management\Data Analytics\Research Project\Datasets\msc_outputs"
data_path = os.path.join(base_path, "data")
model_path = os.path.join(base_path, "models")
plots_path = os.path.join(base_path, "plots")
shap_path = os.path.join(base_path, "shap_plots")


# ============================================================================================================================================
#                                           Step 5's: Saving Cleaned & Trained Assets
# ============================================================================================================================================

def save_all(club_teams_final, X_train, X_test, y_train, y_test, rf_model, explainer, shap_values):

    # saving Cleaned and Split Data
    club_teams_final.to_csv(os.path.join(data_path, "club_teams_final.csv"), index=False)
    X_train.to_csv(os.path.join(data_path, "X_train.csv"), index=False)
    X_test.to_csv(os.path.join(data_path, "X_test.csv"), index=False)
    y_train.to_csv(os.path.join(data_path, "y_train.csv"), index=False)
    y_test.to_csv(os.path.join(data_path, "y_test.csv"), index=False)

    # Saving trained model
    joblib.dump(rf_model, os.path.join(model_path, "rf_model.joblib"))

    # Saving SHAP explainer and values
    with open (os.path.join(shap_path, "explainer.pkl"), "wb") as f:
        pickle.dump(explainer, f)

    with open(os.path.join(shap_path, "shap_values.pkl"), "wb") as f:
         pickle.dump(shap_values, f)

    print(f"Step 5: All files saved successfully at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")   

# ============================================================================================================================================
#                                           Step 6's: Loading All Saved Assets
# ============================================================================================================================================

def load_all():

    # Loading cleaned data 
    club_teams_final = pd.read_csv(os.path.join(data_path, "club_teams_final.csv"))
    X_train = pd.read_csv(os.path.join(data_path, "X_train.csv"))
    X_test = pd.read_csv(os.path.join(data_path, "X_test.csv"))
    y_train = pd.read_csv(os.path.join(data_path, "y_train.csv")).squeeze()
    y_test = pd.read_csv(os.path.join(data_path, "y_test.csv")).squeeze()


    # Loading trained model
    rf_model = joblib.load(os.path.join(model_path, "rf_model.joblib"))

    # Load SHAP explainer and values
    with open (os.path.join(shap_path, "explainer.pkl"), "rb") as f:
        explainer = pickle.load(f)

    with open(os.path.join(shap_path, "shap_values.pkl"), "rb") as f:
        shap_values = pickle.load(f)

    print(f"Step 6: All files loaded successfully at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")   
    return club_teams_final, X_train, X_test, y_train, y_test, rf_model, explainer, shap_values
    
