"""
================================================================================
# Proyecto Final de Compiladores
Módulo | `TwoListener.py`

Daniel Bakas Amuchástegui   | A01657103
Santiago Hernández Guerrero | A01027543

Abril 19, 2022
================================================================================
"""

from antlr.coolListener import coolListener
from antlr.coolParser import coolParser

from util.exceptions import *
from util.structure import *


class TwoListener(coolListener):

    def __init__(self):
        pass

    def exitAdd(self, ctx: coolParser.AddContext):
        left = ctx.expr(0).dataType.name
        right = ctx.expr(1).dataType.name
        if left != 'Int' or right != 'Int':
            raise badarith()
