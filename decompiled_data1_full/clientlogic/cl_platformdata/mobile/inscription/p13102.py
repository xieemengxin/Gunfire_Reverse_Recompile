# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/inscription/p13102.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/inscription/p13102.pyc
# Source Generated with Decompyle++
# File: p13102.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.inscription import CInscription as CCustomPerform
from cl_commondefines import INSCRIPTION_TYPE_EXCLUSIVE, ITEMPERFORM_ENABLE_HOLD
from cl_newformula import Func578

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangeSourceWeaponSpecialAttr(oWarrior, oLifeCycle, 'BulletSize', (lambda *a: Func578(*a, **{
'sAttr': 'BulletSize' }) * 1))


class CPerform(CCustomPerform):
    m_SID = 13102
    m_Name = '水枪专属铭刻二'
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
    m_ItemAttr = {
        'AttDis': (0, 6000, 0),
        'AttSpeed': (0, 6000, 0),
        'ThumpProb': (2000, 0, 0),
        'BulletSpeed': (0, 6000, 0) }
    m_InscriptionType = INSCRIPTION_TYPE_EXCLUSIVE
    m_ElementType = None
    m_LimitList = ((), (1418,), ())
    m_ExcludeList = ((), (), ())
    m_ItemEnableType = ITEMPERFORM_ENABLE_HOLD

