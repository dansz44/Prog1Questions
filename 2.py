'''Objective: Convert a number in any base to the same number in another base'''
#NOTE: Work in progress 
def convertBase(ls, b1, b2):
    return 0

#----USER INPUT----#
try:
    ls = []
    num = int(input('Enter a number: '))
    while num != 0:
        ls.append(num)
        num = int(input('Enter a number: '))
    b1 = int(input('Number is in base: '))
    b2 = int(input('Desired base: '))
    print(ls)
except ValueError:
    print('Invalid data entered :(')
