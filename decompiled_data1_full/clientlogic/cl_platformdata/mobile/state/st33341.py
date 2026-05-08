# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33341.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33341.pyc
# Source Generated with Decompyle++
# File: st33341.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
from cl_platformdata.custom.state.customaction import CustomAction33341 as CustomAction
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_SWITCH_ATT_PERFORM, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_WEAPON_ELEMENTTYPE_REFRESH, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, -1, 2, 0, 0)
    cl_action.CommonListenServantMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, -1, 2)


def CallBack0(oEventCB, oTarget):
    CustomAction(oTarget, oEventCB, {
        205: {
            'DebuffProb': 10000 },
        206: {
            'DebuffProb': 7000 },
        212: {
            'DebuffProb': 1000,
            'ExtraPF': {
                1313: 1,
                8503: 1 } },
        213: {
            'DebuffProb': 4000,
            'ExtraPF': {
                1310: 1 } },
        216: {
            'DebuffProb': 3000 },
        217: {
            'DebuffProb': 10000,
            'ServantExtraPF': {
                7153: 1 } },
        218: {
            'DebuffProb': 7000,
            'ExtraPF': {
                1328: 1 } },
        219: {
            'DebuffProb': 5000,
            'ExtraPF': {
                1326: 1 } },
        'Init': 1 })


def CallBack1(oEventCB, oTarget):
    CustomAction(oTarget, oEventCB, {
        'ChangeWeapon': 1 })


def CallBack2(oEventCB, oTarget):
    CustomAction(oTarget, oEventCB, {
        'ChangeDebuffProb': 1 })


class CState(cl_state.CState):
    m_SID = 33341
    m_Name = '#NT#词条E1属性变更'
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REPLACE
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
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1,
        2: CallBack2 }

