# import pandas
#
# dictionar = {
#     '1':['a', 'b'],
#     '2':['b', 'c'],
#     '3':['c']
# }
#
# data = pandas.DataFrame(dictionar)
# data.to_csv('./test.csv')

nums = [2,7,11,15]
target = 9
rtype = []

for num1 in range(len(nums)):
    for num2 in range(len(nums)):
        if nums[num1] + nums[num2 + 1] == target:
            rtype.extend([nums.index(nums[num1]), nums.index(nums[num2 + 1])])
        if nums[num2 + 1] == nums[-1]:
            break

print(rtype)

