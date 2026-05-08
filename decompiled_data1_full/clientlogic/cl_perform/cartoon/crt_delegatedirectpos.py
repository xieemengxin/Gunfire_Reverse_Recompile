# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/cartoon/crt_delegatedirectpos.pyc
# RelativePath: clientlogic/cl_perform/cartoon/crt_delegatedirectpos.pyc
# Source Generated with Decompyle++
# File: crt_delegatedirectpos.pyc (Python 3.6)

from cl_only import GAME_FRAME
from cl_commondefines import OBJ_ALL, ATT_SHAPE_SECTOR, ATT_SHAPE_SPHERE, ATT_SHAPE_RECTANGLE, CRT_CHECK_CLIENT, CRT_TYPE_DIRECTPOS, HITPART_DIRECTPOS, VICTIM_STATE_VALID
from cl_object.logging import SkillLog
import cl_math
import cl_msgcenter
from .mobject import CBaseCartoon

class DelegateDirectPosCartoon(CBaseCartoon):
    m_WorldLineOutFrame = 2 * GAME_FRAME
    
    def HitTarget(cls, oSkill, dCartoon):
        return cls.HitTargetClient(oSkill, dCartoon)

    HitTarget = classmethod(HitTarget)
    
    def HitTargetClient(cls, oSkill, dCartoon):
        iNodeID = dCartoon['ID']
        if iNodeID not in oSkill.m_NetReceive:
            return 0
        dClient = oSkill.m_NetReceive[iNodeID]
        iHit = 0
        if 'Ray' in dClient:
            iHit = 1
            lstVLST = []
            lstHitInfo = []
            lstRay = dClient['Ray']
            for vHitPos, _, iVictim, _ in lstRay:
                iVictimState = cls.CheckVictimState(oSkill, dCartoon, iVictim)
                if iVictimState == VICTIM_STATE_VALID:
                    dCartoon['AllVLST'].append(iVictim)
                    lstVLST.append(iVictim)
                    dHitInfo = {
                        'Victim': iVictim,
                        'HitPos': vHitPos,
                        'HitArea': HITPART_DIRECTPOS }
                    lstHitInfo.append(dHitInfo)
            
            oSkill.m_Update['LastVLST'] = lstVLST
            oSkill.m_Update['HitInfo'] = lstHitInfo
            dNet = {
                'LastVLST': lstVLST }
            oSkill.Send(dCartoon['ID'], dNet)
        return iHit

    HitTargetClient = classmethod(HitTargetClient)
    
    def InitTraceServer(cls, oSkill, dCartoon, StartPos, EndPos, lstArgs, attshape = ATT_SHAPE_SECTOR, targettype = OBJ_ALL, pierceStatic = False, explosion = False, useclientpos = False, **kwargs):
        dCartoon['Start'] = StartPos
        dCartoon['End'] = EndPos if attshape != ATT_SHAPE_SPHERE else StartPos
        dCartoon['AttShape'] = attshape
        dCartoon['TargetType'] = targettype
        dCartoon['PierceStatic'] = pierceStatic
        dCartoon['EffArgs'] = lstArgs
        dCartoon['AllVLST'] = []
        dCartoon['CrtType'] = CRT_TYPE_DIRECTPOS
        dCartoon['CurPos'] = StartPos if attshape == ATT_SHAPE_SECTOR else dCartoon['End']
        if dCartoon['Start'] != dCartoon['End']:
            dCartoon['Dir'] = cl_math.Vec3Normalize(cl_math.Vec3Minus(dCartoon['End'], dCartoon['Start']))
        elif attshape in (ATT_SHAPE_SECTOR, ATT_SHAPE_RECTANGLE):
            oSkill.Send(dCartoon['ID'], {
                'Over': 1 })
            dCartoon['Over'] = 1
            return None
        dCartoon['Final'] = dCartoon['End']
        dNet = {
            'End': dCartoon['End'] }
        if explosion:
            SendExplosionMsg(oSkill, dCartoon)
        if 'LockTarget' in oSkill.m_Custom:
            dNet['LockTarget'] = oSkill.m_Custom['LockTarget']
        if not useclientpos:
            dNet['Start'] = dCartoon['Start']
        oSkill.Send(dCartoon['ID'], dNet)
        oSkill.Call_Out(cls.m_WorldLineOutFrame, dCartoon['ID'])

    InitTraceServer = classmethod(InitTraceServer)
    
    def IsOver(cls, oSkill, dCartoon):
        iNodeID = dCartoon['ID']
        oSkill.Send(iNodeID, {
            'Over': 1 })
        return 1

    IsOver = classmethod(IsOver)


def SendExplosionMsg(oSkill, dCartoon):
    radius = 0
    if oSkill.m_CheckType & CRT_CHECK_CLIENT:
        radius = oSkill.m_Cache['Radius']
    elif dCartoon['AttShape'] == ATT_SHAPE_SPHERE:
        lstEffArgs = dCartoon['EffArgs']
        radius = lstEffArgs[0]
    else:
        SkillLog.Alert('目前非球形爆炸，还不支持发送【造成爆炸】消息，请联系程序确认。')
        return None
    dData = {
        'Skill': oSkill,
        'Start': dCartoon['Start'],
        'End': dCartoon['End'],
        'Radius': radius }
    if radius <= 0:
        SkillLog.Alert('%d radius is %s' % (oSkill.m_Base['pfid'], radius))
    cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_EXPLOSION, oSkill.m_Game.GetObject(oSkill.m_Base['AID']), dData)

