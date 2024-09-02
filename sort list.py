def sort_list(numbers, order):
    if order == "asc":
        return sorted(numbers)  # Return list in ascending order
    elif order == "desc":
        return sorted(numbers, reverse=True)  # Return list in descending order
    elif order == "none":
        return numbers  # Return the original list
    else:
        return "Invalid order parameter"  # Handle invalid order input

# Example usage
list1 = [4, 3, 2, 1]

# Test with different order values
print(sort_list(list1, "asc"))    # Output: [1, 2, 3, 4]
print(sort_list(list1, "desc"))   # Output: [4, 3, 2, 1]
print(sort_list(list1, "none"))   # Output: [4, 3, 2, 1]
