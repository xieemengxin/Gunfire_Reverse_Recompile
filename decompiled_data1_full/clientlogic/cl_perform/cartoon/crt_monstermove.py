# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/cartoon/crt_monstermove.pyc
# RelativePath: clientlogic/cl_perform/cartoon/crt_monstermove.pyc
# Source Generated with Decompyle++
# File: crt_monstermove.pyc (Python 3.6)

from cl_only import Functor
import cl_math
from .mobject import CBaseCartoon

class MonsterMoveCartoon(CBaseCartoon):
    
    def Trace(cls, oSkill, dCartoon):
        oAttack = oSkill.GetAttack()
        if not oAttack:
            cls.Disable(oSkill, dCartoon)
            return None
        if len(dCartoon['PathLine']) < 2 and cl_math.CheckDistance3D(oAttack.GetPos(), dCartoon['PathLine'][0], 2):
            oSkill.Send(dCartoon['ID'], {
                'Over': 1 })
            cls.Disable(oSkill, dCartoon)
            return None
        cls.StartMove(oAttack, oSkill, dCartoon)

    Trace = classmethod(Trace)
    
    def HitTarget(cls, oSkill, dCartoon):
        return 1

    HitTarget = classmethod(HitTarget)
    
    def InitTraceServer(cls, oSkill, dCartoon, lstPos, speed = 0, iGround = 1):
        dCartoon['PathLine'] = list(lstPos)
        dCartoon['Speed'] = max(0, speed)
        dCartoon['Ground'] = iGround

    InitTraceServer = classmethod(InitTraceServer)
    
    def StartMove(cls, oAttack, oSkill, dCartoon):
        lstPos = dCartoon['PathLine']
        iRet = oAttack.m_MoveCtrl.DirectMove(oAttack, lstPos, dCartoon['Speed'], Functor(PathMoveEnd, oSkill.m_Base['ActNum'], dCartoon['ID']), iGround = dCartoon['Ground'])
        if not iRet:
            oSkill.Halt('monstermovemovefail')
            return None

    StartMove = classmethod(StartMove)
    
    def IsOver(cls, oSkill, dCartoon):
        iNodeID = dCartoon['ID']
        oSkill.Send(iNodeID, {
            'Over': 1 })
        return 1

    IsOver = classmethod(IsOver)


def PathMoveEnd(iActNum, iCartoon, oAttack, tEnd, iFail):
    oGame = oAttack.m_Game
    oSkill = oGame.m_SkillMgr.GetSkill(oAttack.m_ID, iActNum)
    if not oSkill or iCartoon not in oSkill.m_Cartoon:
        return None
    dCartoon = oSkill.m_Cartoon[iCartoon]
    if iFail:
        oSkill.Send(iCartoon, {
            'Over': 1 })
        dCartoon['cls'].Disable(oSkill, dCartoon)
        return None
    oSkill.Update([
        dCartoon['ID']])
    oAttack.m_MoveCtrl.Stop(oAttack)

