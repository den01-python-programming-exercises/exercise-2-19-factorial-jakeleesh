def main():
    #write your code below this line
    last = int(input("Give a number:"))
    factorial = 1
    for i in range(1, last + 1):
        factorial = factorial * i
    print("Factorial: " + str(factorial))

if __name__ == '__main__':
    main()
