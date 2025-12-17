# Math Utility Functions

This project provides a simple set of fundamental mathematical operations: `add`, `subtract`, `multiply`, and `divide`.

## Files

-   `math_utils.py`: Contains the definitions for the `add`, `subtract`, `multiply`, and `divide` functions.
-   `test_math_utils.py`: Contains comprehensive pytest test cases for all functions in `math_utils.py`, covering various scenarios and edge cases.

## Setup

1.  **Prerequisites**: Ensure you have Python 3 installed on your system.
2.  **Install pytest**: If you don't already have `pytest` installed, you can install it using pip:
    ```bash
    pip install pytest
    ```

## How to Run Tests

To execute the test suite:

1.  **Save the Python code**: Save the provided Python code (containing the `add`, `subtract`, `multiply`, `divide` functions) into a file named `math_utils.py`.
2.  **Save the test file**: Save the generated `test_math_utils.py` content into a file with the same name, in the **same directory** as `math_utils.py`.
3.  **Open your terminal**: Navigate to the directory where you saved these two files.
4.  **Run pytest**: Execute the tests using the `pytest` command:
    ```bash
    pytest
    ```

    You will see a summary of the test execution, indicating how many tests passed, failed, or were skipped.

    For a more detailed output, including each test's individual result, you can use the verbose flag:
    ```bash
    pytest -v
    ```
