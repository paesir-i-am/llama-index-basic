import os
from dotenv import load_dotenv
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex

def main():
    load_dotenv()
    docs = SimpleDirectoryReader('data/txt').load_data()
    index = VectorStoreIndex.from_documents(docs)
    qe = index.as_query_engine(similarity_top_k=5)
    print(qe.query('핵심 정책을 3줄로 요약해줘'))

if __name__ == '__main__':
    main()
