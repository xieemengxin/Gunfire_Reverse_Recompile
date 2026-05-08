# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterrelic/p25774.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterrelic/p25774.pyc
# Source Generated with Decompyle++
# File: p25774.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.monsterrelic import CMonsterRelic as CCustomPerform
from cl_commondefines import MONSTERPF_TYPE_ATTACK, OBJ_SELF, PF_TYPE_MONSTERACT, QUALITY_TYPE_NORMAL

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckPerformType(oWarrior, oEventCB, PF_TYPE_MONSTERACT, None) and cl_evcon.CheckMonsterPFAttackType(oWarrior, oEventCB, MONSTERPF_TYPE_ATTACK):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1696, 300, { }, 1, -1, None)


class CPerform(CCustomPerform):
    m_SID = 25774
    m_Name = '战术优势'
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
    m_RelicType = 0
    m_HeroRelic = 5774
    m_Quality = QUALITY_TYPE_NORMAL
    m_ExcludeRelic = ()

