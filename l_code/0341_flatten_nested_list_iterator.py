# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator_v1:
    def __init__(self, nestedList):
        self.flattened_list = []
        self.traverse(nestedList)
        self.current_index = -1

    def traverse(self, lst):
        for item in lst:
            if isinstance(item, int):
                self.flattened_list.append(item)
            elif isinstance(item, list):
                self.traverse(item)


    def next(self) -> int:
        if self.hasNext():
            self.current_index += 1
            return self.flattened_list[self.current_index]
        return -1

    def hasNext(self) -> bool:
        return self.current_index + 1 < len(self.flattened_list)


class NestedIterator:
    def __init__(self, nestedList):
        self.indices = [-1]
        self.lists = [nestedList]
        self.update()

    def update(self):
        idx = self.indices.pop() + 1
        cur_list = self.lists.pop()

        while cur_list:
            if idx == len(cur_list):
                if not self.lists:
                    break
                cur_list = self.lists.pop()
                idx = self.indices.pop() + 1
            elif not isinstance(cur_list[idx], int):
                self.lists.append(cur_list)
                self.indices.append(idx)
                cur_list = cur_list[idx]
                idx = 0
            else:
                self.lists.append(cur_list)
                self.indices.append(idx)
                break


    def next(self) -> int:
        x = self.lists[-1][self.indices[-1]]
        self.update()
        return x

    def hasNext(self) -> bool:
        return len(self.lists) > 0


# def test():
#     lst = [[1, 1], 2, [1, 1]]
#     nested_iter = NestedIterator(lst)
#     ans = [1, 1, 2, 1, 1]
#
#     for num in ans:
#         assert nested_iter.hasNext()
#         assert nested_iter.next() == num


def test_2():
    nestedList = [[1, 1], 2, [1, 1]]
    i, v = NestedIterator(nestedList), []
    while i.hasNext():
        v.append(i.next())
    assert v == [1, 1, 2, 1, 1]