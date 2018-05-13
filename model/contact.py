from sys import maxsize

class Contact:
    def __init__(self, first_name=None,last_name=None, id=None):
        self.first_name=first_name
        self.last_name=last_name
        self.id = id

    def __repr__(self):
        return "%s:%s:" % (self.id, self.first_name)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id==other.id) and self.first_name==other.first_name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

# przed filmem Sortowanie list przed porównaniem
#
#
# class Contact:
#     def __init__(self, first_name=None,last_name=None, id=None):
#         self.first_name=first_name
#         self.last_name=last_name
#         self.id = id
#
#     def __repr__(self):
#         return "%s:%s" % (self.id, self.first_name)
#
#     def __eq__(self, other):
#         return self.id == other.id and self.first_name == other.first_name