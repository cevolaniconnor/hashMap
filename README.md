# hashMap
This script demonstrates how to work with a hash map (dictionary) in Python to solve a common algorithmic problem: finding two numbers that add up to a target value.

Key Features:
Hash Map Iteration: Iterates over key-value pairs in a dictionary.
Target Sum Calculation: Checks if two numbers in the dictionary sum to a given target.
Efficient Lookup: Uses a complementary lookup strategy with a secondary hash map to ensure optimal performance.

How It Works:
The dictionary (nums) contains indices as keys and numbers as values.
The target variable is the desired sum.
As the script loops through the dictionary:
It computes the difference (complement) between the target and the current number.
If the complement exists in a secondary hash map, the script prints the indices of the two numbers and stops execution.
Otherwise, the current number is added to the hash map for future reference.
