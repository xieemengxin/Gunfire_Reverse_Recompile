# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_attachctrl.pyc
# RelativePath: clientlogic/cl_attachctrl.pyc
# Source Generated with Decompyle++
# File: cl_attachctrl.pyc (Python 3.6)

from C_component import ComAttach
from cl_only import PY_FLAG_DEAD
import cl_scene
import cl_math

class CAttachCtrl(ComAttach):
    
    def __init__(self, oOwner):
        self.m_Owner = oOwner
        ComAttach.__init__(self, oOwner.m_Game.m_ID, oOwner.m_ID, 'AttachCtrl')

    
    def C_UpdateAttachPos(self, lstAttach):
        oGame = self.m_Owner.m_Game
        for tAttach in lstAttach:
            (mid, tx, ty, tz) = tAttach
            tPos = (tx, ty, tz)
            obj = oGame.GetObject(mid)
            if not obj:
                continue
            obj.m_Pos = tPos
            cl_scene.GS2CMapGoto(obj, tPos)
        

    
    def Release(self):
        pass



class CAttachCtrlTmp(object):
    
    def __init__(self, oOwner):
        self.m_Owner = oOwner
        self.m_Attach = { }
        self.m_LastPos = (0, 0, 0)

    
    def AddAttach(self, iAttach):
        oGame = self.m_Owner.m_Game
        oAttach = oGame.GetObject(iAttach)
        vBind = self.m_Owner.GetPos()
        if not oAttach:
            return None
        if not self.m_Attach:
            self.m_Owner.Call_Out(self.UpdateAttachPos, 1, 'AttachCtrl')
        vAttach = oAttach.GetPos()
        vOffset = cl_math.Vec3Minus(vAttach, vBind)
        self.m_Attach[iAttach] = vOffset

    
    def DelAttach(self, iAttach):
        if iAttach in self.m_Attach:
            self.m_Attach.pop(iAttach)
        if not self.m_Attach:
            self.m_Owner.Remove_Call_Out('AttachCtrl')

    
    def UpdateAttachPos(self):
        oGame = self.m_Owner.m_Game
        vPos = self.m_Owner.RefreshPos()
        if not cl_math.IsEqual(vPos, self.m_LastPos):
            self.m_LastPos = vPos
            for iAttach in list(self.m_Attach):
                oAttach = oGame.GetObject(iAttach, PY_FLAG_DEAD)
                if not oAttach:
                    self.m_Attach.pop(iAttach)
                    continue
                vNew = cl_math.Vec3Add(self.m_Attach[iAttach], vPos)
                oAttach.WalkTo(vNew)
            
        if self.m_Attach:
            self.m_Owner.Call_Out(self.UpdateAttachPos, 1, 'AttachCtrl')


