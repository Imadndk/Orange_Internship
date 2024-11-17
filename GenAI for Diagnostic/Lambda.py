import json
from datetime import datetime
import botocore.config
import boto3
import botocore
def medical_interpretation_generation(clinical_notes_survey_responses:str)-> str:
    prompt=f"write a diagnosis or interpretation for these medical information {clinical_notes_survey_responses}"
    modelId = "amazon.titan-text-premier-v1:0"
    accept = "application/json"
    contentType = "application/json"
    body= {"inputText":prompt,
           "textGenerationConfig":{
            "maxTokenCount":100,
            'stopSequences':[],
            "temperature":0.5,
            "topP":0.9}
            }
    try:
        
        bedrock=boto3.client('bedrock-runtime', region_name='us-east-1', 
                              config=botocore.config.Config(read_timeout=300, retries={"max_attempts":3}))
        response = bedrock.invoke_model(body=json.dumps(body), modelId=modelId, accept=accept, contentType=contentType)
        response_body = json.loads(response.get("body").read())
        print(response_body.get('results')[0].get('outputText'))
        return response_body.get('results')[0].get('outputText')
    except Exception as e:
        print(f"Error:{e}")
        return ""
def save_output_in_s3(s3_key, s3_bucket, generate_interpretation):
    s3=boto3.client('s3')
    try:
        s3.put_object(Bucket=s3_bucket, Key=s3_key, Body= generate_interpretation)
        print("diagnosis saved to s3")
    except:
        print("not ok")
def lambda_handler(event, context):
    event=json.loads(event['body'])
    clinical_notes_survey_responses=event["cnsr"]
    generate_interpretation=medical_interpretation_generation(clinical_notes_survey_responses=clinical_notes_survey_responses)
    if generate_interpretation:
        now=datetime.now()
        current_time=now.strftime("%H%M%S")
        s3_key=f"diagnosis/{current_time}.txt"
        s3_bucket='awsbedrockmedical'
        save_output_in_s3(s3_key, s3_bucket, generate_interpretation)
    else:
        print("no diagnosis was generated")
        
        
        
    return {
        'statusCode': 200,
        'body': json.dumps('medical diagnosis completed')

  
