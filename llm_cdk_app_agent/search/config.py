import pinecone

INDEX_NAME = "llm-cdk-agent"


def indexList():
    return pinecone.list_indexes()


def vectorStore(index_name: str = INDEX_NAME, dimension: int = 1536, metric: str = "cosine"):
    # check before creating
    if index_name not in indexList():
        # index not existed. Create a new index
        pinecone.create_index(
            name=index_name,
            dimension=dimension,
            metric=metric,
        )
        print(f"created a new index {index_name}")
    else:
        print(f"{index_name} index existed. skip creating.")
        index = pinecone.Index(index_name)
        index_stats_response = index.describe_index_stats()
        vector_count = index_stats_response.total_vector_count
        print(f"total_vector_count is {vector_count}")

        return index
    return pinecone.Index(index_name)
