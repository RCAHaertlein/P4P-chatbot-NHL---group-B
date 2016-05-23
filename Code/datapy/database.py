import os


class Database:

    file = ""
    dictionary = {}

    def __init__(self, file):
        self.file = file
        self.dictionary = {}
        self.reload()


    def add(self, key, msg):
        self.dictionary[key] = msg
        with open(self.file, 'a') as f:
            f.write('\n' + key + "||" + msg)
        self.reload()

    def replace(self,key,msg):
        self.dictionary[key] = msg
        self.rebuild()

    def remove(self,key):
        self.dictionary.pop(key)
        self.rebuild()

    def find(self, key):
        for k in self.dictionary:
            if k == key:
                return True
        return False

    def rebuild(self):
        os.remove(self.file)
        with open(self.file, 'a') as f:
            for key in self.dictionary:
                f.write(key + "||" + self.dictionary[key])
        print("Rebuild database: " + self.file)

    def reload(self):
        with open(self.file, 'r') as f:
            for line in f:
                splitLine = line.split("||")
                self.dictionary[splitLine[0]] = splitLine[1]
        print("Reloaded database: " + self.file)
