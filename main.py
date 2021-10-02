'''
Returneaza true daca n este prim si false daca nu.
'''

def is_prime(n):
  '''
  determina daca un nr. este prim
  :param n: nr. natural
  :return: adevarat sau fals
  '''
  if n<2:
    return False
  else:
    ok=True
    for i in range(2, n//2 +1):
      if n%i == 0:
        ok=False
  if ok:
    return True
  else:
    return False

'''
Returneaza produsul numerelor din lista lst.
'''
def get_product(lst):
  p=1
  for i in lst:
    p=p*i
  return p

'''
Returneaza CMMDC a doua numere x si y folosind primul algoritm.
'''
def get_cmmdc_v1(x, y):
  while x!=y:
    if x>y:
      x=x-y
    else:
      y=y-x
  return x

'''
Returneaza CMMDC a doua numere x si y folosind al doilea algoritm.
'''
def get_cmmdc_v2(x, y):
  while y!=0:
    r=x%y
    x=y
    y=r
  return x

def menu():
  print("Alegeti optiunea:")
  print("1.Verificare prim")
  print("2.Produs n numere")
  print("3.CMMDC V1")
  print("4.CMMDC V2")
  print("0.Iesire")
def main():
  menu()
  option=int(input("Option="))
  while option!=0:
    if option == 1:
      n=int(input("n="))
      print (is_prime(n))
    if option == 2:
      n=int(input("n="))
      lst=[]
      for i in range(0, n):
        x=int(input(""))
        lst.append(x)
      print(get_product(lst))

    if option == 3:
      x=int(input("x="))
      y=int(input("y="))
      get_cmmdc_v1(x, y)
      print(get_cmmdc_v1(x, y))

    if option == 4:
      x=int(input("x="))
      y=int(input("y="))
      print(get_cmmdc_v1(x, y))
    menu()
    option = int(input("Option="))

if __name__ == '__main__':
  main()
assert is_prime(1) == False
assert is_prime(3) == True
assert is_prime(4) == False

assert get_product([2, 3, 4]) == 24
assert get_product([3, 4, 6]) == 72
assert get_product([7, 10, 12]) == 840

assert get_cmmdc_v1(8, 4) == 4
assert get_cmmdc_v1(24, 16) == 8
assert get_cmmdc_v1(35, 15) == 5

assert get_cmmdc_v2(13, 3) == 1
assert get_cmmdc_v2(15, 10) == 5
assert get_cmmdc_v2(21, 14) == 7

