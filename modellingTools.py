import maya.cmds as mc

#freezing all transform and move pivot to the origin
def freeze2Zero():
    sel = mc.ls(sl = True)
    for each in sel:
        mc.makeIdentity(each, a = True, s = True, t = True, r = True)
        mc.move(0,0,0,each+'.scalePivot',a = True, rpr = True)
        mc.move(0,0,0,each+'.rotatePivot',a = True, rpr = True)
freeze2Zero()

    
