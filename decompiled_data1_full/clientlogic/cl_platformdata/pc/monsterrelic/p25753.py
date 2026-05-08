# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterrelic/p25753.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterrelic/p25753.pyc
# Source Generated with Decompyle++
# File: p25753.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.monsterrelic import CMonsterRelic as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, EXECUTETYPE_RELICPF, OBJ_VICTIM, QUALITY_TYPE_NORMAL, WARRIOR_HERO

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.GetVictimHPRatio(oWarrior, oEventCB) <= 15 and cl_evcon.CheckVictimFightType(oWarrior, oEventCB, WARRIOR_HERO):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.EventCBTargetDeath(oWarrior, oEventCB, EXECUTETYPE_RELICPF)


class CPerform(CCustomPerform):
    m_SID = 25753
    m_Name = '终焉审判'
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
    m_HeroRelic = 5753
    m_Quality = QUALITY_TYPE_NORMAL
    m_ExcludeRelic = ()

