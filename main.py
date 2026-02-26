import random

def generate_random_list(count, min_value, max_value):
    return [random.randint(min_value, max_value) for _ in range(count)]

def main():
    count = 12
    min_value = 5
    max_value = 200

    numbers = generate_random_list(count, min_value, max_value)

    print(numbers)

if __name__ == "__main__":
    main()