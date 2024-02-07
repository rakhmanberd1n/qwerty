def histogram(nums):
    for i in nums:
        container = ""
        for j in range(0,i):
            container+='*'
        print(container)

nums = []

n=int(input("Give me the size of list: "))
print("Write down elements of the list: ")
for i in range(0, n):
    inp = int(input())
    nums.append(inp)

histogram(nums)