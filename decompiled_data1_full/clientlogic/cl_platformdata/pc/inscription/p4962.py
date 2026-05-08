# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/inscription/p4962.pyc
# RelativePath: clientlogic/cl_platformdata/pc/inscription/p4962.pyc
# Source Generated with Decompyle++
# File: p4962.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.inscription import CInscription as CCustomPerform
from cl_commondefines import INSCRIPTION_TYPE_EXCLUSIVE, ITEMPERFORM_ENABLE_HOLD
from cl_newformula import Func717

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangeWeaponPerformArgs(oWarrior, oLifeCycle, 4330, 'StateTime', (lambda *a: Func717(*a, **{
'sArg': 'AddStateTime' })))


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonChangeWeaponPerformArgs(oWarrior, oLifeCycle, 4330, 'StateTime', (lambda *a: -Func717(*a, **{
'sArg': 'AddStateTime' })))


class CPerform(CCustomPerform):
    m_SID = 4962
    m_Name = '飞斧'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = {
        1: DisableAction1 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = { }
    m_BaseArgData = {
        'AddStateTime': 400 }
    m_DieDisable = 0
    m_ItemAttr = { }
    m_InscriptionType = INSCRIPTION_TYPE_EXCLUSIVE
    m_ElementType = None
    m_LimitList = ((), (1215,), ())
    m_ExcludeList = ((), (), ())
    m_ItemEnableType = ITEMPERFORM_ENABLE_HOLD

