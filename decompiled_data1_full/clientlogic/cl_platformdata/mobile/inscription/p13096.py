# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/inscription/p13096.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/inscription/p13096.pyc
# Source Generated with Decompyle++
# File: p13096.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.inscription import CInscription as CCustomPerform
from cl_commondefines import INSCRIPTION_TYPE_EXCLUSIVE, ITEMPERFORM_ENABLE_HOLD
from cl_newformula import Func717

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveChangeSourceWeaponPerformAttr(oWarrior, oLifeCycle, 9418, 'HitStaticCount', 0, (lambda *a: Func717(*a, **{
'sArg': 'AttBubbleMul' })))
    cl_action.PassiveChangeSourceWeaponPerformAttr(oWarrior, oLifeCycle, 9418, 'HitCount', 0, (lambda *a: Func717(*a, **{
'sArg': 'AttBubbleMul' })))
    cl_action.CommonChangeWeaponPerformArgs(oWarrior, oLifeCycle, 1939, 'DamMul', 600)


class CPerform(CCustomPerform):
    m_SID = 13096
    m_Name = '水枪专属铭刻一'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = { }
    m_BaseArgData = {
        'AttBubbleMul': 10000 }
    m_DieDisable = 0
    m_ItemAttr = { }
    m_InscriptionType = INSCRIPTION_TYPE_EXCLUSIVE
    m_ElementType = None
    m_LimitList = ((), (1418,), ())
    m_ExcludeList = ((), (), ())
    m_ItemEnableType = ITEMPERFORM_ENABLE_HOLD

