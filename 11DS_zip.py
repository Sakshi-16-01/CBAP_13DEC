#Topic: ZIP
#-----------------------------
#The purpose of zip() is to map the similar index of multiple containers so that they can be used just using as single entity.

#Syntax : zip(*iterators)
#Parameters : 
#Python iterables or containers ( list, string etc )
#Return Value : Returns a single iterator object, having mapped values from all the containers.

# initializing lists 
name = [ "Virat", "Shikhar", "Ravi", "Rahul" ] 
roll_no = [ 4, 1, 3, 2 ] 
marks = [ 40, 50, 60, 70 ] 
  
# using zip() to map values : parallel join
mapped1a = zip(name, roll_no, marks) 

mapped1a  

# converting values to print as set 

mapped1b = list(mapped1a) 
mapped1b  


# printing resultant values  
print ("The zipped result is : ", mapped1b) 

# converting values to print as list 
mapped2b = list(mapped1b)
mapped2b


#Unzipping from zipped DS
# unzipping values 
namz, roll_noz, marksz = zip(*mapped1b) 
print(namz)
print(roll_noz)
print(marksz)
