#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self ,name = "Unknown" , job = "Unemployed"):
        self._name = name
        self.job = job

    def name(self):
        return self._name
        
    def set_name (self , new_name ):
        if isinstance(new_name, str) and 1 <= len(new_name) <= 25:
          self._name = new_name.title()  # Convert to title case
        else:
           print("Name must be a string between 1 and 25 characters.")

  
    def job(self):
       return self._job

    def set_job(self, new_job):
       if new_job.upper() in APPROVED_JOBS:  # Check if job is in the list (case-insensitive)
         self._job = new_job
       else:
          print("Job must be in list of approved jobs.")

# Example usage
person1 = Person("john DOe")
print(person1.name)  
print(person1.job)  

person2 = Person(job="Software Engineer")
print(person2.job)  

person3 = Person("reallyLongNameThatExceedsLimit")  
person3.job = "NotAJob"  

