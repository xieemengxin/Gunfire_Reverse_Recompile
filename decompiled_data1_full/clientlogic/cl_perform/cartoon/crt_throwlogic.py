# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/cartoon/crt_throwlogic.pyc
# RelativePath: clientlogic/cl_perform/cartoon/crt_throwlogic.pyc
# Source Generated with Decompyle++
# File: crt_throwlogic.pyc (Python 3.6)

from cl_commondefines import VICTIM_STATE_VALID, VICTIM_STATE_BLOCK, VICTIM_STATE_HIT
from .mobject import CBaseCartoon
from cl_only import Time2Frame

class ThrowLogicCartoon(CBaseCartoon):
    
    def Trace(cls, oSkill, dCartoon):
        if 'Over' in dCartoon:
            return None
        cls.Update(oSkill, dCartoon)

    Trace = classmethod(Trace)
    
    def IsOver(cls, oSkill, dCartoon):
        oSkill.m_Update['EPFPos'] = dCartoon['CurPos']
        iOver = 0
        iNodeID = dCartoon['ID']
        if 'Over' in dCartoon:
            iOver = 1
        if iOver:
            oSkill.Send(iNodeID, {
                'Over': 1 })
            return 1
        return 0

    IsOver = classmethod(IsOver)
    
    def InitTraceClient(cls, oSkill, dCartoon, iTriggerDelay, pierce = 0, *arg, **kwargs):
        iNodeID = dCartoon['ID']
        dClient = oSkill.m_NetReceive[iNodeID]
        dCartoon['Start'] = dClient['Start']
        dCartoon['CurPos'] = dCartoon['Start']
        dCartoon['SpeedVector'] = dClient['SpeedVector']
        dCartoon['Pierce'] = pierce
        dCartoon['AllVLST'] = []
        dCartoon['AllHitInfo'] = []
        dCartoon['WaitNet'] = oSkill.GetWaitNetFrame(Time2Frame(iTriggerDelay))
        dNet = {
            'Start': dClient['Start'],
            'SpeedVector': dClient['SpeedVector'] }
        oSkill.Send(dCartoon['ID'], dNet)

    InitTraceClient = classmethod(InitTraceClient)
    
    def HitTargetClient(cls, oSkill, dCartoon):
        iNodeID = dCartoon['ID']
        if iNodeID not in oSkill.m_NetReceive:
            return -1
        iHit = 0
        dClient = oSkill.m_NetReceive[iNodeID]
        if 'Ray' in dClient:
            iHit = 1
            lstVLST = []
            lstHitInfo = []
            for _vHitPos, _, iTarget, iHitPart in dClient['Ray']:
                iVictimState = cls.CheckVictimState(oSkill, dCartoon, iTarget)
                if iVictimState == VICTIM_STATE_BLOCK:
                    oSkill.m_Update['HitStatic'] = 1
                    dCartoon['AllVLST'] = []
                    dCartoon['AllHitInfo'] = []
                elif (iVictimState == VICTIM_STATE_VALID or iVictimState == VICTIM_STATE_HIT) and cls.CheckValidDamage(dCartoon, iTarget, iHitPart):
                    lstVLST.append(iTarget)
                    dHitInfo = {
                        'Victim': iTarget,
                        'HitPos': _vHitPos,
                        'HitArea': iHitPart }
                    lstHitInfo.append(dHitInfo)
                    dCartoon['AllVLST'].append(iTarget)
                    dCartoon['AllHitInfo'].append(dHitInfo)
                    dCartoon['Pierce'] -= cls.GetVictimPierceCost(oSkill, iTarget)
                    if dCartoon['Pierce'] <= 0:
                        dCartoon['Over'] = 1
                        break
                dCartoon['CurPos'] = _vHitPos
            
            if 'HitPos' not in dCartoon:
                dCartoon['HitPos'] = []
                dCartoon['HitTimes'] = 0
            dCartoon['HitPos'].append(dCartoon['CurPos'])
            dCartoon['HitTimes'] += 1
            oSkill.m_Update['LastVLST'] = lstVLST
            oSkill.m_Update['HitInfo'] = lstHitInfo
            cls.CollectSkillInfo(oSkill, dCartoon)
        if 'Over' in dClient:
            dCartoon['Over'] = 1
        return iHit

    HitTargetClient = classmethod(HitTargetClient)
    
    def CollectSkillInfo(cls, oSkill, dCartoon):
        lstCartoonPos = oSkill.m_Collect['CartoonPos'] if 'CartoonPos' in oSkill.m_Collect else []
        vStart = dCartoon['Start']
        vEnd = dCartoon['CurPos']
        lstCartoonPos.append((vStart, vEnd))
        oSkill.m_Collect['CartoonPos'] = lstCartoonPos

    CollectSkillInfo = classmethod(CollectSkillInfo)

