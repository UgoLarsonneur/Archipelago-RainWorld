from BaseClasses import Location

class RainWorldLocation(Location):
    game: str = "My Game"

    # override constructor to automatically mark event locations as such
    def __init__(self, player: int, name = "", code = None, parent = None):
        super(RainWorldLocation, self).__init__(player, name, code, parent)
        self.event = code is None