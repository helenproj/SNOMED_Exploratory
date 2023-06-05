def count_rows(filename):
    with open(filename) as file:
        for i, line in enumerate(file):
            pass
        file.close()
        return i


def get_concept(filename, a):
    with open(filename) as file:
        for i, line in enumerate(file):
            if i == a:
                file.close()
                return line


def get_column(filename, a):
    specificlist = []
    with open(filename) as file:
        for line in file:
            word = line.split()
            if word:
                specificlist.append(word[a-1])
    file.close()
    return specificlist


def match_description(filename, conceptID):

    with open(filename) as file:
        for line in file:
            if conceptID in line:
                compare = line
                file.close()
                return compare


number = '100005'
testing = match_description("sct2_Description_Full-en_INT_20230430.txt", number)
print(testing)
test2 = match_description("test_description.txt", number)
print(test2)

print(get_column("test_concept.txt", 1))
count = count_rows("sct2_Concept_Full_INT_20230430.txt")
print("the total concept:", count)
b = 2
concept = get_concept("sct2_Concept_Full_INT_20230430.txt", b)
print("the concept on line", b, "is ", concept)
