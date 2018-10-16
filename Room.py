class Room:
    """
    Title = String
    Description = String
    HP = Int. Under certain circumstances, a room's HP can be affected
    Items = List of items
    Enemies = List of Enemies
    NPC = List of NPCs

    """

    def __init__(self, title, description, hp, items, enemies, npc, canExit):
        self.title = title
        self.description = description
        self.hp = hp
        self.items = items
        self.enemies = enemies
        self.npc = npc
        self.canExit = canExit

    def __str__(self):
        print("----------------------------------------------------------------")
        print(self.title)
        print("----------------------------------------------------------------")
        print(self.description)
        print(self.canExit)
        return("")
