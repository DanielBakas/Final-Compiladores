"""
================================================================================
# Proyecto Final de Compiladores
Módulo | `OneListener.py`

Daniel Bakas Amuchástegui   | A01657103
Santiago Hernández Guerrero | A01027543

Abril 19, 2022
================================================================================
"""


from util.exceptions import *
from antlr.coolListener import coolListener
from antlr.coolParser import coolParser


class OneListener(coolListener):

    def __init__(self):
        self.className = str()
        self.hasMain = False
        self.parent = str()

    def enterAttribute(self, ctx: coolParser.AttributeContext):
        if ctx.ID().getText() == 'self':
            raise anattributenamedself()
        if ctx.expr() and ctx.expr().getText() == 'self':
            raise selfassignment()

    def enterLetdecl(self, ctx:coolParser.LetdeclContext):
        if ctx.ID().getText() == 'self':
            raise letself()

    def enterMethod(self, ctx: coolParser.MethodContext):
        for param in ctx.params:
            if param.TYPE().getText() == 'SELF_TYPE':
                raise selftypeparameterposition()
            if param.ID().getText() == 'self':
                raise selfinformalparameter()

    def enterKlass(self, ctx: coolParser.KlassContext):
        self.className = ctx.TYPE(0).getText()
        if ctx.TYPE(1):
            self.parent = ctx.TYPE(1).getText()
        if self.className == 'Main':
            self.hasMain = True

    def exitKlass(self, ctx: coolParser.KlassContext):
        if (not self.hasMain):
            raise nomain()
        elif self.className == 'Int':
            raise badredefineint()
        elif self.className == 'Object':
            raise redefinedobject()
        elif self.className == 'SELF_TYPE':
            raise selftyperedeclared()
        elif self.parent == 'Bool':
            raise inheritsbool()
        elif self.parent == 'String':
            raise inheritsstring()
        elif self.parent == 'SELF_TYPE':
            raise inheritsselftype()
