from lab3.scanner import is_identifier, is_constant
from lab3.symbol_table import SymbolTable

print(is_identifier("mama"))
print(is_identifier("aaaaaaaaaaaaaaaaaaaaaaaa"))
print(is_identifier("m_a_ma2"))
print(is_identifier("2"))
print(is_identifier("2mama"))
print(is_identifier("#mama"))


print()
print(is_constant("2"))
print(is_constant("'ana'"))
print(is_constant("\"ana\""))
print(is_constant("ana"))
print(is_constant("2.1"))
print(is_constant("2,1"))
print(is_constant("+2"))
print(is_constant("-2"))

mystring = "la aaa    a  a  a"
print(' '.join(mystring.split()))
print(mystring)



# test
sym1 = SymbolTable()
sym1.insert("a")
sym1.insert("b")
sym1.insert("c")
print(sym1.search("a"))
print(sym1.search("b"))
print(sym1.search("c"))
sym2 = SymbolTable()
sym2.insert(1)
sym2.insert(3)
print(sym2.search(1))
print(sym2.search(3))
print(sym2.search(4))

sym3 = SymbolTable()
sym3.insert("b")
sym3.insert("a")
sym3.insert("c")
sym3.insert("e")
sym3.insert("d")


sym1.print()
print()
sym2.print()
print()
sym3.print()