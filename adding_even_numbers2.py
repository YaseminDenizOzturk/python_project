total = 0
for number in range(1,101):
    # ikiye bölümünden kalan sıfır olan sayılar çift sayıdır ve mod alma işlemiyle bu sayıları belirliyorum.
    if number % 2 == 0:
        total += number
    
print(total)
