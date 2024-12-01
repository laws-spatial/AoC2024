from collections import Counter
from utilities import read_data

data = read_data("d1p1")

# set up value lists
left_values: list[int] = []
right_values: list[int] = []

# split values into separate lists
for row in data:
    split_data = row.split("   ")
    left_values.append(int(split_data[0]))
    right_values.append(int(split_data[1]))

# order lists from smallest to largest
left_values.sort()
right_values.sort()

# get difference between values
diff_values = []
for left, right in zip(left_values, right_values):
    value = abs(left-right)
    diff_values.append(value)

# sum values
sum_values = sum(diff_values)
print(f"The answer for puzzle 1 is {sum_values}")

# Puzzle 2
counter = Counter(right_values)

similarity_scores = []

for value in left_values:
    count = counter[value]
    similarity_score = value * count
    similarity_scores.append(similarity_score)

total_similarity_score = sum(similarity_scores)
print(f"The answer for puzzle 2 is {total_similarity_score}")