from Engines.level import endlesslevel, level
class levelSelector:
    def __init__(self) -> None:
        pass

    def getLevel(self,levelNumber, diff, ENEMY_SKINS, BULLET_SKINS):
        if(levelNumber < 0):
            return endlesslevel(diff, ENEMY_SKINS, BULLET_SKINS)