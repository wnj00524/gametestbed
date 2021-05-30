def new_ind(ID = -1, type=1):
    if type == 1:
        i1 = individual(ID, {"hunger": 0, "rest": 0}, None, memory())

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
        self.add_location("eating place", "Where we eat!", "eating")
        self.add_location("resting place", "The place in which we rest.", "resting")


    def return_def_loc(self, title, description, type):
        new_ID = len(self.locations)
        new_loc = location()
        new_loc.ID = new_ID
        new_loc.description = description
        return new_loc

    def add_location(self, title = "default", description = "So empty.", type=None):
        self.locations[title] = self.return_def_loc(title, description, type)


    def add_individual(self, type = 1):
        new_ID = len(self.members)
        temp_individual = new_ind(new_ID,type)
        self.members.append(temp_individual)
        self.locations["the ether"].present.append(self.members[new_ID])



    def tick(self, debug=False):
        for member in self.members:
            #\print(member)
            temp_key = member.location_key[:]
            member.individual_tick()
            #has the location key changed? if so, actually move the individual!
            if temp_key != member.location_key:
                #print(temp_key, " is the same as ", member.location_key)
                self.locations[temp_key].present.pop()
                self.locations[member.location_key].present.append(member)
            if debug:
                print(member.ID, " is currently ", member.state, "\nTired = ", member.needs["rest"], " \nHunger = ", member.needs["hunger"], "\nNow at ", member.location_key)


class memory(dict):
    def __init__(self, locations = {"food": ["eating place"], "rest": ["resting place"]}):
        self["main"] = locations


class individual:
    hour = 0
    def __init__(self, ID, Needs, State, memory = memory(), type = 1, location_key = "the ether"):
        self.ID = ID
        self.needs = Needs
        self.state = State
        self.memory = memory
        self.type = type
        self.location_key = location_key

    def individual_tick(self=None):
        self.hour += 1
        if self.type == 1:
            #set the state
            if self.needs["hunger"] > 5:
                self.state = "food_search"
                self.location_key = self.memory["main"]["food"][0]
            else:
                self.state = "resting"
                self.location_key = self.memory["main"]["rest"][0]

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
        return self.location_key


