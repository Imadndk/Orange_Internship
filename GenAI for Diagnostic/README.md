# **Generative AI System for Medical Diagnosis**

This project integrates **Amazon Bedrock**, **Amazon Lambda** to create a generative AI system for interpreting clinical notes and patient survey responses. It uses state-of-the-art language models like **Amazon Titan** and **Llama 3** to generate medical diagnoses and securely stores the results in an **Amazon S3 data lake**.

---

## **Features**

### 1. **Generative AI for Medical Diagnosis**
- Leverages **Amazon Titan** and **Llama 3** for generating text interpretations of clinical notes and patient survey responses.
- Maintains context and history using **LangChain**, ensuring coherent and context-aware results.

### 2. **Cloud Infrastructure**
- **Amazon Lambda**: Executes serverless function logic.
- **Amazon API Gateway**: Manages secure and scalable API endpoints for real-time interactions.
- **Postman API**: Tests and validates API functionality.

### 3. **Data Storage**
- Stores all generated outputs (medical diagnoses and sentiment analysis results) in an **Amazon S3 data lake** for secure and efficient data access.

---

## **Workflow**

1. **Input Handling**
   - Accepts clinical notes and survey responses via API.
   - Prepares the input for model inference.

2. **Text Generation**
   - Generates medical interpretations using **Amazon Titan** and **Llama 3** through the **Amazon Bedrock API**.
   - Ensures logical and meaningful results by maintaining context with **LangChain**.

3. **Output Management**
   - Results are stored in **Amazon S3**, enabling future access and analysis.

---

## **Deployment and Testing**

### **Deployment**
- **Lambda Functions**: Implements API calls to Bedrock and Comprehend for processing.
- **API Gateway**: Hosts secure endpoints for data submission and retrieval.
- **S3 Data Lake**: Stores outputs for long-term access.

### **Testing**
- **Postman API**: Used to test API endpoints for input submission and output validation.

---

## **Getting Started**

### **Requirements**
- **AWS Services**:
  - Amazon Bedrock
  - Amazon Lambda
  - Amazon API Gateway
  - Amazon S3
- **Tools**:
  - [Postman](https://www.postman.com/) for API testing

### **Steps to Run**
1. **Input Data**:
   - Submit clinical notes and survey responses to the API Gateway endpoint.
2. **Output Generation**:
   - Receive medical interpretations and sentiment analysis results via API response.
   - Outputs are saved to an S3 bucket for later access.
3. **Testing**:
   - Use Postman to send and verify API requests.

---

## **Future Improvements**
- Add support for more advanced language models for greater accuracy.
- Develop real-time dashboards for visualizing patient sentiment and diagnoses.
- Expand multilingual support to serve a diverse patient population.

---

