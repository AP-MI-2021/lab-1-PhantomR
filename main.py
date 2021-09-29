'''
Returns True if n is a prime, False otherwise.
'''
def is_prime(n):
  # 0 and 1 are not primes, by definition
  if (n == 0) or (n == 1):
    return False

  # 2 is a prime
  if (n == 2):
    return True

  # for numbers > 2, we can start checking divisors from 2 up to number / 2 (inclusive because of number 4)
  for d in range(2, (n // 2) + 1 , 2):
    if n % d == 0:
      return False

  # no divisor was found, so the number must be a prime
  return True
'''
Returns the product of the numbers in list 'lst'.
'''
def get_product(lst):
  # your code here
  pass
 
'''
Returns the GCD of two numbers x and y using the first algorithm.
'''
def get_cmmdc_v1(x, y):
  # your code here
  pass
  
'''
Returns the GCD of two numbers x annd y using the second algorithm.
'''
def get_cmmdc_v2(x, y):
  # your code here
  pass

def gui_primality_tester():
  n = int(input("Input the integer whose primality you want tested: "))
  if is_prime(n):
    print("The number is a prime.")
  else:
    print("The number is NOT a prime.")

def gui_list_product():
  pass


def gui_gcd_v1():
  pass

def gui_gcd_v2():
  pass
  
def main():
  # interfata de tip consola aici
  print("""
    1. Primality Tester
    2. Product of the numbers in a list
    3. GCD v1
    4. GCD v2
    -----------------------------------
    0. Exit
  """)

  while(True):
    choice = int(input("Comanda: "))
    if choice == 0:
      print("Good bye.")
    elif choice == 1:
      gui_primality_tester()
    elif choice == 2:
      gui_list_product()
    elif choice == 3:
      gui_gcd_v1()
    elif choice == 4:
      gui_gcd_v2()
    else:
      print("Invalid command :). Please try again.")

    print()

if __name__ == '__main__':
  main()
