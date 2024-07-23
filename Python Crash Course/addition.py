try:
    x = input("Choose a number.")
    x = int(x)
    y = input("Choose another number.")
    y = int(y)

except ValueError:
    print("Sorry, there is an error.")

else:
    sum = x + y
    print(sum)                                                                                                                                                                                                                                                                                