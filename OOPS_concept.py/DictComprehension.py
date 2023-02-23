keys = ['a','b','c','d','e']
values = [1,2,3,4,5]  
  
# but this line shows dict comprehension here  
myDict = { k:v for (k,v) in zip(keys, values)}  
  
# We can use below too
# myDict = dict(zip(keys, values))  
  
print (myDict)


myDict1 = {x: x**2 for x in [1,2,3,4,5]}
print (myDict1)

