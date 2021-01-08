RNA = ""

# Open the text file containing the DNA string.
with open("rosalind_rna.txt") as file:
    DNA = file.read()

    for nucleotide in DNA:
        # If the nucleotide is Thymine, replace it with Uracil.
        if nucleotide == "T":
            RNA += "U"
        else:
            RNA += nucleotide

    file.close()

print(RNA)
