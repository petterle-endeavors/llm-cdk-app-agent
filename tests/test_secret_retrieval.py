from aws_lambda_powertools.utilities import parameters
import os


os.environ["AWS_DEFAULT_REGION"] = "us-east-1"
openai_secret = parameters.get_secret("openai")
pinecone_secret = parameters.get_secret("pinecone")

print(openai_secret[:10])
print(pinecone_secret[:10])