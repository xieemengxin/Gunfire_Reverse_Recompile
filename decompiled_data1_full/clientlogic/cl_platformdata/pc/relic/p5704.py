# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/relic/p5704.pyc
# RelativePath: clientlogic/cl_platformdata/pc/relic/p5704.pyc
# Source Generated with Decompyle++
# File: p5704.pyc (Python 3.6)

from cl_commondefines import DEFEND_TREND_ARMOR, DEFEND_TREND_SHIELD
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import QUALITY_TYPE_NORMAL, RELIC_TYPE_NORMAL

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonForceSetAttr(oWarrior, oLifeCycle, 'ShieldMax', 0)
    cl_action.CommonForceSetAttr(oWarrior, oLifeCycle, 'ArmorMax', 0)
    cl_action.CommonListenMsgCallBackByAttr(oWarrior, oLifeCycle, 'ShieldMax', -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBackByAttr(oWarrior, oLifeCycle, 'ArmorMax', -1, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, None, None)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1106, 0, { }, 1)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonForceSetAttr(oWarrior, oLifeCycle, 'ShieldMax', 0)
    cl_action.CommonForceSetAttr(oWarrior, oLifeCycle, 'ArmorMax', 0)
    cl_action.CommonListenMsgCallBackByAttr(oWarrior, oLifeCycle, 'ShieldMax', -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBackByAttr(oWarrior, oLifeCycle, 'ArmorMax', -1, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, None, None)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1371, 0, { }, 1)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBShieldAndArmor2HP(oWarrior, oEventCB, None)
    cl_evact.EventCBExcessShieldAndArmor2HP(oWarrior, oEventCB)


class CPerform(CCustomPerform):
    m_SID = 5704
    m_Name = '血肉之躯'
    m_MaxLevel = 2
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_RelicType = RELIC_TYPE_NORMAL
    m_DropShape = 5524
    m_ValidRemove = 1
    m_BasePrice = 100
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_NORMAL

