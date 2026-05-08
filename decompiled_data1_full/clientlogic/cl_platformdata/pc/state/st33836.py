# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33836.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33836.pyc
# Source Generated with Decompyle++
# File: st33836.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import DAM_TYPE_PERFORM, OBJ_SELF, PF_SUBMSG_CAREERPF, SKILLCACHE_INT, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func14, Func429, Func604

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 1330, 1, 0):
        if cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'EnhanceAdvancedCombo') == 0:
            if cl_evcon.EventCBCheckSkillCache(oTarget, oEventCB, SKILLCACHE_INT) == 2 and cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'AlreadyEnhanceBasicL3') == 0:
                cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'EnhanceBasicCombo', 1)
                cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, '33836ComboHaltFrame', (lambda *a: Func14(*a) + 38))
                cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'AlreadyEnhanceBasicL3', 1)
                cl_evact.EventCBSetSkillCustomInfo(oTarget, oEventCB, 'TempAddRecoveryMul', (lambda *a: Func604(*a, **{
'sKey': 'TempAddRecoveryMul' }) + Func429(*a, **{
'sArg': 'TalentAffection' })))
                cl_evact.DelayTriggerGroup(oTarget, oEventCB, 5, 1, 160, 1, 0, { })
            elif cl_evcon.EventCBCheckSkillCache(oTarget, oEventCB, SKILLCACHE_INT) == 3:
                if cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, '33836ComboHaltFrame') == 0 or cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func14(*a))) <= cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, '33836ComboHaltFrame'):
                    cl_evact.EventCBSetSkillCustomInfo(oTarget, oEventCB, 'TempAddRecoveryMul', (lambda *a: Func604(*a, **{
'sKey': 'TempAddRecoveryMul' }) + Func429(*a, **{
'sArg': 'TalentAffection' })))
                    cl_evact.StateCBSelfRemove(oTarget, oEventCB)
    elif cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 1336, 1, 0):
        pass
    if cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'EnhanceBasicCombo') == 0:
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'EnhanceAdvancedCombo', 1)
        if cl_evcon.CBGetPFArgs(oTarget, oEventCB, 1336, 'SkillCount') == 0:
            if cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'AlreadyEnhanceAdvancedH1') == 0:
                cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'AlreadyEnhanceAdvancedH1', 1)
                cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, '33836ComboHaltFrame', (lambda *a: Func14(*a) + 38))
                cl_evact.StateCBChangeSkillDamFactor(oTarget, oEventCB, 0, oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('TransDamFactor'), DAM_TYPE_PERFORM, 0, 0)
                cl_evact.DelayTriggerGroup(oTarget, oEventCB, 5, 1, 160, 1, 0, { })
        elif cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, '33836ComboHaltFrame') == 0 or cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func14(*a))) <= cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, '33836ComboHaltFrame'):
            if cl_evcon.CBGetPFArgs(oTarget, oEventCB, 1336, 'SkillCount') == 1 or cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'AlreadyEnhanceAdvancedH2') == 0:
                cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'AlreadyEnhanceAdvancedH2', 1)
                cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, '33836ComboHaltFrame', (lambda *a: Func14(*a) + 38))
                cl_evact.StateCBChangeSkillDamFactor(oTarget, oEventCB, 0, oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('TransDamFactor'), DAM_TYPE_PERFORM, 0, 0)
                cl_evact.RemoveDelayTriggerGroup(oTarget, oEventCB)
                cl_evact.DelayTriggerGroup(oTarget, oEventCB, 5, 1, 160, 1, 0, { })
            elif cl_evcon.CBGetPFArgs(oTarget, oEventCB, 1336, 'SkillCount') == 2 and cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'AlreadyEnhanceAdvancedH3') == 0:
                cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'AlreadyEnhanceAdvancedH3', 1)
                cl_evact.StateCBChangeSkillDamFactor(oTarget, oEventCB, 0, oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('TransDamFactor'), DAM_TYPE_PERFORM, 0, 0)
                cl_evact.StateCBSelfRemove(oTarget, oEventCB)


def CallBack5(oEventCB, oTarget):
    cl_evact.StateCBSelfRemove(oTarget, oEventCB)


class CState(cl_state.CState):
    m_SID = 33836
    m_Name = '#NT#狮子闪身强化招式'
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
        5: CallBack5 }

