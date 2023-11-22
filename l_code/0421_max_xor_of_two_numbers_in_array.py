class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.val = None


class Tree:
    def __init__(self):
        self.root = Node()

    def insert(self, num):
        node = self.root
        bits = self.get_bits(num)

        for bit in bits:
            if bit == 0:
                if node.left is None:
                    node.left = Node()
                node = node.left
            else:
                if node.right is None:
                    node.right = Node()
                node = node.right
        node.val = num

    def get_max_xor(self):
        def calc_xor(node1, node2):
            if node1 is None or node2 is None:
                return 0
            if node1.val is not None:
                return node1.val ^ node2.val

            curr_max = max(calc_xor(node1.left, node2.right), calc_xor(node1.right, node2.left))

            if curr_max == 0:
                curr_max = max(calc_xor(node1.left, node2.left), calc_xor(node1.right, node2.right))

            return curr_max

        return calc_xor(self.root, self.root)

    def get_bits(self, num):
        bits = []

        while num:
            last_bit = (num & 1)
            bits.append(last_bit)
            num = num >> 1

        while len(bits) < 31:
            bits.append(0)

        return bits[::-1]


def find_max_xor(nums):
    tree = Tree()

    for num in nums:
        tree.insert(num)

    return tree.get_max_xor()


def test():
    nums = [3, 10, 5, 25, 2, 8]
    assert find_max_xor(nums) == 28