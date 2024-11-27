def ancestry(P, present, past):
    """
    A recursive function to compute the sequence of ancestors of a person

    Arguments:
        P: dict, key and value are strings where key is a person and value is their parent
        present: string, the current person whose ancestors are to be found
        past: string, the ancestor we are looking for in the ancestry chain

    Return:
        result: list of strings, the sequence of ancestors from 'present' to 'past'
    """
    # Base case: if the current person is the past person, return a list with only 'past'
    if present == past:
        return [present]

    # If the present person has no ancestor, return an empty list
    if present not in P:
        return []

    # Recursive case: find the ancestors
    ancestors = []
    parent = P[present]

    # Recursive call to find ancestors of the parent
    ancestor_path = ancestry(P, parent, past)

    # If the path is not empty, prepend the current person to the path
    if ancestor_path:
        ancestors = [present] + ancestor_path

    return ancestors
