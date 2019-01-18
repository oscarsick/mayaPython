import maya.cmds as mc

#freezing all transform and move pivot to the origin
def freeze2Zero():
    sel = mc.ls(sl = True)
    for each in sel:
        mc.makeIdentity(each, a = True, s = True, t = True, r = True)
        mc.move(0,0,0,each+'.scalePivot',a = True, rpr = True)
        mc.move(0,0,0,each+'.rotatePivot',a = True, rpr = True)
freeze2Zero()

#mel #copied online, togglewireframeOnShade
string $apapap = `getPanel -wf`;
modelEditor -e -wos(!`modelEditor -q -wos $ap`) $apapap;
#mel


import maya.cmds as mc
def os_mergeGroups():
    sel = mc.ls(sl = True)
    for each in sel:
        c = mc.listRelatives(each,c = True, ad = True, type = 'transform')
        geoArr = []
        for child in c:
            if '_geo' in child:
                geoArr.append(child)
        
        print each+' : '+str(len(geoArr)) + ' geos combined.'
        if len(geoArr) == 1:
            mc.parent(geoArr[0], w=True)
        else:
            mc.polyUnite (each, ch = 0, mergeUVSets = 1, centerPivot = True, name = each)
            
