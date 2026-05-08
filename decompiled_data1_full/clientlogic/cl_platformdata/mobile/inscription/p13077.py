# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/inscription/p13077.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/inscription/p13077.pyc
# Source Generated with Decompyle++
# File: p13077.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.inscription import CInscription as CCustomPerform
from cl_commondefines import INSCRIPTION_TYPE_NORMAL, ITEMPERFORM_ENABLE_BOTH, WEAPON_MINOR_PERFORM

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangeSourceWeaponPerformAttrByType(oWarrior, oLifeCycle, WEAPON_MINOR_PERFORM, 'MaxPFBullet', 0, 3000)


class CPerform(CCustomPerform):
    m_SID = 13077
    m_Name = '法杖专属词条1'
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
        'Trajectory': (0, 2000, 0) }
    m_InscriptionType = INSCRIPTION_TYPE_NORMAL
    m_ElementType = None
    m_LimitList = ((23, 24), (), ())
    m_ExcludeList = ((), (), (1704, 1709))
    m_ItemEnableType = ITEMPERFORM_ENABLE_BOTH

