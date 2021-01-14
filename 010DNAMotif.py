# Read string and
file = open("rosalind_subs.txt")
s, t = file.read().rstrip().split()


output = ""
for i in range(len(s) - len(t)):
    if s[i: i + len(t)] == t:
        output += str(i + 1) + " "
print(output)
