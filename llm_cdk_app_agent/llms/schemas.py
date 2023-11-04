from enum import Enum


class ModelName(str, Enum):
    GPT_3_5 = "gpt-3.5-turbo-16k"
    GPT_3_5_INSTRUCT = "gpt-3.5-turbo-instruct"