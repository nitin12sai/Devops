print("Hello, World!")
print("Hi i am Praneet Reddy ")

def print_lexicographical_numbers(n):
    # Create a list of numbers from 1 to n
    numbers = [str(i) for i in range(1, n + 1)]
    
    # Sort the numbers lexicographically
    numbers.sort()
    
    # Print the sorted numbers
    for number in numbers:
        print(number)

# Example usage
n = 20  # You can change this value
print_lexicographical_numbers(n)
