# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/custom/relictalent/customaction.pyc
# RelativePath: clientlogic/cl_platformdata/custom/relictalent/customaction.pyc
# Source Generated with Decompyle++
# File: customaction.pyc (Python 3.6)

from cl_commondefines import PF_TYPE_TRIGGERCLIENT, DAM_TYPE_FIRE, DAM_TYPE_CORRISION, DAM_TYPE_THUNDER
import cl_war
import cl_math
import cl_formula
import cl_snetwar

def CustomAction50009(oWarrior, oEventCB, dInfo):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return None
    oSkill = dMsgInfo['Skill']
    iFromPerform = dInfo['FromPerform'] if 'FromPerform' in dInfo else 0
    iTriggerPerform = oSkill.m_Base['pfid']
    dCustom = oSkill.m_Custom
    if not iFromPerform or iFromPerform != iTriggerPerform:
        return None
    if 'Element' not in dCustom:
        return None
    if dCustom['Element'] == DAM_TYPE_FIRE and 'FirePerform' in dInfo:
        iPerform = dInfo['FirePerform']
    elif dCustom['Element'] == DAM_TYPE_CORRISION and 'CorrisionPerform' in dInfo:
        iPerform = dInfo['CorrisionPerform']
    elif dCustom['Element'] == DAM_TYPE_THUNDER and 'ThunderPerform' in dInfo:
        iPerform = dInfo['ThunderPerform']
    else:
        return None
    iBaseAtt = cl_formula.GetResultByData(oWarrior, dInfo[iPerform], oEventCB.GetCBEventInfo(), dMsgInfo)
    iBaseAtt = iBaseAtt * (10000 + dInfo['AttExtFactor']) // 10000
    pfobj = oWarrior.GetPerform(iPerform)
    pfobj.SetArgValue('Att', iBaseAtt)
    iTargetID = dCustom['TargetID'] if 'TargetID' in dCustom else 0
    if 'pf50010MaxExtra' in dCustom:
        oGame = oWarrior.m_Game
        oVictim = oGame.GetObject(iTargetID)
        if oVictim:
            tPos = oVictim.GetPos()
            vStart = (tPos[0], tPos[1] + oVictim.m_ModelHeight * 0.5, tPos[2])
        else:
            vStart = (0, 0, 0)
    elif 'vEnd' in dCustom:
        pass
    
    vStart = (0, 0, 0)
    vAttackPos = oWarrior.GetPos()
    vDir = cl_math.Vec3Minus((vAttackPos[0], 0, vAttackPos[2]), (vStart[0], 0, vStart[2]))
    fAngle = 180 // pfobj.CalAttr('MaxCover')
    vEnd = cl_math.Vec3DestPosDirPlane(vStart, vDir, 99, fAngle)
    vStartDir = cl_math.Vec3Minus(vEnd, vStart)
    dArgs = {
        'StartX': int(vStart[0] * 100),
        'StartY': int(vStart[1] * 100),
        'StartZ': int(vStart[2] * 100),
        'DirX': int(vStartDir[0] * 100),
        'DirY': int(vStartDir[1] * 100),
        'DirZ': int(vStartDir[2] * 100),
        'MainTarget': iTargetID }
    pfobj.AddCanUseCount()
    cl_snetwar.GS2CNotifyStartSkill(oWarrior.m_Game, oWarrior.m_PlayerID, iPerform, pfobj.m_ID, 0, dArgs = dArgs)

