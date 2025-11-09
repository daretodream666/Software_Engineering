class Tomato:
    global states
    states = [0, 1, 2, 3]

    def __init__(self, index):

        self._index = index  # dynamic
        self._state = states[self._index]  # dynamic

    def grow(self):  # grow tomato
        self._index += 1
        self._state = states[self._index]

    def is_ripe(self):  # check if Tomato is ripe
        if self._state == 3:
            return True
        else:
            return False


class TomatoBush:
    def __init__(self, count):
        self.tomatoes = []
        for i in range(count):  # make tomato list
            self.tomatoes.append(Tomato(0))

    def grow_all(self):  # grow all tomatoes
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):  # check are tomatoes ripe
        for tomato in self.tomatoes:
            if not tomato.is_ripe():
                return False
        return True

    def give_away_all(self):  # clear tomatoes list
        self.tomatoes = []


class Gardener:
    def __init__(self, name, bush):
        self.name = name  # gardener's name / public
        self._plant = bush  # accepts TomatoBush / non-public

    def work(self):  # makes gardener work, grows all tomatoes
        self._plant.grow_all()

    def harvest(self):  # checks can u ripe tomatoes if yes ripe them
        if self._plant.all_are_ripe():
            print("yay we got tomatoes")
            self._plant.give_away_all()
        else:
            print("we cant ripe rn, tomatoes arent rdy")

    @staticmethod
    def knowledge_base():  # give knowledge base like some info
        print(
            "so...\n"
            "basically u can\n"
            "grow tomatos with work()\n"
            "and harvest them with harvest()\n"
            "idk im not a gardener\n"
        )


Gardener.knowledge_base()
bush = TomatoBush(5)
gardener = Gardener("Alex", bush)
gardener.work()
gardener.harvest()
gardener.work()
gardener.work()
gardener.harvest()
