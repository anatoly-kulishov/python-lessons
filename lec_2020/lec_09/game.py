class Dragon:
    id = 0

    def __init__(self):
        self.id = Dragon.id
        Dragon.id += 1


def main():
    obj = Dragon()
    print(obj.id)


main()
