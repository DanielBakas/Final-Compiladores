# Generated from /Users/danielbakas/Documents/Escuela/Tec/Semestre 8/Diseño de Compiladores/Proyecto Final/antlr/cool.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .coolParser import coolParser
else:
    from coolParser import coolParser

# This class defines a complete generic visitor for a parse tree produced by coolParser.

class coolVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by coolParser#program.
    def visitProgram(self, ctx:coolParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#klass.
    def visitKlass(self, ctx:coolParser.KlassContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#method.
    def visitMethod(self, ctx:coolParser.MethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#attribute.
    def visitAttribute(self, ctx:coolParser.AttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#formal.
    def visitFormal(self, ctx:coolParser.FormalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#add.
    def visitAdd(self, ctx:coolParser.AddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#newType.
    def visitNewType(self, ctx:coolParser.NewTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#sub.
    def visitSub(self, ctx:coolParser.SubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#dispatch.
    def visitDispatch(self, ctx:coolParser.DispatchContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#mult.
    def visitMult(self, ctx:coolParser.MultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#lt.
    def visitLt(self, ctx:coolParser.LtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#while.
    def visitWhile(self, ctx:coolParser.WhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#eq.
    def visitEq(self, ctx:coolParser.EqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#lcleetExpr.
    def visitLcleetExpr(self, ctx:coolParser.LcleetExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#div.
    def visitDiv(self, ctx:coolParser.DivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#not.
    def visitNot(self, ctx:coolParser.NotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#staticDispatch.
    def visitStaticDispatch(self, ctx:coolParser.StaticDispatchContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#isVoid.
    def visitIsVoid(self, ctx:coolParser.IsVoidContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#exprDispatch.
    def visitExprDispatch(self, ctx:coolParser.ExprDispatchContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#le.
    def visitLe(self, ctx:coolParser.LeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#block.
    def visitBlock(self, ctx:coolParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#notInt.
    def visitNotInt(self, ctx:coolParser.NotIntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#if.
    def visitIf(self, ctx:coolParser.IfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#case.
    def visitCase(self, ctx:coolParser.CaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#base.
    def visitBase(self, ctx:coolParser.BaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#assign.
    def visitAssign(self, ctx:coolParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#case_stat.
    def visitCase_stat(self, ctx:coolParser.Case_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#let_decl.
    def visitLet_decl(self, ctx:coolParser.Let_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#parenthesis.
    def visitParenthesis(self, ctx:coolParser.ParenthesisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#id.
    def visitId(self, ctx:coolParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#int.
    def visitInt(self, ctx:coolParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#str.
    def visitStr(self, ctx:coolParser.StrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#true.
    def visitTrue(self, ctx:coolParser.TrueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#false.
    def visitFalse(self, ctx:coolParser.FalseContext):
        return self.visitChildren(ctx)



del coolParser