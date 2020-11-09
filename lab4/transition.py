
class Transition:

    def __init__(self, start_state, end_state, value):
        self.start_state = start_state
        self.end_state = end_state
        self.value = value

    def __str__(self):
        return self.start_state + "," + self.value + "->" + self.end_state
