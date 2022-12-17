from Engines.level import endlesslevel, level

"""level selector class
    """
class levelSelector:
    def __init__(self) -> None:
        pass
    
    def getLevel(self,levelNumber, diff, ENEMY_SKINS, BULLET_SKINS):
        """load a given level

        Args:
            levelNumber (int): the number of the level 
            diff (int): difficulity of the level
            ENEMY_SKINS (skin list): list of enemy assets
            BULLET_SKINS (skin list): list of bullet assets

        Returns:
            level object: level to be played 
        """
        #if the level is -1 then it is an endless level
        if(levelNumber < 0):
            return endlesslevel(diff, ENEMY_SKINS, BULLET_SKINS)
