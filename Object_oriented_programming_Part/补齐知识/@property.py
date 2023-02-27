class Father(object):
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        if self.first and self.last:
            return '{}_{}@email.com'.format(self.first, self.last)

    @email.setter
    def email(self, to_change):
        self.first, self.last = to_change.split(' ')

    @email.deleter
    def email(self):
        print('wrong')
        self.first, self.last = None, None


"""create_obj"""

obj = Father('stephen', 'du')
print(obj.first, obj.last, obj.email)
obj.email = 'justin boy'
print(obj.first, obj.last, obj.email)
del obj.email
print(obj.first, obj.last, obj.email)
