# Implementation of Heap's algorithm for generating permutations.
class HeapPerm:

    def __init__(self, n):
        self.permutations = 0
        self.end_print = ""
        self.heap_permutations([n for n in range(1, num + 1)], n)
        print(self.permutations)
        print(self.end_print)

    def heap_permutations(self, array, size):
        # Recursive method will generate all permutations of array "array" of size "size".

        # If size is 1 add it to the list of final permutations.
        if size == 1:
            self.permutations += 1
            to_print = ""
            for element in array:
                to_print += str(element) + " "
            self.end_print += to_print + '\n'

        for i in range(size):
            # Call permutations recursively with decremented size.
            self.heap_permutations(array, size - 1)

            if size % 2 == 1:
                # If size is odd, swap first and last elements.
                temp = array[0]
                array[0] = array[size - 1]
                array[size - 1] = temp
            else:
                # If size is even, swap ith and size - 1 elements.
                temp = array[i]
                array[i] = array[size - 1]
                array[size - 1] = temp


if __name__ == "__main__":
    file = open("rosalind_perm.txt")
    num = int(file.read().rstrip())
    file.close()

    h = HeapPerm(num)
