set1 = {1,2,3,4}
set2 = {3,4,5,6}

#union
union_set = set1 | set2
print("Union:", union_set)  # Output: {1, 2, 3, 4, 5, 6}

#intersection
intersection_set = set1 & set2
print("Intersection:", intersection_set)  # Output: {3, 4}

#difference
difference_set = set1 - set2
print("Difference:", difference_set)  # Output: {1, 2}

#symmetric difference
symmetric_difference_set = set1 ^ set2
print("Symmetric Difference:", symmetric_difference_set)  # Output: {1, 2, 5, 6}