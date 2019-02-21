import maya.cmds as mc

#simple version up texture files
old_v = '009'
v = '010'

sel = mc.ls(sl = True)
for each in sel:
    x = mc.getAttr(each+'.fileTextureName')
    new_x = x.replace(old_v,v)
    mc.setAttr(each+'.fileTextureName',new_x,typ = 'string')
    
 
import maya.cmds as mc

def os_mergeGroups():
    sel = mc.ls(sl = True)
    for each in sel:
        c = mc.listRelatives(each,c = True, ad = True, type = 'transform')
        geoArr = []
        for child in c:
            if '_geo' in child:
                geoArr.append(child)
        
        print each+' : '+str(len(geoArr))
        if len(geoArr) == 1:
            mc.parent(geoArr[0], w=True)
        else:
            mc.polyUnite (each, ch = 0, mergeUVSets = 1, centerPivot = True, name = each)

os_mergeGroups()
    


