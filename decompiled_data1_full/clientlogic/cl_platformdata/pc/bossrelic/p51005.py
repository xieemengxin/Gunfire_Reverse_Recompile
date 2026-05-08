# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/bossrelic/p51005.pyc
# RelativePath: clientlogic/cl_platformdata/pc/bossrelic/p51005.pyc
# Source Generated with Decompyle++
# File: p51005.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.bossrelic import CBossRelic as CCustomPerform
from cl_commondefines import MODEL_TYPE_SPHERE, SIDE_TYPE_MONSTER

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_MONSTER_START_HATE, -1, 0, 1, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.CommonCreateBuildOnRangePlayPoint(oWarrior, oEventCB.GetCBLifeCycle(), 1206, MODEL_TYPE_SPHERE, SIDE_TYPE_MONSTER, 'BOSS', 1)


class CPerform(CCustomPerform):
    m_SID = 51005
    m_Name = '极地妖王试炼'
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
    m_DieDisable = 1
    m_HeroRelic = 0
    m_LimitMonster = { }
    m_ExcludeMonster = {
        3924: 1,
        3925: 1,
        3926: 1,
        3902: 1,
        3904: 1,
        3910: 1,
        3911: 1 }

