import sys
import rag.rag as rag
import config
# print("Текущий sys.path:", sys.path)
class App:
    def __init__(self):
        self.setSysArgv()
    def setSysArgv(self):
        if len(sys.argv) == 3:
            self.filename = sys.argv[1]
            self.content = sys.argv[2]
        else: print('Repeat it again'); return False
        return self
    def run(self, config):
        return rag.Rag(self.filename, self.content, config)
        

if __name__ == "__main__":
    app = App().run(config)

    