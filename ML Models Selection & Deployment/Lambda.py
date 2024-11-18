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
