# Time: O(n)  Space: O(n)
def fizz_buzz(n):
    answer = []
    for j in range(n):
        i = j + 1
        if i % 15 == 0:
            answer.append('FizzBuzz')
        elif i % 3 == 0:
            answer.append('Fizz')
        elif i % 5 == 0:
            answer.append('Buzz')
        else:
            answer.append(str(i))
    return answer


def test():
    assert fizz_buzz(1) == ['1']
    assert fizz_buzz(2) == ['1', '2']
    assert fizz_buzz(3) == ['1', '2', 'Fizz']
    assert fizz_buzz(4) == ['1', '2', 'Fizz', '4']

