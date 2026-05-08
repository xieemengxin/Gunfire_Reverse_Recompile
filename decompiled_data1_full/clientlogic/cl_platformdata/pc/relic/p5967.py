# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/relic/p5967.pyc
# RelativePath: clientlogic/cl_platformdata/pc/relic/p5967.pyc
# Source Generated with Decompyle++
# File: p5967.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import LEVEL_TYPE_BOSS, LEVEL_TYPE_FIGHT, QUALITY_TYPE_CURSE, RELIC_TYPE_CURSE
from cl_newformula import Func207

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckEnterNewSecne(oWarrior, oEventCB):
        if cl_evcon.CheckLevelType(oWarrior, oEventCB, LEVEL_TYPE_BOSS) or cl_evcon.CheckLevelType(oWarrior, oEventCB, LEVEL_TYPE_FIGHT):
            cl_action.CommonAddWarCash(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: -(Func207(*a) * 0.07)))


class CPerform(CCustomPerform):
    m_SID = 5967
    m_Name = '破洞口袋'
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

