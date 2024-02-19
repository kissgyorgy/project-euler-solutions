WORDS = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
}


def make_word(n):
    words = []
    if n // 1_000 > 0:
        words += [WORDS[n // 1_000], "thousand"]
    elif n // 100 > 0:
        words += [WORDS[n // 100], "hundred"]

    if n % 100 in WORDS:
        if words:
            words += ["and"]
        words += [WORDS[n % 100]]
    elif n % 100 - (n % 10) in WORDS:
        if words:
            words += ["and"]
        words += [WORDS[n % 100 - n % 10], "-", WORDS[n % 10]]
    elif n % 10 != 0:
        if words:
            words += ["and"]
        words += [WORDS[n % 10]]

    return " ".join(words)


print(342, make_word(342))
print(340, make_word(340))
print(115, make_word(115))
print(1000, make_word(1000))

sum_letters = 0
for num in range(1, 1001):
    letters = make_word(num).replace(" ", "").replace("-", "")
    print(num, letters, len(letters))
    sum_letters += len(letters)

print("Summary:", sum_letters)
