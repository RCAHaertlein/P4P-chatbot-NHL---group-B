class Database:
    file = ""
    dictionary = {}

    def __init__(self, file):
        self.file = file;
        self.reload()

    def add(self, key, msg):
        self.dictionary[key] = msg
        with open(self.file, 'a') as f:
            f.write('\n' + key + "||" + msg)

    def replace(self,key,msg):
        print("does nothing yet")

    def remove(self,key,msg):
        print("does nothing yet")

    def reload(self):
        with open(self.file, 'r') as f:
            for line in f:
                splitLine = line.split("||")
                self.dictionary[splitLine[0]] = splitLine[1]
        print("Reloaded database: " + self.file)