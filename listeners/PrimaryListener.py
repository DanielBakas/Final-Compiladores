"""
================================================================================
# Proyecto Final de Compiladores
Módulo | `SecondListener.py`

Daniel Bakas Amuchástegui   | A01657103
Santiago Hernández Guerrero | A01027543

Abril 19, 2022
================================================================================
"""


from antlr.coolListener import coolListener
from antlr.coolParser import coolParser

from util.exceptions import *
from util.structure import *


class PrimaryListener(coolListener):

    def __init__(self):
        pass

    def exitBase(self, ctx: coolParser.BaseContext):
        ctx.dataType = ctx.primary().dataType

    def exitFalse(self, ctx: coolParser.FalseContext):
        ctx.dataType = lookupClass('Bool')

    def exitInt(self, ctx: coolParser.IntContext):
        ctx.dataType = lookupClass('Int')

    def exitStr(self, ctx: coolParser.StrContext):
        ctx.dataType = lookupClass('String')

    def exitTrue(self, ctx: coolParser.TrueContext):
        ctx.dataType = lookupClass('Bool')

    # def exitParenthesis(self, ctx: coolParser.ParenthesisContext):
    #     ctx.dataType = ctx.expr().dataType
