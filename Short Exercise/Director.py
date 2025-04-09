students = {
    "Ana": {
"Surname": "Sanchez Fernanez", "Age": 17, "Time in school": "9 months" 
     },
     "Juan": {
"Surname": "Musk Tringer", "Age": 18, "Time in school": "10 months" 
     },
     "Steve": {
"Surname": "Sanchez Fernanez", "Age": 17, "Time in school": "2 years" 
     },
     "Bella": {
"Surname": "RichPur", "Age": 16, "Time in school": "9 years" 
     },
     "Robert": {
"Surname": "Gomez Hernandez", "Age": 19, "Time in school": "2 months" 
     }
}
print("💚Welcome to the YorkRize School Student System", end=" ")
print("Which student would you like to review today?💚")
keys = students.keys()
print("The students are:", keys)
request_directory = input("Enter the name of the student: ")
print("The student is:", students[request_directory])
