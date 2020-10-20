from lab3.program_internal_form import ProgramInternalForm
from lab3.scanner import Scanner
from lab3.symbol_table import SymbolTable


def main():
    sym_constants = SymbolTable()
    sym_identifiers = SymbolTable()
    pif = ProgramInternalForm()
    scanner = Scanner()

    try:
        scanner.scan("p1.txt", sym_constants, sym_identifiers, pif)
    except Exception as err:
        print(err)


main()