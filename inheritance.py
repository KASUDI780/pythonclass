class Dad:
    def __init__(self, color, dadhobby):
        self.color = color
        self.dadhobby = dadhobby
class Mom:
    def __init__(self, color, momhobby):
        self.color = color
        self.momhobby = momhobby
class Boy(Dad):
    def boyinherits(self):
        print(f"Boy inherits {self.color} and the {self.dadhobby}")

# instance
myobj=Boy("African decent","Watching football")
myobj.boyinherits()

class Girl(Mom):
    def girlinherits(self):
        print(f"Girl inherits {self.color} complexion and  {self.momhobby}")

myobj=Girl("Dark" ,"Reading")
myobj.girlinherits()