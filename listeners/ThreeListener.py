from antlr import coolListener, coolParser
from util.exceptions import attrbadinit


class ThreeListener(coolListener):
    def __init__(self):
        self.currentClass = None

    def enterKlass(self, ctx: coolParser.KlassContext):
        self.currentClass = ctx.dataType

