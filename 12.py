def main():
    trinum = 0
    for next_trinum in range(99999999999999999):
        trinum += next_trinum
        print("Next triangle number:", trinum, end="")
        # count the dividers without 1 and trinum
        dividers_num = sum(trinum % n == 0 for n in range(2, trinum))
        dividers_num += 2  # add 1 and trinum itself
        print(", dividers:", dividers_num)
        if dividers_num > 500:
            return trinum


if __name__ == "__main__":
    triangle_number = main()
    print("Result:", triangle_number)
