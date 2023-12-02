digitWords = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
total = 0

with open('Day01/input.txt', 'r') as file:
    for line in file:
        digits = ""
        wordIdices = [None] * len(line)
        for i, word in enumerate(digitWords):
            indexes = [i for i in range(len(line)) if line.startswith(word, i)]
            for index in indexes:
                wordIdices[index] = i+1
        for j, digit in enumerate(wordIdices):
            if digit is not None:
                line = line[:j] + str(digit) + line[j+1:]
        digits = ''.join(c for c in line if c.isdigit())
        total += int(digits[0]+digits[-1])
print(total)
