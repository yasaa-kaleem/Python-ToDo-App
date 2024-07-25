from errors import check_input
import pytest

@pytest.mark.parametrize("user_input, expected_input", [
    (4, [1,2,3]),
    ('A', [1,2,3]),
    ('D', ['A','B','C']),
])

def test_negative(user_input, expected_input):
    with pytest.raises(OSError):
        check_input(user_input, expected_input)

@pytest.mark.parametrize("user_input, expected_input, result", [
    (1, [1], 1),
    (1, [1,2,3], 1),
    (2, [1,2,3], 2),
    ('A', ['A'], 'A'),
    ('A', ['A', 'B', 'C'], 'A'),
    ('B', ['A', 'B', 'C'], 'B'),
])

def test_positive(user_input, expected_input, result):
    assert check_input(user_input, expected_input) == result

# def test_check_input_one_item_num():
#     assert check_input(1, [1]) == 1
    
# def test_check_input_multiple_items_num():
#     assert check_input(1, [1,2,3]) == 1
#     assert check_input(2, [1,2,3]) == 2

# def test_check_input_item_nonexist_num():
#     with pytest.raises(OSError):
#         check_input(4, [1,2,3]) == 4

# def test_check_input_one_item_aplha():
#     assert check_input('A', ['A']) == 'A'
    
# def test_check_input_multiple_items_aplha():
#     assert check_input('A', ['A', 'B', 'C']) == 'A'
#     assert check_input('B', ['A', 'B', 'C']) == 'B'

# def test_check_input_item_nonexist_aplha():
#     with pytest.raises(OSError):
#         check_input('a', [1,2,3]) == 'a'
#         check_input('a', ['A','B','C']) == 'a'