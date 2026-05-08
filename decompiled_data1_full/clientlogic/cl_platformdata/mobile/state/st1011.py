# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st1011.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st1011.pyc
# Source Generated with Decompyle++
# File: st1011.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
import cl_state
from cl_commondefines import OBJ_ENEMY, STATE_ADD_SAMESOURCE, STATE_CLS_SPECIAL, STATE_EFF_SUBSPD

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonChangeAttr(oTarget, oLifeCycle, 'MoveSpeed', oLifeCycle.m_Owner.GetArgValue('MoveSpeedMul'), 0, None)
    cl_action.CommonSendReduceSpeedMessage(oTarget, oLifeCycle)


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.CommonSendReduceSpeedEndMessage(oTarget, oLifeCycle)


class CState(cl_state.CState):
    m_SID = 1011
    m_Name = '#NT#通用减速（特殊，有标签）'
    m_DieRemove = 1
    m_DyingRemove = 1
    m_Type = STATE_CLS_SPECIAL
    m_EffType = STATE_EFF_SUBSPD
    m_AddType = STATE_ADD_SAMESOURCE
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
    m_Action = (StateActAction, StateRemoveAction)
    
    def Enable(self, oTarget):
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_ADD_REDUCESPEEDSTATE, oTarget, {
            'StateID': self.m_ID })
        if cl_state.ValidSubSpeedEnable(oTarget, self):
            return None
        super().Enable(oTarget)

    
    def Release(self):
        if not self.m_Game:
            return None
        oOwner = self.m_Game.GetObject(self.m_Owner)
        if oOwner:
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_REMOVE_REDUCESPEEDSTATE, oOwner, {
                'StateID': self.m_ID,
                'TimeType': self.m_TimeType })
            oOwner.DelStateTime(self.m_ID)
        self.m_LifeCycle.Release()
        self.m_LifeCycle = None
        self.m_Game = None


