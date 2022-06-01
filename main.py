"""
================================================================================
# Proyecto Final de Compiladores
Módulo | `main.py`

Daniel Bakas Amuchástegui   | A01657103
Santiago Hernández Guerrero | A01027543

Abril 19, 2022
================================================================================
"""

from antlr4 import *
from antlr import *
from listeners.OneListener import OneListener
from listeners.TwoListener import TwoListener
from listeners.PrimaryListener import PrimaryListener
from util.structure import setBaseKlasses


def compile(file):

    parser = coolParser(CommonTokenStream(coolLexer(FileStream(file))))
    tree = parser.program()
    setBaseKlasses()
    walker = ParseTreeWalker()
    walker.walk(OneListener(), tree)
    walker.walk(PrimaryListener(), tree)
    walker.walk(TwoListener(), tree)


if __name__ == '__main__':
    compile('resources/semantic/input/badarith.cool')
