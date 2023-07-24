#Print the characters with ASCII codes
#from 32 to 63 on one row:
#64 to 95 on the next row:
#96 to 127 on a third row:

s = ''
for i in range (32,64):
    s += chr(i) #s = s + chr(i)
print(s)

s = ''
for i in range (64,96):
    s += chr(i) #s = s + chr(i)
print(s)

s = ''
for i in range (96,128):
    s += chr(i) #s = s + chr(i)
print(s)


for i in range(55100,55250): 
... s += chr(i)