# import app, config
import ollama

class Rag:
    def __init__(self, filename, content):
        self.loadingDataSet(filename)
    def loadingDataSet(self, filename):
        with open(filename, 'r') as file:
            self.database = file.readlines
    def addChunkDatabase(self, chunk):
        # embedding = ollama
        pass
    # def cosineSim(self)
    