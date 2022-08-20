#HomeWork 1
class Name:
    def __init__(self, first_name, last_name):
        self.first_name = first_name.lower().capitalize()
        self.last_name = last_name.lower().capitalize()
        self.full_name = self.first_name + " " + self.last_name
        self.initials = self.first_name[0] + "." + self.last_name[0]

n = Name('jOhN', 'sILvER')
print(n.first_name)
print(n.last_name)
print(n.full_name)
print(n.initials)