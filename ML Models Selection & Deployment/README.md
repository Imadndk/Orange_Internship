# AI Bracelet: Machine Learning Notebooks

This folder contains Jupyter notebooks for data analysis, model development, evaluation, and deployment as part of the AI Bracelet project.

---

## Notebook Descriptions

1. **EDA and Model Selection**:
   - Exploratory Data Analysis (EDA) and evaluation of various models for:
     - **Blood Pressure Prediction**
     - **Respiratory Rate Prediction**

2. **Model Deployment**:
   - Step-by-step deployment of the selected models (Blood Pressure and Respiratory Rate) using:
     - **AWS SageMaker**
     - **Docker**

3. **LSTM Model**:
   - Development of the **LSTM multiclassification model** to predict urgent medical cases in advance real-time, based on IoT device data.
   - 
4. **API Deployment**:
   - Models are deployed using AWS Lambda and exposed via API Gateway for real-time predictions.

---
## Key Components

### Models
- **Linear Regression**: Blood pressure prediction.
- **XGBoost**: Blood pressure and respiratory rate prediction.
- **LSTM**: Classification model for predicting urgent medical cases.

### AWS Services
- **Amazon SageMaker**: For hosting trained models.
- **AWS Lambda**: To handle real-time inference requests.
- **API Gateway**: Exposes Lambda functions as RESTful APIs.
- **Amazon Timestream**: Stores real-time IoT data for processing.

---

## Lambda and API Gateway Workflow

1. **Lambda Function**:
   - Each model is deployed as an AWS Lambda function.
   - Below is an example Lambda function for invoking the LSTM model hosted on SageMaker:

```python
import json
import boto3

def lambda_handler(event, context):
    client = boto3.client('runtime.sagemaker')
    endpoint_name = 'tensorflow-inference-2024-10-29-18-54-28-088'

    sample = [[
        ###
    ]]
    
    payload = json.dumps(sample)
    
    response = client.invoke_endpoint(
        EndpointName=endpoint_name,
        Body=payload,
        ContentType='application/json'
    )
    
    result = response['Body'].read().decode('utf-8')
    print(result)
    return {
        'statusCode': 200,
        'emergencies': result
    }
```
## Usage

1. Open the `.ipynb` files using Jupyter Notebook or JupyterLab.
2. Follow the instructions within each notebook for running the cells and understanding the workflow.
3. Ensure you have the required libraries installed (`requirements.txt` file provided in the main project).

---

## Notes
- These notebooks demonstrate the full pipeline from EDA to deployment for key ML models.
- Deployment includes configurations for AWS SageMaker and Lambda.

---

For more information about the overall project, refer to the main [README.md](../README.md) file.

