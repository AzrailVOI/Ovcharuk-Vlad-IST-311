#Задание №5
# Генерация массива с простыми числами - идея костыльная, но по другому я не догадался
num = int(input("Введите число: "))

  

def is_prime(n):
  ar = [i for i in range(n+1)]
  ar[1] = 0
  i = 2
  while i <= n**0.5:
    if ar[i] != 0:
      j = 2*i
      while j <= n:
        ar[j] = 0
        j = j + i
    i += 1
  ar = set(ar)
  ar.remove(0)
  arp = sorted(list(ar))
  #print(*arp) #- показывает массив в простыми числами до заданного числа (пример: num = 8; arp = 2 3 5 7)
  larp = len(arp) - 1
  if(n != arp[larp]):
    return False
  else:
    return True

print(is_prime(num))
if(is_prime(num) == True):
  print("Число простое")
else:
  print("Число составное")