def relation(file1, file2):
    """
    Determine the relationship between two files

    Arguments:
        file1, file2: strings, paths to two files
    Return:
        string: 'Equal', 'Subset' or 'No Relation'
    """
    with open(file1, "r") as f1, open(file2, "r") as f2:
        lines1 = [line.strip() for line in f1.readlines()]
        lines2 = [line.strip() for line in f2.readlines()]

    f1_len = len(lines1)
    f2_len = len(lines2)

    if f1_len == f2_len and lines1 == lines2:
        return "Equal"

    if f1_len < f2_len and lines1 == lines2[:f1_len]:
        return "Subset"

    return "No Relation"
