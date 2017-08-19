from gameStates import gameMode
from utils.setting import PLAYER1_HIGH_SCORE, INTRO, PLAYER2_COMPETE


class GameIntro(gameMode.GameMode, object):
    def __init__(self, screen):
        super().__init__(INTRO, screen)

    def process(self):
        # need to change
        # return PLAYER1_HIGH_SCORE
        return PLAYER2_COMPETE