from pathlib import Path

SMALL_TREE = """
   3
  7 4
 2 4 6
8 5 9 3
"""
BIG_TREE = """
              75
             95 64
            17 47 82
           18 35 87 10
          20 04 82 47 65
         19 01 23 75 03 34
        88 02 77 73 07 63 67
       99 65 04 28 06 16 70 92
      41 41 26 56 83 40 80 70 33
     41 48 72 33 47 32 37 16 94 29
    53 71 44 65 25 43 91 52 97 51 14
   70 11 33 28 77 73 17 78 39 68 17 57
  91 71 52 38 17 14 91 43 58 50 27 29 48
 63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return f"Node({self.value})"


def parse_tree(tree):
    tree = tree.strip()
    all_levels = []
    for i, level_str in enumerate(tree.split("\n")):
        level = level_str.strip().split()
        level_nodes = [Node(int(x)) for x in level]
        all_levels.append(level_nodes)

    for i, level in enumerate(all_levels[:-1]):
        for j, node in enumerate(level):
            node.left = all_levels[i + 1][j]
            node.right = all_levels[i + 1][j + 1]

    return all_levels[0][0]


SMALL_TREE = parse_tree(SMALL_TREE)
BIG_TREE = parse_tree(BIG_TREE)


def calc_routes(tree):
    if tree.left is None:
        return tree.value

    return tree.value + max(calc_routes(tree.left), calc_routes(tree.right))


print(calc_routes(SMALL_TREE))
print(calc_routes(BIG_TREE))
