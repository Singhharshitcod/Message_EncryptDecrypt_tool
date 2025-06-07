import random
import string
# function to encrypt your message
def encrypt(str):
# check string length 
 if (len(str)>3):
#    avoid string to reduce time complexity
    lst=[]

    for i in str:
      lst.append(i)
#   remove first element and store it
    a=lst.pop(0)  
#  add at index first  
    lst.append(a)

    i=0;
# loop for intial addition
    while(i<3):
      lst.insert(i,random.choice(string.ascii_letters))
      i=i+1 
#  loop for last addition
    while(i<6):
      lst.append(random.choice(string.digits))
      i=i+1
#conver list into string using join fuction to optimize complexity      
    result=''.join(lst)  
    return result
 
 else:
   lst=[]
   
   for i in str[len(str)-1::-1]:
     lst.append(i)

   result=''.join(lst)
   return result


# function for decrypt your message
def decrypt(str):
# check string length
  if(len(str)>3):
    lst=[]

    for i in str:
      lst.append(i)
   
     # remove intial element
    i=0
    while(i<3):
      lst.pop(0)
      i=i+1
   
    # remove last element
    count=0 
    while(count<3):
      lst.pop(len(lst)-1 )
      count=count+1
      
    # remove last element and insert intially
    a=lst.pop(len(lst)-1)
    lst.insert(0,a)  

    result=''.join(lst)
    return result
  
  else:
    lst=[]
    # reverse the string 
    for i in str[len(str)::-1]:
      lst.append(i)

    result=''.join(lst)
    return result 

str=input("ENTER THE MESSAGE YOU WANT TO ENCRYPT: ")
print("~YOUR ENCRYPTED STRING IS: "+encrypt(str))
print("\n")
print("~YOUR DECRYPTED STRING IS: "+decrypt(encrypt(str)))
print("\n")



   
