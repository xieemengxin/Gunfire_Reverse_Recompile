# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_evcon/evc_passive.pyc
# RelativePath: clientlogic/cl_evcon/evc_passive.pyc
# Source Generated with Decompyle++
# File: evc_passive.pyc (Python 3.6)

from cl_only import SendAlert
from cl_commondefines import DAM_TYPE_WEAKNESS, SKILLCACHE_PARENTACTNUM
from cl_cscommondef import MAIN_HOLD
from cl_hero.herostatus import SNIPE_STATUS_OPEN
import cl_object.reason as reason
import cl_formula
import cl_math
import cl_perform

def PassiveCheckInColdTime(oWarrior, oEventCB, iLite = 0):
    pfobj = oEventCB.GetObject()
    if not pfobj:
        return 1
    if iLite:
        return pfobj.CheckLiteCD()
    if pfobj.InColdTime():
        return 1
    return 0


def PassiveCheckFromSameItem(oWarrior, oEventCB):
    dEventInfo = oEventCB.GetCBEventInfo()
    iPFItem = dEventInfo['ItemID']
    if not iPFItem:
        return 0
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'RS' in dMsgInfo:
        iItem = dMsgInfo['RS'].Query('Item', 0)
    elif 'ItemID' in dMsgInfo:
        iItem = dMsgInfo['ItemID']
    elif 'Skill' in dMsgInfo:
        iItem = dMsgInfo['Skill'].m_Base['Weapon']
    else:
        return 0
    return iPFItem == iItem


def PassiveCBCheckCartoonValid(oWarrior, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return 1
    dEventInfo = oEventCB.GetCBEventInfo()
    sKey = dEventInfo['PFKey']
    oSkill = dMsgInfo['Skill']
    if 'ValidCartoon' not in oSkill.m_Collect or sKey not in oSkill.m_Collect['ValidCartoon']:
        return 1
    dCartoon = oSkill.GetCurCartoon()
    if not dCartoon:
        return 1
    return dCartoon['ID'] == oSkill.m_Collect['ValidCartoon'][sKey]


def PassiveCBGetPFArgs(oWarrior, oEventCB, sArgs):
    dEventInfo = oEventCB.GetCBEventInfo()
    oLifeCycle = dEventInfo['LifeCycle']
    pfobj = oLifeCycle.GetObject()
    if not pfobj:
        return 0
    return pfobj.GetArgValue(sArgs)


def PassiveCBGetPFArgsByFormulaKey(oWarrior, oEventCB, iKey):
    dEventInfo = oEventCB.GetCBEventInfo()
    iPerform = dEventInfo['pfid']
    iItemID = dEventInfo['ItemID']
    pfobj = oWarrior.GetPerform(iPerform, iItemID)
    if not pfobj:
        return 0
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iKey = cl_formula.GetResultByData(oWarrior, iKey, dEventInfo, dMsgInfo)
    return pfobj.GetArgValue(iKey)


def PassiveCBCheckTargetHasState(oWarrior, oEventCB, iState, iFromSameItem = 0, iFromSelf = 0, iFromSelfServant = 0):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    lstTar = dTrans['TargetList']
    if not lstTar:
        return 0
    iTarget = lstTar[0]
    oTarget = oWarrior.m_Game.GetObject(iTarget)
    if not oTarget:
        return 0
    lstState = oTarget.m_State.GetItems(iState)
    if not lstState:
        return 0
    if iFromSelf or iFromSelfServant or iFromSameItem:
        iAttack = 0
        if iFromSelf:
            iAttack = oWarrior.m_ID
        elif iFromSelfServant:
            iAttack = oWarrior.m_Servant
        iTarItem = 0
        if iFromSameItem:
            dEventInfo = oEventCB.GetCBEventInfo()
            iTarItem = dEventInfo['ItemID']
        for oState in lstState:
            if iAttack and oState.m_Attacker != iAttack:
                continue
            if iTarItem and oState.m_Item != iTarItem:
                continue
        else:
            return 0
    return 1


def PassiveCBCheckTargetCanAddHaloState(oWarrior, oEventCB, iState):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    oGame = oWarrior.m_Game
    for iTarget in dTrans['TargetList']:
        oTarget = oGame.GetObject(iTarget)
        if not oTarget:
            continue
        lstState = oTarget.m_State.GetItems(iState)
        if not lstState:
            continue
        for oState in lstState:
            if oState.m_Attacker != oWarrior.m_ID:
                return 0
        
    
    return 1


def PassiveCBGetTaskSaveInfo(oWarrior, oEventCB, sKey):
    pfobj = oEventCB.GetObject()
    oTask = pfobj.GetOwnerTask()
    if not oTask:
        return None
    return oTask.GetSaveData(sKey)


def PassiveCBGetExtraExecuteCount(oWarrior, oEventCB, iPerform):
    dAllHit = oWarrior.Query(oEventCB.m_Key, { })
    if not dAllHit:
        return 0
    dMsgInfo = oEventCB.GetCBMsgInfo()
    oSkill = dMsgInfo['Skill']
    if oSkill.m_Base['pfid'] == iPerform:
        iParentActNum = cl_perform.skillcache.GetSkillCacheByIndex(oSkill, SKILLCACHE_PARENTACTNUM)
    else:
        iParentActNum = oSkill.m_Base['ActNum']
    if not iParentActNum:
        return 99
    return len(dAllHit.get('%s-%s' % (oEventCB.m_Key, iParentActNum), { }))


def EventCBGetWeaponBulletComAttrExcludeCurEffect(oListener, oEventCB, sAttr):
    oWeapon = oListener.m_WieldCon.GetCurWeapon(MAIN_HOLD)
    if not oWeapon:
        return 0
    oBulletCom = oWeapon.GetComponent('Bullet')
    if not oBulletCom:
        return 0
    oAttr = oBulletCom.GetItemAttr(sAttr)
    if oAttr:
        sKey = oEventCB.Key()
        if oAttr.m_Type == 'Link':
            oAttr = oAttr.GetLink(oWeapon.m_ID)
        return oAttr.GetExcludeValue([
            sKey])
    return 0


def PassiveCBCheckTarKeyInPFArgsDict(oWarrior, oEventCB, iKey, sArgs):
    dEventInfo = oEventCB.GetCBEventInfo()
    iPerform = dEventInfo['pfid']
    iItemID = dEventInfo['ItemID']
    pfobj = oWarrior.GetPerform(iPerform, iItemID)
    if not pfobj:
        return 0
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iKey = cl_formula.GetResultByData(oWarrior, iKey, dEventInfo, dMsgInfo)
    return iKey in pfobj.GetArgValue(sArgs, { })


def PassiveCBGetTarKeyInPFArgsDict(oWarrior, oEventCB, iKey, sArgs):
    dEventInfo = oEventCB.GetCBEventInfo()
    iPerform = dEventInfo['pfid']
    iItemID = dEventInfo['ItemID']
    pfobj = oWarrior.GetPerform(iPerform, iItemID)
    if not pfobj:
        return 0
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iKey = cl_formula.GetResultByData(oWarrior, iKey, dEventInfo, dMsgInfo)
    dArgs = pfobj.GetArgValue(sArgs, { })
    if iKey not in dArgs:
        return 0
    return dArgs[iKey]

