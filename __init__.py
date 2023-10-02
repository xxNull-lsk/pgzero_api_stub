from pgzero import music
from pgzero import screen as pgzero_screen
from pgzero.actor import Actor as pgzero_Actor
from pgzero.clock import clock
from pygame import display
from pgzero.rect import ZRect as rect

WIDTH = 800
HEIGHT = 600

screen = pgzero_screen.Screen(display.set_mode((WIDTH, HEIGHT), 0))

class Actor(pgzero_Actor):
    def colliderect(slef, obj) -> bool:
        pass


class Keyboard():
    def __init__(self, *args, **kwargs):
        self.backspace = False
        self.tab = False
        self.clear = False
        self.pause = False
        self.escape = False
        self.up = False
        self.down = False
        self.left = False
        self.right = False
        self.space = False
        self.f1 = False
        self.f2 = False
        self.f3 = False
        self.f4 = False
        self.f5 = False
        self.f6 = False
        self.f7 = False
        self.f8 = False
        self.f9 = False
        self.f10 = False
        self.f11 = False
        self.f12 = False
        self.f13 = False
        self.f14 = False
        self.f15 = False


class Keys():
    def __init__(self, *args, **kwargs):
        self.BACKSPACE=0
        self.TAB=0
        self.CLEAR=0
        self.RETURN=0
        self.PAUSE=0
        self.ESCAPE=0
        self.SPACE=0
        self.EXCLAIM=0
        self.QUOTEDBL=0
        self.HASH=0
        self.DOLLAR=0
        self.AMPERSAND=0
        self.QUOTE=0
        self.LEFTPAREN=0
        self.RIGHTPAREN=0
        self.ASTERISK=0
        self.PLUS=0
        self.COMMA=0
        self.MINUS=0
        self.PERIOD=0
        self.SLASH=0
        self.K_0=0
        self.K_1=0
        self.K_2=0
        self.K_3=0
        self.K_4=0
        self.K_5=0
        self.K_6=0
        self.K_7=0
        self.K_8=0
        self.K_9=0
        self.COLON=0
        self.SEMICOLON=0
        self.LESS=0
        self.EQUALS=0
        self.GREATER=0
        self.QUESTION=0
        self.AT=0
        self.LEFTBRACKET=0
        self.BACKSLASH=0
        self.RIGHTBRACKET=0
        self.CARET=0
        self.UNDERSCORE=0
        self.BACKQUOTE=0
        self.A=0
        self.B=0
        self.C=0
        self.D=0
        self.E=0
        self.F=0
        self.G=0
        self.H=0
        self.I=0
        self.J=0
        self.K=0
        self.L=0
        self.M=0
        self.N=0
        self.O=0
        self.P=0
        self.Q=0
        self.R=0
        self.S=0
        self.T=0
        self.U=0
        self.V=0
        self.W=0
        self.X=0
        self.Y=0
        self.Z=0
        self.DELETE=0
        self.KP0=0
        self.KP1=0
        self.KP2=0
        self.KP3=0
        self.KP4=0
        self.KP5=0
        self.KP6=0
        self.KP7=0
        self.KP8=0
        self.KP9=0
        self.KP_PERIOD=0
        self.KP_DIVIDE=0
        self.KP_MULTIPLY=0
        self.KP_MINUS=0
        self.KP_PLUS=0
        self.KP_ENTER=0
        self.KP_EQUALS=0
        self.UP=0
        self.DOWN=0
        self.RIGHT=0
        self.LEFT=0
        self.INSERT=0
        self.HOME=0
        self.END=0
        self.PAGEUP=0
        self.PAGEDOWN=0
        self.F1=0
        self.F2=0
        self.F3=0
        self.F4=0
        self.F5=0
        self.F6=0
        self.F7=0
        self.F8=0
        self.F9=0
        self.F10=0
        self.F11=0
        self.F12=0
        self.F13=0
        self.F14=0
        self.F15=0
        self.NUMLOCK=0
        self.CAPSLOCK=0
        self.SCROLLOCK=0
        self.RSHIFT=0
        self.LSHIFT=0
        self.RCTRL=0
        self.LCTRL=0
        self.RALT=0
        self.LALT=0
        self.RMETA=0
        self.LMETA=0
        self.LSUPER=0
        self.RSUPER=0
        self.MODE=0
        self.HELP=0
        self.PRINT=0
        self.SYSREQ=0
        self.BREAK=0
        self.MENU=0
        self.POWER=0
        self.EURO=0
        self.LAST=0
        
class Mouse:
    def __init__(self, *args, **kwargs):
        self.LEFT = 0
        self.MIDDLE = 0
        self.RIGHT = 0
        self.WHEEL_UP = 0
        self.WHEEL_DOWN = 0

keys = Keys()
mouse = Mouse()

def animate(object, tween='linear', duration=1, on_finished=None,
                 **targets):
    pass

keyboard = Keyboard()
__all__ = [
    'Actor',
    'clock',
    'keyboard',
    'music',
    'screen',
    'WIDTH',
    'HEIGHT',
    'rect',
    'keys',
    'mouse',
    'animate'
]

__version__ = '0.0.2'
