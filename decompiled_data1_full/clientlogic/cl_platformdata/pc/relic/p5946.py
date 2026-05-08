# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/relic/p5946.pyc
# RelativePath: clientlogic/cl_platformdata/pc/relic/p5946.pyc
# Source Generated with Decompyle++
# File: p5946.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import DAM_MASK_CLASS, DAM_MASK_ELEMENT, QUALITY_TYPE_CURSE, RELIC_TYPE_CURSE
from cl_newformula import Func379

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_HP_CHANGE, -1, 0, 0, 0)
    cl_action.CommonModifyDamResistance(oWarrior, oLifeCycle, (lambda *a: -(25 * Func379(*a))), DAM_MASK_CLASS, DAM_MASK_ELEMENT, 1)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.CommonModifyDamResistance(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: -(25 * Func379(*a))), DAM_MASK_CLASS, DAM_MASK_ELEMENT, 1)


class CPerform(CCustomPerform):
    m_SID = 5946
    m_Name = '脆弱之躯'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = {
        'StateSID': 33354 }
    m_DieDisable = 1
    m_RelicType = RELIC_TYPE_CURSE
    m_DropShape = 5531
    m_ValidRemove = 0
    m_BasePrice = 0
    m_bCanSell = 0
    m_Quality = QUALITY_TYPE_CURSE

