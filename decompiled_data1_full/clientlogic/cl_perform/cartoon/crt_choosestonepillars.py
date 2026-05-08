# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/cartoon/crt_choosestonepillars.pyc
# RelativePath: clientlogic/cl_perform/cartoon/crt_choosestonepillars.pyc
# Source Generated with Decompyle++
# File: crt_choosestonepillars.pyc (Python 3.6)

from cl_only import Time2Frame, PY_FLAG_DEAD
from cl_commondefines import WARRIOR_STONEPILLAR
import cl_math
from .mobject import CBaseCartoon

class ChooseStonePillarsCartoon(CBaseCartoon):
    
    def InitTraceClient(cls, oSkill, dCartoon, waitTime, triggerSection):
        dCartoon['WaitFrame'] = Time2Frame(waitTime)
        dCartoon['CurSec'] = 0
        dCartoon['TriggerSec'] = max(triggerSection, 1)

    InitTraceClient = classmethod(InitTraceClient)
    
    def InitTraceServer(cls, oSkill, dCartoon, waitTime, triggerSection):
        dCartoon['WaitFrame'] = Time2Frame(waitTime)
        dCartoon['CurSec'] = 0
        dCartoon['TriggerSec'] = max(triggerSection, 1)

    InitTraceServer = classmethod(InitTraceServer)
    
    def Trace(cls, oSkill, dCartoon):
        oSkill.Call_Out(dCartoon['WaitFrame'], dCartoon['ID'])

    Trace = classmethod(Trace)
    
    def HitTargetServer(cls, oSkill, dCartoon):
        if dCartoon['StartFrame'] + dCartoon['WaitFrame'] * (dCartoon['CurSec'] + 1) <= oSkill.m_Game.GetFrameNum():
            lstVictim = cls.GetStonePillarPosLst(oSkill, dCartoon)
            oSkill.m_Update['LastVLST'] = lstVictim
            dNet = {
                'LastVLST': lstVictim }
            oSkill.Send(dCartoon['ID'], dNet)
            return 1
        return 0

    HitTargetServer = classmethod(HitTargetServer)
    
    def OnArrive(cls, oSkill, dCartoon):
        dCartoon['CurSec'] += 1
        cls.Trigger(oSkill)
        oSkill.Send(dCartoon['ID'], {
            'Trigger': 1 })

    OnArrive = classmethod(OnArrive)
    
    def IsOver(cls, oSkill, dCartoon):
        iOver = 0
        if dCartoon['TriggerSec'] <= dCartoon['CurSec']:
            iOver = 1
        if iOver:
            oSkill.Send(dCartoon['ID'], {
                'Over': 1 })
            return 1
        return 0

    IsOver = classmethod(IsOver)
    
    def Restart(cls, oSkill, dCartoon):
        oSkill.Call_Out(dCartoon['WaitFrame'], dCartoon['ID'])

    Restart = classmethod(Restart)
    
    def GetStonePillarPosLst(cls, oSkill, dCartoon):
        oGame = oSkill.m_Game
        iScene = oSkill.m_Base['Scene']
        oScene = oGame.m_SceneMgr.GetScene(iScene)
        if not oScene:
            return []
        iAttack = oSkill.m_Base['AID']
        oAttack = oSkill.m_Game.GetObject(iAttack, PY_FLAG_DEAD)
        if not oAttack:
            return []
        vOrigin = oAttack.GetPos()
        if 'Furthest' not in dCartoon:
            lstTrap = oScene.GetObjectsByType('StonePillar')
            lstStone = []
            for iTrap in lstTrap:
                oTrap = oGame.GetObject(iTrap, PY_FLAG_DEAD)
                if not oTrap or oTrap.m_FightType != WARRIOR_STONEPILLAR:
                    continue
                lstStone.append(oTrap)
            
            fMax = 0
            for oStone in lstStone:
                vDest = oStone.GetPos()
                fDis = cl_math.CalDistance3D(vOrigin, vDest)
                fMax = max(fMax, fDis)
            
            dCartoon['StoneLst'] = lstStone
            dCartoon['Furthest'] = fMax
        index = dCartoon['CurSec']
        maxsec = dCartoon['TriggerSec']
        fMaxDis = dCartoon['Furthest']
        lstStone = dCartoon['StoneLst']
        fLeft = fMaxDis * index / maxsec
        fRight = fMaxDis * (index + 1) / maxsec
        lstStoneID = []
        for oStone in lstStone:
            vDest = oStone.GetPos()
            fDis = cl_math.CalDistance3D(vOrigin, vDest)
            if fDis >= fLeft and fDis <= fRight:
                lstStoneID.append(oStone.m_ID)
        
        return lstStoneID

    GetStonePillarPosLst = classmethod(GetStonePillarPosLst)

