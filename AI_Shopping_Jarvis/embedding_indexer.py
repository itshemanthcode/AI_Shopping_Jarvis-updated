import json
import faiss
from sentence_transformers import SentenceTransformer
import numpy as np

# Load the scraped product data from JSON
with open('products.json', 'r', encoding='utf-8') as f:
    products = json.load(f)

# Initialize the Sentence Transformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Generate embeddings for product titles
titles = [product['title'] for product in products]
embeddings = model.encode(titles)

# Save the embeddings index using FAISS
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings))

# Save FAISS index
faiss.write_index(index, "faiss_product_index.index")

# Save product metadata (titles, prices, etc.) separately for later retrieval
with open("product_metadata.json", "w", encoding="utf-8") as f:
    json.dump(products, f, ensure_ascii=False, indent=2)

print("✅ Embeddings and product index saved successfully.")
