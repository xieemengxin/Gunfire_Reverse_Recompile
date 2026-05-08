# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/inscription/p13088.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/inscription/p13088.pyc
# Source Generated with Decompyle++
# File: p13088.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.inscription import CInscription as CCustomPerform
from cl_commondefines import INSCRIPTION_TYPE_RARE, ITEMPERFORM_ENABLE_HOLD

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33282, 0, { }, 1)


class CPerform(CCustomPerform):
    m_SID = 13088
    m_Name = '幸运基伤'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = { }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_ItemAttr = { }
    m_InscriptionType = INSCRIPTION_TYPE_RARE
    m_ElementType = None
    m_LimitList = ((23,), (), ())
    m_ExcludeList = ((), (), ())
    m_ItemEnableType = ITEMPERFORM_ENABLE_HOLD

