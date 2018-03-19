# Robert Call
# Reads from file and makes a dictionary keyed by every word in that file
# for each line in the file finds all occurrences of the word and stores which line it was found
# and how many times it occurred

import re

class xref:
    def __init__(self, _fname):
        self.file_name = _fname
        self.words = []
        self.word_dict = {}
        self.string = ""
        self.read_words()
        self.set_keys()
        self.get_data()

    def read_words(self):
        with open(self.file_name, "r+") as f:
            self.string = f.read()
            self.words = re.findall(r"\b([a-zA-Z]+-*'?[a-zA-Z]*)+\b", self.string)

            self.words += [x.strip(' ') for x in re.findall(r"\s-+[a-zA-Z]?\s*", self.string)]

    def set_keys(self):
        for word in self.words:
            if word not in self.word_dict.keys():
                self.word_dict[word] = []

    def get_data(self):
        count = 0
        for line in self.string.splitlines():
            words_in_line = re.findall(r"\b([a-zA-Z]+-*'?[a-zA-Z]*)+\b", line)
            words_in_line+= [x.strip(' ') for x in re.findall(r"\s-+[a-zA-Z]?\s*", line)]
            count += 1
            for eword in words_in_line:
                occ = words_in_line.count(eword)
                self.word_dict[eword].append((count, occ))

    def print_all(self):
        keys = self.word_dict.keys()
        keys = sorted(keys)
        keys = sorted(keys, key=lambda s: s.lower())
        longest = max(keys, key=len)
        for key in keys:
            print()
            print('-'*125)
            count = 0
            print(str("\n" + key+":").ljust(len(longest)+10), end='')
            for item in self.word_dict[key]:
                if count < 9:
                    count += 1
                    print(':' + str(item[0])+ ':'+str(item[1]), end=', ')
                else:
                    print("\n".ljust(len(longest)+10), end='')
                    count = 0

    def print_list(self, list):
        keys = list
        keys = sorted(keys)
        keys = sorted(keys, key=lambda s: s.lower())
        longest = max(keys, key=len)
        for key in keys:
            print()
            count = 0
            print(str("\n" + key+":").ljust(len(longest)+4), end='')
            for item in self.word_dict[key]:
                if count < 9:
                    count += 1
                    print(':' + str(item[0])+ ':'+str(item[1]), end=', ')
                else:
                    print("\n".ljust(len(longest)+4), end='')
                    count = 0


if __name__ == '__main__':
    c = xref("Strings.txt")
    with open("search.txt", "r+") as sfile:
        lines = sfile.read().splitlines()
        c.print_list(lines)