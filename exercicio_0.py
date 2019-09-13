# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 10:13:23 2015

@author: aa02
"""
changed
key = ''
x = []
y = []
z = []

fileout=open('ex0.out','w')
fileout.write('"x"'',''"y"'',''"z"'+'\n')

for line in open('ex0.in'):
    
    columns = line.strip().split()
       
    if ':EndHeader' in columns[0]:
        key = ':EndHeader'    
   
    else:  
        if key == ':EndHeader' :
            x = columns[0]            
            y = columns[1]
            z = columns[2]
            fileout.write(x + ',' + y +  ','  + z+'\n') 
            
  
fileout.close()

print x
print y
print z

