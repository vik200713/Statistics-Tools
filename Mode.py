import re

freq = {}


def get_and_process_input():
    unprocessed_data = input("Enter the data in given format CL1-CL2=f,CL2-CL3=f1 eg:(100-200=40,200-300=10): ")
    split_unprocessed_data = unprocessed_data.split(',')
    for a in split_unprocessed_data:
        pattern = r"^([0-9]*)-([0-9]*)=(\d*\.?\d*|[0-9]+)$"
        match = re.search(pattern, a)
        freq.update({f"{match.group(1)}-{match.group(2)}": float(match.group(3))})


class Mode:
    def __init__(self, dictionary):
        self.cl1 = None
        self.f1 = None
        self.f0 = None
        self.f2 = None
        self.h = None
        self.max_index = None
        self.dictionary = dictionary

    def f(self):
        value_list = list(self.dictionary.values())

        self.f1 = max(value_list)
        self.max_index = value_list.index(self.f1)

        self.f0 = 0 if value_list[0] == self.f1 else value_list[self.max_index - 1]
        self.f2 = 0 if value_list[-1] == self.f1 else value_list[self.max_index + 1]

    def l_and_h(self):
        key_list = list(self.dictionary.keys())
        modal_class = key_list[self.max_index]
        pattern = '^([0-9]+)-([0-9]+)$'
        match = re.match(pattern, modal_class)
        self.cl1 = float(match.group(1))
        l1 = float(match.group(2))
        self.h = l1 - self.cl1

    def value(self):
        self.f()
        self.l_and_h()
        top = self.f1 - self.f0
        bottom = (2 * self.f1) - self.f0 - self.f2
        return '{:.2f}'.format(self.cl1 + (top / bottom * self.h))


try:
    get_and_process_input()
    print(f"Your Mode for \n{freq} is:\n" + "%.2f" % float(Mode(freq).value()))
except AttributeError:
    print('\n')
    print("Oops your type of input is wrong, try again.")
