import os

path = os.getcwd()
print("The current working directory is %s:" % path)
print("-----------------------------------------------")
print("")

fh = open('studentIDs.txt', 'r')
while True:
    # read line
    line = fh.readline()
    # in python 2, print line
    # in python 3
    os.mkdir(line)
    # check if line is not empty
    if not line:
        break
fh.close()



