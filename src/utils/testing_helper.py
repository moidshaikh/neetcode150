from typing import Callable, Any


# Helper function for tests
def assert_solution(func: Callable, input_data: Any, expected_output: Any):
    """
    Generalized assertion function

    :param func: The function to be tested
    :type func: Callable
    :param input_data: The input (can be a single value or a tuple for multiple args)
    :type input_data: Any
    :param expected_output: Expected result
    :type expected_output: Any
    """
    # handle case where function might take multiple arguments.
    if isinstance(input_data, tuple):
        actual = func(*input_data)
    else:
        actual = func(input_data)

    assert actual == expected_output, (
        f"FAILED: Input: {input_data} | Expected: {expected_output} | Actual: {actual}"
    )
