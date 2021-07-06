
class Record_Person:
    def __init__(self):
        self.__details = {}
        self.linked_online_ids = set()
        self.linked_locations = set()
        self.linked_groups = set()
        self.linked_events = set()
        self.first_name = ""
        self.last_name = ""

        # useful dunder methods
    def __str__(self):
        return self.first_name + " " + self.last_name



    #setters

    @property
    def linked_events(self):
        return self.__details["linked_events"]

    @property
    def linked_online_ids(self):
        return self.__details["linked_emails"]

    @linked_events.setter
    def linked_events(self, linked_events):

        self.__details["linked_events"] = linked_events

    @linked_online_ids.setter
    def linked_online_ids(self, linked_emails):
        self.__details["linked_emails"] = linked_emails




    @property
    def linked_groups(self):
        return self.__details["linked_groups"]

    @linked_groups.setter
    def linked_groups(self, linked_groups):
        self.__details["linked_groups"] = linked_groups

    @property
    def linked_locations(self):
        return self.__details["linked_locations"]

    @linked_locations.setter
    def linked_locations(self, linked_locations):
        self.__details["linked_locations"] = linked_locations

    @property
    def first_name(self):
        return self.__details["firstname"]

    @first_name.setter
    def first_name(self, first_name):
        self.__details["firstname"] = first_name

    @property
    def last_name(self):
        return self.__details["lastname"]

    @last_name.setter
    def last_name(self, last_name):
        self.__details["lastname"] = last_name




    #Linking methods - check internal to see if it's been called by another linking method. Avoid infinte loops!

    def link_online_alias(self, email, internal=False):
        self.linked_online_ids.add(email)
        if not internal:
            email.link_person(self,True)

    def link_group(self, group, internal=False):
        self.linked_groups.add(group)
        if not internal:
            group.link_person(self, True)

    def link_event(self, event, internal=False):
        self.linked_events.add(event)
        if not internal:
            event.link_person(self, True)

    def link_location(self, location, internal=False):
        self.linked_locations.add(location)
        if not internal:
            location.link_person(self, True)




class Record_Online_ID:
    def __init__(self):
        self.value = ""
        self.linked_people = set()

    def link_person(self, person, internal=False):
        self.linked_people.add(person)
        if not internal:
            person.link_online_alias(self, True)

class Record_Location:
    def __init__(self):
        self.value = ""
        self.linked_people = set()
        self.linked_events = set()

    def link_person(self, person, internal=False):
        if str(type(person)) == "<class 'Tests.records.Record_Person'>":
            self.linked_people.add(person)
            if not internal:
                person.link_location(self, True)
        else:
            print("Error - not person record being added to location. Record left untouched.")

    def link_event(self, event, internal=False):
        self.linked_events.add(event)
        if not internal:
            event.link_location(self, True)

class Record_Group:
    def __init__(self):
        self.name = ""
        self.details = {}
        self.linked_people = set()

    def link_person(self, person, internal=True):
        self.linked_people.add(person)
        if not internal:
            person.link_record(self,True)


class Record_Event:
    def __init__(self):
        self.description = ""
        self.linked_people = set()
        self.linked_locations = set()

    def link_person(self, person, internal = False):
        self.linked_people.add(person)
        if not internal:
            person.link_person(self, True)

    def link_location(self, location, internal = False):
        self.linked_locations.add(location)
        if not internal:
            location.link_event(location, True)

