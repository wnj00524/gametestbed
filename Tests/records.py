
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

    def search_names(self, item):
        found = False
        if item.strip().lower() in self.first_name.lower():
            found = True
        elif item.strip().lower() in self.last_name.lower():
            found = True
        return found

    def search_alias(self, item):

        found = False
        for record in self.linked_online_ids:
            if item.strip().lower() in record.value.lower():
                found = True
        return found

    def search_locations(self, item):
        found = False
        for record in self.linked_locations:
            if item.strip().lower() in record.value.lower():
                found = True
        return found

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
        if isinstance(email, Record_Online_ID):
            self.linked_online_ids.add(email)
            if not internal:
                email.link_person(self,True)
        else:
            print("Non-online alias record - person record not updated.")
            return -1

    def link_group(self, group, internal=False):
        if isinstance(group, Record_Group):
            self.linked_groups.add(group)
            if not internal:
                group.link_person(self, True)
        else:
            print("Non group record - person record not updated.")
            return -1

    def link_event(self, event, internal=False):
        if isinstance(event, Record_Event):
            self.linked_events.add(event)
            if not internal:
                event.link_person(self, True)

        else:
            print("Non event record - person record not updated.")
            return -1

    def link_location(self, location, internal=False):
        if isinstance(location, Record_Location):
            self.linked_locations.add(location)
            if not internal:
                location.link_person(self, True)
        else:
            print("Non location record - person record not updated.")
            return -1




class Record_Online_ID:
    #dunder methods
    def __init__(self):
        self.value = ""
        self.linked_people = set()

    #search helper

    def search_record(self, s_val):
        print("Record reads " + self.value)
        print("Search is " + s_val)
        if s_val.strip().lower() in self.value.lower():
            return True
        else:
            return False

    def link_person(self, person, internal=False):
        if isinstance(person, Record_Person):
            self.linked_people.add(person)
            if not internal:
                person.link_online_alias(self, True)
            return 1
        else:
            print("Non person record - online alias record not updated.")
            return -1


class Record_Location:
    def __init__(self):
        self.value = ""
        self.linked_people = set()
        self.linked_events = set()

    def link_person(self, person, internal=False):
        if isinstance(person, Record_Person):
            self.linked_people.add(person)
            if not internal:
                person.link_location(self, True)
            return 1
        else:
            print("Error - not person record being added to location. Record left untouched.")
            return -1

    def link_event(self, event, internal=False):
        if isinstance(event, Record_Event):
            self.linked_events.add(event)
            if not internal:
                event.link_location(self, True)
            return 1
        else:
            print("Non event record - location record left untouched.")

class Record_Group:
    def __init__(self):
        self.name = ""
        self.details = {}
        self.linked_people = set()

    def link_person(self, person, internal=False):
        if isinstance(person, Record_Person):
            self.linked_people.add(person)
            if not internal:
                person.link_group(self, True)
            return 1
        else:
            print("Non person record - group record untouched")
            return -1


class Record_Event:
    def __init__(self):
        self.description = ""
        self.linked_people = set()
        self.linked_locations = set()

    def link_person(self, person, internal = False):
        if isinstance(person, Record_Person):
            self.linked_people.add(person)
            if not internal:
                person.link_person(self, True)
            return 1
        else:
            print("Non person record - event record untouched.")


    def link_location(self, location, internal = False):
        if isinstance(location, Record_Location):
            self.linked_locations.add(location)
            if not internal:
                location.link_event(location, True)
            return 1
        else:
            print("Non location record - event record untouched.")

