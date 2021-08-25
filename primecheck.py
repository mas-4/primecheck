from sympy import isprime

printlimit = 1000001

def pi():
    x = 3
    π = 2 # π(3) = 2
    while True:
        π += isprime(x)
        if x % printlimit == 0:
            print("x={:,}, π(x)={:,}, π(x)/x={}".format(x, π, π/x))
        x+=2

if __name__ == '__main__':
    pi()
