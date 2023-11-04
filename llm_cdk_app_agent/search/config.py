import os
import pinecone
from aws_lambda_powertools.utilities import parameters


os.environ["AWS_DEFAULT_REGION"] = "us-east-1"
pinecone_secret = str(parameters.get_secret("pinecone"))


class PineconeManager:
    "Managing pinecone configurations!"

    def __init__(self, api_key=pinecone_secret, env_key="us-east-1-aws", index_name="llm-cdk-agent"):
        self.api_key = api_key
        self.env_key = env_key
        self.index_name = index_name
        pinecone.init(api_key=self.api_key, environment=self.env_key)

    def list_indexes(self):
        "Getting all indexes and returns as a list."
        return pinecone.list_indexes()

    def create_or_get_index(self, dimension=1536, metric="cosine"):
        "Creation of our vector database index!"
        if self.index_name not in self.list_indexes():
            pinecone.create_index(
                name=self.index_name,
                dimension=dimension,
                metric=metric,
            )
            print(f"created a new index {self.index_name}")
        else:
            print(f"{self.index_name} index existed. Skip creating.")
            index = pinecone.Index(self.index_name)
            index_stats_response = index.describe_index_stats()
            vector_count = index_stats_response.total_vector_count
            print(f"total_vector_count is {vector_count}")

        return pinecone.Index(self.index_name)


pn = PineconeManager()
print(pn.list_indexes())
print(pn.create_or_get_index())