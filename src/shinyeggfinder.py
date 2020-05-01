import re


def make_expression(tsvs):
    expr = r""
    for tsv_ in tsvs:
        expr = expr + r"\[" + tsv_.strip() + r"\]|"
    expr = expr[:-1]
    return expr


print("Welcome to Shiny Egg Finder!")

# Obtaining the file containing the TSVs
while True:
    filename = input("Enter the path of the textfile containing the TSV list\n")
    try:
        if filename == "":
            filename = "tsv.txt"
        f = open(filename, mode="r")
        break
    except FileNotFoundError:
        print("The entered file is not found")


# Reading the TSVs
tsv_list = []
for tsv in f:
    while len(tsv) <= 4:
        tsv = "0" + tsv
    tsv_list.append(tsv)
f.close()


# Obtaining the file containing KeySAVe Data
while True:
    filename = input("Enter the path of the textfile containing KeySAVe output\n")
    try:
        if filename == "":
            filename = "keysave.txt"
        f = open(filename, mode="r")
        break
    except FileNotFoundError:
        print("The entered file is not found")


# Reading KeySAVe Data
keysave = f.readlines()
f.close()


# Regular Expression used for matching
expression = make_expression(tsv_list)
ESVRegex = re.compile(expression)
shiny_eggs = ESVRegex.findall("".join(keysave))


# Printing Shiny Eggs!
print(shiny_eggs)
print("The Shiny Eggs are:-")
for egg in shiny_eggs:
    print(egg[1:-1])
