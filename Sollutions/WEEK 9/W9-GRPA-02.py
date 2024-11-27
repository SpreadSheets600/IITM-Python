def linear(P, Q, k):
    """
    A recursive function to determine if a list is a scalar multiple of the other

    Arguments:
        P: list of integers
        Q: list of integers
        k: integer
    Return:
        result: bool
    """
    if len(P) != len(Q):
        return False  # Lists must be of the same length

    if len(P) == 0:
        return True  # If both lists are empty, they are scalar multiples

    if P[0] != k * Q[0]:
        return False  # If any element doesn't match, return False

    return linear(P[1:], Q[1:], k)  # Check the rest of the lists
