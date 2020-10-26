from lab3.program_internal_form import ProgramInternalForm
from lab3.scanner import Scanner
from lab3.symbol_table import SymbolTable


def main():
    sym_constants = SymbolTable()
    sym_identifiers = SymbolTable()
    pif = ProgramInternalForm()
    scanner = Scanner()

    try:
        scanner.scan("p2.txt", sym_constants, sym_identifiers, pif)
        print("lexically correct")
        print("--------------------------------------")
        print("PIF")
        print("--------------------------------------")
        print(pif)
        f = open("PIF.out", "w")
        f.write(str(pif))
        print("--------------------------------------")
        print("SYM CONSTANTS")
        print("--------------------------------------")
        sym_constants.print()
        print(sym_constants)
        print("--------------------------------------")
        print("SYM IDENTIFIERS")
        print("--------------------------------------")
        sym_identifiers.print()
        print(sym_identifiers)
        f = open("ST.out", "w")
        f.write(str(sym_constants) + "\n" + str(sym_identifiers))
    except Exception as err:
        print(err)


main()
