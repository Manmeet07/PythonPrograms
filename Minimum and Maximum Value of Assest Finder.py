lst = []
num = int(input('How many numbers: '))
for n in range(num):
    numbers = int(input('Enter number: '))
    lst.append(numbers)
print("Maximum Value of Asset is :", max(lst), "\nMinimum value of Asset is :", min(lst))
