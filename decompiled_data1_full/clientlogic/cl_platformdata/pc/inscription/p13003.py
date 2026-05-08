# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/inscription/p13003.pyc
# RelativePath: clientlogic/cl_platformdata/pc/inscription/p13003.pyc
# Source Generated with Decompyle++
# File: p13003.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.inscription import CInscription as CCustomPerform
from cl_commondefines import INSCRIPTION_TYPE_NORMAL, ITEMPERFORM_ENABLE_HOLD, PF_SUBMSG_FILLBULLET

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_FILLBULLET, 0, 0, 0)
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK_END, -1, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveCBChangeSourceWeaponAttr(oWarrior, oEventCB, 'Att', 0, 8000)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.PassiveCBChangeSourceWeaponAttr(oWarrior, oEventCB, 'Att', 0, 0)


class CPerform(CCustomPerform):
    m_SID = 13003
    m_Name = '蓄势待发-近战（排斥火锏）'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_ItemAttr = { }
    m_InscriptionType = INSCRIPTION_TYPE_NORMAL
    m_ElementType = None
    m_LimitList = ((20,), (), ())
    m_ExcludeList = ((6, 10), (), (1606,))
    m_ItemEnableType = ITEMPERFORM_ENABLE_HOLD

