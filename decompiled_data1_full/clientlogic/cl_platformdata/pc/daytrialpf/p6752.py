# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/daytrialpf/p6752.pyc
# RelativePath: clientlogic/cl_platformdata/pc/daytrialpf/p6752.pyc
# Source Generated with Decompyle++
# File: p6752.pyc (Python 3.6)

from cl_commondefines import DEFEND_TREND_SHIELD, DEFEND_TREND_ARMOR
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.daytrial import CPerform as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonForceSetAttr(oWarrior, oLifeCycle, 'ShieldMax', 0)
    cl_action.CommonForceSetAttr(oWarrior, oLifeCycle, 'ArmorMax', 0)
    cl_action.CommonListenMsgCallBackByAttr(oWarrior, oLifeCycle, 'ShieldMax', -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBackByAttr(oWarrior, oLifeCycle, 'ArmorMax', -1, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, None, None)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBShieldAndArmor2HP(oWarrior, oEventCB, None)


class CPerform(CCustomPerform):
    m_SID = 6752
    m_Name = '护盾值/护甲值全部转化为生命值'
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

