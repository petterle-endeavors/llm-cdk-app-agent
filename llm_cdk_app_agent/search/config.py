import pinecone

class PineconeManager:
    def __init__(self, api_key, env_key, index_name="llm-cdk-agent"):
        self.api_key = api_key
        self.env_key = env_key
        self.index_name = index_name
        pinecone.init(api_gitkey=self.api_key, environment=self.env_key)

    def list_indexes(self):
        return pinecone.list_indexes()

    def create_or_get_index(self, dimension=1536, metric="cosine"):
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
