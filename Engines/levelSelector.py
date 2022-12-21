import Engines.level

"""level selector class
    """
class levelSelector:
    def __init__(self) -> None:
        pass
    
    def getLevel(self,levelNumber, diff, ENEMY_SKINS, BULLET_SKINS,BOSS_SKINS):
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
            return Engines.level.endlesslevel(diff, ENEMY_SKINS, BULLET_SKINS,BOSS_SKINS)
        if(levelNumber == 0):
            return Engines.level.levelOne(diff, ENEMY_SKINS, BULLET_SKINS,BOSS_SKINS)
        if(levelNumber == 1):
            return Engines.level.levelTwo(diff, ENEMY_SKINS, BULLET_SKINS,BOSS_SKINS)
        if(levelNumber == 2):
            return Engines.level.levelThree(diff, ENEMY_SKINS, BULLET_SKINS,BOSS_SKINS)
        if(levelNumber == 3):
            return Engines.level.levelFour(diff, ENEMY_SKINS, BULLET_SKINS,BOSS_SKINS)
        if(levelNumber == 4):
            return Engines.level.levelFive(diff, ENEMY_SKINS, BULLET_SKINS,BOSS_SKINS)
        if(levelNumber == 5):
            return Engines.level.levelSix(diff, ENEMY_SKINS, BULLET_SKINS,BOSS_SKINS)
        if(levelNumber == 6):
            return Engines.level.levelSeven(diff, ENEMY_SKINS, BULLET_SKINS,BOSS_SKINS)
        if(levelNumber == 7):
            return Engines.level.levelEight(diff, ENEMY_SKINS, BULLET_SKINS,BOSS_SKINS)