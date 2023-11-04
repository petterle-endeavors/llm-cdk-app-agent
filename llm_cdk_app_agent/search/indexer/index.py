import pinecone

# ingesting docs
# ingesting codebase


# index = vectorStore()


def upsert_docs(index):
    index.upsert(
        [
            ("A", [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1], {"type": "docs", "tool": "CDK"}),
            ("E", [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5], {"type": "docs", "tool": "FastAPI"}),
        ]
    )


def upsert_code(index):
    index.upsert(
        [
            ("B", [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2], {"type": "code"}),
            ("C", [0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3], {"type": "code"}),
            ("D", [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4], {"type": "code"}),
        ]
    )
