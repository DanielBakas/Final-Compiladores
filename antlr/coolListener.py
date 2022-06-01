# Generated from /Users/danielbakas/Documents/Escuela/Tec/Semestre 8/Diseño de Compiladores/Proyecto Final/antlr/cool.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .coolParser import coolParser
else:
    from coolParser import coolParser

# This class defines a complete listener for a parse tree produced by coolParser.
class coolListener(ParseTreeListener):

    # Enter a parse tree produced by coolParser#program.
    def enterProgram(self, ctx:coolParser.ProgramContext):
        pass

    # Exit a parse tree produced by coolParser#program.
    def exitProgram(self, ctx:coolParser.ProgramContext):
        pass


    # Enter a parse tree produced by coolParser#klass.
    def enterKlass(self, ctx:coolParser.KlassContext):
        pass

    # Exit a parse tree produced by coolParser#klass.
    def exitKlass(self, ctx:coolParser.KlassContext):
        pass


    # Enter a parse tree produced by coolParser#method.
    def enterMethod(self, ctx:coolParser.MethodContext):
        pass

    # Exit a parse tree produced by coolParser#method.
    def exitMethod(self, ctx:coolParser.MethodContext):
        pass


    # Enter a parse tree produced by coolParser#attribute.
    def enterAttribute(self, ctx:coolParser.AttributeContext):
        pass

    # Exit a parse tree produced by coolParser#attribute.
    def exitAttribute(self, ctx:coolParser.AttributeContext):
        pass


    # Enter a parse tree produced by coolParser#formal.
    def enterFormal(self, ctx:coolParser.FormalContext):
        pass

    # Exit a parse tree produced by coolParser#formal.
    def exitFormal(self, ctx:coolParser.FormalContext):
        pass


    # Enter a parse tree produced by coolParser#add.
    def enterAdd(self, ctx:coolParser.AddContext):
        pass

    # Exit a parse tree produced by coolParser#add.
    def exitAdd(self, ctx:coolParser.AddContext):
        pass


    # Enter a parse tree produced by coolParser#newType.
    def enterNewType(self, ctx:coolParser.NewTypeContext):
        pass

    # Exit a parse tree produced by coolParser#newType.
    def exitNewType(self, ctx:coolParser.NewTypeContext):
        pass


    # Enter a parse tree produced by coolParser#sub.
    def enterSub(self, ctx:coolParser.SubContext):
        pass

    # Exit a parse tree produced by coolParser#sub.
    def exitSub(self, ctx:coolParser.SubContext):
        pass


    # Enter a parse tree produced by coolParser#dispatch.
    def enterDispatch(self, ctx:coolParser.DispatchContext):
        pass

    # Exit a parse tree produced by coolParser#dispatch.
    def exitDispatch(self, ctx:coolParser.DispatchContext):
        pass


    # Enter a parse tree produced by coolParser#mult.
    def enterMult(self, ctx:coolParser.MultContext):
        pass

    # Exit a parse tree produced by coolParser#mult.
    def exitMult(self, ctx:coolParser.MultContext):
        pass


    # Enter a parse tree produced by coolParser#lt.
    def enterLt(self, ctx:coolParser.LtContext):
        pass

    # Exit a parse tree produced by coolParser#lt.
    def exitLt(self, ctx:coolParser.LtContext):
        pass


    # Enter a parse tree produced by coolParser#while.
    def enterWhile(self, ctx:coolParser.WhileContext):
        pass

    # Exit a parse tree produced by coolParser#while.
    def exitWhile(self, ctx:coolParser.WhileContext):
        pass


    # Enter a parse tree produced by coolParser#eq.
    def enterEq(self, ctx:coolParser.EqContext):
        pass

    # Exit a parse tree produced by coolParser#eq.
    def exitEq(self, ctx:coolParser.EqContext):
        pass


    # Enter a parse tree produced by coolParser#lcleetExpr.
    def enterLcleetExpr(self, ctx:coolParser.LcleetExprContext):
        pass

    # Exit a parse tree produced by coolParser#lcleetExpr.
    def exitLcleetExpr(self, ctx:coolParser.LcleetExprContext):
        pass


    # Enter a parse tree produced by coolParser#div.
    def enterDiv(self, ctx:coolParser.DivContext):
        pass

    # Exit a parse tree produced by coolParser#div.
    def exitDiv(self, ctx:coolParser.DivContext):
        pass


    # Enter a parse tree produced by coolParser#not.
    def enterNot(self, ctx:coolParser.NotContext):
        pass

    # Exit a parse tree produced by coolParser#not.
    def exitNot(self, ctx:coolParser.NotContext):
        pass


    # Enter a parse tree produced by coolParser#staticDispatch.
    def enterStaticDispatch(self, ctx:coolParser.StaticDispatchContext):
        pass

    # Exit a parse tree produced by coolParser#staticDispatch.
    def exitStaticDispatch(self, ctx:coolParser.StaticDispatchContext):
        pass


    # Enter a parse tree produced by coolParser#isVoid.
    def enterIsVoid(self, ctx:coolParser.IsVoidContext):
        pass

    # Exit a parse tree produced by coolParser#isVoid.
    def exitIsVoid(self, ctx:coolParser.IsVoidContext):
        pass


    # Enter a parse tree produced by coolParser#exprDispatch.
    def enterExprDispatch(self, ctx:coolParser.ExprDispatchContext):
        pass

    # Exit a parse tree produced by coolParser#exprDispatch.
    def exitExprDispatch(self, ctx:coolParser.ExprDispatchContext):
        pass


    # Enter a parse tree produced by coolParser#le.
    def enterLe(self, ctx:coolParser.LeContext):
        pass

    # Exit a parse tree produced by coolParser#le.
    def exitLe(self, ctx:coolParser.LeContext):
        pass


    # Enter a parse tree produced by coolParser#block.
    def enterBlock(self, ctx:coolParser.BlockContext):
        pass

    # Exit a parse tree produced by coolParser#block.
    def exitBlock(self, ctx:coolParser.BlockContext):
        pass


    # Enter a parse tree produced by coolParser#notInt.
    def enterNotInt(self, ctx:coolParser.NotIntContext):
        pass

    # Exit a parse tree produced by coolParser#notInt.
    def exitNotInt(self, ctx:coolParser.NotIntContext):
        pass


    # Enter a parse tree produced by coolParser#if.
    def enterIf(self, ctx:coolParser.IfContext):
        pass

    # Exit a parse tree produced by coolParser#if.
    def exitIf(self, ctx:coolParser.IfContext):
        pass


    # Enter a parse tree produced by coolParser#case.
    def enterCase(self, ctx:coolParser.CaseContext):
        pass

    # Exit a parse tree produced by coolParser#case.
    def exitCase(self, ctx:coolParser.CaseContext):
        pass


    # Enter a parse tree produced by coolParser#base.
    def enterBase(self, ctx:coolParser.BaseContext):
        pass

    # Exit a parse tree produced by coolParser#base.
    def exitBase(self, ctx:coolParser.BaseContext):
        pass


    # Enter a parse tree produced by coolParser#assign.
    def enterAssign(self, ctx:coolParser.AssignContext):
        pass

    # Exit a parse tree produced by coolParser#assign.
    def exitAssign(self, ctx:coolParser.AssignContext):
        pass


    # Enter a parse tree produced by coolParser#case_stat.
    def enterCase_stat(self, ctx:coolParser.Case_statContext):
        pass

    # Exit a parse tree produced by coolParser#case_stat.
    def exitCase_stat(self, ctx:coolParser.Case_statContext):
        pass


    # Enter a parse tree produced by coolParser#let_decl.
    def enterLet_decl(self, ctx:coolParser.Let_declContext):
        pass

    # Exit a parse tree produced by coolParser#let_decl.
    def exitLet_decl(self, ctx:coolParser.Let_declContext):
        pass


    # Enter a parse tree produced by coolParser#parenthesis.
    def enterParenthesis(self, ctx:coolParser.ParenthesisContext):
        pass

    # Exit a parse tree produced by coolParser#parenthesis.
    def exitParenthesis(self, ctx:coolParser.ParenthesisContext):
        pass


    # Enter a parse tree produced by coolParser#id.
    def enterId(self, ctx:coolParser.IdContext):
        pass

    # Exit a parse tree produced by coolParser#id.
    def exitId(self, ctx:coolParser.IdContext):
        pass


    # Enter a parse tree produced by coolParser#int.
    def enterInt(self, ctx:coolParser.IntContext):
        pass

    # Exit a parse tree produced by coolParser#int.
    def exitInt(self, ctx:coolParser.IntContext):
        pass


    # Enter a parse tree produced by coolParser#str.
    def enterStr(self, ctx:coolParser.StrContext):
        pass

    # Exit a parse tree produced by coolParser#str.
    def exitStr(self, ctx:coolParser.StrContext):
        pass


    # Enter a parse tree produced by coolParser#true.
    def enterTrue(self, ctx:coolParser.TrueContext):
        pass

    # Exit a parse tree produced by coolParser#true.
    def exitTrue(self, ctx:coolParser.TrueContext):
        pass


    # Enter a parse tree produced by coolParser#false.
    def enterFalse(self, ctx:coolParser.FalseContext):
        pass

    # Exit a parse tree produced by coolParser#false.
    def exitFalse(self, ctx:coolParser.FalseContext):
        pass



del coolParser