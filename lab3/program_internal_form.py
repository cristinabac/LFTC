
class ProgramInternalForm:
    def __init__(self):
        self.__content = []

    def add(self, code, idd):
        self.__content.append((code, idd))

    def __str__(self):
        return str(self.__content)
