# def square_digits_sequence(n):
#     nums = []
#     while n not in nums:
#         nums.append(n)
#         n = sum(list(map(lambda x: int(x)**2, list(str(n)))))
#     return len(nums) + 1