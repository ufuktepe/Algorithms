from node import SLLNode


def add_two_nums(l1, l2):
    def get_value(head):
        res = 0

        cur = head
        mult = 1

        while cur:
            res += cur.val * mult
            cur = cur.next
            mult *= 10

        return res

    def get_linked_list(val):
        cur = None
        head = None

        while val > 0:
            digit = val % 10
            val = val // 10
            node = SLLNode(digit)

            if cur is None:
                cur = head = node
            else:
                cur.next = node
                cur = cur.next

        return head

    num1 = get_value(l1)
    num2 = get_value(l2)

    num3 = num1 + num2

    return get_linked_list(num3)



n1 = SLLNode(1)
n2 = SLLNode(2)
n1.next = n2

add_two_nums(n1, n1)