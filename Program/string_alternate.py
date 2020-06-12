def string_alternative(sentence):
    clist = []

    for i in range(0, len(sentence), 2):
        clist.append(sentence[i])

    print(clist)


def main():
    sentence = input("Input string:")
    string_alternative(sentence)


if __name__ == "__main__":
    main()