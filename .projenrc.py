from projen.python import PythonProject


AUTHORS = [
    "Jacob Petterle",
]
project = PythonProject(
    author_email="jacobpetterle@tai-tutor.team",
    author_name=AUTHORS[0],
    module_name="llm_cdk_app_agent",
    name="llm-cdk-app-agent",
    version="0.1.0",
    description="A CDK app for deploying the LLM agent",
    poetry=True,
    deps=[
        "pinecone-client@2.2.4",
        "langchain@0.0.330",
        "beautifulsoup4@4.12.0",
        "openai@0.28.1",
        "unstructured@0.10.0",
        "tiktoken@0.5.1",
        "python@^3.8.1",
        "watchdog@^3.0.0",
        "aws-lambda-powertools@^2.26.0",
        "jmespath@^1.0.1",
        "boto3@^1.28.78",
    ],
    dev_deps=["projen@<=0.72.20"],
)


project.synth()
