from typing import Type
from antlr import coolListener, coolParser
from util.exceptions import attrbadinit ,attroverride

from antlr.coolListener import coolListener
from antlr.coolParser import coolParser
from util.exceptions import redefinedclass, dupformals, signaturechange, overridingmethod4

from util.structure import *

class ThreeListener(coolListener):
    def __init__(self):
        self.currentClass = None

    def enterKlass(self, ctx: coolParser.KlassContext):
        self.currentClass = ctx.dataType

    def enterAttribute(self, ctx: coolParser.AttributeContext):
        name = ctx.ID().getText()
        type = ctx.TYPE().getText()

        try:
            ctx.currentClass.lookupAttribute(name)
            raise attroverride
        except KeyError:
            ctx.currentClass.addAttribute(name, type)

