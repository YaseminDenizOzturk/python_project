# insan ömrünün ortalama 80 yıl olduğu varsayılarak oluşturulmuştur.

age = input("What is your current age? ")
age_as_int = int(age)

years_remaining = 80 - age_as_int

#kalan günler kalan yıl sayısının 365 ile çarpımı sonucunda bulunur.
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

text = f"You have {days_remaining} days, {weeks_remaining} weeks, {months_remaining} months"

print(text)