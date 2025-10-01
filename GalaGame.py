import pygame
import pgzrun
WIDTH = 700
HEIGHT = 900
spaceship = Actor("ship.png")
spaceship.x = 300
spaceship.y = 800
bullets = []
enemys = []
for i in range(5):
    for j in range(5):
        enemy = Actor("bug.png")
        enemy.x = 100 + i * 100 
        enemy.y = 100 + j * 100 
        enemys.append(enemy)




def draw():
    screen.clear
    screen.fill("black")
    spaceship.draw()
    for i in enemys:
        i.draw()
    for i in bullets:
        i.draw()



def update():
    for i in enemys:
        i.y = i.y+0.5
        for r in bullets:
            if r.colliderect(i):
                bullets.remove(r)
                enemys.remove(i)
    if keyboard.left:
        spaceship.x = spaceship.x -10
    if keyboard.right:
        spaceship.x = spaceship.x +10
    for i in bullets:
        i.y = i.y-10



def on_key_down(key):
    global bullets,enemys
    if key == keys.SPACE:
        bullet = Actor("bullet.png")
        bullet.x = spaceship.x
        bullet.y = spaceship.y
        bullets.append(bullet)


    



    



































pgzrun.go()