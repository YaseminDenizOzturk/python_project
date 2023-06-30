import random
from hangman_word import word_list
hangman = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

#hangman = hangman[::-1] #böyle ters çevrilebilir
hangman.reverse() #yada böyle ters çevrilir eğer bunu bir değişkene eşitlersen değişken None olur yani fonksiyon adres üzerinde değişiklik yapıyor ve geriye değer döndermiyor
end_of_game = False
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

lives = 6
#guess = input("Guess a letter: ").lower()
# kullanıcıdan aldığım harfin küçük harf olmasını istediğim için lower() ekledim. büyük harf girerse de lower ile küçük harfe dönüştürülecektir.

display = []
for _ in range(word_length):
    display += "_"
# print(display)



while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print("You have already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word.You lose a life")
        lives -= 1
        if lives == 0:
            # oyunun sona ermesi için 85.kod satırı gereklidir.
            end_of_game = True
            print("You lose!")
    print(f"{' '.join(display)}")

    # print(display) 93. satır yerine bu olsaydı ' ',' ' şeklinde görünürdü. join sayesinde diziyi birleştirdim.

    if "_" not in display:
        end_of_game = True
        print("You Win!")

    print((hangman[lives]))
