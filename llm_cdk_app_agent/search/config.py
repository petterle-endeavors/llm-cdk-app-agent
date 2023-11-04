import pinecone
from openai import OpenAIEmbeddings
from langchain.vectorstores import Pinecone

INDEX_NAME = "llm-cdk-agent"


def index_list() -> List[str]:
    return pinecone.list_indexes()


def create_index(index_name: str = INDEX_NAME, dimension: int = 1536, metric: str = "cosine"):
    # check before creating
    if index_name not in index_list():
        # index not existed. Create a new index
        pinecone.create_index(
            name=index_name,
            dimension=dimension,
            metric=metric,
        )
        print(f"created a new index {index_name}")
    else:
        print(f"{index_name} index existed. skip creating.")


def insert(data: List[Document], embeddings: OpenAIEmbeddings, index=INDEX_NAME) -> Pinecone:
    return Pinecone.from_documents(data, embedding=embeddings, index_name=index)


def need_text_embedding():
    need_text_embedding = False
    index = pinecone.Index(INDEX_NAME)
    index_stats_response = index.describe_index_stats()
    # Example of index_stats_reponse
    # index_stats_response is {'dimension': 1536,
    # 'index_fullness': 0.0,
    # 'namespaces': {'': {'vector_count': 532}},
    # 'total_vector_count': 532}
    vector_count = index_stats_response.total_vector_count
    print(f"total_vector_count is {vector_count}")

    if vector_count == 0:
        need_text_embedding = True
    return need_text_embedding
