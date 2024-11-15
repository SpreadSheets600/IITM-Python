def minor_matrix(M, i, j):
    """
    Compute the "minor matrix"

    Arguments:
        M: list of lists
        i: integer
        j: integer
    Return:
        M_ij: list of lists
    """

    M_ij = [row[:j] + row[j + 1 :] for row in (M[:i] + M[i + 1 :])]

    return M_ij
