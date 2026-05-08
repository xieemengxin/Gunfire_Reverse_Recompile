# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/inscription/p13054.pyc
# RelativePath: clientlogic/cl_platformdata/pc/inscription/p13054.pyc
# Source Generated with Decompyle++
# File: p13054.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.inscription import CInscription as CCustomPerform
from cl_commondefines import INSCRIPTION_TYPE_GEMINI, ITEMPERFORM_ENABLE_BOTH

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_APPEND_INSCRIPTION, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_REMOVE_INSCRIPTION, -1, 2, 0, 0)
    cl_action.CommonShareWeaponInscription(oWarrior, oLifeCycle)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventCBUpdateShareWeaponInscription(oWarrior, oEventCB, 1)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventCBUpdateShareWeaponInscription(oWarrior, oEventCB, 0)


class CPerform(CCustomPerform):
    m_SID = 13054
    m_Name = '共享铭刻'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        1: DoCallBackAction1,
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_ItemAttr = { }
    m_InscriptionType = INSCRIPTION_TYPE_GEMINI
    m_ElementType = None
    m_LimitList = ((), (), ())
    m_ExcludeList = ((), (), ())
    m_ItemEnableType = ITEMPERFORM_ENABLE_BOTH

