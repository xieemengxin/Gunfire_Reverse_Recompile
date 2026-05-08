# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p4214.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p4214.pyc
# Source Generated with Decompyle++
# File: p4214.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DP, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_condition.GetWeaponBulletCnt(oWarrior, oEventCB.GetCBLifeCycle()) == 0:
        cl_evact.EventChangeSkillCache(oWarrior, oEventCB, 'DebuffProb', 0, -10000)


class CPerform(CCustomPerform):
    m_SID = 4214
    m_Name = '鸩鬼一、二段攻击'
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

