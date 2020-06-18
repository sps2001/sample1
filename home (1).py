#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1.simple calculator
a=float(input("value of a "))
b=float(input("value of b "))
print("sum of two numbers=",a+b)
print("difference of two numbers",a-b)
print("product of two numbers",a*b)
print("division of two numbers",a/b)
print("modules of two numbers",a%b)
print("exponential of two numbers",a**b )


# In[4]:


#2.simple interest
P=float(input("enter the priciple amount"))
T=float(input("enter the time"))
R=float(input("enter rate of interest"))
SI=(P*T*R)/100
print("simple interest=",SI)


# In[5]:


#3.area os circle
r=float(input("Enter the radius of the circle="))
a=(22/7)*r**2
print("Area of circle",a)


# In[6]:


#4.Area of triangle
a=float(input("enter frist side of triangle"))
b=float(input("enter second side of triangle"))
c=float(input("enter tried side of triangle"))
s=(a+b+c)/2
area =(s*(s-a)*(s-b)*(s-c))**0.5
print("the area of triangle is",area)


# In[7]:


#5.celsius to fahrenheit
c=float(input("enter temperature in celsius"))
f=(c*9/5)*32
print("temperature in fahrenheit is ",f)


# In[8]:


#6.0area of rectangle
l=float(input("enter the length of rectangle"))
b=float(input("enter the breadth of rectanglr"))
a=l*b
print("the area of rectangle is ",a)


# In[9]:


#7.perimeter of square
s=float(input("enter the side of the square "))
a=4*s
print("perimeter of the square is ",a)


# In[10]:


#8.circumference of a circle
r=float(input("enter the radius of the circle"))
c=2*(22/7)*r
print("circumference of the circle is ",c)


# In[11]:


#9.swapping of two numbers
a=float(input("value of a"))
b=float(input("value of b"))
temp,a=a,b
b=temp
print("the value of a after swapping=",a)
print("the value of b after swapping=",b)


# In[ ]:




