task = input()

if task == "odd_char":
    result = []
    while True:
        line = input()
        if line.endswith("."):
            words = line.split()
            final_word = list(
                map(lambda word: word[::2] + ("." if word[-1] == "." else ""), words)
            )
            result.append(" ".join(final_word))
            break

        words = line.split()
        odd_line = list(map(lambda word: word[::2], words))
        result.append(" ".join(odd_line))

    print(" ".join(result))
