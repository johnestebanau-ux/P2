students = int(input("How many students?:"))

for i in range(students):
   print("Student", 1 + 1)

   name = input("Enter name: ")
   activity1 = float(input("Activity 1:"))
   activity2 = float(input("Activity 2:"))
   activity3 = float(input("Activity 3:"))

   average = (activity1 + activity2 + activity3) / 3

   if average >= 90: 
       status = "Excellent"

   elif average >= 80: 
       status = "Very Good"

   elif average >= 75: 
       status = "Passed"

   else: 
       status = "Failed"

   print("---Student Result---")
   print("Name:", name)
   print("Average:", round(average, 2))
   print("Status:", status)
