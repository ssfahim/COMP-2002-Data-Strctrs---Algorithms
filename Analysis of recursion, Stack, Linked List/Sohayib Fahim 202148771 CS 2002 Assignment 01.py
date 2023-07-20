#  SOHAYIB SAZID FAHIM
#  202148771

x = int(input("Enter an integer: "))
if x <= 1:
    print("Input an integer that is greater than or equals 2")
else:
    def g(n):
        square = (n ** 2)
        exponent = (2 ** n - 1)
        solve = square / exponent
        if n == 1:
            return 1
        else:
            return solve + g(n - 1)
    print(g(x))
