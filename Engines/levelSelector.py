import level
class levelSelector:
    def __init__(self) -> None:
        pass

    def getLevel(self,levelNumber, diff):
        if(levelNumber < 0):
            return level.endlesslevel(diff)