"""
––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Proyecto Final de Compiladores
Módulo | `anattributenamedselfListener.py`

Daniel Bakas Amuchástegui   | A01657103
Santiago Hernández Guerrero | A01027543

Abril 19, 2022
––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
"""


from util.exceptions import *
from antlr.coolListener import coolListener
from antlr.coolParser import coolParser


class anattributenamedselfListener(coolListener):

    def __init__(self):
        self.isNamedSelf = False

    def enterFeature(self, ctx: coolParser.FeatureContext):
        if ctx.ID().getText() == 'self':
            self.isNamedSelf = True

    def exitFeature(self, ctx: coolParser.FeatureContext):
        if (not self.isNamedSelf):
            raise anattributenamedself()
