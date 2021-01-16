import re

profile = []
bases = {"A": 0, "C": 1, "G": 2, "T": 3}

file = open("rosalind_cons.txt")
# Find DNA strings in input file with regex.
groups = re.findall("[ATCG]+", file.read().replace('\n', ''))
for group in groups:
    # Create profile matrix according to length of group.
    if not profile:
        profile = [[0 for n in range(len(group))] for m in range(4)]

    # Loop through each DNA string.
    for i in range(len(group)):
        # Increment the correct i for each j of the profile matrix, depending on nucleotide.
        profile[bases[group[i]]][i] += 1

file.close()

consensus = ""
for i in range(len(profile[0])):
    highest = 0
    # Skip profile[0][i] as that is the original highest.
    for j in range(1, 4):
        if profile[j][i] > profile[highest][i]:
            highest = j

    # Append the most common nucleotide to the consensus.
    consensus += list(bases.keys())[highest]

print(consensus)
for i in range(len(profile)):
    row = ""
    row += list(bases.keys())[i] + ": "
    for n in profile[i]:
        row += str(n) + " "
    print(row)
