# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/inscription/p4840.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/inscription/p4840.pyc
# Source Generated with Decompyle++
# File: p4840.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.inscription import CInscription as CCustomPerform
from cl_commondefines import INSCRIPTION_TYPE_GEMINI, ITEMPERFORM_ENABLE_BOTH

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveSetLinkAttr(oWarrior, oLifeCycle, 'Trajectory', None)


class CPerform(CCustomPerform):
    m_SID = 4840
    m_Name = '弹道复制'
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
    m_InscriptionType = INSCRIPTION_TYPE_GEMINI
    m_ElementType = None
    m_LimitList = ((), (), ())
    m_ExcludeList = ((7, 19, 20), (), ())
    m_ItemEnableType = ITEMPERFORM_ENABLE_BOTH

