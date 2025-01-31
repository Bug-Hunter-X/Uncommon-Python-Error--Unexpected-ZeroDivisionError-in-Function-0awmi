def function_with_uncommon_error(x):
    try:
        if x == 0:
            return 1 / x
        else:
            return x + 1
    except ZeroDivisionError:
        return float('inf')  # Or handle it differently, like raising a custom exception
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None