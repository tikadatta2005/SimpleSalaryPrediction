from utils import connectDB;

datas = connectDB.collection.find();

n=0

x=0
y=0

xy=0
xx=0

for data in datas:
    #import data
    salary = float((data['salary']))
    hours = float((data['workingHours']))
    #make summation
    x+=hours
    y+=salary
    #make xy and xx
    xy+=salary*hours
    xx+=hours*hours
    n+=1
