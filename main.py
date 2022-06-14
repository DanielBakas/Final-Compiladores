"""
================================================================================
# Proyecto Final de Compiladores
Módulo | `main.py`

Daniel Bakas Amuchástegui   | A01657103
Santiago Hernández Guerrero | A01027543

Abril 19, 2022
================================================================================
"""

from antlr import *
from listeners.HierarchyListener import HierarchyListener
from listeners.OneListener import OneListener
from listeners.ProgramWriter import ProgramWriter
from listeners.ThreeListener import ThreeListener
from listeners.TreePrinter import TreePrinter
from listeners.TwoListener import TwoListener
from util.structure import setBaseKlasses


def compile(file):
    parser = coolParser(CommonTokenStream(coolLexer(FileStream(file))))
    tree = parser.program()
    setBaseKlasses()
    walker = ParseTreeWalker()
    walker.walk(OneListener(), tree)
    walker.walk(HierarchyListener(), tree)
    walker.walk(TwoListener(), tree)
    walker.walk(ThreeListener(), tree)
    walker.walk(TreePrinter(), tree)
    walker.walk(ProgramWriter(), tree)


if __name__ == '__main__':
    compile('resources/semantic/input/simplecase.cool')
