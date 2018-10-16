import random

class Player:
    def __init__(self, name, hp, gender, race, atk, defe, score):
        self.name = name
        self.hp = hp
        self.maxhp = hp
        self.gender = gender
        self.race = race
        self.atk = atk
        self.defe = defe
        self.ailment = "Normal"
        self.luck = random.randint(0,10)
        self.score = score
    def __str__(self):
        if(self.atk < 5):
            tempatkstr = "Your attack is so weak you wouldn't be able to lethally injure a fly. Good luck out there."
        elif(self.atk == 5):
            tempatkstr = "Your attack is okay, not much to talk about."
        elif(self.atk > 5):
            tempatkstr = "Your attack is so strong, you can split mountains in half."
        if(self.defe < 2):
            tempdefstr = "Your defense is so weak sneezing could send you to the ER. Good luck out there."
        elif (self.defe == 3):
            tempdefstr = "Your defense is meh. Nothing special."
        elif (self.defe > 3):
            tempdefstr = "Your defense is so strong, you could withstand a nuclear warhead."
        return f"Your name is {self.name}. You are a {self.gender} {self.race} with {self.hp} HP remaining." \
               f" \n{tempatkstr} \n{tempdefstr} \nIf a number could summarize your luck, it'd be {self.luck}/10. \n"

    #def getPlayerName(self): Not needed
    #    return self.name

    def hurt(self, value):
        """

        Args:

        Returns:


        """
        print(f"{self.name} loses {value} HP!")
        self.hp -= value


    def recover(self, value):
        print(f"{self.name} recovers {value} HP!")
        self.hp += value


