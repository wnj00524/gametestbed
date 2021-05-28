def new_ind(ID = -1, type=1):
    if type == 1:
        i1 = individual(ID, {"hunger": 0, "rest": 0}, None)

    return i1




class pop_c:
    ID = -1
    members = []
    def tick(self, debug=False):
        for member in self.members:
            #\print(member)
            member.tick()
            if debug:
                print(member.ID, " is currently ", member.state, "\nTired = ", member.Needs["rest"], " \nHunger = ", member.Needs["hunger"])



class individual:
    def __init__(self, ID, Needs, State):
        self.ID = ID
        self.Needs = Needs
        self.state = State

    def tick(self=None):
        if self.Needs["hunger"] > 5:
            self.state = "food_search"
        else:
            self.state = "resting"

        if self.state == "resting" and self.Needs["rest"] > 0:
            self.Needs["rest"] -= 1
        elif self.state == "food_search":
            #do food logic
            self.Needs["hunger"] -= 3
        else:

            self.Needs["rest"] += 1
            self.Needs["hunger"] += 1


