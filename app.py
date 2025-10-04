import sys
# import config
class App:
    def setFileName(self, File):
        self.filename=File
        return self
    def setSearchContent(self, Content):
        self.content=Content
        return self
    def setSysArgv(self, Sysargv):
        if len(sys.argv) == 3:
            filename = sys.argv[1]
            self.setFileName(filename)
        else: print('Repeat it again')
        return self
    def getFileName(self):
        return self.filename
    def getSearchContent(self):
        return self.content
        

if __name__ == "__main__":
    app = App().setSysArgv(sys.argv)

    