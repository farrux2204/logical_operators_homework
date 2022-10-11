def main(a,b):
    """
    Given two integers a, b,  check the following statement "At least one of the numbers 'a' and 'b' is positive".
    Args:
        a(int): parameter a
        b(int): parameter b
    Returns:
        bool: answer
    """
    return bool(a<0 and b>0) or (a>0 and b<0)
print(main(1,-3))