def new_ind(ID = -1, type=1):
    if type == 1:
        i1 = individual(ID, {"hunger": 0, "rest": 0}, None, memory({}))

    return i1

class location(dict):
    def __init__(self, ID = -1, present = [], type = None, description = "So empty."):
        self.ID = ID
        self.type = type
        self.present = present
        self.description = description


class population:

    def __init__(self, ID = -1, members = [], locations = {}):
        self.ID = ID
        self.members = members
        self.locations = locations
        self.add_location("the ether","The starting ether.", "ether")


    def return_def_loc(self, title, description, type):
        new_ID = len(self.members)
        new_loc = location()
        new_loc.ID = new_ID
        new_loc.description = description
        return new_loc

    def add_location(self, title = "default", description = "So empty.", type=None):
        self.locations[title] = self.return_def_loc(title, description, type)


    def tick(self, debug=False):
        for member in self.members:
            #\print(member)
            member.individual_tick()
            if debug:
                print(member.ID, " is currently ", member.state, "\nTired = ", member.Needs["rest"], " \nHunger = ", member.Needs["hunger"])


class memory:
    def __init__(self, locations = {"food": [], "rest": []}):
        locations = locations

class individual:
    hour = 0
    def __init__(self, ID, Needs, State, Memory, type = 1):
        self.ID = ID
        self.needs = Needs
        self.state = State
        self.memory = Memory
        self.type = type

    def individual_tick(self=None):
        self.hour += 1
        if self.type == 1:
            #set the state
            if self.needs["hunger"] > 5:
                self.state = "food_search"
            else:
                self.state = "resting"

            #carry out actions


            #update the needs
            if self.state == "resting" and self.needs["rest"] > 0:
                self.needs["rest"] -= 1
            elif self.state == "food_search":
                #do food logic
                self.needs["hunger"] -= 3
            else:
                self.needs["rest"] += 1
                self.needs["hunger"] += 1


