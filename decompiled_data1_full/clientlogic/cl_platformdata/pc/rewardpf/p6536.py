# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/rewardpf/p6536.pyc
# RelativePath: clientlogic/cl_platformdata/pc/rewardpf/p6536.pyc
# Source Generated with Decompyle++
# File: p6536.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_formula import g_HpTypeIndex, GetResultByData
from . import CPerform as CCustomPerform
from cl_commondefines import OBJ_SELF
from cl_newformula import Func308

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1339, 0, { }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PREDICTDAMED, -1, 0, 0, 24)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1339, 0, { }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PREDICTDAMED, -1, 0, 0, 24)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1339, 0, { }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PREDICTDAMED, -1, 0, 0, 24)


def Action4(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1339, 0, { }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PREDICTDAMED, -1, 0, 0, 24)


def Action5(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1339, 0, { }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PREDICTDAMED, -1, 0, 0, 24)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    if cl_evcon.GetTargetStateCount(oWarrior, oEventCB, 1339, None, None) > 0 and not cl_evcon.CheckDamFromSelf(oWarrior, oEventCB, 0):
        CustomAction(oWarrior, oEventCB, {
            'HPDamReduce': (lambda *a: Func308(*a) * 15) })


class CPerform(CCustomPerform):
    m_SID = 6536
    m_Name = '紧急防护'
    m_MaxLevel = 5
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3,
        4: Action4,
        5: Action5 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0


def CustomAction(oWarrior, oEventCB, dInfo):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dEventInfo = oEventCB.GetCBEventInfo()
    iReduce = GetResultByData(oWarrior, dInfo['HPDamReduce'], dEventInfo, dMsgInfo)
    lstPredictChange = dMsgInfo['PredictChange']
    iExcessChange = dMsgInfo['ExcessChange']
    iBreakShield = 0
    iBreakArmor = 0
    iCurShield = oWarrior.Shield()
    iCurArmor = oWarrior.Armor()
    iCurHP = oWarrior.HP()
    if iCurShield > 0 and iCurShield <= lstPredictChange[g_HpTypeIndex['Shield']]:
        iBreakShield = 1
    if iCurArmor > 0 and iCurArmor <= lstPredictChange[g_HpTypeIndex['Armor']]:
        iBreakArmor = 1
    if iBreakShield or iBreakArmor:
        idx = g_HpTypeIndex['HP']
        lstPredictChange[idx] = lstPredictChange[idx] * (100 - iReduce) // 100
        iExcessChange = iExcessChange * (100 - iReduce) // 100
        if iCurHP > lstPredictChange[idx] and iExcessChange > 0:
            iTotalDam = lstPredictChange[idx] + iExcessChange
            if iTotalDam >= iCurHP:
                iExcessChange = iTotalDam - iCurHP
                lstPredictChange[idx] = iCurHP
            else:
                lstPredictChange[idx] = iTotalDam
                iExcessChange = 0
        dMsgInfo['ExcessChange'] = iExcessChange

