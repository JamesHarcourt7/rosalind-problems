import re

highestGC = 0.0
highestGCID = ""

with open("rosalind_gc.txt") as file:
    # Use regex to split up the input file into FASTA ID of the string and the GC-content.
    for group in re.findall(">[A-Za-z]+_[0-9]+[ATCG]+", file.read().replace('\n', '')):

        # Use regex to split up further into ID and DNA string.

        # Ignore the first character '>' in GCID.
        GCID = re.findall(">[A-Za-z]+_[0-9]+", group)[0][1:]
        DNA = re.findall("[ATCG]+", group)[0]

        # Calculate GC content of the DNA string.
        count = 0
        for nucleotide in DNA:
            if nucleotide == "C" or nucleotide == "G":
                count += 1
        GC = count / len(DNA) * 100

        # Compare with the highest GC and update if necessary.
        if GC > highestGC:
            highestGC = GC
            highestGCID = GCID

    # Close file after operation.
    file.close()

print(highestGCID)
print(highestGC)
