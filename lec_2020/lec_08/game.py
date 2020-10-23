class Dragon:
    id = 0

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.id = Dragon.id
        Dragon.id += 1

    def is_alive(self):
        return self.health > 0

    def get_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def talk(self):
        print(self.name, 'health', self.health, '. Hit me!')

    def final_cry(self):
        print(self.name, 'is dead...')


def main():
    enemy__list = [Dragon('Smog'), Dragon('Hidra')]
    finish = False
    while not finish:
        enemy = enemy__list[0]
        print('ID:', enemy.id)
        enemy.talk()
        damage = int(input())
        enemy.get_damage(damage)
        if not enemy.is_alive():
            enemy.final_cry()
            enemy__list.pop(0)
        if not enemy__list:
            finish = True
    print('You Win!')


main()
