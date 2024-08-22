name : str = input("Enter your name: ")
numbers = []
num1 : int = int(input("Enter your First favourite number : "))
num2 : int = int(input("Enter your Second favourite number : "))
num3 : int = int(input("Enter your Third favourite number : "))
numbers.append(num1)
numbers.append(num2)
numbers.append(num3)

print(f"Hello, {name}! Let's explore your favorite numbers:")
for number in numbers:
    even = number
    if even%2 == 0 :
        print(f"The {even} is even")
    else:
        print(f"The {even} is odd")

for num in numbers:
    sq = num
    print(f"The number {num} and its square is : {(num, num*num)}")


# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


prime = is_prime(sum(numbers))


print(f"Amazing! The sum of your favorite numbers is: {sum(numbers)}")
if prime:
    print(f"Wow! {sum(numbers)} is prime")

