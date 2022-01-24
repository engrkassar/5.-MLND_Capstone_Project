import boto3


def lambda_handler(event, context):
    
    # The SageMaker runtime is what allows us to invoke the endpoint that we've created.
    runtime = boto3.Session().client('sagemaker-runtime')


    # Now we use the SageMaker runtime to invoke our endpoint, sending the review we were given
    response = runtime.invoke_endpoint(EndpointName = 'sagemaker-xgboost-2022-01-23-19-00-01-915',# The name of the endpoint we created
                                       ContentType = 'text/csv',                 # The data format that is expected
                                       Body = event['body'][2:]) # The actual data

    # The response is an HTTP response whose body contains the result of our inference
    result = round(float(response['Body'].read().decode('utf-8')))


    return {
        'statusCode' : 200,
        'headers' : { 'Content-Type' : 'text/plain', 'Access-Control-Allow-Origin' : '*' },
        'body' : result
    }

