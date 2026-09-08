fruits = {"apple", "banana", "cherry"}

fruits.add("orange")
print(fruits)  # Output: {'banana', 'orange', 'cherry', 'apple'}

fruits.remove("banana")
print(fruits)  # Output: {'orange', 'cherry', 'apple'}

fruits.discard("grape")  # No error if "grape" is not in the set
print(fruits)  # Output: {'orange', 'cherry', 'apple'}

removed_item = fruits.pop()  # Removes and returns an arbitrary item
print(removed_item)  # Output: (arbitrary item removed)
print(fruits)  # Output: (remaining items in the set)

fruits.clear()  # Removes all items from the set
print(fruits)  # Output: set()