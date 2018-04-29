def checkSum(name,check=False):
    if check==True:
        print("check status is true")
    print("check name="+name)



checkSum('sujj')
checkSum('sujj',True)


class Util(object):
    def __init__(self,method="check"):
        self.method = method



print(Util().__str__)
#lists
a1=[1,2,3,4,5,6,7,8]
nums = list(range(5)) 
print(a1[0:-1])
print(nums.__len__())
print(nums[:])
animals=['lion','cat','fish','horse']
for i in animals:
    print(i)
animals = ['cat', 'dog', 'monkey']

#maybe the interceptor implements the codes as key,value pair or turple
for idx, animal in enumerate(animals):
    print('#%d: %s' % (idx + 1, animal))


nums = [0, 1, 2, 3, 4]
squares = []
for x in nums:
    squares.append(x ** 2)
print(squares)   # Prints [0, 1, 4, 9, 16]


nums = [0, 1, 2, 3, 4]
squares = [x ** 2 for x in nums]
print(squares)   # Prints [0, 1, 4, 9, 16]

numbers=[0,1,2,3,4,5,6,7,8,9]
squrt = [x**2 for x in numbers]
print (squrt)


words1 =['I',"He","She"]
words2 = ['love','eat','run','hit','chase']
words3=['food','flower','butterfly','fly','pig','glass']
#{(x,y,z):x for x in words1,y for y in words2,z for z in words3} 
#still list can also support the condition to create it.
#[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
sentence =[( x, y ,z) for x in words1 for y in words2 for z in words3]
#print(sentence)
for s in sentence:
    print(s[0]+" "+s[1]+" "+s[2])
#dictionary
d = {'cat': 'cute', 'dog': 'furry'} 

d['dog']='food'
print(d['cat'])
print(d['dog'])

d = {'person': 2, 'cat': 4, 'spider': 8}
for animal in d:
    legs = d[animal]
    print('A %s has %d legs' % (animal, legs))


#sets
animals = {'cat', 'dog'}
print('cat' in animals)   # Check if an element is in a set; prints "True"
print('fish' in animals)  # prints "False"
animals.add('fish')       # Add an element to a set
print('fish' in animals)  # Prints "True"
print(len(animals))       # Number of elements in a set; prints "3"
animals.add('cat')        # Adding an element that is already in the set does nothing
print(len(animals))       # Prints "3"
animals.remove('cat')     # Remove an element from a set
print(len(animals))       # Prints "2"


#Tuples
d = {(x, x + 1): x for x in range(10)}  