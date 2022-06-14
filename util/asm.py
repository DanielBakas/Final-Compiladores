from string import Template

dataHeaderString = """
    .data
    .align  2
    .globl  class_nameTab
    .globl  Main_protObj
    .globl  Int_protObj
    .globl  String_protObj
    .globl  bool_const0
    .globl  bool_const1
    .globl  _int_tag
    .globl  _bool_tag
    .globl  _string_tag
"""

baseClassTagTemplate = Template("""
_int_tag:
    .word   $intTag
_bool_tag:
    .word   $boolTag
_string_tag:
    .word   $stringTag
""")

memoryManagerString = """
    .globl  _MemMgr_INITIALIZER
_MemMgr_INITIALIZER:
    .word   _NoGC_Init
    .globl  _MemMgr_COLLECTOR
_MemMgr_COLLECTOR:
    .word   _NoGC_Collect
    .globl  _MemMgr_TEST
_MemMgr_TEST:
    .word   0
"""

intTemplate = Template("""
    .word   -1
int_const$idx:
    .word   $tag
    .word   4
    .word   Int_dispTab
    .word   $value
""")

emptyStringTemplate = Template("""
    .word   -1
str_const$idx:
    .word   $tag
    .word   5
    .word   String_dispTab
    .word   int_const$sizeIdx
    .byte   0
    .align  2
""")

stringTemplate = Template("""
    .word   -1
str_const$idx:
    .word   $tag
    .word   $size
    .word   String_dispTab
    .word   int_const$sizeIdx
    .ascii  "$value"
    .byte   0
    .align  $align
""")

nameTabHeaderString = """
class_nameTab:"""

nameTabRowTemplate = Template("""
    .word   str_const$idx""")

objectTableHeaderString = """
class_objTab:"""

objectTableRowTemplate = Template("""
    .word   ${name}_protObj
    .word   ${name}_init""")

dispatchTableHeaderTemplate = Template("""
${objectname}_dispTab:""")

dispatchTableRowTemplate = Template("""
    .word   ${objectname}.${methodname}""")

protoObjectTableHeaderTemplate = Template("""
    .word   -1
${objectname}_protObj:""")

protoObjectTableTemplate = Template("""
    .word   $classCounter
    .word   $numberofRows
    .word   ${objname}_dispTab""")

wordTemplate = Template("""
    .word   $content
""")

boolString = """
    .word   -1
bool_const0:
    .word   3
    .word   4
    .word   Bool_dispTab
    .word   0
    .word   -1
bool_const1:
    .word   3
    .word   4
    .word   Bool_dispTab
    .word   1
"""

heapString = """
   .globl  heap_start 
heap_start:
    .word   0 
"""

textString = """
    .text    
    .globl  Main_init 
    .globl  Int_init 
    .globl  String_init 
    .globl  Bool_init 
    .globl  Main.main 
"""
