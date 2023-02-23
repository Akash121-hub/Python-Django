def test_generator(nums):
    for i in range(len(nums)):
        yield i
abc = [1,3,4,5]
instan = test_generator(abc)

print(instan.__next__())
print(instan.__next__())
print(instan.__next__())
print(instan.__next__())
# print(instan.__next__())