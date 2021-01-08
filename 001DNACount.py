# Counters for each type of nucleotide in DNA string.
adenosine = 0
cytosine = 0
guanine = 0
thymine = 0

# Open the text file containing the data set.
with open("rosalind_dna.txt") as file:
    dna = file.read()
    for char in dna:
        if char == "A":
            adenosine += 1
        elif char == "C":
            cytosine += 1
        elif char == "G":
            guanine += 1
        elif char == "T":
            thymine += 1

    file.close()

print(adenosine, cytosine, guanine, thymine)
