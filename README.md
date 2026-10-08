![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-REST%20API-009688)
![Scikit--learn](https://img.shields.io/badge/Scikit--learn-1.6.1-F7931E)
![Status](https://img.shields.io/badge/Status-Completed-success)

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-REST%20API-009688)
![Scikit--learn](https://img.shields.io/badge/Scikit--learn-1.6.1-F7931E)
![Status](https://img.shields.io/badge/Status-Completed-success)

# House Price Prediction API

An end-to-end machine learning regression project that predicts house prices based on property characteristics such as bedrooms, bathrooms, living area, location, building year, and property condition.

The project covers the complete machine learning workflow, including exploratory data analysis, data preprocessing, feature transformation, model training, model comparison, evaluation, residual analysis, model serialization, and deployment through a FastAPI REST API.

## Project Overview

This project demonstrates how a machine learning regression model can be developed and exposed as a REST API for real-time house price predictions.

The workflow includes:

* Data loading and preprocessing
* Exploratory Data Analysis (EDA)
* Feature engineering and transformation
* Handling numerical and categorical features
* Training multiple regression models
* Model performance comparison
* Residual analysis
* Best model selection
* Saving trained model artifacts
* Building a FastAPI backend
* Creating prediction endpoints
* Serving predictions through a REST API

## Project Structure

```text
house_price_api/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   └── model/
│       ├── house_price_model.joblib
│       └── model_metadata.joblib
│
├── notebooks/
│   └── house_price_prediction.ipynb
│
├── .gitignore
├── README.md
└── requirements.txt
```

## Technologies Used

* Python 3.11
* FastAPI
* Scikit-learn
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Joblib
* Jupyter Notebook
* Uvicorn

## Machine Learning Models

The project compares multiple regression algorithms:

* Linear Regression
* Random Forest Regressor
* Gradient Boosting Regressor

The models are evaluated using appropriate regression performance metrics, and the best-performing model is selected for deployment.

## Machine Learning Workflow

1. Load the house price dataset
2. Perform data cleaning and preprocessing
3. Conduct Exploratory Data Analysis
4. Analyze numerical and categorical features
5. Apply feature transformations
6. Split the dataset into training and testing sets
7. Train multiple regression models
8. Compare model performance
9. Perform residual analysis
10. Select the best-performing model
11. Save the trained model using Joblib
12. Save model metadata
13. Build the FastAPI application
14. Create an API endpoint for predictions
15. Serve predictions through the REST API

## Model Artifacts

The trained model and supporting information are stored in the `app/model/` directory.

### `house_price_model.joblib`

Contains the trained machine learning regression model used for house price prediction.

### `model_metadata.joblib`

Contains the metadata required by the API for processing input features and generating predictions.

## API

The project uses **FastAPI** to expose the trained machine learning model through a REST API.

### Run the API

From the project root directory:

```bash
uvicorn app.main:app --reload
```

The API will be available locally at:

```text
http://127.0.0.1:8000
```

## API Documentation

FastAPI automatically provides interactive API documentation.

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

The Swagger interface can be used to provide property details and test house price predictions directly from the browser.

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/house_price_api.git
```

Navigate to the project directory:

```bash
cd house_price_api
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment on Windows:

```bash
venv\Scripts\activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Running the Project

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

Then open the Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

Use the API endpoint to enter the required house/property details and generate a predicted house price.

## Example Prediction Inputs

The API can accept property-related information such as:

```text
Bedrooms
Bathrooms
Living Area
Location
Building Year
Property Condition
```

The trained regression model processes these features and returns the predicted house price.

## Notebook

The complete machine learning development process is available in:

```text
notebooks/house_price_prediction.ipynb
```

The notebook contains:

* Data exploration
* Data visualization
* Preprocessing
* Feature transformation
* Model training
* Model comparison
* Evaluation
* Residual analysis
* Model selection

## Key Features

* End-to-end machine learning regression pipeline
* Multiple model comparison
* Feature preprocessing and transformation
* Residual analysis
* Serialized model artifacts
* REST API using FastAPI
* Interactive Swagger API documentation
* Deployment-ready project structure

## Purpose

This project was developed to demonstrate practical knowledge of:

* Machine Learning
* Regression
* Data Preprocessing
* Exploratory Data Analysis
* Model Evaluation
* Model Serialization
* REST API Development
* FastAPI
* Python

It demonstrates how a machine learning model can be transformed from a Jupyter Notebook experiment into a usable API service.

## Author

**Harshavarthini K**

Mechanical & Automobile Engineer
Interested in Automotive Systems, Vehicle Testing, Software Testing, Python, and Machine Learning.
