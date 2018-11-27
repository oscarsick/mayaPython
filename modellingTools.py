import maya.cmds as mc

sel = mc.ls(sl = True)
for each in sel:
    print each
