# Add function @contributor : Sathwik Narkedimilli
def Sub(a, b):
    return a - b


c = Sub(50, 5)
print(c)

def mul(a,b):
    return a*b
print(mul(2,3))


#Add function @contributor : Saran Kumar
def square_n(a):
    return a*a


def sub(a, b):
    return a-b-a


print(sub(3, 2))

#Add function @contributor : Nikhil Gorle
def xor(a,b):
    return a^b

#Add function @contributor : Praneeth Reddy
def power(a,b):
    return a**b

def cubed(a):
    return a*a*a

# <<<<<< HEAD
#=======
#divide function @contributor : Patella Nitin Sai
def power(a,b):
    return a/b
#print function function @contributor : Patella Nitin Sai

def divide(a,b):
    return a/b

# Func in temp branc
def mul(a, b):
    return a**b

def temp(a,b,c):
    return a*b**c
print(temp(2,3,4))

print(mul(3, 6))

#>>>>>>> ead2381db1bafec25fb9cae392fb07fe4a8403f4

#Add function @contributor :R.Arun kumar
def max_of_four(a, b, c, d):
    return max(a, b, c, d)
print(max_of_four(1, 5, 3, 4))


#<<<<<<< HEAD
#Add function @contributor :D.rishikesh
def fibonacci(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

n = int(input("Enter how many Fibonacci numbers you want: "))
print(fibonacci(n))
#=======
# Added a cool print statement @ contributor : Anil Kumar (21BEC056)
def cool():
    print("I Love Devops")
    print("I love programming")


## Add function @contributor : MANCHALA SRINU 21BCS062
def print_lexicographical_numbers(n):
    numbers = [str(i) for i in range(1, n + 1)]
    numbers.sort()
    
    for number in numbers:
        print(number)

n = 20  
print_lexicographical_numbers(n)

## Add function 
def min_of_four(a, b, c, d):
    return min(a, b, c, d)
print(min_of_four(2, 7, 3, 4))
#>>>>>>> ead2381db1bafec25fb9cae392fb07fe4a8403f4
