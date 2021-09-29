'''
Returns True if n is a prime, False otherwise.
'''
def is_prime(n):
  # your code here
  pass
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
  pass

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
