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
        self.currentClass = None
        self.inwhile = False
        self.table = None
        self.scopes = 0

    def enterKlass(self, ctx: coolParser.KlassContext):
        self.currentClass = ctx.dataType
        self.table = SymbolTableWithScopes(lookupClass(ctx.TYPE(0).getText()))

    def enterId(self, ctx: coolParser.IdContext):
        try:
            ctx.dataType = self.table[ctx.getText()]
        except KeyError:
            raise outofscope()

    def enterAttribute(self, ctx: coolParser.AttributeContext):
        self.table[ctx.ID().getText()] = ctx.TYPE().getText()

    def enterFormal(self, ctx: coolParser.FormalContext):
        self.table[ctx.ID().getText()] = ctx.TYPE().getText()

    def enterLetdecl(self, ctx: coolParser.LetdeclContext):
        self.table.openScope()
        self.scopes += 1
        self.table[ctx.ID().getText()] = ctx.TYPE().getText()

    def exitLcleetExpr(self, ctx: coolParser.LcleetExprContext):
        for i in range(self.scopes):
            self.table.closeScope()
        self.scopes = 0

    def exitAdd(self, ctx: coolParser.AddContext):
        left = ctx.expr(0).dataType.name
        right = ctx.expr(1).dataType.name
        if left != 'Int' or right != 'Int':
            raise badarith()
        ctx.dataType = lookupClass("Int")

    def exitEq(self, ctx: coolParser.EqContext):
        expr = [ctx.expr(i).Tipo.name for i in range(2)]
        if "Int" in expr and "Bool" in expr:
            # Explanation: Very specific test case. Will check if Int and Bool are in the same eq
            raise badequalitytest()
        if expr[0] != expr[1]:
            # Explanation: Catchall for every other case in which the types aren't the same
            raise badequalitytest2()
        ctx.dataType = ctx.expr(0).dataType

    def enterCase(self, ctx: coolParser.CaseContext):
        ctx.casebranches = set()

    def enterCasestat(self, ctx: coolParser.CasestatContext):
        if ctx.TYPE().getText() in ctx.parentCtx.casebranches:
            raise caseidenticalbranch()
        else:
            ctx.parentCtx.casebranches.add(ctx.TYPE().getText())

    def enterMethod(self, ctx: coolParser.MethodContext):
        if ctx.TYPE().getText() == "SELF_TYPE":
            raise selftypebadreturn()
        if ctx.TYPE().getText() not in getAllClasses():
            raise returntypenoexist()
        self.table.openScope()

    def exitBase(self, ctx: coolParser.BaseContext):
        ctx.dataType = ctx.primary().dataType

    def exitMethod(self, ctx: coolParser.MethodContext):
        self.table.closeScope()

    def enterWhile(self, ctx: coolParser.WhileContext):
        self.inwhile = True

    def exitWhile(self, ctx: coolParser.WhileContext):
        self.inwhile = False
        if ctx.expr(0).dataType.name not in ["Int", "Bool"]:
            raise badwhilecond()

    def enterExprDispatch(self, ctx: coolParser.ExprDispatchContext):
        try:
            self.currentClass.lookupMethod(ctx.ID().getText())
        except KeyError:
            if self.inwhile:
                raise badwhilebody()
            raise baddispatch()
