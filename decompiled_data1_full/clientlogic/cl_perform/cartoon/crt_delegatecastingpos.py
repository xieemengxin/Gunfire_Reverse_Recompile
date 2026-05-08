# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/cartoon/crt_delegatecastingpos.pyc
# RelativePath: clientlogic/cl_perform/cartoon/crt_delegatecastingpos.pyc
# Source Generated with Decompyle++
# File: crt_delegatecastingpos.pyc (Python 3.6)

from cl_only import Time2Frame, GAME_FRAME
from cl_commondefines import OBJ_ALL, ATT_SHAPE_SECTOR, HITPART_DIRECTPOS, VICTIM_STATE_VALID
from .mobject import CBaseCartoon

class DelegateCastingPosCartoon(CBaseCartoon):
    m_WorldLineOutFrame = 2 * GAME_FRAME
    
    def HitTarget(cls, oSkill, dCartoon):
        return cls.HitTargetClient(oSkill, dCartoon)

    HitTarget = classmethod(HitTarget)
    
    def Disable(cls, oSkill, dCartoon):
        cls.End(oSkill)

    Disable = classmethod(Disable)
    
    def AllOver(cls, oSkill, dCartoon):
        oSkill.PopStack(dCartoon)

    AllOver = classmethod(AllOver)
    
    def IsOver(cls, oSkill, dCartoon):
        iNodeID = dCartoon['ID']
        iOver = 0
        if 'DelegateOver' in dCartoon:
            iOver = 1
            dSendOverPlayer = dCartoon['DelegateOver']
            lstLiveOnlinePlayer = oSkill.m_Game.m_WarMgr.GetLiveOnlinePlayer()
            if set(dSendOverPlayer.keys()) == set(lstLiveOnlinePlayer):
                cls.AllOver(oSkill, dCartoon)
        iCurFrame = oSkill.m_Game.GetFrameNum()
        if dCartoon['StartFrame'] + dCartoon['WaitFrame'] <= iCurFrame:
            iOver = 1
        if 'Over' in dCartoon and dCartoon['Over'] <= iCurFrame:
            cls.AllOver(oSkill, dCartoon)
        if iOver:
            dCartoon['Over'] = iCurFrame + cls.m_WorldLineOutFrame
            oSkill.Call_Out(cls.m_WorldLineOutFrame, iNodeID)
            oSkill.Send(iNodeID, {
                'Over': 1 })
            return 1
        return 0

    IsOver = classmethod(IsOver)
    
    def InitTraceServer(cls, oSkill, dCartoon, StartPos, OffsetPos, iIntervalTime, iTotalTime, lstArgs, attshape = ATT_SHAPE_SECTOR, targettype = OBJ_ALL, *args, **kwargs):
        dCartoon['Start'] = StartPos
        dCartoon['Offset'] = OffsetPos
        dCartoon['IntervalFrame'] = Time2Frame(iIntervalTime)
        dCartoon['WaitFrame'] = (Time2Frame(iTotalTime) // dCartoon['IntervalFrame']) * dCartoon['IntervalFrame']
        dCartoon['AttShape'] = attshape
        dCartoon['TargetType'] = targettype
        dCartoon['EffArgs'] = lstArgs
        dCartoon['Count'] = 0
        dCartoon['CurPos'] = StartPos
        dNet = {
            'Start': StartPos,
            'Offset': OffsetPos,
            'Time': iTotalTime }
        oSkill.Send(dCartoon['ID'], dNet)
        oSkill.Call_Out(dCartoon['WaitFrame'], dCartoon['ID'])

    InitTraceServer = classmethod(InitTraceServer)
    
    def HitTargetClient(cls, oSkill, dCartoon):
        iNodeID = dCartoon['ID']
        if iNodeID not in oSkill.m_NetReceive:
            return 0
        oAttack = oSkill.GetAttack()
        if oAttack:
            vPos = oAttack.GetPos()
            dCartoon['CurPos'] = vPos
        cls.CollectSkillInfo(oSkill, dCartoon)
        dClient = oSkill.m_NetReceive[iNodeID]
        iHit = 0
        if 'Count' in dClient:
            iCount = dClient['Count']
            if iCount <= dCartoon['Count']:
                return iHit
            dCartoon['Count'] = iCount
            if 'Ray' in dClient:
                iHit = 1
                lstVLST = []
                lstHitInfo = []
                lstRay = dClient['Ray']
                for vHitPos, _, iVictim, _ in lstRay:
                    iVictimState = cls.CheckVictimState(oSkill, dCartoon, iVictim)
                    if iVictimState == VICTIM_STATE_VALID:
                        lstVLST.append(iVictim)
                        dHitInfo = {
                            'Victim': iVictim,
                            'HitPos': vHitPos,
                            'HitArea': HITPART_DIRECTPOS }
                        lstHitInfo.append(dHitInfo)
                
                oSkill.m_Update['LastVLST'] = lstVLST
                oSkill.m_Update['HitInfo'] = lstHitInfo
                dNet = {
                    'Count': iCount,
                    'LastVLST': lstVLST,
                    'Ray': lstRay }
                oSkill.Send(dCartoon['ID'], dNet)
        if 'Over' in dClient:
            dDelegateOver = dCartoon.setdefault('DelegateOver', { })
            dDelegateOver[dClient['Source']] = 1
        return iHit

    HitTargetClient = classmethod(HitTargetClient)
    
    def CollectSkillInfo(cls, oSkill, dCartoon):
        lstCartoonPos = oSkill.m_Collect['CartoonPos'] if 'CartoonPos' in oSkill.m_Collect else []
        vStart = dCartoon['Start']
        vEnd = dCartoon['CurPos']
        lstCartoonPos.append((vStart, vEnd))
        oSkill.m_Collect['CartoonPos'] = lstCartoonPos

    CollectSkillInfo = classmethod(CollectSkillInfo)

