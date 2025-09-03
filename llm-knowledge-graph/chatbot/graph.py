import os
from dotenv import load_dotenv
from langchain_neo4j import Neo4jGraph


load_dotenv()

# tag::graph[]
graph = Neo4jGraph(
    url=os.getenv("NEO4J_URI"),
    username=os.getenv("NEO4J_USERNAME"),
    password=os.getenv("NEO4J_PASSWORD")
)

#end::graph[]