
import os
import requests
import pandas as pd  


def lambda_handler(event,context):
    print("deploy lamda code from github")
    response=requests.get('https://jsonplaceholder.typicode.com/posts/1')
    data=response.json()
    
    df=pd.DataFrame([data])
    print(df.head())
    
    
    ##We also required env var to register in lambda function
    print("Environment Variable:")
    defined_variables=["ENV","API_KEY","LOG_LEVEL"]
    
    for key in defined_variables:
        value=os.environ.get(key)
        if value is not None:
            print(f"{key}:{value}")
            
    return  {
                "StatusCode":200,
                "body": "Lambda function executed successfully"
        }
    