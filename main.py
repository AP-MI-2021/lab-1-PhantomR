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
  product = 1
  for element in lst:
    product *= element

  return product
 
'''
Returns the GCD of two numbers x and y using Euclid's subtraction-based algorithm.
'''
def get_cmmdc_v1(x, y):
  # if the two numbers are the same, their GCD is their common value
  if x == y:
    return x

  # if the two numbers are distinct, we call recursively, changing only the
  # largest's value by subtracting the lower one from it
  if x > y:
    return get_cmmdc_v1(x - y, y)
  else:
    return get_cmmdc_v1(x, y - x)

  
'''
Returns the GCD of two numbers x annd y using Euclid's division-based algorithm.
'''
def get_cmmdc_v2(x, y):
  # if x is 0, then the GCD of the two is y
  if x == 0:
    return y

  # if x is non-zero, then the GCD can be computed recursively as the GCD of the numbers (y MOD x) and x
  return get_cmmdc_v2(y % x, x)

def gui_primality_tester():
  n = int(input("Input the integer whose primality you want tested: "))
  if is_prime(n):
    print("The number is a prime.")
  else:
    print("The number is NOT a prime.")

def gui_list_product():
  # Read the length of the list
  n = int(input("Input the length of the list: "))
  lst = []

  # Read an integer and add it to the list at each step
  for i in range(0, n):
    element = int(input("list[" + str(i) + "] = "))
    lst.append(element)

  list_product = get_product(lst)
  print("The product of the elements in the list is: " + str(list_product))

def gui_gcd_v1():
  first_number = int(input("Input the first number: "))
  second_number = int(input("Input the second number: "))

  gcd = get_cmmdc_v1(first_number, second_number)
  print("The GCD of the two numbers is: " + str(gcd))

def gui_gcd_v2():
  first_number = int(input("Input the first number: "))
  second_number = int(input("Input the second number: "))

  gcd = get_cmmdc_v2(first_number, second_number)
  print("The GCD of the two numbers is: " + str(gcd))
  
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
    choice = int(input("Command: "))

    if choice == 0:
      print("Good bye.")
      break
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
