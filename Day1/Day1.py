import re

numHelper = "one|two|three|four|five|six|seven|eight|nine"
pattern = re.compile(r'(?=(\d|%s))' % numHelper)
nums = numHelper.split('|')

file = open("input.txt", "r")
lines = file.readlines()
numberlist = []
for line in lines:
    onlyNum = []
    for num in pattern.findall(line):
        if num in nums:
            num = str(nums.index(num) + 1)
        onlyNum.append(num)
    numberlist.append(int(onlyNum[0] + onlyNum[-1]))
result = sum(numberlist)
print(result)