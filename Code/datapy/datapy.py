# So this is the Datapy liberary created by Wander van der Wal.
# The idea is very simple, we have databases that Datapy is in control of.
from datapy.database import Database

databases = {}

class Datapy:
    def __init__(self, file):
        new(file)
        get(file)

    def get(self,file):
        return get(file)


def new(file):
    if find(file):
        return False
    databases[file] = Database(file);
    return True

def get(file):
    if find(file):
        return databases[file]
    return None

# Check if a database already exists
def find(file):
    for key in databases:
        if key == file:
            return True
    return False