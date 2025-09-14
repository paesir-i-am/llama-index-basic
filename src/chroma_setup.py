import os
from dotenv import load_dotenv
import chromadb
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core import StorageContext, VectorStoreIndex, SimpleDirectoryReader

def main():
    load_dotenv()
    CHROMA_PATH = os.getenv('CHROMA_PATH', './chroma_store')
    embed_model = OpenAIEmbedding(model='text-embedding-3-small')

    client = chromadb.PersistentClient(path=CHROMA_PATH)
    collection = client.get_or_create_collection('workshop')

    vector_store = ChromaVectorStore(chroma_collection=collection)
    storage_context = StorageContext.from_defaults(vector_store=vector_store)

    docs = SimpleDirectoryReader('data/txt').load_data()
    index = VectorStoreIndex.from_documents(docs, storage_context=storage_context, embed_model=embed_model)
    qe = index.as_query_engine(similarity_top_k=5)
    print(qe.query('핸드북 핵심 개념 3개를 설명해줘'))

if __name__ == '__main__':
    main()
