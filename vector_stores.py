import chromadb

class ResumeStore:
    def __init__(self, db_path="./chroma_db"):
        self.client = chromadb.PersistentClient(path=db_path)
        # Chroma handles tokenization and embeddings automatically via all-MiniLM-L6-v2 by default
        self.collection = self.client.get_or_create_collection("resumes")

    def add_resume(self, candidate_id: str, text: str):
        self.collection.add(
            documents=[text],
            metadatas=[{"source": "resume", "candidate_id": candidate_id}],
            ids=[candidate_id]
        )

    def search_similar(self, query: str, n_results: int = 5):
        return self.collection.query(
            query_texts=[query],
            n_results=n_results
        )