import re


def translate(rna, codon_table):
    protein_string = ""
    # Loop through the RNA by index, stepping by 3.
    for i in range(0, len(rna), 3):
        codon = rna[i] + rna[i + 1] + rna[i + 2]
        amino_acid = codon_table[codon]

        # If a stop codon is encountered, translation is finished.
        if amino_acid == "Stop":
            return protein_string

        protein_string += amino_acid

    return protein_string


if __name__ == "__main__":
    # Read the RNA string from the input file.
    file = open("rosalind_prot.txt")
    rna_string = file.read().rstrip()
    file.close()

    # Get the RNA codon table and sort into a dictionary.
    table = open("RNACodonTable.txt")
    codon_dict = {}
    # Use regex to find all groups with codon and corresponding amino acid.
    for group in re.findall("[A-Z]{3}\\s[A-Za-z]{1,4}", table.read()):
        # String slice and add to dictionary -> codon : amino acid
        codon_dict[group[:3]] = group[4:]
    table.close()

    print(translate(rna_string, codon_dict))
