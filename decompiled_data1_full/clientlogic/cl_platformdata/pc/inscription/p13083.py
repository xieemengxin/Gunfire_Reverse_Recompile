# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/inscription/p13083.pyc
# RelativePath: clientlogic/cl_platformdata/pc/inscription/p13083.pyc
# Source Generated with Decompyle++
# File: p13083.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.inscription import CInscription as CCustomPerform
from cl_commondefines import INSCRIPTION_TYPE_RARE, ITEMPERFORM_ENABLE_HOLD, PF_SUBMSG_THROW

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33245, 0, { }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_THROW, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_USE_CAREERPF, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33245, 1, 600)


class CPerform(CCustomPerform):
    m_SID = 13083
    m_Name = '第一批法杖专属词条3'
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
    m_LimitList = ((23,), (), ())
    m_ExcludeList = ((), (), ())
    m_ItemEnableType = ITEMPERFORM_ENABLE_HOLD

