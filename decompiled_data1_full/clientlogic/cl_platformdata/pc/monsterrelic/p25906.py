# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterrelic/p25906.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterrelic/p25906.pyc
# Source Generated with Decompyle++
# File: p25906.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.monsterrelic import CMonsterRelic as CCustomPerform
from cl_commondefines import MG_CASH, MG_SOURCE_KILLMONSTER, QUALITY_TYPE_CURSE

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_OWNERGETMINIGAMETIME, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_condition.RandomTrigger(oWarrior, oEventCB.GetCBLifeCycle(), 10, 2) and cl_evcon.CheckMiniGameSource(oWarrior, oEventCB, MG_SOURCE_KILLMONSTER) and cl_evcon.CheckMiniGameType(oWarrior, oEventCB, MG_CASH):
        cl_evact.PassiveChangeMiniGameInfo(oWarrior, oEventCB, 0, 0, 10000, 0)


class CPerform(CCustomPerform):
    m_SID = 25906
    m_Name = '黑毛公鸡'
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
    m_HeroRelic = 5906
    m_Quality = QUALITY_TYPE_CURSE
    m_ExcludeRelic = ()

