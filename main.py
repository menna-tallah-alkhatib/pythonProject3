# # السؤال الاول
x=[12,75,150,180,145,525,50]
for v in range(len(x)):
    if(x[v]>500):
        break
    if(x[v]%5==0 and x[v]<=150  ):
        print(x[v])

print("///////////////////////////////////////////////////")

# السؤال الثاني
x=False

for i in range(5):
     print(i)
     x=True
if not x:
    print("not Done!")
else:
    print("Done!")
print("///////////////////////////////////////////////////")


# السؤال الثالث
x=input("enter num")
x=int(x)
i=int(x)
z=0
while(i!=0):
    z+=int(i%10)
    z*=10
    i=int(i/10)
z=int(z/10)
print(z)
print("///////////////////////////////////////////////////")
# السؤال الرابع
x1=["Ten","Twenty","thirty"]
x2=[10,220,30]
dict1={}
for v in range(len(x1)):
    dict1[x1[v]]=x2[v]
print(dict1)
print("///////////////////////////////////////////////////")
# السؤال الخامس
s={
    "name":"kelly",
    "age":25,
    "salary":8000,
    "city":"New york"
}
keys=['name','salary']
for v2 in range(len(keys)):
   s.pop(keys[v2])
print(s)
print("///////////////////////////////////////////////////")


# السؤال السادس
x1={ "yellow","orange","Black"}
x2={"Blue","Green","Red"}
x3=x1.union(x2)
print(x3)

print("///////////////////////////////////////////////////")

# السؤال السابع

s1={10,20,30,40,50}
s2={30,40,50,60,70}
s3=s1.intersection(s2)
print(s3)

print("///////////////////////////////////////////////////")

# السؤال الثامن

t=(10,20,30,40,50)
t1=(t[4],t[3],t[2],t[1],t[0])

print(t1)

print("///////////////////////////////////////////////////")

#السؤال التاسع
t=("o",[10,20,30],(5,15,25))

print(t[1][1])

print("///////////////////////////////////////////////////")



# السؤال العاشر

t=(10,20,30,40)
a=t[0]
b=t[1]
c=t[2]
d=t[3]
print(a)
print(b)
print(c)
print(d)