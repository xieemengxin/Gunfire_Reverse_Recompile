# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st20026.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st20026.pyc
# Source Generated with Decompyle++
# File: st20026.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import CURE_TYPE_PERFORM, DAM_TYPE_FIRE, DAM_TYPE_PERSISTENCE, DAM_TYPE_TRUE, DAM_USE_ALL, FIGHT3_KEY_EVACT_IGNELEFIRE, OBJ_ENEMY, OBJ_SELF, STATE_ADD_HIGH, STATE_CLS_ABNORMAL, STATE_EFF_NONE, WARRIOR_HERO
from cl_newformula import Func408, Func417

def DelayAction(oTarget, oLifeCycle):
    if cl_condition.CheckTargetFightType(oTarget, oLifeCycle, WARRIOR_HERO):
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, None, None)
    else:
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 1, None, None)


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.CommonSendRemoveDeBuffStateMessage(oTarget, oLifeCycle)


def CallBack0(oEventCB, oTarget):
    if not cl_evcon.CheckHasLogicKey(oTarget, oEventCB, FIGHT3_KEY_EVACT_IGNELEFIRE):
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        if cl_evcon.CheckHasState(oTarget, oEventCB, 32548):
            cl_evact.EventTargetCure(oTarget, oEventCB, (lambda *a: Func408(*a) * 20 / 100 + 0), CURE_TYPE_PERFORM | DAM_USE_ALL, 1, 0, None)
        else:
            cl_evact.EventTargetDamage(oTarget, oEventCB, (lambda *a: Func408(*a) * 20 / 100 + 0), DAM_TYPE_PERSISTENCE | DAM_TYPE_TRUE | DAM_TYPE_FIRE | DAM_USE_ALL, 0, 0, 1, None, None, None, None, None, None, None, None)


def CallBack1(oEventCB, oTarget):
    if not cl_evcon.CheckHasLogicKey(oTarget, oEventCB, FIGHT3_KEY_EVACT_IGNELEFIRE):
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_evact.EventTargetDamage(oTarget, oEventCB, (lambda *a: (Func408(*a) * 20 / 100) * Func417(*a, **{
'iType': 'FireAbnormalFactor' }) / 100 + 0), DAM_TYPE_PERSISTENCE | DAM_TYPE_TRUE | DAM_TYPE_FIRE | DAM_USE_ALL, 1, 0, 1, None, None, None, None, None, None, None, None)


class CState(cl_state.CState):
    m_SID = 20026
    m_Name = '燃烧异常'
    m_DieRemove = 1
    m_IsShow = 1
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
    m_Action = (None, StateRemoveAction)
    m_DelayAction = {
        'action': DelayAction,
        'delay': 100,
        'firsttime': 50 }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1 }
    
    def CheckHighAttr(self, oTarget, oOldState):
        iOldVal = oOldState.GetArgValue('AbnormalSourceDam', None)
        if iOldVal is None:
            dOldCache = oOldState.GetArgValue('Cache')
            iOldVal = dOldCache['Att'] if dOldCache else 0
        iCurVal = self.GetArgValue('AbnormalSourceDam', None)
        if iCurVal is None:
            dCurCache = self.GetArgValue('Cache')
            iCurVal = dCurCache['Att'] if dCurCache else 0
        return iOldVal < iCurVal


