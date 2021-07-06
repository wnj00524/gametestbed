
class Record_Person:
    def __init__(self):
        self.__details = {}
        self.linked_emails = set()
        self.linked_locations = set()
        self.linked_groups = set()
        self.linked_events = set()
        self.first_name = ""
        self.last_name = ""

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



    def link_email(self, email, internal=False):
        self.linked_emails.append(email)
        if not internal:
            email.link_person(self,True)



class Record_Email:
    def __init__(self):
        self.value = ""
        self.linked_people = set()

    def link_person(self, person, internal=False):
        self.linked_people.append(person)
        if not internal:
            person.link_email(self,True)

class Record_Location:
    def __init__(self):
        self.value = ""
        self.linked_people = set()

class Record_Group:
    def __init__(self):
        self.name = ""
        self.details = {}
        self.linked_people = set()


class Record_Event:
    def __init__(self):
        self.description = ""
        self.linked_people = set()
        self.linked_locations = set()
