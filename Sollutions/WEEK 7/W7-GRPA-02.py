def merge(D1, D2, priority):
    """
    Merge two dicts

    Arguments:
        - D1: first dictionary
        - D2: second dictionary
        - priority: string
    Returns: D; merged dictionary
    """
    if priority == "first":
        merged_dict = {**D2, **D1}
    elif priority == "second":
        merged_dict = {**D1, **D2}
    else:
        raise ValueError("Priority Must Wither Be 'first' Or 'second")

    return merged_dict
