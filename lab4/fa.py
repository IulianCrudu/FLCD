from collections import defaultdict


class FiniteAutomata:
    def __init__(self, file_name: str):
        self.states = []
        self.alphabet = []
        self.neighbours = defaultdict(list)
        self.initial_state = None
        self.final_states = []
        self.transitions = {}
        self.read_file(file_name)

    def read_file(self, file_name: str):
        file = open(file_name, "r")
        lines = file.readlines()

        self.states = lines[0].strip().split(",")
        self.alphabet = lines[1].strip().split(",")
        self.initial_state = lines[2].strip()
        self.final_states = lines[3].strip().strip(",")

        for line in lines[4:]:
            elements = line.strip().split(",")
            first = elements[0]
            second = elements[1]
            values = elements[2:]

            self.neighbours[first].append(second)
            self.transitions[(first, second)] = values

        file.close()

    def check_if_sequence_is_accepted(self, sequence, state):
        if len(sequence) == 0:
            return state in self.final_states

        for neighbor in self.neighbours[state]:
            values = self.transitions[(state, neighbor)]

            if sequence[0] in values:
                if self.check_if_sequence_is_accepted(sequence[1:], neighbor):
                    return True

        return False

    def check_sequence(self, sequence) -> bool:
        return self.check_if_sequence_is_accepted(sequence, self.initial_state)

    def print_menu(self):
        print("1. The set of states")
        print("2. The alphabet")
        print("3. All the transitions")
        print("4. Initial State")
        print("5. Final States")
        print("6. Check sequence is accepted")
        print("0. Exit")
        print("")

    def menu(self):
        while True:
            self.print_menu()
            option = input("Select option: ")

            if option == "1":
                print(f"The states are: {','.join(self.states)}")
            elif option == "2":
                print(f"The alphabet is: {','.join(self.alphabet)}")
            elif option == "3":
                print(f"The transitions are: {self.transitions}")
            elif option == "4":
                print(f"Initial state is: {self.initial_state}")
            elif option == "5":
                print(f"Final states are: {self.final_states}")
            elif option == "6":
                sequence = input("Sequence to be checked: ")
                if self.check_sequence(sequence):
                    print("The sequence is accepted")
                else:
                    print("The sequence is not accepted")
            elif option == "0":
                print("Bye bye!")
                break


if __name__ == "__main__":
    fa = FiniteAutomata("fa_integer_constant.in")
    fa.menu()
