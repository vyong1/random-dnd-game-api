class Encounter():
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

e = Encounter(
    desc = "You see a merchant", 
    actions_outcomes = {
        "1.) Kill Him" :  "Gain 30 gold. Lose morality :(",
        "2.) Buy a sword" : "Spent 5 gold, got an Iron Sword",
        "3.) Buy platemail" : "Spent 10 gold, got Platemail"
    })

# print(e.act("1.) Kill Him"))
print(e.act_index(3))