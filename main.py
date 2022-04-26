"""
––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Proyecto Final de Compiladores
Módulo | `main.py`

Daniel Bakas Amuchástegui   | A01657103
Santiago Hernández Guerrero | A01027543

Abril 19, 2022
––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
"""

from antlr4 import *
from antlr import *
from listeners import *


def compile(file):
    parser = coolParser(CommonTokenStream(coolLexer(FileStream(file))))
    tree = parser.program()
    walker = ParseTreeWalker()
    walker.walk(nomainListener(), tree)


if __name__ == '__main__':
    compile('semantic/input/anattributenamedself.cool')
