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
        return "{}\n{}".format(self.desc, str(self.actions_outcomes))
    
    def generate_random_encounter():
        encounter = PeacefulEncounter(
            desc = "You <encounter synonym> a <person>", 
            actions_outcomes = {
                "1.) <action 1>" :  "<outcome 1>",
                "1.) <action 2>" :  "<outcome 2>",
            })
        return encounter

class CombatEncounter():
    def __init__(self, desc, name, hp, ac, enemy_dmg_range):
        self.desc = desc
        self.name = name
        self.hp = hp
        self.ac = ac
        self.enemy_dmg_range = enemy_dmg_range
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

def read_peaceful_encounters(filename="peaceful_encounters.txt"):
    f = open(filename, "r")
    all_encounters = []
    lines = []
    for line in f:
        if (line.strip() == "/begin"):
            lines = []
        elif (line.strip() == ""):
            pass
        elif (line.strip() == "/end"):
            desc = lines[0].strip()
            actions_outcomes = {}
            for action_outcome in lines[1:]:
                split = action_outcome.split(" | ")
                action = split[0].strip()
                outcome = split[1].strip()
                actions_outcomes[action] = outcome
            encounter = PeacefulEncounter(desc=desc, actions_outcomes=actions_outcomes)
            all_encounters.append(encounter)
        else:
            lines.append(line)
    f.close()
    return all_encounters


encs = read_peaceful_encounters()
for enc in encs:
    print(enc)