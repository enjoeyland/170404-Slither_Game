import pygame

from assembler.assembler import Assembler, Assembler_NotCreatedError
from event import eventDistributor
from event.eventCreators import snakeEventCreator
from event.eventHandlers import keyboardEventHandler, tickEventHandler, crashItemEventHandler
from gameObject import score, level
from gameObject.items import item, apple
from gameObject.player import snake, snakeAction, skin
from gameObject.player import snakeDisplayHandler
from ui import scoreTable, popUp
from utils import dataSavor, listener, utility
from utils.setting import DEFAULT_SPEED, DEFAULT_THICK, SKIN_DEFAULT, PLAYER1_HIGH_SCORE, P1_HIGH_SCORE_LISTENING_EVENT


class P1H_assembler(Assembler):
    def __init__(self, screen):
        self.screen = screen
        self.createGroupItem()
        self.createScore()

        self.createEventDistributor()
        self.createKeyboardEventHandler()
        self.createTickEventHandler()
        self.createCrashItemEventHandler()

        self.createPlayer()

        self.createScoreDisplay()
        self.createScoreTable()

        self.createSnakeEventCreator()

        self.createPausePage()
        self.createAppleItemSpawner()
        self.createLevelHandler(PLAYER1_HIGH_SCORE)


    def createGroupItem(self):
        self._groupItem = pygame.sprite.Group()
    def getGroupItem(self):
        if self._groupItem is not None:
            return self._groupItem
        else:
            raise Assembler_NotCreatedError("createScore")


    def createScore(self):
        """ create score """
        self._Score = score.Score()

    def getScore(self):
        if self._Score is not None:
            return self._Score
        else:
            raise Assembler_NotCreatedError("createScore")



    def createScoreDisplay(self):
        """ create related to score display """
        self._ScoreDisplayHandler = score.ScoreDisplayHandler(self.getScore())
        self._ScoreSavor = dataSavor.ScoreSavor()

    def getScoreDisplayHandler(self):
        if self._ScoreDisplayHandler is not None:
            return self._ScoreDisplayHandler
        else:
            raise Assembler_NotCreatedError("createScoreDisplay")

    def getScoreSavor(self):
        if self._ScoreSavor is not None:
            return self._ScoreSavor
        else:
            raise Assembler_NotCreatedError("createScoreDisplay")



    def createScoreTable(self):
        """ create related to score table at the end of game """
        self._ScoreTable = scoreTable.ScoreTable()

    def getScoreTable(self):
        if self._ScoreTable is not None:
            return self._ScoreTable
        else:
            raise Assembler_NotCreatedError("createScoreTable")



    def createListenerHandler(self):
        """ create listener handler """
        self.__listener = listener.ListenerHandler()

    def getListenerHandler(self):
        if self.__listener is not None:
            self.__listener = None
            return self.__listener
        else:
            raise Assembler_NotCreatedError("createScoreTable")



    def createEventDistributor(self):
        """ create event distributor """
        self._PygameEventDistributor = eventDistributor.pygameEventDistributor(P1_HIGH_SCORE_LISTENING_EVENT)

    def getPygameEventDistributor(self):
        if self._PygameEventDistributor is not None:
            return self._PygameEventDistributor
        else:
            raise Assembler_NotCreatedError("createEventDistributor")



    def createKeyboardEventHandler(self):
        """ create keyboard event handler """
        self._KeyboardEventHandler = keyboardEventHandler.KeyboardEventHandler(self.getPygameEventDistributor())

    def getKeyboardEventHandler(self):
        if self._KeyboardEventHandler is not None:
            return self._KeyboardEventHandler
        else:
            raise Assembler_NotCreatedError("createKeyboardEventHandler")



    def createTickEventHandler(self):
        """ create tick event handler """
        self._TickEventHandler = tickEventHandler.TickEventHandler(self.getPygameEventDistributor())

    def getTickEventHandler(self):
        if self._TickEventHandler is not None:
            return self._TickEventHandler
        else:
            raise Assembler_NotCreatedError("createTickEventHandler")

    def createCrashItemEventHandler(self):
        self._CrashItemEventHandler = crashItemEventHandler.CrashItemEventHandler(self.getPygameEventDistributor(),self.screen,self.getScore())

    def getCrashItemEventHandler(self):
        if self._CrashItemEventHandler is not None:
            return self._CrashItemEventHandler
        else:
            raise Assembler_NotCreatedError("createCrashItemEventHandler")



    def createSnakeEventCreator(self):
        """ create snake event creator """
        self._SnakeEventCreator = snakeEventCreator.SnakeEventCreator(self.getPlayer(), self.getGroupItem())

    def getSnakeEventCreator(self):
        if self._SnakeEventCreator is not None:
            return self._SnakeEventCreator
        else:
            raise Assembler_NotCreatedError("createSnakeEventCreator")

    def createPlayer(self):
        """ create player """
        self._player = snake.Snake(self.getPygameEventDistributor(), 1, DEFAULT_SPEED, DEFAULT_THICK, skin.Skin(), skinNum= SKIN_DEFAULT)
        self._SnakeAction = snakeAction.SnakeAction(self._player, self.getKeyboardEventHandler())
        self._SnakeDisplayHandler = snakeDisplayHandler.SnakeDisplayHandler(self._player)

    def getPlayer(self):
        if self._player is not None:
            return self._player
        else:
            raise Assembler_NotCreatedError("createPlayer")

    def getSnakeAction(self):
        if self._SnakeAction is not None:
            return self._SnakeAction
        else:
            raise Assembler_NotCreatedError("createPlayer")

    def getSnakeDisplayHandler(self):
        if self._SnakeDisplayHandler is not None:
            return self._SnakeDisplayHandler
        else:
            raise Assembler_NotCreatedError("createPlayer")



    def createPausePage(self):
        """ create pause page """
        self._PausePage = popUp.PausePage()

    def getPausePage(self):
        if self._PausePage is not None:
            return self._PausePage
        else:
            raise Assembler_NotCreatedError("createPausePage")



    def createAppleItemSpawner(self):
        """ create apple item generator """
        appleImg = utility.loadImage("apple")
        soundAppleBite = utility.loadSound("Apple_Bite")
        soundAppleBite.set_volume(1)
        self._ApplePrototype = apple.Apple(appleImg, sound = soundAppleBite)
        self._itemAppleSpawner = item.ItemSpawner(self._ApplePrototype)

    def getItemAppleSpawner(self):
        if self._itemAppleSpawner is not None:
            return self._itemAppleSpawner
        else:
            raise Assembler_NotCreatedError("createAppleItemSpawner")



    def createLevelHandler(self, gameName):
        """ create game state handler """
        self._LevelHandler = level.LevelHandler(gameName, self.getPlayer(), {"apple" : self.getItemAppleSpawner()})


    def getLevelHandler(self):
        if self._LevelHandler is not None:
            return self._LevelHandler
        else:
            raise Assembler_NotCreatedError("createGameHandler")