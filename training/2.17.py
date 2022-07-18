# Write a Python program to remove an empty tuple(s) from a list of tuples.
L = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
L = [t for t in L if t]
print(L)




# result_list = []

# for t in L:
#   if t is True:
#      result_list.append(t)