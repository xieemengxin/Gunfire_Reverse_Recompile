# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterrelic/p25801.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterrelic/p25801.pyc
# Source Generated with Decompyle++
# File: p25801.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.monsterrelic import CMonsterRelic as CCustomPerform
from cl_commondefines import DAM_TYPE_SCENE, DAM_TYPE_TRUE, DAM_USE_ALL, QUALITY_TYPE_LOW, WARRIOR_HERO
from cl_newformula import Func374

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BREAKSHIELD, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BREAKARMOR, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetRangeTargetByFightType(oWarrior, oEventCB, 12, WARRIOR_HERO, None, 0, 0, 0, 0, { }, -1, None, None, None, None)
    cl_evact.EventSplitTargetExecCBFuncAction(oWarrior, oEventCB, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 20028, 600, { }, -1, -1, None)
    cl_evact.EventTargetDamage(oWarrior, oEventCB, (lambda *a: Func374(*a) * 15 / 100), DAM_TYPE_SCENE | DAM_TYPE_TRUE | DAM_USE_ALL, 1, 0, 0, 0, 0, 0, 0, 0, None, None, None)


class CPerform(CCustomPerform):
    m_SID = 25801
    m_Name = '雷鸣反击'
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
    m_RelicType = 0
    m_HeroRelic = 5801
    m_Quality = QUALITY_TYPE_LOW
    m_ExcludeRelic = ()

