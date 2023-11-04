from aws_lambda_powertools.utilities import parameters
import os


os.environ["AWS_DEFAULT_REGION"] = "us-east-1"
secret = parameters.get_secret("openai")

print(secret[:10])