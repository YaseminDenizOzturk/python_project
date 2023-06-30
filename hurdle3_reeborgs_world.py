def turn_right():
    turn_left()
    turn_left()
    turn_left()
# doğrudan sağa dönüş fonkisyonu olmadığı için sağa dönüş fonksiyonu oluşturdum.
# robotun sağa dönmesi için üç kez sola dönmesi gerekir.

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    

while not at_goal():
    if wall_in_front():
        # önünde duvar varsa jump fonksiyonunun adımlarını uygulayacak.
        jump()
    else:
        # önünde duvar yoksa ilerlemeye devam edecek.
        move()

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################