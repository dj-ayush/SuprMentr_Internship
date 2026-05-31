# Logic Builder Program

def fizz_buzz():
    fizz_count = 0
    buzz_count = 0
    fizzbuzz_count = 0

    for i in range(1, 51):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
            fizzbuzz_count += 1
        elif i % 3 == 0:
            print("Fizz")
            fizz_count += 1
        elif i % 5 == 0:
            print("Buzz")
            buzz_count += 1
        else:
            print(i)

    print("\nCount Summary:")
    print("Fizz count:", fizz_count)
    print("Buzz count:", buzz_count)
    print("FizzBuzz count:", fizzbuzz_count)

# Calling the function
fizz_buzz()