class Node:
    def __init__(self, data, level):
        self.data = data
        self.level = level

    def generate_child(self):
        x, y = self.find('_')
        val_list = [(x, y-1), (x, y+1), (x-1, y), (x+1, y)]
        children = []
        for i, j in val_list:
            child = self.shuffle(x, y, i, j)
            if child:
                children.append(Node(child, self.level + 1))
        return children

    def shuffle(self, x1, y1, x2, y2):
        n = len(self.data)
        if 0 <= x2 < n and 0 <= y2 < n:
            temp_puz = [row[:] for row in self.data]
            temp_puz[x1][y1], temp_puz[x2][y2] = temp_puz[x2][y2], temp_puz[x1][y1]
            return temp_puz

    def find(self, x):
        for i, row in enumerate(self.data):
            for j, val in enumerate(row):
                if val == x:
                    return i, j


class Puzzle:
    def __init__(self, size):
        self.n = size
        self.open = []
        self.closed = []

    def process(self):
        print("Start state matrix \n")
        start = [['1', '2', '3'], ['_', '4', '6'], ['7', '5', '8']]

        for row in start:
            for element in row:
                print(element, end=' ')
            print()  # Add a new line after each row

        
        print("Goal state matrix \n")

        goal = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '_']]
        for row in goal:
            for element in row:
                print(element, end=' ')
            print()  # Add a new line after each row

        start = Node(start, 0)
        self.open.append(start)
        print("\n\n")
        while self.open:
            cur = self.open.pop(0)
            print("")
            print("  | ")
            print("  | ")
            print(" \\'/ \n")
            for row in cur.data:
                print(*row)
            if cur.data == goal:
                break
            for child in cur.generate_child():
                self.open.append(child)


puz = Puzzle(3)
puz.process()
