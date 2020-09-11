import time
from bst import BST

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

"""
Replace the nested for loops below with your improvements
efficiency of O(n^2) because: 
    nested for loops exponential increase work 

for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)

runtime = 6 seconds
----------------------------------------------------------
Binary Search Tree improvement
efficienct of O(n log n) because:
    O(log n) # Binary Search Tree
  + O(n)     # Size of second file
"""
#initialize the Binary Search Tree
bst = BST('')
#traverse file line by line
for name_1 in names_1:
    #insert each line into BST
    bst.insert(name_1)

#traverse other file line by line
for name_2 in names_2:
    #if current line value is in BST
    if bst.contains(name_2):
        #add value to array of duplicates
        duplicates.append(name_2)
"""
runtime = .06 seconds
"""
end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
