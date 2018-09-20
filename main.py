def lookie(givenlist,usernum):
  if usernum in givenlist:
    return True
  else:
    return False

usernum = int(input("Please enter a number to see if it is in the list"))
givenlist = [1, 3, 5, 30, 42, 43, 500]

print(lookie(givenlist,usernum))