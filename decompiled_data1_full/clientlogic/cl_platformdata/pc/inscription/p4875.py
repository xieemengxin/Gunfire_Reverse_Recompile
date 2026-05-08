# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/inscription/p4875.pyc
# RelativePath: clientlogic/cl_platformdata/pc/inscription/p4875.pyc
# Source Generated with Decompyle++
# File: p4875.pyc (Python 3.6)

from cl_only import PY_FLAG_DEAD, Second2Frame, Functor
from cl_commondefines import OBJ_ATTACK, OBJ_VICTIM, DAM_TYPE_WEAPON, DAM_USE_ALL, DAM_TYPE_WEAKNESS, WARRIOR_MONSTER
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
import cl_math
import cl_object.reason
import cl_snetwar
from cl_perform.inscription import CInscription as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, INSCRIPTION_TYPE_EXCLUSIVE, ITEMPERFORM_ENABLE_HOLD, OBJ_SELF

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_CMD_SWITCHSNIPE, -1, 0, 0, 0)
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    if cl_evcon.CheckShootStatus(oWarrior, oEventCB):
        cl_evact.EventClientBehavior(oWarrior, oEventCB, 2011, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckShootStatus(oWarrior, oEventCB):
        CustomAction(oWarrior, oEventCB, {
            'ClientBehavior': 2012,
            'TargetNum': 2 })


class CPerform(CCustomPerform):
    m_SID = 4875
    m_Name = '死亡标记'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_ItemAttr = { }
    m_InscriptionType = INSCRIPTION_TYPE_EXCLUSIVE
    m_ElementType = None
    m_LimitList = ((11,), (), ())
    m_ExcludeList = ((), (), ())
    m_ItemEnableType = ITEMPERFORM_ENABLE_HOLD


def CustomAction(oWarrior, oEventCB, dInfo):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return None
    dEvent = oEventCB.GetCBEventInfo()
    iWeapon = dEvent['ItemID']
    oWeapon = oWarrior.m_WieldCon.GetItemByID(iWeapon)
    if not oWeapon:
        return None
    sKey = 'LockTarget%d' % CPerform.m_SID
    lstTarget = oWeapon.QueryTmp(sKey, [])
    if not lstTarget:
        return None
    iTargetNum = dInfo['TargetNum'] if 'TargetNum' in dInfo else 1
    if len(lstTarget) > iTargetNum:
        lstTarget = lstTarget[:iTargetNum]
    oGame = oWarrior.m_Game
    vOwner = oWarrior.GetPos()
    iAttack = oWarrior.m_ID
    oSkill = dMsgInfo['Skill']
    fBulletSpeed = oSkill.m_Cache['BulletSpeed']
    iAtt = oSkill.m_Cache['Att']
    iCrazyEff = oSkill.m_Cache['CrazyEff']
    iElementType = oSkill.m_Cache['ElementType']
    dDamFactor = dMsgInfo['DamFactor']
    iClientBehavior = dInfo['ClientBehavior'] if 'ClientBehavior' in dInfo else 2012
    for iTarget in lstTarget:
        oTarget = oGame.GetObject(iTarget, PY_FLAG_DEAD)
        if not oTarget or oTarget.m_FightType & WARRIOR_MONSTER != WARRIOR_MONSTER:
            continue
        vTarget = oTarget.GetPos()
        fDis = cl_math.CalDistance3D(vOwner, vTarget)
        iFlyFrame = Second2Frame(fDis / fBulletSpeed)
        if iFlyFrame > 0:
            sCallKey = 'pf%d-%d' % (CPerform.m_SID, oSkill.m_Base['ActNum'])
            oTarget.Call_Out(Functor(DelayDamage, oTarget, iAttack, iAtt, iCrazyEff, iElementType, iClientBehavior, dDamFactor), iFlyFrame, sCallKey)
            continue
        DelayDamage(oTarget, iAttack, iAtt, iCrazyEff, iElementType, iClientBehavior, dDamFactor)
    


def DelayDamage(oTarget, iAttack, iAtt, iCrazyEff, iElementType, iBehavior, dDamFactor):
    if oTarget.IsDead():
        return None
    oGame = oTarget.m_Game
    iTarget = oTarget.m_ID
    oAttack = oGame.GetObject(iAttack)
    if oAttack and iBehavior:
        cl_snetwar.GS2CTriggerBehavior(oTarget.m_Game, iTarget, iBehavior, [
            oAttack.m_PlayerID])
    iDamage = iAtt
    oReason = cl_object.reason.CStrReason('pf%d' % CPerform.m_SID, None, {
        'DamType': DAM_TYPE_WEAPON | DAM_USE_ALL | iElementType | DAM_TYPE_WEAKNESS })
    lstDam = [
        (iDamage, oReason)]
    dDamage = {
        'AID': iAttack,
        'CurVID': iTarget,
        'MainDam': lstDam,
        'FlowDam': [],
        'RS': oReason,
        'DamFactor': dDamFactor,
        'CrazyEff': iCrazyEff }
    oTarget.ReceiveDamage(iAttack, dDamage)

