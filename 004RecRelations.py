file = open("rosalind_fib.txt")
data = file.read().rstrip().split(" ")

# Take n and k values from the text file.
n = int(data[0])
k = int(data[1])

rabbit_pairs = [1, 1]
# Remove 2 from n as we already have the populations for first and second month.
for month in range(n - 2):
    # Add the new offspring to the
    offspring = rabbit_pairs[len(rabbit_pairs) - 2] * k
    rabbit_pairs.append(offspring + rabbit_pairs[len(rabbit_pairs) - 1])

# Output the last amount of rabbit pairs in the sequence.
print(rabbit_pairs[-1])
