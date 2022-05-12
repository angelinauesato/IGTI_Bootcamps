import boto3
import pandas as pd

#create a client to interact with aws s3
s3_client = boto3.client('s3')

s3_client.download_file('database-igti-auo-edc', 
                        'data/movies_metadata.csv',
                        'data/movies_metadata.csv')
df = pd.read_csv('data/movies_metadata.csv')
print(df)
#The maximum size of a file that you can upload by using the Amazon S3 console is 160 GB. 
#To upload a file larger than 160 GB, use the AWS CLI, AWS SDK, or Amazon S3 REST API.
s3_client.upload_file('data/ibge.csv',
                        'database-igti-auo-edc',
                        'data/ibge.csv')