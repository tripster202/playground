import random
from faker import Faker

fake = Faker()

def demonstrate_collections():
    print("Welcome to the Python Collections Tutorial!")
    print("We will explore Lists, Dictionaries, Sets, and Tuples using fake data.\n")

    # 1. List: Ordered, allows duplicates, mutable
    print("1. List Example:")
    fake_names = [fake.name() for _ in range(5)]
    print(f"Original List: {fake_names}")
    fake_names.append(fake.name())
    print(f"List after adding an element: {fake_names}")
    print(f"Accessing the first element: {fake_names[0]}\n")

    # 2. Dictionary: Key-value pairs, unordered (insertion order preserved in Python 3.7+), mutable
    print("2. Dictionary Example:")
    fake_profile = {fake.name(): fake.email() for _ in range(5)}
    print(f"Original Dictionary: {fake_profile}")
    random_key = random.choice(list(fake_profile.keys()))
    print(f"Accessing value for a random key ({random_key}): {fake_profile[random_key]}")
    fake_profile[fake.name()] = fake.email()
    print(f"Dictionary after adding a new key-value pair: {fake_profile}\n")

    # 3. Set: Unordered, no duplicates, mutable
    print("3. Set Example:")
    fake_cities = {fake.city() for _ in range(5)}
    print(f"Original Set: {fake_cities}")
    fake_cities.add(fake.city())
    print(f"Set after adding an element: {fake_cities}")
    print(f"Checking if a city is in the set: {'New York' in fake_cities}\n")

    # 4. Tuple: Ordered, allows duplicates, immutable
    print("4. Tuple Example:")
    fake_numbers = tuple(random.randint(1, 100) for _ in range(5))
    print(f"Original Tuple: {fake_numbers}")
    print(f"Accessing the second element: {fake_numbers[1]}")
    print(f"Count of a specific number in the tuple: {fake_numbers.count(fake_numbers[0])}\n")

    print("End of the tutorial. Happy coding!")

if __name__ == "__main__": 
    demonstrate_collections()