def colatz(number, step = 1):   
    print(f"{step}: {number}")
    if number % 2 == 0:
        number = number / 2
        if number == 1:
            return
        else:
            colatz(number, step + 1)
    else:
        number = number * 3 + 1
        if number == 1:
            return
        else:
            colatz(number, step + 1)
try:
    number = int(input("Enter the first number:"))
    if number <= 0:
        raise ValueError
    colatz(number, step = 1)
except ValueError:
    print("Enter positive integer")