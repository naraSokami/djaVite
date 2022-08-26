TYPES = {
    'date': 'DateTimeField',
    'str': 'CharField',
    'int': 'IntegerField',
}

class Column:
    def __init__(self, name, type='str', options={}):
        self.name = name
        self.type = type
        self.options = options


    def str(self):
        return f'{self.name} = models.{TYPES[self.type]}({", ".join([f"{str(k)}={str(v)}" for k, v in self.options.items()])})'

    



class Model:
    def __init__(self, name, app, v=True):
        self.name = name
        self.columns = {}
        self.app = app


    def getColumns():
        matches = re.search()


    def hasColumn(name):
        pass


    def addColumn(name, value):
        pass


    def removeColumn(name):
        pass


    def remove():
        pass