from math import ceil

from antlr import coolListener, coolParser
from util.asm import *
from util.structure import getAllClasses


class ProgramWriter(coolListener):

    def __init__(self):
        self.output = ""

        self.intnum = 2
        self.strNum = 4
        self.boolnum = 3

        self.intPieces = set()
        self.strPieces = set()
        self.intIndexes = {}
        self.strIndexes = {}

        self.strings = []
        self.ints = []

    def enterInt(self, ctx: coolParser.IntContext):
        self.ints += ctx.INTEGER().getText()

    def enterStr(self, ctx: coolParser.StrContext):
        self.strings += ctx.STRING().getText()

    def exitProgram(self, ctx: coolParser.ProgramContext):
        # Add integers
        for integer in self.ints:
            self.addInt(integer)
        # Add strings
        for str in self.strings:
            self.addString(str)

        # nameTable
        ntpiece = nameTabHeaderString
        base = ['Object', 'IO', 'Int', 'Bool', 'String']
        for klass in base:
            self.addString(klass)
            ntpiece += nameTabRowTemplate.substitute(idx=self.strIndexes[klass])
        for klass in getAllClasses().keys():
            if klass in base:
                continue
            self.addString(klass)
            ntpiece += nameTabRowTemplate.substitute(idx=self.strIndexes[klass])
        self.output += ntpiece

        # Obj table
        obj = objectTableHeaderString
        for klass in getAllClasses():
            obj += objectTableRowTemplate.substitute(name=klass)
        self.output += obj

        # dispatch table
        for klassInstance in getAllClasses().values():
            fragment = dispatchTableHeaderTemplate.substitute(objectname=klassInstance.name)
            for obj, methods in klassInstance.getAllMethods().items():
                for method in list(methods):
                    fragment += dispatchTableRowTemplate.substitute(objectname=obj, methodname=method)
            self.output += fragment

        # proto objects
        counter = 0
        for klass in getAllClasses().values():
            self.output += protoObjectTableHeaderTemplate.substitute(objectname=klass.name)
            attrbus = []
            if klass.getAllAttributes():
                for attr in klass.getAllAttributes().keys():
                    attrbus += wordTemplate.substitute(content=2)
            self.output += protoObjectTableTemplate.substitute(classCounter=counter,
                                                               numberofRows=len(attrbus) + 3,
                                                               objname=klass.name)
            for a in attrbus:
                self.output += a
            counter += 1

        temp = self.output
        self.output = dataHeaderString + baseClassTagTemplate.substitute(intTag=self.intnum, boolTag=self.boolnum,
                                                                         stringTag=self.strNum) + memoryManagerString
        for s in self.intPieces:
            self.output += s

        for s in self.strPieces:
            self.output += s

        self.output += temp
        # Finishing strings
        self.output += boolString + heapString + textString

        # Writeout
        with open("out.s", "w") as file1:
            file1.write(self.output.replace("\n\n", "\n"))

    def addString(self, s: str):
        if s in self.strIndexes:
            return
        if s == "":
            if 0 not in self.intIndexes:
                self.addInt(0)
            self.strPieces.add(
                emptyStringTemplate.substitute(tag=self.strNum, idx=len(self.strIndexes),
                                               sizeIdx=self.intIndexes[0]))
        else:
            if len(s) not in self.intIndexes:
                self.addInt(len(s))
                strintindex = self.intIndexes[len(s)]
                size = ceil(4 + ((len(s) + 1) / 4))
                align = 0
                if not len(s) + 1 % 4 == 0:
                    n = len(s) + 1
                    align = (n + 4 - 1) // 4 * 4 - 1 - len(s) - 1
                self.strPieces.add(
                    stringTemplate.substitute(tag=self.strNum, idx=len(self.strIndexes), size=size, value=s,
                                              align=align,
                                              sizeIdx=strintindex))
        self.strIndexes[s] = len(self.strIndexes)

    def addInt(self, number):
        if number in self.intIndexes:
            return
        intstr = intTemplate.substitute(idx=len(self.intIndexes), tag=self.intnum, value=number)
        self.intIndexes[number] = len(self.intPieces)
        self.intPieces.add(intstr)
