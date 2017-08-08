# list = [3,1]
# swap = list[0]
# list[0] = list[1]
# list[1]= swap
# print(list)       //this works to swap the #'s!

bubblelist = [5,4,3,2,1]
def swap():
    for i in range(len(bubblelist)-1):
        for i in range(len(bubblelist)- 1):
            if bubblelist[i] > bubblelist[i+1]:
                switch = bubblelist[i+1]
                bubblelist[i+1] = bubblelist[i]
                bubblelist[i] = switch
swap()
print(bubblelist)

# not finished- binary sorting
list = [2,3,7,12,19,22]
x = 40
midpoint = len(list/2)
def rounding_up:
    if float(midpoint) % 2 == 0
    else:
        float(midpoint) + 0.5
def binarySort(list, x):
    for i in range(len(list)-1):
        if list[midpoint] < x:
            if i[midpoint] == x:
                return True
            else:
                del list[0:midpoint]
                return False
        elif list[midpoint] > x:
            if i[midpoint] == x:
                return True
            else:
                del list[midpoint:len(list)]
                return False
binarySort(list,x)
if True:
    print("This number is in the list!")
if False:
    print("boohoo :( error 404: number not found ;-;")
