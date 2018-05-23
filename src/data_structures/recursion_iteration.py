from stack.stack import Stack

def array_sum_recursive(array, total=0):
    if array:
        return array_sum_recursive(array[1:], total + array[0])
    return total


def array_sum_iterative(array):
    total = 0
    while array:
        total += array[0]
        array = array[1:]
    return total


def fibonacci_recursive(n, a=1, b=1):
    if n == 0:
        return a
    return fibonacci_recursive(n-1, b, a+b)


def fibonacci_iterative_stack(n):
    if n == 0:
        return 1
    st = Stack(max_size=300)
    a, b = 1, 1
    for _ in range(n):
        st.push(a)
        st.push(b)
        a, b = b, a+b
    return st.pop()


def fibonacci_iterative_count(n):
    a, b = 1,1
    for _ in range(n):
        a, b = b, a+b
    return a


def ackermann_recursive(m, n):
    if m == 0:
        return n + 1
    if n == 0:
        return ackermann_recursive(m - 1, 1)
    return ackermann_recursive(m - 1, ackermann_recursive(m, n-1))


def ackermann_iterative(m, n):
    st = Stack()
    st.push(m)
    while len(st):
        m = st.pop()
        if m == 0:
            n += 1
        elif n == 0:
            n = 1
            st.push(m-1)
        else:
            st.push(m-1)
            st.push(m)
            n -= 1
    return n



