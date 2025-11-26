# Assignment_10.py

# Required installations
# pip install pinecone-client openai

import os
from pinecone import Pinecone, ServerlessSpec
from openai import AzureOpenAI

# Step 1 Set environment variables
os.environ[AZURE_OPENAI_ENDPOINT] = 
os.environ[AZURE_OPENAI_API_KEY] = 
os.environ[AZURE_DEPLOYMENT_NAME] = text-embedding-3-small
os.environ[PINECONE_API_KEY] = 

# Step 2 Initialize clients
client = AzureOpenAI(
    api_version=2024-07-01-preview,
    azure_endpoint=os.getenv(AZURE_OPENAI_ENDPOINT),
    api_key=os.getenv(AZURE_OPENAI_API_KEY),
)

pc = Pinecone(api_key=os.getenv(PINECONE_API_KEY))

# Step 3 Create Pinecone index
index_name = product-similarity-index
if index_name not in [index[name] for index in pc.list_indexes()]
    pc.create_index(
        name=index_name,
        dimension=1536,
        spec=ServerlessSpec(cloud=aws, region=us-east-1),
    )
index = pc.Index(index_name)

# Step 4 Sample product data
products = [
    {id prod1, title Red T-Shirt},
    {id prod2, title Blue Jeans},
    {id prod3, title Black Leather Jacket},
    {id prod4, title White Sneakers},
    {id prod5, title Green Hoodie},
]

# Step 5 Generate embeddings and upsert
def get_embedding(text)
    response = client.embeddings.create(
        input=text,
        model=os.getenv(AZURE_DEPLOYMENT_NAME)
    )
    return response.data[0].embedding

vectors = []
for p in products
    embedding = get_embedding(p[title])
    vectors.append((p[id], embedding))
index.upsert(vectors)

# Step 6 Query for top 3 similar products
query = clothing item for summer
query_embedding = get_embedding(query)
top_k = 3
results = index.query(vector=query_embedding, top_k=top_k, include_metadata=False)

# Step 7 Display results
print(fTop {top_k} similar products for the query '{query}'n)
for match in results.matches
    product_id = match.id
    score = match.score
    product = next(p for p in products if p[id] == product_id)
    print(f- {product['title']} (Similarity score {score.4f}))