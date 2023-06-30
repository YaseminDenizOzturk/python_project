for number in range(1,101):
    # if içindeki şartı ilk sıraya koymak önemli çünkü değilse şıklarına koysaydım 3 e veya 5 e bölümünden sıfır kaldığı için o şartı sağlayıp diğerlerini konrtol etmeyecekti.
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
    # kalan sayıları aynen yazdırması için else print(number) yazdım.

