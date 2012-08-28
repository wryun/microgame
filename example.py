from microgame import *

game = Game(20, 20, 32, 32)
game.set_tick(3000)

crunch = Sound('crunch.wav')
hero = Sprite('hero.gif', rand(game.width), rand(game.height))

candies = []
for _ in range(10):
    candies.append(Sprite('candy.png', rand(game.width), rand(game.height)))

while game.is_running():
    key = game.get_key()
    if key == K_UP:
        hero.y -= 1
    elif key == K_DOWN:
        hero.y += 1
    elif key == K_LEFT:
        hero.x -= 1
    elif key == K_RIGHT:
        hero.x += 1

    for candy in reversed(candies):
        if candy.x == hero.x and candy.y == hero.y:
            crunch.play()
            candies.remove(candy)

    if len(candies) == 0:
        game.end()

    if game.is_tick():
        candies.append(Sprite('candy.png', rand(game.width), rand(game.height)))

    game.draw(hero)
    game.draw(candies)
