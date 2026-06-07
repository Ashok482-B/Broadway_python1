#list
data=[1,23,4,5,6,7]
print(type(data))
print(data)
print(data[-3])

data=["hello","hiii","bye"]
print(data)
print(len(data))

print(data[2])
print(data[-3])

#mixed data types in list
data=["hello",1,"hii",85,True,None]
print(data)

#Slicing
data=["hello",1,"hii",85,True,None]
print(data[2:3])
print(data[:5])
print(data[2:])
print(data[:])

#adding data in list
#append
#insert
#concatination


#append
data=[1,"hello",3,4]
data.append("one")
print(data)

data=[]
data.append("lets")
data.append("23")
data.append(24)
print(data)

#insert
data=["hello",10,"bye"]
data.insert(1,20)
print(data)
#not good practise
data.insert(100,500)
print(data)

#Extend
a=[1,2,3,5,6]
b=[7,8,9,10]
a.extend(b)
print(a)
b.extend(a)
print(b)

#concatination +
a=[1,2,3,5,6]
b=[7,8,9,10]
c=a+b
print(c)
print(a,b,c)

#Delete(del)
#remove
#pop
#clear

#Delete(del)
d=[1,2,3,5,6]
del d[0]
print(d)

#Remove
b=[7,8,9,10]
b.remove(7)
print(b[1])

#pop


