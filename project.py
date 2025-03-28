import os
numlist=0
originallist=[]
#---------New list-------------
def newlist(originallist): 
  originallist.append([])
  return originallist
#---------New task-------------
def newtask(numlist,originallist):
  if numlist==0:
    print("Make a list before trying to add tasks to one!!\n")
  else:
    taskchoice=int(input("Select which list to add a task to, 1 through %d:\n" % numlist))
    taskchoice=taskchoice-1
    add=input(("Type what task you would like to add to this list: \n"))
    originallist[taskchoice].append(add)
#------Show task lists----------
def show(numlist,originallist):
  for numlist in originallist:
    print(numlist)
#-------Remove task------------
def removetask(numlist,originallist):
  tasknum=0
  listchoice=int(input("Which list would you like to remove from? 1 through %d:\n" % numlist))
  if listchoice>numlist or listchoice<1:
    print("Invalid choice!!\n")
  else:
    listchoice=listchoice-1
    for i in originallist[listchoice]:
      tasknum=tasknum+1
    if tasknum==0:
      print("Choose a list with tasks!!\n")
    else:
      print(originallist[listchoice])
      taskchoice=int(input("Which position is the task you would like to remove? 1 through %d:\n" % tasknum))
      if taskchoice>tasknum or taskchoice<1:
        print("Invalid choice!\n")
      else:
        taskchoice=taskchoice-1
        originallist[listchoice].pop(taskchoice)
  return originallist
#-------Remove list------------
def removelist(numlist,originallist):
  for numlist in originallist:
    print(numlist)
  listchoice=int(input("Choose the to-do list you would like to remove, 1 through %d \n" % numlist))
  if listchoice<1 or listchoice>numlist:
    print("Invalid choice!")
  else:
    listchoice=listchoice-1
    originallist.pop(listchoice)
  return originallist
#-----------Main---------------
choice=""
print("a) Make new to-do list")
print("b) Add task to to-do list")
print("c) Show task lists")
print("d) Remove task from to-do list")
print("e) Remove to-do list")
print("z) Exit")
while choice != "z":
  choice=input("Select an option: ")
  if choice=='a':
    numlist=numlist+1
    print(newlist(originallist))
  if choice=="b":
    newtask(numlist,originallist)
  if choice=='c':
    show(numlist,originallist)
  if choice=='d':
    removetask(numlist,originallist)
  if choice=='e':
    removelist(numlist,originallist)
    numlist=0
    for i in originallist:
      numlist=numlist+1
for numlist in originallist:
  print(numlist)
print("Task list done! Program complete.")