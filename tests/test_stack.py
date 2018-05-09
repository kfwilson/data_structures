import string

import pytest

from stack.stack import Stack, StackOverflowError

_orderable_lists = [list(range(15)), [c for c in string.ascii_letters], [1, 3, 1.1, -50, 0, 3.1415639]]
_unorderable_lists = [['banana', 50, False], [1, 2, 3, None],
                      [c for c in string.ascii_letters] + list(range(10))]
_constructor_args_non_empty = _unorderable_lists + _orderable_lists
_constructor_args_with_empty = _unorderable_lists + _orderable_lists + [[]]


@pytest.fixture(params=_constructor_args_with_empty, ids=repr)
def constructor_arg(request):
    return request.param


@pytest.fixture(params=_constructor_args_non_empty, ids=repr)
def constructor_arg_non_empty(request):
    return request.param


def test_stack_empty_constructor():
    st = Stack()
    assert st.head is None


def test_push(constructor_arg):
    st = Stack(constructor_arg)
    st.push('test')
    assert st.pop() == 'test'


def test_constructor_list_order(constructor_arg_non_empty):
    st = Stack(constructor_arg_non_empty)
    assert st.pop() == constructor_arg_non_empty[-1]


def test_pop_empty_stack():
    with pytest.raises(IndexError):
        Stack().pop()


def test_peek_empty_stack():
    with pytest.raises(IndexError):
        Stack().peek()


def test_stack_constructor_oversize_error(constructor_arg):
    with pytest.raises(StackOverflowError):
        Stack(constructor_arg, len(constructor_arg)-1)


def test_push_oversize(constructor_arg):
    st = Stack(constructor_arg, len(constructor_arg))
    with pytest.raises(StackOverflowError):
        st.push('one too many')


def test_peek_leaves_element_on_stack(constructor_arg_non_empty):
    st = Stack(constructor_arg_non_empty)
    st.peek()
    assert st.peek() == constructor_arg_non_empty[-1]