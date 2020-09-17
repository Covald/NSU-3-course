import math
def func(a,b,c):
    d = b**2 - 4*a*c
    print(f"Discriminant is {d}")
    if d < 0:
        print("Unsolved equation || the discriminant is less than zero")
    elif d==0:
        print(f"Answer - {-b / (2 * a)}")
    else:
        print(f"Answer - {[(-b + math.sqrt(d)) / (2 * a), (-b - math.sqrt(d)) / (2 * a)]}")
a,b,c = map(int, input("Input a,b,c from ax^2+bx+c=0 - ").split())
func(a,b,c)
