# import app, config
import ollama

class Rag:
    def __init__(self, filename, content, config):
        # self.loadingDataSet(filename)
        self.filename = filename
        self.content = content
        self.config = config
        self.VECTOR_DB = []
        self.run()
    def loadingDataSet(self, filename):
        with open(filename, 'r') as file:
            self.database = file.readlines()
    def addChunkDatabase(self, chunk):
        embedding = ollama.embed(model=self.config.EMBEDDING_MODEL, input=chunk)['embeddings'][0]
        self.VECTOR_DB.append((chunk, embedding))
    def addDatasetToDatabase(self):
        for chunk in self.database:
            self.addChunkDatabase(chunk)
    def cosineSimilarity(self, a, b):
        dot_product = sum([x * y for x, y in zip(a, b)])
        norm_a = sum([x ** 2 for x in a]) ** 0.5
        norm_b = sum([x ** 2 for x in b]) ** 0.5
        return dot_product/ (norm_a * norm_b)
    def retrive(self, top_n=3):
        query_embedding = ollama.embed(model=self.config.EMBEDDING_MODEL, input=self.content)['embeddings'][0]
        similarities = []
        for chunk, embedding in self.VECTOR_DB:
            similarity = self.cosineSimilarity(query_embedding, embedding)
            similarities.append((chunk, similarity))
        # Sorting high relevant
        similarities.sort(key=lambda x: x[1], reverse=True)
        return similarities[:top_n]
    def run(self):
        self.loadingDataSet(self.filename)
        self.addDatasetToDatabase()
        for chunk, similarity in self.retrive():
            if similarity < 0.6:
                break
            
            print(f' - (similarity: {similarity:.2f}) {chunk}')
        # print(self.retrive())
    
    