import dataclasses


@dataclasses.dataclass
class Alien:
    name: str
    age: int


def generate_aliens():
    alien_count = 100000
    alien_list = [Alien(name=f'{i}', age=1) for i in range(alien_count)]
    return alien_list
