import regex as re

with open ('input.txt') as f:
    lines = f.read().split()

digit_words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def getNumbers (line):
    def getDigit(target):
        return str(digit_words.index(target)+1) if target in digit_words else target

    matches = re.findall(r'\d|'+'|'.join(digit_words), line, overlapped=True)
    first_digit = getDigit(matches[0])
    last_digit = getDigit(matches[-1])

    return int(first_digit + last_digit)

numbers = []

for x in lines:
    numbers.append(getNumbers(x))

print(sum(numbers))