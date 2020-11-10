from lab4.transition import Transition


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
        lhs = line[0]  # start state, value
        rhs = line[1]  # end state
        lhs = lhs.split(",")
        return Transition(lhs[0].strip(), rhs.strip(), lhs[1].strip())

    def read_from_file(self, file_name):
        '''
        first line: Q
        second line: E
        third line: q0
        4th line: F (final state)
        the remaining lines are the transitions: S
        '''
        f = open(file_name)
        Q = self.split_line(f.readline())
        E = self.split_line(f.readline())
        q0 = f.readline().strip()
        F = self.split_line(f.readline())
        # now, read all the other lines
        S = []
        for line in f:
            S.append(self.split_transition(line))

        return FiniteAutomata(Q, E, S, q0, F)

    def is_dfa(self):
        transition_list = []
        for transition in self.S:
            trans_tuple = (transition.start_state, transition.value)
            if trans_tuple in transition_list:
                return False
            transition_list.append(trans_tuple)
        return True

    def verify_sequence(self, sequence):
        # keep the current state: we start from the initial state
        current_state = self.q0

        # construct dictionary of transitions
        # (start state, value): end state
        transition_dict = {}
        for transition in self.S:
            trans_tuple = (transition.start_state, transition.value)
            transition_dict[trans_tuple] = transition.end_state

        for s in sequence:
            # print(str((current_state, s)) + "->" + transition_dict[(current_state, s)])
            if (current_state, s) in transition_dict.keys():
                current_state = transition_dict[(current_state, s)]  # get the next state
            else:
                return False

        return current_state in self.F

    def __str__(self):
        return 'Q = { ' + ', '.join(self.Q) + ' }\n' \
               + 'E = { ' + ', '.join(self.E) + ' }\n' \
               + 'q0 = ' + str(self.q0) + '\n' \
               + 'F = { ' + ', '.join(self.F) + ' }\n' \
               + 'S = { ' + ' '.join([str(trans) for trans in self.S]) + ' }\n'
