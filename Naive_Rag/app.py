import os
from dotenv import load_dotenv
import chromadb
import google.generativeai as genai
from chromadb.utils import embedding_functions

load_dotenv()

gemini_key = os.getenv("Gemini_api_key")
# print(gemini_key)
op_key = os.getenv("Openai_api_key")

gemini_ef = embedding_functions.GoogleGenerativeAiEmbeddingFunction(
        api_key=gemini_key, task_type="RETRIEVAL_QUERY"
    )

chroma_client = chromadb.PersistentClient(path="chroma_persistent_storage")
collection_name = "document_qa_collection"
collection = chroma_client.get_or_create_collection(
    name=collection_name, embedding_function=gemini_ef
)
# genai.configure(api_key=gemini_key)
genai.configure(api_key=gemini_key)
model=genai.GenerativeModel("gemini-2.0-flash")
# contents = [
#     {
#         "role": "user",
#         "parts": [
#             {"text": "You are a helpful assistant. Please provide clear and concise answers. "
#                      "Now, answer this: What is human life expectancy in the United States? Keep the response within 200 tokens."}
#         ]
#     }
# ]
# resp =  model.generate_content(contents)
# print(resp.text)

def load_documents_from_directory(directory_path):
    print("==== Loading documents from directory ====")
    documents = []
    for filename in os.listdir(directory_path):
        if filename.endswith(".txt"):
            with open(
                os.path.join(directory_path, filename), "r", encoding="utf-8"
            ) as file:
                documents.append({"id": filename, "text": file.read()})
    return documents

def split_text(text, chunk_size=1000, chunk_overlap=20):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start = end - chunk_overlap
    return chunks

directory_path = "./news_articles"
documents = load_documents_from_directory(directory_path)
print(f"Loaded {len(documents)} documents")

chunked_documents = []
for doc in documents:
    chunks = split_text(doc["text"])
    print("==== Splitting docs into chunks ====")
    for i, chunk in enumerate(chunks):
        chunked_documents.append({"id": f"{doc['id']}_chunk{i+1}", "text": chunk})

# print(chunked_documents[1])
# print(f"Split documents into {len(chunked_documents)} chunks")
model_eb = 'models/embedding-001'
def get_gemini_embedding(text):
    response = genai.embed_content(
        model=model_eb,
        content=text,
        task_type="retrieval_document")

    # embedding = response.data[0].embedding
    print("==== Generating embeddings... ====")
    return response["embedding"]

for doc in chunked_documents:
    print("==== Generating embeddings... ====")
    doc["embedding"] = get_gemini_embedding(doc["text"])
# print(doc["embedding"])

