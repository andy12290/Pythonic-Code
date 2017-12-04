# This is related to string formatting for the string 3.5
name = 'Michael'
age = 43


# python but not
#print('This is %s and my age is %d' %(name,age))

# pythonic
# for this version we dont have to worry about the string or int

print('This is {} and my age is {}' .format(name,age))

