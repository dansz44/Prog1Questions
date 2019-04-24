'''Restriction: Only numbers in up to base 36 can be converted'''

def convertBase(ls, b1, b2):
    '''Converts numbers -> base 10'''
    b10List = []
    for i in range(0, len(ls)):
        if ls[i] < 0:   #Checks if number is negative, then makes it positive
            ls[i] = ls[i] * -1
        try:    #Checks if number entered is within base bounds
            b10num = int(str(ls[i]), b1)
            b10List.append(b10num)
        except ValueError: #Error lies here, for when the number is out of bounds of base
            if ls[i] // 10 > b1:
               b10List.append(0)
            else:
                b10List.append(ls[i] // 10)
    return b10List
    '''Converts base 10 numbers -> desired base''' #This part functions normally (I think)
    finalList = []
    for i in range(0, len(b10List)):
        while b10List[i]:
            finalList.append(int(b10List[i] % b2))
            b10List[i] //= b2
    return finalList[::-1]
def main():
    ls = []
    num = int(input('Enter a number: '))
    while num != 0:
        ls.append(num)
        num = int(input('Enter a number: '))
    b1 = int(input('Number is in base: '))
    b2 = int(input('Desired base: '))
    print(convertBase(ls,b1,b2))

main()