def normalize(numbers):
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result


path = "/tmp/my_numbers.txt"
"""
with open(path, "w") as f:
    for i in [15, 80, 35]:
        f.write("%d\n" % i)
"""


class ReadVisits(object):
    def __init__(self, path):
        self.path = path

    def __iter__(self):
        with open(self.path, "r") as f:
            for line in f:
                yield int(line)


it = ReadVisits(path)
print(normalize(it))
