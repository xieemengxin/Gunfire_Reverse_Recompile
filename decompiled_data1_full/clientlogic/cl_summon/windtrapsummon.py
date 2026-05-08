# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_summon/windtrapsummon.pyc
# RelativePath: clientlogic/cl_summon/windtrapsummon.pyc
# Source Generated with Decompyle++
# File: windtrapsummon.pyc (Python 3.6)

from cl_commondefines import PATHMODE_COLLISIONLESS, CURVE_COMEANDGO
from cl_only import Functor
import cl_math
import cl_msgcenter
from . import mobject

class CWindTrapSummon(mobject.CBaseSummon):
    
    def __init__(self, oGame, nid):
        super().__init__(oGame, nid)
        sAttKey = 'MinSpeed'
        self.SetAttr(sAttKey, 0, 0)
        sAttKey = 'ChangeDistance'
        self.SetAttr(sAttKey, 0, 0)
        sAttKey = 'ModelRadius'
        self.SetAttr('ModelRadius', 0, 0)

    
    def CurveMove(self, iStep, iTpye, oOwner, tPos, iFail):
        lstMovePos = self.Query('MoveInfo', None)
        if iStep == len(lstMovePos) - 1:
            iStep = 0
        else:
            iStep += 1
        self.StartMove(iStep, iTpye)

    
    def StartMove(self, iStep, iTpye):
        lstMovePos = self.Query('MoveInfo', None)
        lstPos = self.Query('InitPos', None)
        vNow = self.GetPos()
        fSpeed = self.MoveSpeed()
        fDistance = self.QueryAttr('ChangeDistance')
        fMinSpeed = self.QueryAttr('MinSpeed') / 100
        if iTpye == CURVE_COMEANDGO:
            if cl_math.CalDistance3D(lstPos[0], vNow) - fDistance < 1e-06:
                fSpeed = self.MoveSpeed() * cl_math.CalDistance3D(lstPos[0], vNow) / fDistance
            elif cl_math.CalDistance3D(lstPos[len(lstPos) - 1], vNow) - fDistance < 1e-06:
                fSpeed = self.MoveSpeed() * cl_math.CalDistance3D(lstPos[len(lstPos) - 1], vNow) / fDistance
            if fSpeed < fMinSpeed:
                fSpeed = fMinSpeed
        func = Functor(self.CurveMove, iStep, iTpye)
        vPos = lstMovePos[iStep]
        self.m_MoveCtrl.AirMove(self, vPos, fSpeed, True, func)

    
    def Remove(self, sReason):
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_REMOVESUMMON, self, { }, oGame = self.m_Game)
        super(CWindTrapSummon, self).Remove(sReason)

    
    def Call_Out_Suspendable(self, func, iDelay, sFlag):
        self.Call_Out(func, iDelay, sFlag)

    
    def Remove_Call_Out_Suspendable(self, sFlag):
        self.Remove_Call_Out(sFlag)


