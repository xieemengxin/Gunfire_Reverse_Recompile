# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_summon/windsummon.pyc
# RelativePath: clientlogic/cl_summon/windsummon.pyc
# Source Generated with Decompyle++
# File: windsummon.pyc (Python 3.6)

from cl_commondefines import DAM_USE_HP, DAM_TYPE_SCENE
from cl_only import PY_FLAG_DEAD, Functor, PY_FLAG_MONSTERTARGET
import cl_math
import cl_object
import cl_msgcenter
import cl_modeldefine
from . import mobject

class CWindSummon(mobject.CBaseSummon):
    
    def __init__(self, *args):
        super().__init__(*args)
        self.m_DataSID = 1029
        self.SetAttr('ModelRadius', 4, 0)

    
    def StartMove(self, iTarget):
        func = Functor(self.TraceMove, iTarget)
        self.m_MoveCtrl.FollowMove(self, iTarget, 0, func, iPyFlag = PY_FLAG_MONSTERTARGET)

    
    def TraceMove(self, iTarget, oOwner, tPos, iFail):
        if not self.m_Game.GetObject(iTarget, PY_FLAG_MONSTERTARGET):
            iTarget = self.GetNearestPlayer()
            if not iTarget:
                oReason = cl_object.reason.CStrReason('notarget', None, {
                    'DamType': DAM_TYPE_SCENE | DAM_USE_HP })
                self.HPModifyDam(0, [
                    [
                        self.HP(),
                        oReason]])
                return None
        self.m_MoveCtrl.m_ArriveInfo = ()
        self.m_MoveCtrl.m_FollowDeflexion = { }
        self.StartMove(iTarget)

    
    def GetNearestPlayer(self):
        lstLive = self.m_Game.m_WarMgr.GetLiveHero()
        if not lstLive:
            return None
        iRet = None
        fMinDis = 268435455
        vSelf = self.GetPos()
        oOwner = self.GetOwner()
        for iLive in lstLive:
            oHero = self.m_Game.GetObject(iLive, PY_FLAG_MONSTERTARGET)
            if not oHero:
                continue
            vHero = oHero.GetPos()
            if oOwner and oOwner.m_DataSID == 3915:
                (fTargetRadius, _) = cl_modeldefine.GetModelDefine(oHero.m_Shape, 'NavMesh')
                vRet = self.m_Game.Scene_NavMeshRayCast(self.m_Scene, (135, 1.5, 135), (vHero[0], 1.5, vHero[2]))
                if cl_math.CalDistance(vRet, vHero) > 2 * fTargetRadius:
                    continue
                continue
            fDis = cl_math.CalDistance(vSelf, vHero)
            if fDis < fMinDis:
                iRet = iLive
                fMinDis = fDis
        
        return iRet

    
    def Remove(self, sReason):
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_REMOVESUMMON, self, { }, oGame = self.m_Game)
        super(CWindSummon, self).Remove(sReason)

    
    def OnInitAttr(self, clsData, dAddData):
        self.m_Speed = self.QueryAttr('MoveSpeed')


