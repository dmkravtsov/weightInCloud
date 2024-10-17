# Flask App for Weight Prediction

This project demonstrates the deployment of a machine learning model to predict weight based on height. The model is served via a Flask web application, allowing users to interact with it through both an HTML form and an API endpoint. The deployment is intended to run on Microsoft Azure.

## Features

- **Model**: A linear regression model predicts weight based on height.
- **Flask Web Application**: Users can input height via an HTML form or send POST requests to the API.
- **Deployment**: The app is designed for cloud deployment using Microsoft Azure.

## Usage

1. **HTML Form**: Enter height in centimeters on the homepage, and the predicted weight will be returned.
2. **API**: Send a POST request to `/predict` with a JSON body containing the height to get a predicted weight.
   - Example request:
     ```json
     {
       "height": 175
     }
     ```

## Deployment

The app is designed to be deployed on Microsoft Azure App Service. The trained model is stored locally and can be uploaded to Azure Blob Storage for cloud deployment.

### Steps to Deploy on Azure

1. Upload the project to GitHub.
2. Connect the GitHub repository to Azure App Service.
3. Configure the environment to load the necessary dependencies from `requirements.txt`.
4. Run the app on Azure to make the API and HTML form available online.

## Requirements

- Flask
- scikit-learn
- joblib
- gunicorn

Install dependencies via:

```bash
pip install -r requirements.txt
