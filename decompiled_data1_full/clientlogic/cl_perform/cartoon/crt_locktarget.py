# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/cartoon/crt_locktarget.pyc
# RelativePath: clientlogic/cl_perform/cartoon/crt_locktarget.pyc
# Source Generated with Decompyle++
# File: crt_locktarget.pyc (Python 3.6)

from cl_only import PY_FLAG_DEAD, GAME_FRAME_SECOND, Second2Frame, SendAlert
from cl_commondefines import CRT_CHECK_SERVER, MONSTER_PART_UNTAGGED
from cl_pxlayer import PXMASK_LIVEOBJ
from .mobject import CBaseCartoon
from cl_object.logging import SkillLog
import cl_math

class LockTargetCartoon(CBaseCartoon):
    
    def Trace(cls, oSkill, dCartoon):
        if 'Over' in dCartoon:
            return None
        cls.Update(oSkill, dCartoon)

    Trace = classmethod(Trace)
    
    def Restart(cls, oSkill, dCartoon):
        if oSkill.m_CheckType & CRT_CHECK_SERVER:
            oSkill.Call_Out(1, dCartoon['ID'])

    Restart = classmethod(Restart)
    
    def IsOver(cls, oSkill, dCartoon):
        iNodeID = dCartoon['ID']
        if oSkill.m_CheckType & CRT_CHECK_SERVER:
            iOver = cls.IsOverServer(oSkill, dCartoon)
        else:
            iOver = cls.IsOverClient(oSkill, dCartoon)
        if iOver:
            if 'Final' not in dCartoon:
                dCartoon['Final'] = dCartoon['CurPos']
            oSkill.Send(iNodeID, {
                'Over': 1 })
        return iOver

    IsOver = classmethod(IsOver)
    
    def InitTraceClient(cls, oSkill, dCartoon, vStartPos, vShowPos, iTarget, fMaxDistance, fSpeed, *args, **kwargs):
        iNodeID = dCartoon['ID']
        dClient = oSkill.m_NetReceive[iNodeID]
        dCartoon['Start'] = dClient['Start']
        dCartoon['CurPos'] = dClient['Start']
        dCartoon['LockTarget'] = list(dClient['LockTarget'])[0]
        dCartoon['AllVLST'] = []
        dCartoon['AllHitInfo'] = []
        iFlyFrame = Second2Frame(fMaxDistance / fSpeed)
        dCartoon['WaitNet'] = oSkill.GetWaitNetFrame(iFlyFrame)
        dNet = {
            'Start': dCartoon['Start'],
            'LockTarget': [
                dCartoon['LockTarget']] }
        oSkill.Send(dCartoon['ID'], dNet)

    InitTraceClient = classmethod(InitTraceClient)
    
    def HitTargetClient(cls, oSkill, dCartoon):
        if 'Over' in dCartoon:
            SendAlert('err', '%s %s %s 命中后没结束' % (oSkill.m_Game.m_ID, oSkill.m_Base['pfid'], cls.__name__))
            return -1
        iNodeID = dCartoon['ID']
        if iNodeID not in oSkill.m_NetReceive:
            return -1
        dClient = oSkill.m_NetReceive[iNodeID]
        if 'LockTarget' in dClient:
            iNewTarget = list(dClient['LockTarget'])[0]
            iOldTarget = dCartoon['LockTarget']
            if iNewTarget != iOldTarget:
                dCartoon['LockTarget'] = iNewTarget
                dNet = {
                    'LockTarget': [
                        dCartoon['LockTarget']] }
                oSkill.Send(dCartoon['ID'], dNet)
        if 'Ray' not in dClient or not dClient['Ray']:
            return 0
        lstVLST = []
        lstSend = []
        lstHitInfo = []
        iLockTarget = dCartoon['LockTarget']
        iHit = 0
        for vHitPos, vNormal, iVictim, iHitPart in dClient['Ray']:
            if iVictim != iLockTarget:
                continue
            iHit = 1
            dHitInfo = {
                'Victim': iVictim,
                'HitPos': vHitPos,
                'HitArea': iHitPart }
            dCartoon['AllVLST'].append(iVictim)
            lstVLST.append(iVictim)
            lstHitInfo.append(dHitInfo)
            dCartoon['AllHitInfo'].append(dHitInfo)
            lstSend.append((vHitPos, vNormal, iVictim, iHitPart))
            dCartoon['Final'] = vHitPos
            dCartoon['Over'] = 1
        
        oSkill.m_Update['LastVLST'] = lstVLST
        oSkill.m_Update['HitInfo'] = lstHitInfo
        dNet = {
            'Ray': lstSend }
        oSkill.Send(dCartoon['ID'], dNet)
        return iHit

    HitTargetClient = classmethod(HitTargetClient)
    
    def IsOverClient(cls, oSkill, dCartoon):
        iNodeID = dCartoon['ID']
        if iNodeID not in oSkill.m_NetReceive:
            return 0
        dClient = oSkill.m_NetReceive[iNodeID]
        if 'Over' in dClient:
            return 1
        return 0

    IsOverClient = classmethod(IsOverClient)
    
    def InitTraceServer(cls, oSkill, dCartoon, vStartPos, vShowPos, iTarget, fMaxDistance, fSpeed, *args, **kwargs):
        dCartoon['Start'] = vStartPos
        dCartoon['Distance'] = fMaxDistance
        dCartoon['SpeedPerFrame'] = fSpeed * GAME_FRAME_SECOND
        dCartoon['CurPos'] = vStartPos
        dCartoon['LockTarget'] = iTarget
        oGame = oSkill.m_Game
        oLockTarget = oGame.GetObject(dCartoon['LockTarget'], PY_FLAG_DEAD)
        if oLockTarget:
            vTarget = oLockTarget.GetCenter()
            dCartoon['LockPos'] = vTarget
        else:
            dCartoon['Over'] = 1
            oSkill.Send(dCartoon['ID'], {
                'Over': 1 })
            cls.Disable(oSkill, dCartoon)
            SkillLog.Debug('%d locktargetcrt not target %d %d' % (oSkill.m_Base['pfid'], oSkill.m_Base['AID'], iTarget))
            return None
        dNet = {
            'Start': dCartoon['Start'],
            'LockTarget': [
                iTarget] }
        oSkill.Send(dCartoon['ID'], dNet)

    InitTraceServer = classmethod(InitTraceServer)
    
    def HitTargetServer(cls, oSkill, dCartoon):
        oGame = oSkill.m_Game
        vCur = dCartoon['CurPos']
        oLockTarget = oGame.GetObject(dCartoon['LockTarget'], PY_FLAG_DEAD)
        if oLockTarget:
            vTarget = oLockTarget.GetCenter()
            dCartoon['LockPos'] = vTarget
        else:
            iOldTarget = dCartoon['LockTarget']
            dCartoon['LockTarget'] = 0
            cls.Trigger(oSkill)
            iNewTarget = dCartoon['LockTarget']
            oNewTarget = oGame.GetObject(iNewTarget, PY_FLAG_DEAD)
            if oNewTarget:
                dCartoon['LockPos'] = oNewTarget.GetCenter()
            if iOldTarget != iNewTarget:
                dNet = {
                    'LockTarget': [
                        iNewTarget] }
                oSkill.Send(dCartoon['ID'], dNet)
        vTarget = dCartoon['LockPos']
        iLockTarget = dCartoon['LockTarget']
        iPerFrameDis = dCartoon['SpeedPerFrame']
        iTargetDis = cl_math.CalDistance3D(vCur, vTarget)
        if iTargetDis <= iPerFrameDis:
            dCartoon['Over'] = 1
            oLockTarget = oGame.GetObject(iLockTarget, PY_FLAG_DEAD)
            if not oLockTarget:
                dCartoon['Final'] = vTarget
                return 0
            lstVictim = oGame.Scene_RaycastMultiple(oSkill.m_Base['Scene'], vCur, vTarget, PXMASK_LIVEOBJ, {
                'ExcludeFlag': PY_FLAG_DEAD })
            for iVictim, dHit in lstVictim:
                if iVictim != iLockTarget:
                    continue
                oSkill.m_Update['LastVLST'] = [
                    iLockTarget]
                vHitPos = dHit['Pos']
                dNet = {
                    'Ray': [
                        (vHitPos, (0, 0, 0), iLockTarget, MONSTER_PART_UNTAGGED)] }
                oSkill.Send(dCartoon['ID'], dNet)
                dCartoon['Final'] = vHitPos
                return 1
            
            dCartoon['Final'] = vTarget
            return 0
        vDir = cl_math.Vec3Normalize(cl_math.Vec3Minus(vTarget, vCur))
        vTar = cl_math.Vec3Mad(vCur, vDir, iPerFrameDis)
        dCartoon['CurPos'] = vTar
        return 0

    HitTargetServer = classmethod(HitTargetServer)
    
    def IsOverServer(cls, oSkill, dCartoon):
        if 'Over' in dCartoon or (oSkill.m_Game.GetFrameNum() - dCartoon['StartFrame']) * dCartoon['SpeedPerFrame'] > dCartoon['Distance']:
            return 1
        return 0

    IsOverServer = classmethod(IsOverServer)

