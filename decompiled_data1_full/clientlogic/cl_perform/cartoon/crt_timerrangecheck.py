# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/cartoon/crt_timerrangecheck.pyc
# RelativePath: clientlogic/cl_perform/cartoon/crt_timerrangecheck.pyc
# Source Generated with Decompyle++
# File: crt_timerrangecheck.pyc (Python 3.6)

from cl_only import Time2Frame, GAME_FRAME
from cl_commondefines import VICTIM_STATE_VALID, CRT_RANGECHECK_ENTER, CRT_RANGECHECK_EXIT
import cl_msgcenter
from .mobject import CBaseCartoon

class TimerRangeCheckCartoon(CBaseCartoon):
    m_NeedCtrlNet = 0
    
    def Trace(cls, oSkill, dCartoon):
        cls.Update(oSkill, dCartoon)

    Trace = classmethod(Trace)
    
    def IsOver(cls, oSkill, dCartoon):
        iOver = 0
        iNodeID = dCartoon['ID']
        if iNodeID in oSkill.m_NetReceive and 'Over' in oSkill.m_NetReceive[iNodeID]:
            iOver = 1
        elif dCartoon['EndFrame'] <= oSkill.m_Game.GetFrameNum():
            iOver = 1
        if iOver:
            oSkill.Send(dCartoon['ID'], {
                'Over': 1 })
            return 1
        return 0

    IsOver = classmethod(IsOver)
    
    def InitTraceClient(cls, oSkill, dCartoon, iCheckTime, triggerTrans, fCheckRange, iTargetType, *args, **kwargs):
        dCartoon['CheckTime'] = iCheckTime
        dCartoon['CheckRange'] = fCheckRange
        dCartoon['TargetType'] = iTargetType
        dCartoon['OnCheckRangeTarget'] = { }
        oGame = oSkill.m_Game
        iCheckFrame = Time2Frame(iCheckTime)
        dCartoon['EndFrame'] = oGame.GetFrameNum() + iCheckFrame
        oSkill.m_Collect['CheckEndFrame'] = dCartoon['EndFrame']
        oSkill.Call_Out(iCheckFrame + GAME_FRAME, dCartoon['ID'], dCartoon['Casting'])

    InitTraceClient = classmethod(InitTraceClient)
    
    def HitTargetClient(cls, oSkill, dCartoon):
        iNodeID = dCartoon['ID']
        if iNodeID not in oSkill.m_NetReceive:
            return 0
        dClient = oSkill.m_NetReceive[iNodeID]
        if 'LastVLST' not in dClient:
            return 0
        lstClientVLST = dClient['LastVLST']
        dOnCheckRangeTarget = dCartoon['OnCheckRangeTarget']
        oAttack = oSkill.GetAttack()
        for iVictim in lstClientVLST:
            iVictimState = cls.CheckVictimState(oSkill, dCartoon, iVictim)
            if iVictimState == VICTIM_STATE_VALID:
                dMsgInfo = {
                    'CurVID': iVictim,
                    'Skill': oSkill }
                if iVictim not in dOnCheckRangeTarget:
                    dOnCheckRangeTarget[iVictim] = 1
                    cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_TRIGGERCRT_RANGECHECK, oAttack, dInfo = dMsgInfo, iSub = CRT_RANGECHECK_ENTER)
                    continue
                dOnCheckRangeTarget.pop(iVictim, 0)
                cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_TRIGGERCRT_RANGECHECK, oAttack, dInfo = dMsgInfo, iSub = CRT_RANGECHECK_EXIT)
        
        return 0

    HitTargetClient = classmethod(HitTargetClient)

