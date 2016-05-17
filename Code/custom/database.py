class Database():
    file = ""
    dictionary = {}

    def __init__(self,file):
        self.file = file;
        with open(file, 'r') as f:
            for line in f:
                splitLine = line.split("||")
                self.dictionary[splitLine[0]] = splitLine[1]
    def add(self,key,msg):
        print("does nothing yet")
    def replace(self,key,msg):
        print("does nothing yet")
    def remove(self,key,msg):
        print("does nothing yet")