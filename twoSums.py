nums = {
	0: 2,
	1: 11,
	2: 7,
	3: 15,
	4: 4
}

target = 9
seen = {}

for index, number in nums.items():
	complement = target - number
	if complement in seen:
		print(f'With a target of {target}')
		print(f"The two sums are at indices: {seen[complement]}, {index} ")
		print(f'With numbers {complement} and {number}')
		break
	seen[number] = index