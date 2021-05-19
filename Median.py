import re
freq = {}


def get_and_process_input():
    unprocessed_data = input("Enter the data in given format CL1-CL2=f,CL2-CL3=f1 eg:(100-200=40,200-300=10): ")
    if unprocessed_data == 'dev':
        split_unprocessed_data = ['100-200=10', '200-300=90', '300-400=60']
    else:
        split_unprocessed_data = unprocessed_data.split(',')
    for a in split_unprocessed_data:
        pattern = r"^([0-9]*)-([0-9]*)=(\d*\.?\d*|[0-9]+)$"
        match = re.search(pattern, a)
        freq.update({f"{match.group(1)}-{match.group(2)}": float(match.group(3))})


class Median:
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.cl1 = None
        self.cf = None
        self.cf_list = None
        self.n = None
        self.f = None
        self.h = None
        self.index = None

    @property
    def median(self):
        value_list = list(self.dictionary.values())
        self.n = sum(value_list)
        n_by_2 = self.n / 2
        self.cf_list = []
        for element in value_list:
            self.cf_list.append(sum(value_list[:value_list.index(element) + 1]))
        foo = []
        for element in self.cf_list:
            foo.append(abs(element - n_by_2))
        self.index = foo.index(min(foo))
        self.cf = self.cf_list[self.index - 1]
        self.f = list(self.dictionary.values())[self.index]

    @property
    def l_and_h(self):
        key_list = list(self.dictionary.keys())
        median_class = key_list[self.index]
        pattern = '^([0-9]+)-([0-9]+)$'
        match = re.match(pattern, median_class)
        self.cl1 = float(match.group(1))
        l1 = float(match.group(2))
        self.h = l1 - self.cl1

    def calculation(self):
        self.median
        self.l_and_h
        top = (self.n / 2) - self.cf
        fraction = top / self.f
        result = self.cl1 + (fraction * self.h)
        return result


try:
    get_and_process_input()
    print(f"Your Mode for \n{freq} is:\n" + "%.2f" % float(Median(freq).calculation()))
except AttributeError:
    print('\n')
    print("Oops your type of input is wrong, try again.")
