# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/inscription/p4815.pyc
# RelativePath: clientlogic/cl_platformdata/pc/inscription/p4815.pyc
# Source Generated with Decompyle++
# File: p4815.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.inscription import CInscription as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, EXECUTETYPE_INSCRIPTIONPF, INSCRIPTION_TYPE_RARE, ITEMPERFORM_ENABLE_HOLD, OBJ_VICTIM, WARRIOR_NORBOX, WARRIOR_NORLARGESUMMON, WARRIOR_NORMAL

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckVictimFightType(oWarrior, oEventCB, WARRIOR_NORMAL) and cl_evcon.CheckHitWeakness(oWarrior, oEventCB, None) and cl_evcon.CheckRandom(oWarrior, oEventCB, 100, 25) and cl_evcon.CheckVictimFightType(oWarrior, oEventCB, WARRIOR_NORBOX) == 0 and cl_evcon.CheckVictimFightType(oWarrior, oEventCB, WARRIOR_NORLARGESUMMON) == 0:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.EventCBTargetDeath(oWarrior, oEventCB, EXECUTETYPE_INSCRIPTIONPF)


class CPerform(CCustomPerform):
    m_SID = 4815
    m_Name = '一击而溃'
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
    m_ItemAttr = { }
    m_InscriptionType = INSCRIPTION_TYPE_RARE
    m_ElementType = None
    m_LimitList = ((), (1505, 1504, 1503, 1502, 1501, 1507, 1508, 1510, 1513, 1215), ())
    m_ExcludeList = ((), (), ())
    m_ItemEnableType = ITEMPERFORM_ENABLE_HOLD

