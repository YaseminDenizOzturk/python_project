def turn_right():
    turn_left()
    turn_left()
    turn_left()
# doğrudan sağa dönüş fonkisyonu olmadığı için sağa dönüş fonksiyonu oluşturdum.
# robotun sağa dönmesi için üç kez sola dönmesi gerekir.

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
# for döngüsüyle denediğim bu kısmı while döngüsüyle de oluşturabilirim.
while not at_goal():
# hedefe ulaşmadığı sürece robot bu işlemlere devam etmeli.
    jump()

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
