#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self , name = "Unknown", breed ="Unknown"):
        self.name =name
        self.breed = breed

    def name (self):
        return self._name
        

    def set_name (self , new_name):
        if isinstance(new_name , str) and 1 <= len(new_name) <= 25:
            self._name = new_name
        else:
            print("Name must be string between 1 and 25 characters ")

    def breed (self , breed):
        return self._breed  


    def set_breed (self , breed):
        self.breed=breed
        if breed != APPROVED_BREEDS :
            print ("Breed must be in list of approved breeds.")

            pass
