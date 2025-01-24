"""Question One: Algorithm Engineering Skill-Check."""

# TODO: The imports in the following source code block may no longer
# adhere to the industry best practices for Python source code.
# You must reorganize and/or add the imports so that they adhere
# to the industry best practices for Python source code.

from typing import Any, Dict, List

# Introduction: Read This First! {{{

# Keep in mind these considerations as you implement the required functions:

# --> You must implement Python functions to complete each of these steps,
# bearing in mind that one defective function may break another function.

# --> This may has functions that may be seeded with defects; this means
# that you will have to improve various aspects of this code to ensure
# that it passes the various tests and checks.

# --> Your source code must adhere to industry best practices in, for instance,
# source code formatting, variable naming, and documentation.

# --> You may refer to the checks that are specified in the exam/gatorgrade.yml
# file in this GitHub repository for the configuration and name of each tool
# used to analyze the code inside of this file.

# }}}

# Part (a) {{{

# Implement the following function(s) that process a list and adhere to the
# following function specification.

# Function description:
# The function detect_duplicates should:
# --> Take as input a list of any values (e.g., integers or strings)
# --> Return a boolean that indicates whether or not there are any duplicate values
# --> The function should not modify the input list when it searches for duplicates

# TODO: These function(s) may not not have all of the correct type annotations
# for certain variables. You must add all of any needed type annotations so
# that the function and any code that uses it passes the type checker.

# TODO: These function(s) may not have a docstring and thus it may not adhere to
# best practices for Python source code. You may need to add a docstring so that
# this function is correctly documented by an software engineer using it.


def detect_duplicates(input_list):
    """Determine whether or not the input list contains a duplicate value."""
    return False


# }}}

# Part (b) {{{

# Implement the following function(s) that process a list and adhere to the
# following function specification.

# Function description:
# The function detect_duplicates_in_lists should:
# --> Take as input a list of lists of any values
# --> Return a list of booleans that indicate whether or not there are any duplicate values
# --> The function should not modify the input list when it searches for duplicates

# TODO: These function(s) may not not have all of the correct type annotations
# for certain variables. You must add all of any needed type annotations so
# that the function and any code that uses it passes the type checker.

# TODO: These function(s) may not have a docstring and thus it may not adhere to
# best practices for Python source code. You may need to add a docstring so that
# this function is correctly documented by an software engineer using it.


def detect_duplicates_in_lists(list_of_lists):
    return [True]


# }}}

# Part (c) {{{

# Repair the following function(s) that process a dictionary and should adhere
# to the following function specification.

# Function description:
# The function detect_duplicates_in_dict should:
# --> Take as input a dictionary with string keys and string values
# --> Return a boolean indicating whether or not there are any duplicates in the values

# TODO: These function(s) may not not have all of the correct type annotations
# for certain variables. You must add all of any needed type annotations so
# that the function and any code that uses it passes the type checker.

# TODO: These function(s) may not have a docstring and thus it may not adhere to
# best practices for Python source code. You may need to add a docstring so that
# this function is correctly documented by an software engineer using it.


def detect_duplicates_in_dict(input_dict: Dict[str, str]) -> bool:
    values = list(input_dict.keys())
    return detect_duplicates(values)


# }}}


# Part (d) {{{

# Implement the following function(s) that process a dictionary and adhere to
# the following function specification.

# Function description:
# The function detect_duplicates_below_threshold should:
# --> Take as input a dictionary with string keys and string values
# --> Take as input an integer threshold that represents the maximum number of
#     duplicates allowed in the string values
# --> Return a boolean indicating whether or not the number of duplicates in the
#     values is below the threshold
# --> Enforce the duplicate threshold with a "greater than or equals to" comparison

# Here are some examples to illustrate how this function works:
# --> detect_duplicates_below_threshold_in_dict({"a": "1", "b": "2", "c": "1"}, 2) returns True
#     because there is one duplicate and that is below (or equal to) the threshold of 2
# --> detect_duplicates_below_threshold_in_dict({"a": "1", "b": "2", "c": "1"}, 1) returns True
#     because there is one duplicate and that is below (or equal to) the threshold of 1

# Please refer to the test cases in the exam/tests/test_question_one.py file
# to understand the expected behavior of this function.

# TODO: These function(s) may not not have all of the correct type annotations
# for certain variables. You must add all of any needed type annotations so
# that the function and any code that uses it passes the type checker.

# TODO: These function(s) may not have a docstring and thus it may not adhere to
# best practices for Python source code. You may need to add a docstring so that
# this function is correctly documented by an software engineer using it.


def detect_duplicates_below_threshold_in_dict(
    input_dict: Dict[str, str], threshold: int
) -> bool:
    """Determine whether or not the number of duplicates in the input dictionary's values is below the threshold."""
    duplicates_count = 0
    if duplicates_count <= threshold:
        return True
    return False

# }}}
