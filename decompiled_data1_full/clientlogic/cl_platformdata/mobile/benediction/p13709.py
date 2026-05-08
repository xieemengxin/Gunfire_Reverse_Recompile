# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/benediction/p13709.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/benediction/p13709.pyc
# Source Generated with Decompyle++
# File: p13709.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.benediction import CBenediction as CCustomPerform
from cl_commondefines import INSCRIPTION_TYPE_EXCLUSIVE

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GREATEDROPWEAPON, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GREATEWEAPON, -1, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckRandom(oWarrior, oEventCB, 100, 75):
        cl_evact.EventCBAddWeaponEnhanceCnt(oWarrior, oEventCB, 1, 'Bene13709')


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventCBChangeWeaponInscriptionNumBySource(oWarrior, oEventCB, INSCRIPTION_TYPE_EXCLUSIVE, 1, {
        1: 1,
        2: 1,
        3: 1,
        4: 1,
        5: 1 }, INSCRIPTION_TYPE_EXCLUSIVE)


class CPerform(CCustomPerform):
    m_SID = 13709
    m_Name = '顶级装备'
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
    m_Career = None

