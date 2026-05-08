# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33634.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33634.pyc
# Source Generated with Decompyle++
# File: st33634.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import DAM_MASK_ELEMENT, OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func404, Func429

def StateActAction(oTarget, oLifeCycle):
    cl_action.StateSetSelfCount(oTarget, oLifeCycle, (lambda *a: Func429(*a, **{
'sArg': 'StateCount' })))


def StateCountAction(oTarget, oLifeCycle):
    cl_action.CommonChangeAttr(oTarget, oLifeCycle, 'ArmorMax', 0, (lambda *a: Func404(*a) * 100), 0)
    cl_action.CommonChangeAttr(oTarget, oLifeCycle, 'ShieldMax', 0, (lambda *a: Func404(*a) * 100), 0)
    cl_action.CommonChangeAttr(oTarget, oLifeCycle, 'HPMax', 0, (lambda *a: Func404(*a) * 100), 0)
    cl_action.CommonChangeAttr(oTarget, oLifeCycle, 'MoveSpeed', (lambda *a: Func404(*a) * 50), 0, 0)
    cl_action.CommonChangeBaseDamRatio(oTarget, oLifeCycle, 0, (lambda *a: Func404(*a) * 300), DAM_MASK_ELEMENT, 1)
    cl_action.CommonChangeCareerPerformAttr(oTarget, oLifeCycle, 'ColdTime', (lambda *a: -Func404(*a) * 50), 0, 1)


class CState(cl_state.CState):
    m_SID = 33634
    m_Name = '超载令牌'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_EXCLUDE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 60
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 0
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_Action = (StateActAction, None)
    m_CountFunc = {
        'action': StateCountAction }

