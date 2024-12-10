# Orange Maroc Internship (Orange Summer Challenge 2024)
# AI Bracelet: Real-Time Health Monitoring and Alert System

The **AI Bracelet Project** is an innovative health monitoring solution designed to predict and alert users about critical health conditions such as heart attacks, hyperglycemia, and hypoglycemia. Leveraging **IoT devices**, **machine learning**, and **generative AI**, it provides real-time insights and personalized health reports accessible via a mobile app.

---

## Overview

### Key Features
- **Real-Time Health Monitoring**: Track vital signs such as heart rate, oxygen saturation, body temperature, respiratory rate, and blood pressure.
- **Urgency Prediction**: Predict critical medical conditions 30 seconds in advance using an LSTM-based real-time classification model.
- **Generative AI Integration**: Generate text-based medical interpretations of clinical notes and patient surveys using Amazon Bedrock API.
- **Sentiment Analysis**: Analyze patient responses with Amazon Comprehend to provide deeper insights.
- **Context Retention**: Maintain diagnostic and conversational histories using LangChain Memory.
- **Mobile App Integration**: Display vital signs, predictions, alerts, and health reports with user-friendly visualization.

---

## Technical Architecture

### Data Flow
1. **IoT Devices**: Collect vital signs every 3 seconds approximately and stream them to **Amazon Timestream**.
2. **Machine Learning Models**:
   - **LSTM Classification Model**: Predict urgent medical cases with ~80% accuracy, trained on panel data.
   - **Linear Regression and XGBoost**: Estimate blood pressure and respiratory rate in real-time.
3. **AWS Lambda**:
   - Processes incoming data for inference.
   - Triggers patient surveys and calls Amazon Bedrock API for text generation.
4. **Amazon Bedrock**:
   - Uses **Amazon Titan** and **LLama 3** to generate medical interpretations.
5. **Amazon Comprehend**:
   - Performs sentiment analysis on patient responses.
6. **LangChain Memory**:
   - Preserves diagnostic and conversational context for continuity.
7. **Amazon S3**:
   - Stores generative AI outputs and patient data securely.
8. **Mobile App**:
   - Displays health insights and reports, sends notifications and alerts.
## Setup AWS Resources
**Amazon Timestream:**

Configure a database and table for IoT data ingestion.

**Amazon SageMaker:**

Deploy pre-trained models (LSTM, Linear Regression, XGBoost) for real-time inference.

**Amazon Bedrock:**

Enable Amazon Titan and LLama 3 models for text generation.

**Amazon S3:**

Set up a bucket for storing outputs and diagnostic logs.

**AWS Lambda:**

Deploy Lambda functions using the lambda directory.

**API Gateway**

**Amazon CloudWatch**

Configure APIs for triggering models and handling requests.
---

## Features

### Real-Time Prediction
- Predict heart attack, hyperglycemia, and hypoglycemia 30 seconds in advance.
- Ensure efficient data flow from IoT sensors to SageMaker models via Amazon Timestream.

### Generative AI Capabilities
- Generate text-based medical interpretations using **Amazon Titan** and **LLama 3** via **Amazon Bedrock**.
- Retain context with **LangChain Memory** to provide continuity in patient diagnostics.
- Perform sentiment analysis using **Amazon Comprehend** to enrich understanding of patient feedback.

### Deployment and Testing
- All models deployed with **AWS SageMaker**, containerized with **Docker**, and integrated using **AWS Lambda**.
- APIs tested with **Postman**, with system monitoring via **Amazon CloudWatch**.

---

