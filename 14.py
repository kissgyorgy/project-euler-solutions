def calc_chain_len(n):
    chain_len = 1

    while n != 1:
        chain_len += 1

        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1

    return chain_len


def find_max_chain(below):
    max_chain_n = 0
    max_chain_len = 0
    for n in range(below, 1, -1):
        chain_len = calc_chain_len(n)
        if chain_len > max_chain_len:
            max_chain_len = chain_len
            max_chain_n = n
    return (max_chain_n, max_chain_len)


if __name__ == "__main__":
    below = 1_000_000
    print(find_max_chain(below))
