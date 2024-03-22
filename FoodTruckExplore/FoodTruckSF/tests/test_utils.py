import pytest
from FoodTruckSF.utils import paginate_query, get_prev_and_next_page

@pytest.mark.parametrize("page, page_size, expected_skip, expected_limit", [
    (4, 10, 30, 10),  # Example case 1
    (1, 10, 0, 10),   # Example case 2
])
def test_paginate_query(page, page_size, expected_skip, expected_limit):
    result_skip, result_limit = paginate_query(page, page_size)
    assert result_skip == expected_skip, f"Expected skip to be {expected_skip}, but got {result_skip}"
    assert result_limit == expected_limit, f"Expected limit to be {expected_limit}, but got {result_limit}"

@pytest.mark.parametrize("page, page_size, count, expected_prev_page, expected_next_page", [
    (4, 10, 100, 3, 5),  # Middle of series
    (1, 10, 100, None, 2),  # First page
    (10, 10, 100, 9, None),  # Last page
    (5, 20, 100, 4, None),  # Larger page size, not at start or end
    (2, 40, 100, 1, 3),  # Case where total items are exactly divisible by page size
])
def test_get_prev_and_next_page(page, page_size, count, expected_prev_page, expected_next_page):
    prev_page, next_page = get_prev_and_next_page(page, page_size, count)
    assert prev_page == expected_prev_page, f"Expected prev_page to be {expected_prev_page}, but got {prev_page}"
    assert next_page == expected_next_page, f"Expected next_page to be {expected_next_page}, but got {next_page}"
