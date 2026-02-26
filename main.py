import random

def main():
    count = 12
    min_value = 5
    max_value = 200

    numbers = []
    for _ in range(count):
        numbers.append(random.randint(min_value, max_value))

    print(numbers)

if __name__ == "__main__":
    main()