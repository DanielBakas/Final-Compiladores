"""
––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Proyecto Final de Compiladores
Módulo | `letselfListener.py`

Daniel Bakas Amuchástegui   | A01657103
Santiago Hernández Guerrero | A01027543

Abril 19, 2022
––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
"""


from util.exceptions import *
from antlr.coolListener import coolListener
from antlr.coolParser import coolParser


class letselfListener(coolListener):

    def __init__(self):
        self.main = False

    def enterKlass(self, ctx: coolParser.KlassContext):
        if ctx.TYPE(0).getText() == 'Self':
            self.main = True

    def exitKlass(self, ctx: coolParser.KlassContext):
        if (not self.main):
            raise letself()