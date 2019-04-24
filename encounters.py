import roll

class PeacefulEncounter():
    def __init__(self, desc, actions_outcomes):
        self.desc = desc
        self.actions_outcomes = actions_outcomes

    def act_index(self, index):
        for action, outcome in self.actions_outcomes.items():
            if (action[0] == str(index)):
                return outcome
        return "You didn't select a proper action"

    def act(self, action):
        return self.actions_outcomes[action]

    def __str__(self):
        return self.desc

class CombatEncounter():
    def __init__(self, desc, name, hp, ac, dmg):
        self.desc = desc
        self.name = name
        self.hp = hp
        self.ac = ac
        self.dmg = dmg
        self.actions = [
            '1.) Attack', 
            '2.) Flee']
    
    def attack(self, hit_bonus, dmg_range):
        # Roll to hit
        hit = roll.d20(bonus=hit_bonus)
        print(hit)
        if (hit < self.ac): # Miss
            print("The attack misses!")
            return 0
        else: # Hit
            dmg_taken = roll.roll(dmg_range)
            print("{} takes {} damage!".format(self.name, dmg_taken))
            return dmg_taken

    def __str__(self):
        return self.desc

merchant_encounter = PeacefulEncounter(
    desc = "You see a merchant", 
    actions_outcomes = {
        "1.) Kill Him" :  "Gain 30 gold. Lose morality :(",
        "2.) Buy a sword" : "Spent 5 gold, got an Iron Sword",
        "3.) Buy platemail" : "Spent 10 gold, got Platemail"
    })

bandit_encounter = CombatEncounter(
    desc = "You see a bandit",
    name = "Bandit",
    hp = "20",
    ac = 14,
    dmg = (1, 8)
)

bandit_encounter.attack(8, (1, 20))