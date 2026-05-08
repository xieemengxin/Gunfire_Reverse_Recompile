# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33075.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33075.pyc
# Source Generated with Decompyle++
# File: st33075.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_ENEMY, STATE_ADD_HIGH, STATE_CLS_ABNORMAL, STATE_EFF_NONE
from cl_newformula import Func619

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonAddState(oTarget, oLifeCycle, 33075, 1003, {
        'MoveSpeedMul': (lambda *a: Func619(*a, **{
'sAttr': 'Decelerate' })) }, 0)


class CState(cl_state.CState):
    m_SID = 33075
    m_Name = '#NT#致命装置-组件减速状态'
    m_Type = STATE_CLS_ABNORMAL
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_HIGH
    m_TargetType = OBJ_ENEMY
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
    
    def CheckHighAttr(self, oTarget, oOldState):
        if 'arg' not in oOldState.m_StateInfo or 'arg' not in self.m_StateInfo:
            return 0
        dOldStateArg = oOldState.m_StateInfo['arg']
        dNewStateArg = self.m_StateInfo['arg']
        iOldStateLevel = dOldStateArg['50105PFLV'] if '50105PFLV' in dOldStateArg else 0
        iNewStateLevel = dNewStateArg['50105PFLV'] if '50105PFLV' in dNewStateArg else 0
        return iNewStateLevel > iOldStateLevel


