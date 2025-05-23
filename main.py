import modules.train as model
import utils.connectDB as db

while(True):
    print("\n\n")
    hours = input("Please Enter Your Working Hours : ")
    salary = model.calcSalary(float(hours))

    print(f"Your salary is predicted to be : {salary}")

    satisfy=input("Are you satisfied with the prediction (Y/N) : ")
    if(satisfy.capitalize()=="Y"):
        db.collection.find_one_and_update({"workingHours":float(hours)}, {"$set":{"salary":salary}}, upsert=True)
        continue;
    
    correction = float(input("Please Enter Correct Salary : "))
    db.collection.find_one_and_update({"workingHours":float(hours)}, {"$set":{"salary":correction}}, upsert=True)
    print(f"Thankyou for correcting me!");

