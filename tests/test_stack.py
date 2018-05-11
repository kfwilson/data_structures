import string

import pytest

from stack.stack import Stack, StackOverflowError

_lists = [list(range(15)), 
          [c for c in string.ascii_letters], 
          [5, 22.35, -15.26845, -1, .0025],
          ['words', 235, False],
          [None, 'a', 1, 5],
          [c for c in string.ascii_letters] + list(range(15))]
_lists_with_empty = _lists + [[]]


@pytest.fixture(params=_lists_with_empty, ids=repr)
def list_arg(request):
    return request.param


@pytest.fixture(params=_lists, ids=repr)
def list_arg_non_empty(request):
    return request.param


def test_stack_empty_constructor():
    st = Stack()
    assert st._ll.head is None


def test_push(list_arg):
    st = Stack(list_arg)
    st.push('test')
    assert st.pop() == 'test'


def test_constructor_list_order(list_arg_non_empty):
    st = Stack(list_arg_non_empty)
    assert st.pop() == list_arg_non_empty[-1]


def test_pop_empty_stack():
    with pytest.raises(IndexError):
        Stack().pop()


def test_peek_empty_stack():
    with pytest.raises(IndexError):
        Stack().peek()


def test_stack_constructor_oversize_error(list_arg_non_empty):
    with pytest.raises(StackOverflowError):
        Stack(list_arg_non_empty, len(list_arg_non_empty)-1)


def test_non_integer_max_size_error(list_arg):
    with pytest.raises(TypeError):
        Stack(list_arg, 1.0)


def test_negative_max_size_error(list_arg):
    with pytest.raises(ValueError):
        Stack(list_arg, -5)


def test_push_oversize(list_arg):
    st = Stack(list_arg, len(list_arg))
    with pytest.raises(StackOverflowError):
        st.push('one too many')


def test_peek_leaves_element_on_stack(list_arg_non_empty):
    st = Stack(list_arg_non_empty)
    st.peek()
    assert st.peek() == list_arg_non_empty[-1]


def test_len(list_arg):
    st = Stack(list_arg)
    assert len(st) == len(list_arg)