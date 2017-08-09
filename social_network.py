class User:
    # Define the fields and methods for your object here.
    def __init__(self,name):
        self.name = name
        self.friends = []

    def addFriend(self,friend):
        

    def getname(self):
        return self.name

    def getfriends(self):
        return self.friends

    name = input("What is your name?")

class Network:
    # Define the fields and methods for your object here.
    def __init__(self,userlist):
        self.userlist = []

    def getuserlist(self):
        return self.userlist

def main():
    # Define the program flow for your user interface here.
    name = input("What is your name?")
    User(name)

# Runs your program.
if __name__ == '__main__':
    main()
