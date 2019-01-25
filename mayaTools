import maya.cmds as mc


old_v = '009'
v = '010'

sel = mc.ls(sl = True)
for each in sel:
    x = mc.getAttr(each+'.fileTextureName')
    new_x = x.replace(old_v,v)
    mc.setAttr(each+'.fileTextureName',new_x,typ = 'string')
    
    
    


