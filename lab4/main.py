from lab4.finite_automata import FiniteAutomata


def main():
    fa = FiniteAutomata(None, None, None, None, None)
    fa = fa.read_from_file("fa2.txt")
    print(fa)

    while True:
        print("Commands list:")
        print("1 - for the list of states(Q)")
        print("2 - for the alphabet(Sigma)")
        print("3 - for the initial state(q0)")
        print("4 - for the list of final states(F)")
        print("5 - for the list of transitions(S)")
        print("0 - exit")
        cmd = input("Enter your command:")
        if cmd == "0":
            break
        elif cmd == "1":
            print(fa.Q)
        elif cmd == "2":
            print(fa.E)
        elif cmd == "3":
            print(fa.q0)
        elif cmd == "4":
            print(fa.F)
        elif cmd == "5":
            print(' '.join([' -> '.join([str(part) for part in trans]) for trans in fa.S]))
        else:
            print("invalid command")

main()