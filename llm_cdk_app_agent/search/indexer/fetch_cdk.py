import subprocess
import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import DirectoryLoader, TextLoader, PythonLoader


# Function that downloads wheel files
def download_wheel():
    # Check if directory .cache/wheels exists
    if not os.path.exists(".cache/wheels"):
        os.makedirs(".cache/wheels")

    if not os.path.exists(".cache/py_folders"):
        os.makedirs(".cache/py_folders")

    """Function that downloads wheel files and unzips it."""
    # Download wheel file
    # python -m pip download --only-binary :all: --dest . --no-cache aws-cdk-lib
    subprocess.run(
        ["python", "-m", "pip", "download", "--only-binary", ":all:", "--dest", ".cache/wheels", "--no-cache", "aws-cdk-lib"]
    )

    # Unzip wheel file
    # unzip aws_cdk_lib-1.130.0-py3-none-any.whl
    subprocess.run(["unzip", ".cache/wheels/aws_cdk_lib-2.104.0-py3-none-any.whl", "-d", ".cache/py_folders"])


# Read in aws_lambda and aws_s3 __init__.py files
def read_init():
    """Read in aws_lambda and aws_s3 __init__.py files."""
    # Read in aws_lambda __init__.py file
    with open(".cache/py_folders/aws_cdk/aws_lambda/__init__.py", "r") as f:
        aws_lambda_init = f.read()

    # Read in aws_s3 __init__.py file
    with open(".cache/py_folders/aws_cdk/aws_s3/__init__.py", "r") as f:
        aws_s3_init = f.read()

    return aws_lambda_init, aws_s3_init


# Recursively split text
def split_docs(doc: tuple):
    """Recursively split text."""
    loader = DirectoryLoader(".cache/py_folders/aws_cdk/aws_lambda", glob="**/*.py", loader_cls=PythonLoader)


if __name__ == "__main__":
    test, _ = read_init()

    print(split_docs(test))
