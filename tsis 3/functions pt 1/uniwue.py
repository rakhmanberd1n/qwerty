def unique(nums):
    uniq=[]
    for i in range(0,len(nums)):
        isdup=False
        for j in range(i+1,len(nums)):
            if nums[i]==nums[j]:
                isdup=True
        if not isdup:
            uniq.append(nums[i])
    print(uniq)

nums = []

n=int(input("Give me the size of list: "))
print("Write down elements of the list: ")
for i in range(0, n):
    inp = int(input())
    nums.append(inp)

unique(nums)