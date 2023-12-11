#!/usr/bin/env python
# coding: utf-8

# In[1]:


#In object-oriented programming (OOP), classes and objects are fundamental concepts. Here's an explanation of each:"
#Class:

#A class is a blueprint or template for creating objects.
#it defines the properties (attributes) and behaviors (methods) that all objects of its type share.
#A class doesn't have its own existence; it serves as a definition for creating objects.
#Think of a class as a recipe for baking a cake. The recipe specifies the ingredients and instructions, but it doesn't represent an actual cake until you follow the recipe to create one.
#Object:

#An object is an instance of a class.
#It represents a concrete entity with specific attributes and behaviors defined by its class.
#An object is a manifestation of the class in the real world.
#Using the cake analogy, an object would be an actual cake made following the recipe of the class. It will have its own unique size, flavor, and decorations, even though it shares the fundamental characteristics of all cakes based on the recipe.
#Example:
class Car:
  def __init__(self, color, brand, model):
    self.color = color
    self.brand = brand
    self.model = model

  def accelerate(self):
    print(f"{self.brand} {self.model} is accelerating!")

  def stop(self):
    print(f"{self.brand} {self.model} has stopped.")

my_car = Car("red", "Honda", "Civic")

my_car.accelerate()
my_car.stop()


# In[3]:


#Encapsulation: 
#Abstraction: 
#Inheritance: 
#Polymorphism: 
"this is the second answer"


# In[4]:


#In Python, the __init__() function, also known as the constructor, is crucial for object initialization. It serves several important purposes:
class Car:
  def __init__(self, color, brand, model):
    self.color = color
    self.brand = brand
    self.model = model

  def accelerate(self):
    print(f"{self.brand} {self.model} is accelerating!")

  def stop(self):
    print(f"{self.brand} {self.model} has stopped.")

my_car = Car("red", "Honda", "Civic")

my_car.accelerate()
my_car.stop()


# In[5]:


#In object-oriented programming (OOP), the keyword self is used within methods to refer to the current object instance. It serves several important purposes:


# In[6]:


#In object-oriented programming (OOP), inheritance is a powerful concept that allows new classes to inherit properties and functionalities from existing classes. This promotes code reuse, improves efficiency, and facilitates code organization. There are four main types of inheritance:


# In[7]:


class Animal:
  def __init__(self, name):
    self.name = name

  def eat(self):
    print(f"{self.name} is eating.")

class Dog(Animal):
  def bark(self):
    print(f"{self.name} is barking!")

dog = Dog("Max")
dog.eat()
dog.bark()


# In[ ]:




