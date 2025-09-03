import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings


load_dotenv()

# tag::llm[]
# Create the LLM
llm = ChatOpenAI(
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    model_name="gpt-3.5-turbo"
)
# end::llm[]

# tag::cypher_llm[]
# Create the LLM for query to Cypher conversion
cypher_llm = ChatOpenAI(
    openai_api_key=os.getenv("OPENAI_API_KEY"), 
    model="gpt-4",
    temperature=0
)
# end::cypher_llm[]

# tag::embedding[]
# Create the Embedding model
embeddings = OpenAIEmbeddings(
    openai_api_key=os.getenv("OPENAI_API_KEY")
)
# end::embedding[]
