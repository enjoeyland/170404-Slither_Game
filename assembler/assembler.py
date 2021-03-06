import pygame

from event import eventDistributor
from event.eventCreators import snakeEventCreator
from event.eventCreators.arrowKeyEventCreator import ArrowKeyEventCreator
from event.eventHandlers import keyboardEventHandler, tickEventHandler, crashItemEventHandler
from event.eventQueue import EventQueue
from gameObject import level
from gameObject.items import item, apple
from gameObject.player import snake, snakeAction
from gameObject.player import snakeDisplayHandler
from ui import scoreTable, popUp
from utils import dataSavor, listener, score
from utils.setting import SKIN_DEFAULT, RIGHT, SCREEN_MID, GREEN


class Assembler_NotCreatedError(Exception):
    # def __init__(self, funcName):
    def __init__(self):
        pass
        # self.funcName = funcName
    def __str__(self):
        # return "function '%s' is not created" % self.funcName
        return "function is not created"

def checkNotNone(func):
    def wrapper(*args):
        result = func(*args)
        try:
            return result
        except AttributeError:
            raise Assembler_NotCreatedError()
    return wrapper


class Assembler(object):
    def __init__(self):
        self.players = []

    def createEventQueue(self):
        self._EventQueue = EventQueue()
    @checkNotNone
    def getEventQueue(self):
        try:
            return self._EventQueue
        except AttributeError:
            return pygame.event

    def createArrowKeyEventCreator(self):
        self._ArrowKeyEventCreator = ArrowKeyEventCreator(self.getEventQueue())
    @checkNotNone
    def getArrowKeyEventCreator(self):
        return self._ArrowKeyEventCreator


    def createGroupItem(self):
        self._groupItem = pygame.sprite.Group()
    @checkNotNone
    def getGroupItem(self):
        return self._groupItem



    def createScore(self):
        """ create score """
        self._Score = score.Score()
    @checkNotNone
    def getScore(self):
        return self._Score



    def createScoreDisplay(self):
        """ create related to score display """
        self._ScoreDisplayHandler = score.ScoreDisplayHandler(self.getScore())
        self._ScoreSavor = dataSavor.ScoreSavor()
    @checkNotNone
    def getScoreDisplayHandler(self):
            return self._ScoreDisplayHandler
    @checkNotNone
    def getScoreSavor(self):
            return self._ScoreSavor



    def createScoreTable(self):
        """ create related to score table at the end of game """
        self._ScoreTable = scoreTable.ScoreTable()
    @checkNotNone
    def getScoreTable(self):
        return self._ScoreTable



    def createListenerHandler(self):
        """ create listener handler """
        self.__listener = listener.ListenerHandler()
    def getListenerHandler(self):
        if self.__listener is not None:
            self.__listener = None
            return self.__listener
        else:
            raise Assembler_NotCreatedError()



    def createPygameEventDistributor(self, eventListToListen):
        """ create event distributor """
        self._PygameEventDistributor = eventDistributor.pygameEventDistributor(eventListToListen)
    def createEventQueueDistributor(self, eventListToListen):
        """ create event distributor """
        self._EventQueueDistributor = eventDistributor.EventQueueDistributor(self.getEventQueue(), eventListToListen)
    def getEventDistributor(self):
        try:
            return self._PygameEventDistributor
        except AttributeError:
            try:
                return self._EventQueueDistributor
            except AttributeError:
                raise Assembler_NotCreatedError()



    def createKeyboardEventHandler(self):
        """ create keyboard event handler """
        self._KeyboardEventHandler = keyboardEventHandler.KeyboardEventHandler(self.getEventDistributor())
    @checkNotNone
    def getKeyboardEventHandler(self):
        return self._KeyboardEventHandler



    def createTickEventHandler(self):
        """ create tick event handler """
        self._TickEventHandler = tickEventHandler.TickEventHandler(self.getEventDistributor())
    @checkNotNone
    def getTickEventHandler(self):
        return self._TickEventHandler

    def createCrashItemEventHandler(self, screen, snake, score):
        self._CrashItemEventHandler = crashItemEventHandler.CrashItemEventHandler(self.getEventDistributor(), screen, snake, score)
    @checkNotNone
    def getCrashItemEventHandler(self):
        return self._CrashItemEventHandler



    def createSnakeEventCreator(self, gameState):
        """ create snake event creator """
        self._SnakeEventCreator = snakeEventCreator.SnakeEventCreator(self.getEventQueue(), self._getSnake(), self.getGroupItem(), gameState)
    @checkNotNone
    def _getSnakeEventCreator(self):
        return self._SnakeEventCreator


    def createRelatedToSnake(self,speed, thick, skin, control, skinNum = SKIN_DEFAULT, firstHeadDirection = RIGHT, headPos = SCREEN_MID, color = GREEN, length = 1):
        """ create player """
        self._snake = snake.Snake(self.getEventDistributor(), speed, thick, skin, skinNum=skinNum, firstHeadDirection=firstHeadDirection, headPos=headPos, color=color, length=length)
        self._SnakeAction = snakeAction.SnakeAction(self._snake, self.getKeyboardEventHandler(), control)
        self._SnakeDisplayHandler = snakeDisplayHandler.SnakeDisplayHandler(self._snake)

    @checkNotNone
    def _getSnake(self):
        return self._snake
    @checkNotNone
    def _getSnakeAction(self):
        return self._SnakeAction
    @checkNotNone
    def _getSnakeDisplayHandler(self):
        return self._SnakeDisplayHandler



    def createPausePage(self):
        """ create pause page """
        self._PausePage = popUp.PausePage()
    @checkNotNone
    def getPausePage(self):
        return self._PausePage



    def createAppleItemSpawner(self, appleImg, appleSound = None):
        """ create apple item generator """
        if appleSound:
            appleSound.set_volume(1)
        self._ApplePrototype = apple.Apple(appleImg, sound = appleSound)
        self._itemAppleSpawner = item.ItemSpawner(self._ApplePrototype)
    @checkNotNone
    def getItemAppleSpawner(self):
        return self._itemAppleSpawner



    def createLevelHandler(self, gameName, snake = None,ItemSpawners = None):
        """ create game state handler """
        self._LevelHandler = level.LevelHandler(gameName, mSnake = snake, ItemSpawners = ItemSpawners)
    @checkNotNone
    def getLevelHandler(self):
        return self._LevelHandler

    def getPlayers(self):
        return self.players