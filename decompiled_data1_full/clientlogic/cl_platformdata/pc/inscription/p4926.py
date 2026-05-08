# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/inscription/p4926.pyc
# RelativePath: clientlogic/cl_platformdata/pc/inscription/p4926.pyc
# Source Generated with Decompyle++
# File: p4926.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.inscription import CInscription as CCustomPerform
from cl_commondefines import INSCRIPTION_TYPE_EXCLUSIVE, ITEMPERFORM_ENABLE_HOLD
from cl_newformula import Func338

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_TRIGGERSKILL, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.PassiveCheckFromSameItem(oWarrior, oEventCB) and cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'pf4926', None) == 0:
        cl_evact.PassiveCBSetCollectInfo(oWarrior, oEventCB, 'pf4926', 1, 0)
        cl_evact.EventChangeSkillCache(oWarrior, oEventCB, 'LuckyHit', (lambda *a: Func338(*a) * 25 + 0), 0)


class CPerform(CCustomPerform):
    m_SID = 4926
    m_Name = '正义'
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
    m_InscriptionType = INSCRIPTION_TYPE_EXCLUSIVE
    m_ElementType = None
    m_LimitList = ((), (1408,), ())
    m_ExcludeList = ((), (13024,), ())
    m_ItemEnableType = ITEMPERFORM_ENABLE_HOLD

