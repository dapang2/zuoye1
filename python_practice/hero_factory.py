from python_practice.ez import ez
from python_practice.jinks import jks
from python_practice.timo import timo
from python_practice.police import police



class Herofactory:

    def create_hero(self, name):
        if name == 'jks':
            return jks()
        elif name == 'ez':
            return ez()
        elif name == 'timo':
            return timo()
        elif name == 'police':
            return police()
        else:
            raise Exception("此英雄不再英雄工厂")


hero_factory = Herofactory()
timo = hero_factory.create_hero("timo")
police = hero_factory.create_hero("police")
police.speak_lines()
timo.speak_lines()
timo.fight(police.hp,police.power,timo)

