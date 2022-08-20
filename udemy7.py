#Example

class Character():
    max_speed = 100
    death_health = 0

    def __init__(self, race, damage=10, armor=10):
        self.race = race #self.__race = race
        self.damage = damage
        self.armor = armor
        self.health = 100 #self._health = 100

    def hit(self, damage):
        self.health -= damage #self._health -= damage

    #unit = Character("Ork")
    #print(unit.race)
    #print(Character.max_speed)

    def is_dead(self):
        return self.health == Character.death_health

    #unit.hit(20)
    #print(unit.health)
    #print(unit.is_dead)

    @property  #
    def health(self):
        return self._health
    @property  #
    def race(self):
        return self.__race

    @property
    def current_speed(self):
        return self._current_speed

    @current_speed.setter
    def current_speed(self, current_speed):
        if current_speed < 0:
            self._current_speed = 0:
        elif current_speed > 100:
            self.current_speed = 100
        else:
            self._current_speed = current_speed

        #c.current_speed
        #c.current_speed = 50
        




