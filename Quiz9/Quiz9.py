def subsetsUtil(A, subset, index):
    global count
    print(*subset)
    count += 1

    for i in range(index, len(A)):
        subset.append(A[i])
        subsetsUtil(A, subset, i + 1)
        subset.pop(-1)
    return

def subsets(A):
    subset = []
    index = 0
    subsetsUtil(A, subset, index)

global count
count = 0
arr_3 = [1, 2, 3]
print("Subsets of n = 3 are: ")
subsets(arr_3)
print("Total number of subsets for n = 3 is " + str(count))
print()

count = 0
arr_5 = [1, 2, 3, 4, 5]
print("Subsets of n = 5 are: ")
subsets(arr_5)
print("Total number of subsets for n = 5 is " + str(count))
print()


count = 0
arr_7 = [1, 2, 3, 4, 5, 6, 7]
print("Subsets of n = 7 are: ")
subsets(arr_7)
print("Total number of subsets for n = 7 is " + str(count))