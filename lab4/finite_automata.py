
class FiniteAutomata:

    def __init__(self, Q, E, S, q0, F):
        self.Q = Q
        self.E = E
        self.S = S
        self.q0 = q0
        self.F = F

    def split_line(self, line):
        return [elem.strip() for elem in line.split(',')]

    def split_transition(self, line):
        line = line.split("=")
        lhs = line[0]
        rhs = line[1]
        lhs = lhs.split(",")
        return ((lhs[0],lhs[1]),rhs)


    def read_from_file(self, fileName):
        '''
        first line: Q
        second line: E
        third line: q0
        4th line: F (final state)
        the remaining lines are the transitions: S
        '''
        f = open(fileName)
        Q = self.split_line(f.readline())
        E = self.split_line(f.readline())
        q0 = f.readline().strip()
        F = self.split_line(f.readline())
        # now, read all the other lines
        S = []
        for line in f:
            S.append(self.split_transition(line))

        return FiniteAutomata(Q, E, S, q0, F)

    def __str__(self):
        return 'Q = { ' + ', '.join(self.Q) + ' }\n' \
               + 'E = { ' + ', '.join(self.E) + ' }\n' \
               + 'q0 = ' + str(self.q0) + '\n' \
               + 'F = { ' + ', '.join(self.F) + ' }\n' \
               + 'S = { ' + ' '.join([' -> '.join([str(part) for part in trans]) for trans in self.S]) + ' }\n'
