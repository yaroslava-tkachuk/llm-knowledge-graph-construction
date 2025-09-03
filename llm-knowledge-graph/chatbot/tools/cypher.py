from dotenv import load_dotenv
from typing import Any

from llm import llm, cypher_llm
from graph import graph
from langchain_neo4j import GraphCypherQAChain
from langchain.prompts import PromptTemplate
from langchain_neo4j import GraphCypherQAChain
from langchain.prompts import PromptTemplate


load_dotenv()

# You task is to update this tool to generate and run a Cypher statement, and return the results.

# Create cypher_generation prompt
CYPHER_GENERATION_TEMPLATE = """Task:Generate Cypher statement to query a graph database.
Instructions:
Use only the provided relationship types and properties in the schema.
Do not use any other relationship types or properties that are not provided.
Only include the generated Cypher statement in your response.

Always use case insensitive search when matching strings.

Schema:
{schema}

Examples: 
# Use case insensitive matching for entity ids
MATCH (c:Chunk)-[:HAS_ENTITY]->(e)
WHERE e.id =~ '(?i)entityName'

# Find documents that reference entities
MATCH (d:Document)<-[:PART_OF]-(:Chunk)-[:HAS_ENTITY]->(e)
WHERE e.id =~ '(?i)entityName'
RETURN d

# Find the most popular labels
MATCH (n)
UNWIND labels(n) AS label
RETURN label, count(*) AS count
ORDER BY count DESC
LIMIT 10

# Find the most popular technologies
MATCH (c:Chunk)-[:HAS_ENTITY]->(t:Technology)
RETURN t.name AS technology, count(c) AS mentions
ORDER BY mentions DESC
LIMIT 10

The question is:
{question}"""

cypher_generation_prompt = PromptTemplate(
    template=CYPHER_GENERATION_TEMPLATE,
    input_variables=["schema", "question"],
)

# Create the cypher_chain
cypher_chain = GraphCypherQAChain.from_llm(
    qa_llm=llm,
    cypher_llm=cypher_llm,
    graph=graph,
    cypher_prompt=cypher_generation_prompt,
    verbose=True,
    allow_dangerous_requests=True
)

def run_cypher(q: str) -> dict[str, Any]:
    return cypher_chain.invoke({"query": q})
  