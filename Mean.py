import re
freq = {}


class Mean:
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.pattern = '^([0-9]*)-([0-9]*)$'
        match = re.search(self.pattern, list(self.dictionary.keys())[0])
        self.dif = float(match.group(2)) - float(match.group(1))

    def check_dict(self):
        for a in self.dictionary.keys():
            match = re.search(self.pattern, a)
            ca1 = float(match.group(1))
            ca2 = float(match.group(2))
            if self.dif != (ca2 - ca1):
                print("Dictionary not calculatable")
                raise TypeError("This type of dictionary is not calculatable")

    def calculate_xi(self):
        xi = []
        for elem in self.dictionary.keys():
            match = re.search(self.pattern, elem)
            ca1 = float(match.group(1))
            xi.append(ca1 + (self.dif / 2))
        return xi

    def calculate_fi(self):
        fi = list(self.dictionary.values())
        return fi

    def calculate_fixi(self):
        fixi = []
        num = 0
        for a in self.calculate_xi():
            fixi.append(self.calculate_fi()[num] * self.calculate_xi()[num])
            num += 1
        return fixi

    def __repr__(self):
        self.check_dict()
        return f"{sum(self.calculate_fixi()) / sum(self.calculate_fi())}"


unprocessed_data = input("Enter the data in given format CL1-CL2=f,CL2-CL3=f1 eg:(100-200=40,200-300=10): ").split(',')
print(unprocessed_data)

for a in unprocessed_data:
    pattern = "^([0-9]*)-([0-9]*)=([0-9]+)"
    match = re.search(pattern, a)
    freq.update({f"{match.group(1)}-{match.group(2)}":float(match.group(3))})

print(freq)
print("%.2f" % float(Mean(freq).__repr__()))