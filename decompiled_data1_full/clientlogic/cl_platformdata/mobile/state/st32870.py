# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st32870.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st32870.pyc
# Source Generated with Decompyle++
# File: st32870.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func429

def StateActAction(oTarget, oLifeCycle):
    if cl_condition.CalFormula(oTarget, oLifeCycle, (lambda *a: Func429(*a, **{
'sArg': 'Att' }))) == 1:
        cl_action.CommonReplaceChildNode(oTarget, oLifeCycle, 'Servant.ServantAttack', 'Servant.ServantLuWuAttack')
    if cl_condition.CalFormula(oTarget, oLifeCycle, (lambda *a: Func429(*a, **{
'sArg': 'Att' }))) == 2:
        cl_action.CommonReplaceChildNode(oTarget, oLifeCycle, 'Servant.ServantAttack', 'Servant.ServantStoneAttack')
        cl_action.CommonReplaceChildNode(oTarget, oLifeCycle, 'Servant.ServantTurret', 'Servant.ServantStoneTurret')
        cl_action.CommonModifyChoosePFArgs(oTarget, oLifeCycle, {
            '0-7': {
                7150: 1000,
                7148: 100,
                7141: 10 },
            '7-18': {
                7150: 1000,
                7142: 10 } })
        cl_action.CommonChangePerformAttr(oTarget, oLifeCycle, 7151, 'AttDistance', 0, 15)
    if cl_condition.CalFormula(oTarget, oLifeCycle, (lambda *a: Func429(*a, **{
'sArg': 'Att' }))) == 3:
        cl_action.CommonReplaceChildNode(oTarget, oLifeCycle, 'Servant.ServantAttack', 'Servant.ServantSeaAttack')
        cl_action.CommonReplaceChildNode(oTarget, oLifeCycle, 'Servant.ServantTurret', 'Servant.ServantSeaTurret')
        cl_action.CommonChangePerformAttr(oTarget, oLifeCycle, 7151, 'AttDistance', 0, 50)
    if cl_condition.CalFormula(oTarget, oLifeCycle, (lambda *a: Func429(*a, **{
'sArg': 'Att' }))) == 4:
        cl_action.CommonPauseMonsterOwnerAgent(oTarget, oLifeCycle)
    if cl_condition.CalFormula(oTarget, oLifeCycle, (lambda *a: Func429(*a, **{
'sArg': 'Att' }))) == 5:
        cl_action.CommonReplaceChildNode(oTarget, oLifeCycle, 'Servant.ServantAttack', 'Servant.ServantLuoHouAttack')
        cl_action.CommonModifyChoosePFArgs(oTarget, oLifeCycle, {
            '0-3': {
                7150: 1000,
                7148: 100,
                7141: 10 },
            '3-18': {
                7150: 1000,
                7142: 10 } })
        cl_action.CommonReplaceChildNode(oTarget, oLifeCycle, 'Servant.ServantTurret', 'Servant.ServantLuoHouTurret')
        cl_action.CommonChangePerformAttr(oTarget, oLifeCycle, 7151, 'AttDistance', 0, 30)
    if cl_condition.CalFormula(oTarget, oLifeCycle, (lambda *a: Func429(*a, **{
'sArg': 'Att' }))) == 6:
        cl_action.CommonReplaceChildNode(oTarget, oLifeCycle, 'Servant.ServantAttack', 'Servant.ServantDMAttack')
        cl_action.CommonReplaceChildNode(oTarget, oLifeCycle, 'Servant.ServantTurret', 'Servant.ServantDMTurret')
        cl_action.CommonModifyChoosePFArgs(oTarget, oLifeCycle, {
            '0-4': {
                7150: 1000,
                7148: 100,
                7141: 10 },
            '4-18': {
                7150: 1000,
                7142: 10 } })
        cl_action.CommonChangePerformAttr(oTarget, oLifeCycle, 7141, 'AttDistance', 0, 1)
        cl_action.CommonChangePerformAttr(oTarget, oLifeCycle, 7148, 'AttDistance', 0, 1)
        cl_action.CommonChangePerformAttr(oTarget, oLifeCycle, 7151, 'AttDistance', 0, 15)
    if cl_condition.CalFormula(oTarget, oLifeCycle, (lambda *a: Func429(*a, **{
'sArg': 'Att' }))) == 7:
        cl_action.CommonReplaceChildNode(oTarget, oLifeCycle, 'Servant.ServantAttack', 'Servant.ServantDemonAttack')
        cl_action.CommonReplaceChildNode(oTarget, oLifeCycle, 'Servant.ServantTurret', 'Servant.ServantDemonTurret')


class CState(cl_state.CState):
    m_SID = 32870
    m_Name = '#NT#御灵师仆特殊行为'
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_EXCLUDE
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
    m_ShowStateCnt = 0
    m_Action = (StateActAction, None)

