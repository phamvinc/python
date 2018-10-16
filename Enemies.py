class Enemies:
    def __init__(self, name, description, hp, atk, defe):
        self.name = name
        self.description = description
        self.hp = hp
        self.atk = atk
        self.defe = defe
    def __str__(self):
        print("----------------------------------------------------------------")
        print(self.name)
        print("----------------------------------------------------------------")
        print(self.description)
        return("")
