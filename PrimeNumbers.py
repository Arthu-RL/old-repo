import math

def verify_prime(x: int) -> bool:
    """
    Verifies if a given number is a prime number.
    
    Parameters:
    x (int): The number to check for primality.

    Returns:
    bool: True if the number is prime, False otherwise.
    """
    
    if x < 2:
        print("That is not a prime number!")
        return False
    elif x == 2:
        print("Prime found!")
        return True

    if x % 2 == 0:
        print("That is not a prime number!")
        return False

    sqrt_x = math.isqrt(x)
    cont = 3

    while cont <= sqrt_x:
        if x % cont == 0:
            print(f"That is not a prime number, remainder of {x} divided by {cont} is 0")
            return False
        cont += 2

    print("Prime found!")
    return True
