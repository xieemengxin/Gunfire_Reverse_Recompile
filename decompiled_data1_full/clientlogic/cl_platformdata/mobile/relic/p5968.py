# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/relic/p5968.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/relic/p5968.pyc
# Source Generated with Decompyle++
# File: p5968.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import QUALITY_TYPE_CURSE, RELIC_TYPE_CURSE
from cl_newformula import Func597

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'MoveSpeed', -1000, 0, 0)
    cl_action.CommonListenMsgCallBackByAttr(oWarrior, oLifeCycle, 'MoveSpeed', -1, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.CommonClearForceAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'MoveSpeed')
    if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func597(*a))) >= 80:
        cl_action.CommonForceSetAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'MoveSpeed', int(cl_action.CommonGetOwnerAttrBaseValue(oWarrior, oEventCB.GetCBLifeCycle(), 'MoveSpeed') * 180))


class CPerform(CCustomPerform):
    m_SID = 5968
    m_Name = '枷锁缠身'
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
    m_RelicType = RELIC_TYPE_CURSE
    m_DropShape = 5531
    m_ValidRemove = 0
    m_BasePrice = 0
    m_bCanSell = 0
    m_Quality = QUALITY_TYPE_CURSE

