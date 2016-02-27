class felidae(object):
    @staticmethod
    def carnivorous():
        return True
    @staticmethod
    def can_roar():
        pass # method exists but doesn't do anything
    @staticmethod
    def has_spots():
        return False

class Pantherinae(felidae):
    @staticmethod
    def can_roar():
        print "ddoy"

class Lion(Pantherinae):
    species_name = "P. leo"

class Leopard(Pantherinae):
    species_name = "leopard"
    def has_spots(self):
        return True

Pantherinae.can_roar()
