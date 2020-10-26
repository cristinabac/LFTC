
import re

from lab3.program_internal_form import ProgramInternalForm
from lab3.symbol_table import SymbolTable

separators = ['[', ']', '{', '}', '(', ')', ';', ' ', ':', ',', '\n', '\t']
operators = ['+', '-', '*', '/', '%', '<', '<=', '=', '>=', '>',
             '>>', '<<', '==', '&&', '||', '!', '!=', '&', '~',
             '|', '^', '++', '--', ',']
reservedWords = ['oare', 'nup', 'numar_intreg', 'da_la_pc', 'arata', 'parcurge', 'sir', 'de', 'caracter',
                 'creste_valoarea', 'egalite_fraternite', 'primeste']

def is_identifier(token):
    return re.match(r'^[a-zA-Z]([a-zA-Z]|[0-9]|_)*$', token) is not None


def is_constant(token):
    return re.match('^(0|[\+\-]?[1-9][0-9]*)$|^\'.*\'$|^\".*\"$', token) is not None


class Scanner:

    def __init__(self):
        self.__read_tokens()

    def __read_tokens(self):
        file = open("token.in")
        list_of_tokens = []
        for line in file:
            for word in line.split():
                list_of_tokens.append(word)
        self.list_of_tokens = list_of_tokens

    '''
    def __detect_tokens(self, line):
        lst = []
        for separator in separators:
            new = " " + separator + " "
            line = line.replace(separator, new)

        for operator in operators:
            new = " " + operator + " "
            line = line.replace(operator, new)

        # remove multiple spaces
        line = ' '.join(line.split())

        for word in line.split():
            lst.append(word)
        # for token in get_tokens_from_line(line, separators):
        #     lst.append(token)
        return lst
    '''

    def __detect_tokens(self, line):
        lst = []  # final list with all tokens

        pos = 0  # position in line
        while pos < len(line):
            # check for string constants:  "ana are mere"
            if line[pos] == "\"":
                pos2 = pos + 1
                while pos2 < len(line) and line[pos2] != "\"":
                    pos2 += 1
                string_constant = line[pos:pos2+1]
                lst.append(string_constant)
                pos = pos2
            # check for string constants: 'ana are mere'
            elif line[pos] == "\'":
                pos2 = pos + 1
                while pos2 < len(line) and line[pos2] != "\'":
                    pos2 += 1
                string_constant = line[pos:pos2+1]
                lst.append(string_constant)
                pos = pos2
            # check for white spaces
            elif line[pos] == " " or line[pos] == "\n" or line[pos] == "\t":
                pass
            # check for separators (but not white spaces)
            elif line[pos] in separators:
                lst.append(line[pos])
            else:
                # not separator, " or '
                # check for double operators
                if line[pos] in operators and pos < len(line) - 1 and line[pos:pos + 2] in operators:
                    new_token = line[pos:pos + 2]
                    lst.append(new_token)
                    pos += 1
                elif line[pos] in operators:  # simple operator
                    lst.append(line[pos])
                else:
                    # detect the token
                    pos2 = pos + 1
                    while pos2 < len(line) and line[pos2] not in separators and line[pos2] not in operators:
                        pos2 += 1
                    new_token = line[pos:pos2]
                    lst.append(new_token)
                    pos = pos2 - 1

            pos += 1

        return lst

    def scan(self, filename, symbol_table_constants: SymbolTable, symbol_table_identifiers: SymbolTable, pif: ProgramInternalForm):
        file = open(filename)
        line_count = 0
        for line in file:
            line_count += 1
            # print(line)
            tokens = self.__detect_tokens(line)
            print(line, "line nr: ", line_count, tokens, "\n")
            for token in tokens:
                if token in self.list_of_tokens:
                    pif.add(token, 0)
                elif token in separators:
                    pif.add(token, 0)
                elif is_constant(token):
                    if symbol_table_constants.search(token) is None:
                        symbol_table_constants.insert(token)
                    index = symbol_table_constants.search(token)
                    pif.add("CONST", index)
                elif is_identifier(token):
                    if symbol_table_identifiers.search(token) is None:
                        symbol_table_identifiers.insert(token)
                    index = symbol_table_identifiers.search(token)
                    pif.add("ID", index)
                else:
                    raise Exception("Lexical error on line " + str(line_count) + ", unknown token: " + token)



