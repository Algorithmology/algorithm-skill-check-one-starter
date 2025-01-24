"""Confirm the correctness of functions in question_one."""

import pytest

# ruff: noqa: PLR2004
from questions.question_one import (
    detect_duplicates,
    detect_duplicates_below_threshold_in_dict,
    detect_duplicates_in_dict,
    detect_duplicates_in_lists,
)


@pytest.mark.question_one_part_a
def test_detect_duplicates():
    """Confirm correctness of question part."""
    assert detect_duplicates([1, 2, 3, 4, 1])
    assert not detect_duplicates([1, 2, 3, 4, 5])
    assert detect_duplicates([1, 1, 1, 1, 1])
    assert not detect_duplicates([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    assert not detect_duplicates([])
    assert not detect_duplicates([1])
    assert detect_duplicates([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1])
    assert not detect_duplicates([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])


@pytest.mark.question_one_part_b
def test_detect_duplicates_in_lists():
    """Confirm correctness of question part."""
    assert detect_duplicates_in_lists([[1, 2, 3, 4, 1], [1, 2, 3, 4, 5]]) == [
        True,
        False,
    ]
    assert detect_duplicates_in_lists(
        [[1, 1, 1, 1, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2]]
    ) == [True, True]
    assert detect_duplicates_in_lists([[], [1]]) == [False, False]
    assert detect_duplicates_in_lists(
        [
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 5, 11],
        ]
    ) == [False, True]


@pytest.mark.question_one_part_c
def test_detect_duplicates_in_dict():
    """Confirm correctness of question part."""
    assert detect_duplicates_in_dict({"a": "1", "b": "2", "c": "1"})
    assert not detect_duplicates_in_dict({"a": "1", "b": "2", "c": "3"})
    assert detect_duplicates_in_dict({"a": "1", "b": "1", "c": "1"})
    assert not detect_duplicates_in_dict(
        {"a": "1", "b": "2", "c": "3", "d": "4"}
    )
    assert not detect_duplicates_in_dict({})
    assert not detect_duplicates_in_dict({"a": "1"})


@pytest.mark.question_one_part_d
def test_detect_duplicates_below_threshold_dict():
    """Confirm correctness of question part."""
    assert detect_duplicates_below_threshold_in_dict(
        {"a": "1", "b": "2", "c": "1"}, 2
    )
    assert detect_duplicates_below_threshold_in_dict(
        {"a": "1", "b": "2", "c": "1"}, 1
    )
    assert detect_duplicates_below_threshold_in_dict(
        {"a": "1", "b": "2", "c": "3"}, 1
    )
    assert detect_duplicates_below_threshold_in_dict(
        {"a": "1", "b": "2", "c": "3"}, 0
    )
    assert detect_duplicates_below_threshold_in_dict(
        {"a": "1", "b": "1", "c": "1"}, 2
    )
    assert not detect_duplicates_below_threshold_in_dict(
        {"a": "1", "b": "1", "c": "1"}, 1
    )
    assert detect_duplicates_below_threshold_in_dict(
        {"a": "1", "b": "1", "c": "2", "d": "3", "e": "3"}, 3
    )
    assert detect_duplicates_below_threshold_in_dict(
        {"a": "1", "b": "1", "c": "2", "d": "3", "e": "3"}, 2
    )
    assert not detect_duplicates_below_threshold_in_dict(
        {"a": "1", "b": "1", "c": "2", "d": "3", "e": "3"}, 1
    )
    assert detect_duplicates_below_threshold_in_dict({}, 1)
    assert detect_duplicates_below_threshold_in_dict({}, 0)
    assert detect_duplicates_below_threshold_in_dict({"a": "1"}, 1)
    assert detect_duplicates_below_threshold_in_dict({"a": "1"}, 0)
