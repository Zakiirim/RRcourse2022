def fizzbuzz() -> None:
    """It loops from 1 to 100 inclusive and
    for each number prints:
    
    * If multiple of 3: "Fizz".
    * If multiple of 5: "Buzz".
    * If multiple of 3 and 5: "FizzBuzz".
    * If not multiple of 3 or 5: prints the number.
    """
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)
