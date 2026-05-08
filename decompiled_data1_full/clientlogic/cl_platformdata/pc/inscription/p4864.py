# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/inscription/p4864.pyc
# RelativePath: clientlogic/cl_platformdata/pc/inscription/p4864.pyc
# Source Generated with Decompyle++
# File: p4864.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.inscription import CInscription as CCustomPerform
from cl_commondefines import INSCRIPTION_TYPE_NORMAL, ITEMPERFORM_ENABLE_HOLD
from cl_newformula import Func345

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, -1, 0, 0, 0)
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK_END, -1, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.PassiveCheckFromSameItem(oWarrior, oEventCB):
        cl_evact.EventCBRecordHitCartoon(oWarrior, oEventCB, None)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.PassiveCheckFromSameItem(oWarrior, oEventCB):
        cl_evact.EventCBRecoverBulletByMishitBullet(oWarrior, oEventCB, (lambda *a: Func345(*a)), 0)


class CPerform(CCustomPerform):
    m_SID = 4864
    m_Name = '物尽其用'
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
    m_LimitList = ((), (), ())
    m_ExcludeList = ((7, 12, 19, 20), (), (1409, 1408, 1407, 1406, 1404, 1401, 1415, 1801, 1701))
    m_ItemEnableType = ITEMPERFORM_ENABLE_HOLD

