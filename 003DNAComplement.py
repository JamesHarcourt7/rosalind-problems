reverse_complement = ""
# Use a dictionary to store complements of each nucleotide.
complements = {"A": "T", "T": "A", "C": "G", "G": "C"}

with open("rosalind_revc.txt") as file:
    DNA = file.read().rstrip()
    # Convert each nucleotide in the string to its complement.
    for nucleotide in DNA:
        # Add the complement to the start of the string so the final result is reversed.
        reverse_complement = complements[nucleotide] + reverse_complement
    file.close()
print(reverse_complement)
