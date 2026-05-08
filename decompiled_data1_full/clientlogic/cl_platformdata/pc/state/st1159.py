# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st1159.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st1159.pyc
# Source Generated with Decompyle++
# File: st1159.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_SYNC, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func404

def StateCountAction(oTarget, oLifeCycle):
    cl_action.StateChangeSourceWeaponAttr(oTarget, oLifeCycle, 'Accuracy', (lambda *a: Func404(*a) * -20 + 0), 0)
    cl_action.StateChangeSourceWeaponAttr(oTarget, oLifeCycle, 'Att', 0, (lambda *a: Func404(*a) * 1000))
    cl_action.StateChangeSourceWeaponAttr(oTarget, oLifeCycle, 'CrazyEff', (lambda *a: Func404(*a) * 4000), 0)


class CState(cl_state.CState):
    m_SID = 1159
    m_Name = '#NT#新瞳被动效果'
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_SYNC
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 5
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 0
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_CountFunc = {
        'action': StateCountAction }

