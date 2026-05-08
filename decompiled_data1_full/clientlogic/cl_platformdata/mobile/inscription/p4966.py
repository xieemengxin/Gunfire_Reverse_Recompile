# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/inscription/p4966.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/inscription/p4966.pyc
# Source Generated with Decompyle++
# File: p4966.pyc (Python 3.6)

from cl_platformdata.custom.inscription.customaction import CustomAction4966 as CustomAction
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.inscription import CInscription as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DPSUBMSG_NOFIRE, INSCRIPTION_TYPE_EXCLUSIVE, ITEMPERFORM_ENABLE_HOLD

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DP, DPSUBMSG_NOFIRE, 0, 0, 0)
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK_END, DPSUBMSG_NOFIRE, 1, 0, 0)
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_HALT, -1, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 9791, 0, 0):
        cl_action.CommonListenSnapshotMsg(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_ATTACKPF, ATTACKERSUBMSG_NORMAL, 2, 0, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 9791, 0, 0):
        cl_action.CommonDoneSnapshotMsg(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_ATTACKPF, ATTACKERSUBMSG_NORMAL)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        1722: 1 }, 0, 0):
        CustomAction(oWarrior, oEventCB, {
            'Perform': 9791,
            'Key': 'PF4966',
            'AddValue': 25,
            'MaxValue': 300 })


class CPerform(CCustomPerform):
    m_SID = 4966
    m_Name = '凤鸣专属1'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_ItemAttr = { }
    m_InscriptionType = INSCRIPTION_TYPE_EXCLUSIVE
    m_ElementType = None
    m_LimitList = ((), (1701,), ())
    m_ExcludeList = ((), (), ())
    m_ItemEnableType = ITEMPERFORM_ENABLE_HOLD

