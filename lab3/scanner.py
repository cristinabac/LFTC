# separators = ['[', ']', '{', '}', '(', ')', ';', ' ', ':']
# operators = ['+', '-', '*', '/', '%', '<', '<=', '=', '>=', '>',
#              '>>', '<<', '==', '&&', '||', '!', '!=', '&', '~',
#              '|', '^', '++', '--', ',']
# reservedWords = ['oare', 'nup', 'numar_intreg', 'da_la_pc', 'arata', 'parcurge', 'sir', 'de', 'caracter',
#                  'creste_valoarea', 'egalite_fraternite', 'primeste']
#
# everything = separators + operators + reservedWords
# codification = dict([(everything[i], i + 2) for i in range(len(everything))])
# codification['identifier'] = 0
# codification['constant'] = 1
#
# def get_tokens(tokens_file):
#     file = open(tokens_file)
#     list_of_tokens = []
#     for line in file:
#         for word in line.split():
#             list_of_tokens.append(word)
#     return list_of_tokens
#
# print(get_tokens("token.in"))

import re

from lab3.program_internal_form import ProgramInternalForm
from lab3.symbol_table import SymbolTable


def is_identifier(token):
    return re.match(r'^[a-zA-Z]([a-zA-Z]|[0-9]|_)*$', token) is not None


print(is_identifier("mama"))
print(is_identifier("aaaaaaaaaaaaaaaaaaaaaaaa"))
print(is_identifier("m_a_ma2"))
print(is_identifier("2"))
print(is_identifier("2mama"))
print(is_identifier("#mama"))


def is_constant(token):
    return re.match('^(0|[\+\-]?[1-9][0-9]*)$|^\'.*\'$|^\".*\"$', token) is not None


print()
print(is_constant("2"))
print(is_constant("'ana'"))
print(is_constant("\"ana\""))
print(is_constant("ana"))
print(is_constant("2.1"))
print(is_constant("2,1"))


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

    def __detect_tokens(self, line):
        lst = []
        for word in line.split():
            lst.append(word)
        return lst

    def scan(self, filename, symbol_table_constants: SymbolTable, symbol_table_identifiers: SymbolTable, pif: ProgramInternalForm):
        file = open(filename)
        line_count = 0
        for line in file:
            line_count += 1
            tokens = self.__detect_tokens(line)
            for token in tokens:
                if token in self.list_of_tokens:
                    pif.add(token, 0)
                elif is_constant(token):
                    index = symbol_table_constants.search(token)
                    pif.add(token, index)
                elif is_identifier(token):
                    index = symbol_table_identifiers.search(token)
                    pif.add(token, index)
                else:
                    raise Exception("Lexical error on line " + str(line_count)) #print token



