# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st1890.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st1890.pyc
# Source Generated with Decompyle++
# File: st1890.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
from . import statedata
from cl_commondefines import OBJ_SELF, STATE_ADD_REFRESHORSYNC, STATE_CLS_ABNORMAL, STATE_EFF_SUBSPD

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonChangeAttr(oTarget, oLifeCycle, 'MoveSpeed', oLifeCycle.m_Owner.GetArgValue('MoveSpeedMul'), 0, 0)


class CState(statedata.CStateData):
    m_SID = 1890
    m_Name = '#NT#同来源刷新时间减速'
    m_Type = STATE_CLS_ABNORMAL
    m_EffType = STATE_EFF_SUBSPD
    m_AddType = STATE_ADD_REFRESHORSYNC
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 0
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 0
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_Action = (StateActAction, None)

