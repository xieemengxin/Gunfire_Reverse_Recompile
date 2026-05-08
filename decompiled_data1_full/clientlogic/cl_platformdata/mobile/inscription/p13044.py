# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/inscription/p13044.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/inscription/p13044.pyc
# Source Generated with Decompyle++
# File: p13044.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.inscription import CInscription as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, INSCRIPTION_TYPE_EXCLUSIVE, ITEMPERFORM_ENABLE_HOLD, OBJ_ATTACK
from cl_newformula import Func546

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, (lambda *a: 400 * Func546(*a, **{
'sid': 9290 })), 0, 0, '')
    CustomAction(oWarrior, oEventCB, {
        'MaxTimes': 25 })


class CPerform(CCustomPerform):
    m_SID = 13044
    m_Name = '织云'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_ItemAttr = { }
    m_InscriptionType = INSCRIPTION_TYPE_EXCLUSIVE
    m_ElementType = None
    m_LimitList = ((), (1214,), ())
    m_ExcludeList = ((), (13043,), ())
    m_ItemEnableType = ITEMPERFORM_ENABLE_HOLD


def CustomAction(oWarrior, oEventCB, dInfo):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'CurVID' not in dMsgInfo:
        return None
    iMaxTimes = dInfo['MaxTimes'] if 'MaxTimes' in dInfo else 0
    dEventInfo = oEventCB.GetCBEventInfo()
    iItemID = dEventInfo['ItemID']
    oSkillMgr = oWarrior.m_Game.m_SkillMgr
    lstSkill = oSkillMgr.GetSkillBySID(9290)
    for oCurSkill in lstSkill:
        if oCurSkill.m_Base['AID'] != oWarrior.m_ID:
            continue
        if oCurSkill.m_Base['Weapon'] != iItemID:
            continue
        if 'DamTimes' not in oCurSkill.m_Collect:
            oCurSkill.m_Collect['DamTimes'] = { }
        dDamTimes = oCurSkill.m_Collect['DamTimes']
        iCurVID = dMsgInfo['CurVID']
        if iCurVID not in dDamTimes:
            dDamTimes[iCurVID] = 1
            continue
        if iMaxTimes != 0 and dDamTimes[iCurVID] < iMaxTimes:
            dDamTimes[iCurVID] += 1
    

