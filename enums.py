from enum import Enum

#class synthax
class Color(Enum):
    RED=1
    GREEN=2
    BLUE=3

#functional
Color=Enum('Color',[('RED',1),('GREEN',2),('BLUE',3)])
# Color.BLUE

print(Color.BLUE)