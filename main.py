import datetime
time=datetime.datetime.now()

purpose=input("for read a file/for write a file=\n")
person=input("\nfor kishan/rohan?=\n")
act=input("\nfor food/exercise?=\n")


def read(name,action): 
  with open(f"{name}_{action}.txt","r") as rr:
    print(rr.read())
  

def write(name,action):
  
  with open(f"{name}_{action}.txt","a") as ww:
    if act=="food":
      ww.write(f"\ntime was {time} and you ate {name_of_food_exe}.")        
    elif act=="exercise":
      ww.write(f"\ntime was {time} and you did {name_of_food_exe}")
    print("your entry is done")
  


if purpose=="read":         
  read(person,act)  
  
if purpose=="write":
    name_of_food_exe=input("\nwhat do you want to add?") 
    write(person,act)