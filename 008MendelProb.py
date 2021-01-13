# Get integer inputs k, n and m from input file.
k, m, n = [int(n) for n in open("rosalind_iprb.txt").read().rstrip().split()]

pop_size = k + m + n

# There are only 3 events where offspring is homozygous recessive.
# Calculating the probability for these 3 events will give us the overall probability
# that offspring is homozygous recessive and this can be used to find the
# probability of a dominant trait in the offspring phenotype.

# Event of nxn has a 100% chance of being homozygous recessive.
nxn = (n / pop_size) * ((n - 1) / (pop_size - 1))
# Event of nxm has a 50% chance of being homozygous recessive.
nxm = (n / pop_size) * (m / (pop_size - 1)) * 0.5
# Event of mxn has a 50% chance of being homozygous recessive.
mxn = (m / pop_size) * (n / (pop_size - 1)) * 0.5
# Event of mxm has a 25% chance of being homozygous recessive.
mxm = (m / pop_size) * ((m - 1) / (pop_size - 1)) * 0.25

# Probability of offspring showing dominant trait is 1 - P(homozygous recessive)
prob = 1 - (nxn + nxm + mxn + mxm)
print(prob)
