"""
================================================================================
# Proyecto Final de Compiladores
Módulo | `HierarchyListener.py`

Construye el arbol de clases. Establece las relaciones de herencia entre las clases.

Daniel Bakas Amuchástegui   | A01657103
Santiago Hernández Guerrero | A01027543

Abril 19, 2022
================================================================================
"""

from antlr.coolListener import coolListener
from antlr.coolParser import coolParser
from util.exceptions import redefinedclass, dupformals, signaturechange, overridingmethod4

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

    def exitMethod(self, ctx: coolParser.MethodContext):
        parsedparams = None
        if ctx.params:
            parsedparams = set()
            seen_param_names = set()
            for param in ctx.params:
                if type(param) == coolParser.FormalContext:
                    if param.ID().getText() in seen_param_names:
                        raise dupformals()
                    parsed = frozenset(
                        [param.TYPE().getText(), param.ID().getText()])
                    seen_param_names.add(param.ID().getText())
                    parsedparams.add(parsed)
        try:
            method = Method(ctx.TYPE(), parsedparams)
            overridenmethod = self.currentKlass.lookupMethod(
                ctx.ID().getText())
            if len(method.params) != len(overridenmethod.params):
                raise signaturechange()
        except KeyError:
            pass
        try:
            overridenmethod = self.currentKlass.lookupMethod(
                ctx.ID().getText())
            if method.params.values() != overridenmethod.params.values():
                raise overridingmethod4()
        except KeyError:
            pass
        self.currentKlass.addMethod(ctx.ID().getText(), method)

    def exitAttribute(self, ctx: coolParser.AttributeContext):
        ctx.ID().dataType = lookupClass(ctx.TYPE().getText())

    def exitBase(self, ctx: coolParser.BaseContext):
        if type(ctx.primary()) != coolParser.IdContext and \
                not type(ctx.primary()) is coolParser.ParenthesisContext:
            ctx.dataType = ctx.primary().dataType

    def exitFalse(self, ctx: coolParser.FalseContext):
        ctx.dataType = lookupClass('Bool')

    def exitInt(self, ctx: coolParser.IntContext):
        ctx.dataType = lookupClass('Int')

    def exitStr(self, ctx: coolParser.StrContext):
        ctx.dataType = lookupClass('String')

    def exitTrue(self, ctx: coolParser.TrueContext):
        ctx.dataType = lookupClass('Bool')
