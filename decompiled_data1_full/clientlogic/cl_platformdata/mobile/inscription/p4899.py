# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/inscription/p4899.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/inscription/p4899.pyc
# Source Generated with Decompyle++
# File: p4899.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.inscription import CInscription as CCustomPerform
from cl_commondefines import EXTGRADE_GROUP1, INSCRIPTION_TYPE_GEMINI, ITEMPERFORM_ENABLE_BOTH

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPONBASEGRADE, -1, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, None, None)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.PassiveLinkBaseGrade(oWarrior, oEventCB.GetCBLifeCycle(), EXTGRADE_GROUP1)


class CPerform(CCustomPerform):
    m_SID = 4899
    m_Name = '等级叠加'
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
    m_InscriptionType = INSCRIPTION_TYPE_GEMINI
    m_ElementType = None
    m_LimitList = ((), (), ())
    m_ExcludeList = ((), (), ())
    m_ItemEnableType = ITEMPERFORM_ENABLE_BOTH

