'''Objective: Convert a number in any base to the same number in another base'''

def convertBase(ls, b1, b2):
    '''Converting number list -> base 10'''
    b10 = 0
    b10List = []
    for i in range(0, len(ls)): #Iterates through list of numbers
        digits = [int(x) for x in str(ls[i])] #Separates multi-digit nums into individual digits
        print(digits) #Just for testing, shows separation of digits
        exp = len(digits)-1
        for j in range(0, len(digits)):
            b10 += digits[j] * (b1**exp)
            exp -= 1
        b10List.append(b10)
        b10 = 0
    print(b10List) #outputs final list of the numbers in base 10
    '''Converting from base 10 -> desired base'''
    #[not started]

#----USER INPUT----#
try:
    ls = []
    num = int(input('Enter a number: '))
    while num != 0:
        ls.append(num)
        num = int(input('Enter a number: '))
    b1 = int(input('Number is in base: '))
    b2 = int(input('Desired base: '))
    #print(ls)
    print(convertBase(ls,b1,b2))
except ValueError:
    print('Invalid data entered :(')

'''Things I need to fix: '''
# Currently first block of the function doesn't take into account if the number is out of the bases range,
#   i.e 98 base 8 *should* return 0, but doesn't in the code
#   Solution might have something to do with % and finding a remainder?
# Base 10 -> desired base conversion not coded yet