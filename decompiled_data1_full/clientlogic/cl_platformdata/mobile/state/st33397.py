# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33397.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33397.pyc
# Source Generated with Decompyle++
# File: st33397.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, CREATE_PLANT, DAM_MASK_ELEMENT, EQUIP_LASER, OBJ_SELF, OBJ_VICTIM, PF_SUBMSG_CAREERPF, PF_SUBMSG_THROW, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_only import PY_FLAG_EXCLUDEMONSTERHATE
from cl_newformula import Func429, Func437, Func604, Func731

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_USE_CAREERPF, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_THROW, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DP, -1, 5, 0, 0)
    cl_action.CommonSetPyFlag(oTarget, oLifeCycle, PY_FLAG_EXCLUDEMONSTERHATE, 1)
    cl_action.CommonSetCustomData(oTarget, oLifeCycle, 'ActiveHiding', 1)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_WEAPONFIRE, -1, 16, 0, 0)
    if cl_condition.CheckHero(oTarget, oLifeCycle, 217):
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 4, 0, 0)
    if cl_condition.CheckHero(oTarget, oLifeCycle, 213):
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 8, 0, 0)
    if cl_condition.CalFormula(oTarget, oLifeCycle, (lambda *a: Func731(*a, **{
'iSuit': 15112 }))) < 3:
        cl_action.CommonChangeAttr(oTarget, oLifeCycle, 'MoveSpeed', 3000, 0, 0)
        cl_action.CommonStateStatistics(oTarget, oLifeCycle, 33397, 4000, 'RatioAdd')
        cl_action.CommonStateStatistics(oTarget, oLifeCycle, 33397, 800, 'RatioMul')
    else:
        cl_action.CommonChangeAttr(oTarget, oLifeCycle, 'MoveSpeed', 6000, 0, 0)
        cl_action.CommonStateStatistics(oTarget, oLifeCycle, 33397, 5000, 'RatioAdd')
        cl_action.CommonStateStatistics(oTarget, oLifeCycle, 33397, 1000, 'RatioMul')
    if cl_condition.CalFormula(oTarget, oLifeCycle, (lambda *a: Func429(*a, **{
'sArg': 'AddDam' }))):
        cl_action.CommonSetStateCount(oTarget, oLifeCycle, 33489, 10000, None)
    else:
        cl_action.CommonAddState(oTarget, oLifeCycle, 33397, 33491, {
            'Att': oLifeCycle.m_Owner.GetArgValue('Cache') }, 0)
    if cl_condition.CheckHero(oTarget, oLifeCycle, 219):
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 2, 0, 0)
    if cl_condition.CheckHero(oTarget, oLifeCycle, 207):
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 11, 0, 0)
    if cl_condition.CheckHero(oTarget, oLifeCycle, 220):
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 17, 0, 0)
    if cl_condition.CheckHero(oTarget, oLifeCycle, 221):
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 18, 0, 0)


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 3, 0, 0)
    cl_action.CommonSetStateCount(oTarget, oLifeCycle, 33489, 0, None)
    cl_action.CommonSetCustomData(oTarget, oLifeCycle, 'ActiveHiding', 0)


def CallBack0(oEventCB, oTarget):
    if not cl_evcon.CheckInPointPerform(oTarget, oEventCB, {
        1310: 1 }, 0, 0) or cl_evcon.CheckInPointPerform(oTarget, oEventCB, {
        1325: 1,
        1301: 1,
        1305: 1,
        1918: 1 }, 0, 0):
        if cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func429(*a, **{
'sArg': 'AddDam' }))):
            cl_evact.StateCBChangeSkillDamFactor(oTarget, oEventCB, 0, (lambda *a: (Func437(*a, **{
'sKey': 'RatioAdd' }) + Func437(*a, **{
'sKey': 'RatioMul' }) * Func429(*a, **{
'sArg': 'Cover' })) * Func429(*a, **{
'sArg': 'Cover' })), DAM_MASK_ELEMENT, 1, 0)
            cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 33402, 200, {
                'Att': oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('Cover'),
                'TalentLevel': cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'RatioAdd'),
                'Cache': cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'RatioMul'),
                'AbnormalSourceDam': 1 }, None)
            cl_evact.StateCBSelfRemove(oTarget, oEventCB)
        else:
            cl_evact.StateCBSelfRemove(oTarget, oEventCB)


def CallBack1(oEventCB, oTarget):
    if not cl_evcon.CheckPerformUnCrtByOwner(oTarget, oEventCB):
        if cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func429(*a, **{
'sArg': 'AddDam' }))):
            cl_evact.StateCBChangeSkillDamFactor(oTarget, oEventCB, 0, (lambda *a: (Func437(*a, **{
'sKey': 'RatioAdd' }) + Func437(*a, **{
'sKey': 'RatioMul' }) * Func429(*a, **{
'sArg': 'Cover' })) * Func429(*a, **{
'sArg': 'Cover' })), DAM_MASK_ELEMENT, 1, 0)
            cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 33402, 200, {
                'Att': oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('Cover'),
                'TalentLevel': cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'RatioAdd'),
                'Cache': cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'RatioMul'),
                'AbnormalSourceDam': 1 }, None)
            cl_evact.StateCBSelfRemove(oTarget, oEventCB)
        else:
            cl_evact.StateCBSelfRemove(oTarget, oEventCB)


def CallBack2(oEventCB, oTarget):
    if cl_evcon.CheckInPointPerform(oTarget, oEventCB, {
        1326: 1 }, 0, 0):
        if cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func429(*a, **{
'sArg': 'AddDam' }))):
            cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 33402, 200, {
                'Att': oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('Cover'),
                'TalentLevel': cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'RatioAdd'),
                'Cache': cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'RatioMul'),
                'AbnormalSourceDam': 2 }, None)
            cl_evact.StateCBSelfRemove(oTarget, oEventCB)
        else:
            cl_evact.StateCBSelfRemove(oTarget, oEventCB)


def CallBack3(oEventCB, oTarget):
    cl_action.CommonSetPyFlag(oTarget, oEventCB.GetCBLifeCycle(), PY_FLAG_EXCLUDEMONSTERHATE, 0)


def CallBack4(oEventCB, oTarget):
    cl_evact.EventGetTargetByServant(oTarget, oEventCB)
    cl_evact.StateCBAddVictimState(oTarget, oEventCB, 33403, 0, 1, { }, 0, 0, None)


def CallBack5(oEventCB, oTarget):
    if cl_evcon.CheckWeaponType(oTarget, oEventCB, EQUIP_LASER):
        if cl_condition.CheckHero(oTarget, oEventCB.GetCBLifeCycle(), 207) and cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func429(*a, **{
'sArg': 'AddDam' }))):
            cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 33402, 200, {
                'Att': oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('Cover'),
                'TalentLevel': cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'RatioAdd'),
                'Cache': cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'RatioMul'),
                'AbnormalSourceDam': 2 }, None)
            cl_evact.StateCBSelfRemove(oTarget, oEventCB)
        elif cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func429(*a, **{
'sArg': 'AddDam' }))):
            cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 33402, 200, {
                'Att': oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('Cover'),
                'TalentLevel': cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'RatioAdd'),
                'Cache': cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'RatioMul'),
                'AbnormalSourceDam': 2 }, None)
            cl_evact.StateCBSelfRemove(oTarget, oEventCB)
        else:
            cl_evact.StateCBSelfRemove(oTarget, oEventCB)
    elif cl_condition.CheckHero(oTarget, oEventCB.GetCBLifeCycle(), 207) and cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func429(*a, **{
'sArg': 'AddDam' }))):
        cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 33402, 200, {
            'Att': oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('Cover'),
            'TalentLevel': cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'RatioAdd'),
            'Cache': cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'RatioMul'),
            'AbnormalSourceDam': 2 }, None)
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)
    elif cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func429(*a, **{
'sArg': 'AddDam' }))):
        cl_evact.StateCBChangeSkillDamFactor(oTarget, oEventCB, 0, (lambda *a: (Func437(*a, **{
'sKey': 'RatioAdd' }) + Func437(*a, **{
'sKey': 'RatioMul' }) * Func429(*a, **{
'sArg': 'Cover' })) * Func429(*a, **{
'sArg': 'Cover' })), DAM_MASK_ELEMENT, 1, 0)
        cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 33402, 200, {
            'Att': oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('Cover'),
            'TalentLevel': cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'RatioAdd'),
            'Cache': cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'RatioMul'),
            'AbnormalSourceDam': 1 }, None)
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)
    else:
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)


def CallBack8(oEventCB, oTarget):
    if cl_evcon.CheckInPointPerform(oTarget, oEventCB, {
        1310: 1 }, 0, 0):
        cl_evact.StateCBChangeSkillDamFactor(oTarget, oEventCB, 0, (lambda *a: (Func437(*a, **{
'sKey': 'RatioAdd' }) + Func437(*a, **{
'sKey': 'RatioMul' }) * Func429(*a, **{
'sArg': 'Cover' })) * Func429(*a, **{
'sArg': 'Cover' })), DAM_MASK_ELEMENT, 1, 0)
        cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 33402, 200, {
            'Att': oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('Cover'),
            'TalentLevel': cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'RatioAdd'),
            'Cache': cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'RatioMul'),
            'AbnormalSourceDam': 1 }, None)
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)


def CallBack11(oEventCB, oTarget):
    if cl_evcon.CheckInPointPerform(oTarget, oEventCB, {
        1670: 1 }, 0, 0) and cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func604(*a, **{
'sKey': 'TalentSkill' }))):
        if cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func429(*a, **{
'sArg': 'AddDam' }))):
            cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 33402, 200, {
                'Att': oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('Cover'),
                'TalentLevel': cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'RatioAdd'),
                'Cache': cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'RatioMul'),
                'AbnormalSourceDam': 2 }, None)
            cl_evact.StateCBSelfRemove(oTarget, oEventCB)
        else:
            cl_evact.StateCBSelfRemove(oTarget, oEventCB)


def CallBack12(oEventCB, oTarget):
    if cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func429(*a, **{
'sArg': 'AddDam' }))):
        cl_evact.StateCBChangeSkillDamFactor(oTarget, oEventCB, 0, (lambda *a: (Func437(*a, **{
'sKey': 'RatioAdd' }) + Func437(*a, **{
'sKey': 'RatioMul' }) * Func429(*a, **{
'sArg': 'Cover' })) * Func429(*a, **{
'sArg': 'Cover' })), DAM_MASK_ELEMENT, 0, 0)
        cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 33402, 200, {
            'Att': oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('Cover'),
            'TalentLevel': cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'RatioAdd'),
            'Cache': cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'RatioMul'),
            'AbnormalSourceDam': 1 }, None)
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)
    else:
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)


def CallBack16(oEventCB, oTarget):
    if cl_evcon.CheckWeaponType(oTarget, oEventCB, EQUIP_LASER):
        cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 33402, 200, {
            'Att': oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('Cover'),
            'TalentLevel': cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'RatioAdd'),
            'Cache': cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'RatioMul'),
            'AbnormalSourceDam': 2 }, None)
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)


def CallBack17(oEventCB, oTarget):
    if cl_evcon.CheckInPointPerform(oTarget, oEventCB, {
        1310: 1,
        1330: 1,
        1331: 1,
        1332: 1,
        1336: 1,
        1337: 1,
        1435: 1 }, 1, 0):
        cl_evact.StateCBSendInvisibleEndMsg(oTarget, oEventCB)
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)


def CallBack18(oEventCB, oTarget):
    cl_evact.EventGetTargetByPlants(oTarget, oEventCB)
    cl_evact.StateCBAddVictimState(oTarget, oEventCB, 33403, 0, 1, { }, 0, 0, None)
    cl_action.CommonListenMsgCallBack(oTarget, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_GARDENER_OPERATION_PLANT, CREATE_PLANT, 19, 0, 0)


def CallBack19(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
    cl_evact.StateCBAddVictimState(oTarget, oEventCB, 33403, 0, 1, { }, 0, 0, None)


class CState(cl_state.CState):
    m_SID = 33397
    m_Name = '破隐一击'
    m_DieRemove = 1
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REPLACE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 3
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 0
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_GameBroadcast = 1
    m_Action = (StateActAction, StateRemoveAction)
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1,
        2: CallBack2,
        3: CallBack3,
        4: CallBack4,
        5: CallBack5,
        8: CallBack8,
        11: CallBack11,
        12: CallBack12,
        16: CallBack16,
        17: CallBack17,
        18: CallBack18,
        19: CallBack19 }

