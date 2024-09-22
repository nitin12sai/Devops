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


#Add function @contributor :R.Arun kumar
def max_of_four(a, b, c, d):
    return max(a, b, c, d)
print(max_of_four(1, 5, 3, 4))


#Add function @contributor :D.rishikesh
def fibonacci(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

n = int(input("Enter how many Fibonacci numbers you want: "))
print(fibonacci(n))
