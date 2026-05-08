# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/custom/devicecomp/customaction.pyc
# RelativePath: clientlogic/cl_platformdata/custom/devicecomp/customaction.pyc
# Source Generated with Decompyle++
# File: customaction.pyc (Python 3.6)

from cl_only import PY_FLAG_DEAD
from cl_object.logging import OtherLog
import cl_war
import cl_msgcenter

def CustomAction50213(oWarrior, oEventCB, dInfo):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    oSkill = dMsgInfo['Skill']
    iVictim = oSkill.m_Base['VID']
    oPerform = oWarrior.GetPerform(dInfo['PerformId'])
    dData = { }
    dData['Custom'] = {
        'lstHitVictim': [
            iVictim],
        'MulAtt': dInfo['MulAtt'] }
    if cl_war.UsePerform(oWarrior, oPerform, dData):
        iCost = dInfo['CostBullet']
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_COMCOSTBULLET, oWarrior, {
            'Cost': iCost,
            'AID': oWarrior.m_ID })


def CustomAction50123(oWarrior, oEventCB, dInfo):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return None
    oSkill = dMsgInfo['Skill']
    if 'ExtraAttack' not in oSkill.m_Custom:
        return None
    sReason = dInfo['RS'] if 'RS' in dInfo else ''
    iCurVID = dMsgInfo['CurVID']
    if sReason == 'ExtraAttack50122':
        dTransInfo = oEventCB.GetCBTransInfo()
        if dTransInfo['TargetList']:
            iTargetVID = dTransInfo['TargetList'][0]
        else:
            iTargetVID = iCurVID
    else:
        iTargetVID = iCurVID
    oVictim = oWarrior.m_Game.GetObject(iTargetVID, PY_FLAG_DEAD)
    if not oVictim:
        return None
    iAttack = dMsgInfo['AID']
    oReason = dMsgInfo['RS']
    if iCurVID not in oSkill.m_Update:
        OtherLog.Debug('gameid %d extraattack err %s %s' % (oWarrior.m_Game.m_ID, oReason, oSkill.m_Update))
        if 'CurVID' not in oSkill.m_Update:
            return None
        if oSkill.m_Update['CurVID'] not in oSkill.m_Update:
            return None
        iCurVID = oSkill.m_Update['CurVID']
    iBaseMainDam = oSkill.m_Update[iCurVID]['MainDam'][0][0] * dInfo['BaseFactor'] // 100
    oAttackReason = oReason.ExtInfo({
        sReason: 1 })
    iBallisticType = oSkill.m_Custom['BallisticType'] if 'BallisticType' in oSkill.m_Custom else 0
    if iTargetVID not in oSkill.m_Update:
        if iBallisticType == 2:
            oSkill.m_Update[iTargetVID] = {
                'LuckyHit': oSkill.m_Update[iCurVID]['LuckyHit'],
                'CrazyEff': oSkill.m_Update[iCurVID]['CrazyEff'] }
        else:
            oSkill.m_Update[iTargetVID] = { }
    oSkill.m_Update[iTargetVID]['MainDam'] = [
        [
            iBaseMainDam,
            oAttackReason]]
    oSkill.m_Update[iTargetVID]['RS'] = oAttackReason
    if iBallisticType == 2:
        oVictim.ReceiveAttack(iAttack, oSkill, False, 0)
    else:
        oVictim.ReceivePerform(iAttack, oSkill)


def CalGroup(oWarrior, oEventCB, dInfo):
    dEnergyToGroup = dInfo['EnergyToGroup']
    iNowEnergy = oWarrior.DeviceEnergy()
    iGroup = 0
    for iEnergy in dEnergyToGroup:
        if iNowEnergy >= iEnergy:
            iGroup = dEnergyToGroup[iEnergy]
            continue
    
    oPerform = oEventCB.GetObject()
    if iGroup == oPerform.GetArgValue('EnergyGroup'):
        oPerform.SetArgValue('ChangeGroup', 0)
        return None
    oPerform.SetArgValue('ChangeGroup', 1)
    oPerform.SetArgValue('EnergyGroup', iGroup)

dAction50122 = {
    'CalGroup': CalGroup,
    'ExtraAttack': CustomAction50123 }

def CustomAction50122(oWarrior, oEventCB, dInfo):
    sAction = dInfo['Action']
    if sAction in dAction50122:
        cFun = dAction50122[sAction]
        cFun(oWarrior, oEventCB, dInfo)

