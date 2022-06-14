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
from util.exceptions import redefinedclass

from util.structure import *


class HierarchyListener(coolListener):

    def __init__(self):
        self.currentKlass = None

    def enterKlass(self, ctx: coolParser.KlassContext):
        mainType = ctx.TYPE(0).getText()
        inheritance = None
        if ctx.TYPE(1):
            inheritance = ctx.TYPE(1).getText()

        if mainType in getAllClasses():
            raise redefinedclass()

        if ctx.TYPE(1) is not None:
            klass = Klass(mainType, inheritance)
        else:
            klass = Klass(mainType)
        ctx.dataType = klass
        self.currentKlass = klass

    def exitAttribute(self, ctx: coolParser.AttributeContext):
        ctx.ID().dataType = lookupClass(ctx.TYPE().getText())

    def exitBase(self, ctx: coolParser.BaseContext):
        if type(ctx.primary()) != coolParser.IdContext and \
                not type(ctx.primary()) is coolParser.SubContext:
            ctx.dataType = ctx.primary().dataType

    def exitFalse(self, ctx: coolParser.FalseContext):
        ctx.dataType = lookupClass('Bool')

    def exitInt(self, ctx: coolParser.IntContext):
        ctx.dataType = lookupClass('Int')

    def exitStr(self, ctx: coolParser.StrContext):
        ctx.dataType = lookupClass('String')

    def exitTrue(self, ctx: coolParser.TrueContext):
        ctx.dataType = lookupClass('Bool')
