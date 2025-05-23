import modules.data as data
import utils.connectDB as db

#data
x = data.x #summation of x
y= data.y #summation of y
xy = data.xy #summation of xy
xx=data.xx #summation x2
n=data.n#length

#slope m
m=((n*xy)-(x*y))/((n*xx)-(x*x))
#constant c
c = (y - m * x) / n

def calcSalary(hours):
    exist = db.collection.find_one({"workingHours":hours})
    if(exist):return exist['salary']
    salary= m * hours + c
    return round(salary);