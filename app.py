import sys
from rag import Rag
# import config
class App:
    def __init__(self):
        self.setSysArgv()
        return self
    def setSysArgv(self):
        if len(sys.argv) == 3:
            self.filename = sys.argv[1]
            self.content = sys.argv[2]
        else: print('Repeat it again')
        return self
    def run(self):
        return Rag(self.filename, self.content)
        

if __name__ == "__main__":
    app = App()

    