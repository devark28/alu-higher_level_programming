#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
i=0
for c in str:
  print(f"{i}: {c}")
  i+=1
str=str[39:66]+str[107:110]+str[0:5]
print(str)