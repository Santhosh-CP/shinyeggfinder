import re

# Obtaining the file containing the TSVs
print("Welcome to Shiny Egg Finder!")
while True:
    filename = input("Enter the path of the text file containing the TSV list (default name 'tsv.txt')\n")
    try:
        if filename == "":
            filename = "tsv.txt"
        f = open(filename, mode="r")
        break
    except FileNotFoundError:
        print("The entered file is not found")

# Reading the TSVs
tsv_list = []
expr = r""  # Used to generate the string used for pattern matching
for tsv in f:
    while len(tsv) <= 4:
        tsv = "0" + tsv
    expr = expr + r"\[" + tsv.strip() + r"\]|"
    tsv_list.append(tsv)
expr = expr[:-1]
f.close()

# Obtaining the file containing KeySAVe Data
while True:
    filename = input("Enter the path of the text file containing KeySAVe output (default name 'keysave.txt')\n")
    try:
        if filename == "":
            filename = "keysave.txt"
        f = open(filename, mode="r", encoding="utf-8")
        break
    except FileNotFoundError:
        print("The entered file is not found")

# Reading KeySAVe Data
key_save = f.readlines()
f.close()

# Regular Expression used for matching
ESVRegex = re.compile(expr)
matched_tsv = []
any_matches = False

# Printing Shiny Eggs!
for line in key_save:
    shiny = ESVRegex.search(line)
    if shiny:
        if not any_matches:
            print("\nThe Shiny Eggs are:-")
            any_matches = True
        print(line.strip())
        if shiny.group(0) not in matched_tsv:
            matched_tsv.append(shiny.group(0))

# Printing Matched TSV
if any_matches:
    print("\nThe matched TSVs are:-")
    for tsv in matched_tsv:
        print(tsv)
else:
    print("No eggs match the given TSVs")
