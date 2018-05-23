import pytest
import recursion_iteration as ri
import random

random.seed(98121)
_ints = [random.randint(1, 100) for _ in range(0,10)]
_small_ints = [random.randint(1, 10) for _ in range(0,5)]
_lists = [list(range(15)),_ints, [random.uniform(1, 100) for _ in range(0,10)], [], [5]]


@pytest.fixture(params=_lists, ids=repr)
def list_arg(request):
    return request.param


@pytest.fixture(params=_ints, ids=repr)
def int_arg(request):
    return request.param


@pytest.fixture(params=_small_ints, ids=repr)
def small_int_arg(request):
    return request.param


def test_array_sum_iterative(list_arg):
    assert ri.array_sum_recursive(list_arg) == ri.array_sum_iterative(list_arg)


def test_fibonacci_iterative_stack(int_arg):
    assert ri.fibonacci_recursive(int_arg) == ri.fibonacci_iterative_stack(int_arg)


def test_fibonacci_iterative_count(int_arg):
    assert ri.fibonacci_recursive(int_arg) == ri.fibonacci_iterative_count(int_arg)


def test_fibonacci_iterative_stack_0():
    assert ri.fibonacci_recursive(0) == ri.fibonacci_iterative_stack(0)


def test_fibonacci_iterative_count_0():
    assert ri.fibonacci_recursive(0) == ri.fibonacci_iterative_count(0)


def test_ackermann_iterative_m_0(small_int_arg):
    assert ri.ackermann_recursive(0, small_int_arg) == ri.ackermann_iterative(0, small_int_arg)


@pytest.mark.parametrize('m', [1,2])
def test_ackermann_iterative_n_0(m):
    assert ri.ackermann_recursive(m, 0) == ri.ackermann_iterative(m, 0)


@pytest.mark.parametrize('m', [1,2])
def test_ackermann_iterative_small_args(m, small_int_arg):
    assert ri.ackermann_recursive(m, small_int_arg) == ri.ackermann_iterative(m, small_int_arg)