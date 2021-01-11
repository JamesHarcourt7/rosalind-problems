file = open("rosalind_hamm.txt")
# Get each DNA string from the file.
dna1, dna2 = file.read().rstrip().split()
file.close()

# Compare each nucleotide at each index and increment hamming distance if they are different.
hamming = 0
for i in range(len(dna1)):
    if dna1[i] != dna2[i]:
        hamming += 1

print(hamming)
