
class ProgramInternalForm:
    def __init__(self):
        self.__content = []

    def add(self, code, idd):
        self.__content.append((code, idd))

    def __str__(self):
        my_str = ""
        for pair in self.__content:
            my_str += str(pair) + "\n"
        return my_str
