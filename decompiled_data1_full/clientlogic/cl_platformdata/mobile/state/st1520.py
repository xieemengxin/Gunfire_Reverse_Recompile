# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st1520.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st1520.pyc
# Source Generated with Decompyle++
# File: st1520.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import DPSUBMSG_DEFAULT, EQUIP_LASER, EXTGRADE_GROUP2, MAIN_HOLD, OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func404, Func410, Func428, Func429, Func437, Func509, Func526, Func784, Func795

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_AFTERADDWEAPON, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_BEFOREREPLACEWEAPON, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_WEAPONFIRE, DPSUBMSG_DEFAULT, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_UPDATE_STRENGTHATT, -1, 9, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATE_START, -1, 8, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_TRIGGERCARTOON, -1, 14, 0, 0)


def StateCountAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 7, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventCBChangeWeaponExtGrade(oTarget, oEventCB, EXTGRADE_GROUP2, (lambda *a: Func404(*a)))
    cl_evact.EventCBChangeWeaponAttr(oTarget, oEventCB, 'AttSpeed', 0, (lambda *a: Func437(*a, **{
'sKey': 'AttSpeedAdd' }) + Func437(*a, **{
'sKey': 'ExtraAttSpeedAdd' })))


def CallBack1(oEventCB, oTarget):
    cl_evact.EventCBChangeWeaponExtGrade(oTarget, oEventCB, EXTGRADE_GROUP2, 0)
    cl_evact.EventCBChangeWeaponAttr(oTarget, oEventCB, 'AttSpeed', 0, 0)


def CallBack2(oEventCB, oTarget):
    cl_action.CommonSetCustomData(oTarget, oEventCB.GetCBLifeCycle(), 'StrengthLayer', (lambda *a: Func410(*a, **{
'sid': 33639 })))
    if cl_condition.GetStateCount(oTarget, oEventCB.GetCBLifeCycle(), 33639) > 0 and cl_evcon.CheckInPointPerform(oTarget, oEventCB, {
        1315: 1,
        1319: 1,
        8505: 1 }, 1, 0) == 0:
        cl_evact.EventCBSetCustomData(oTarget, oEventCB, 'StrengthWeaponAtt', (lambda *a: Func509(*a, **{
'sAttr': 'Att' })))
        if cl_evcon.CheckWeaponType(oTarget, oEventCB, EQUIP_LASER):
            cl_evact.EventSetSkillCache(oTarget, oEventCB, 'Att', (lambda *a: Func795(*a, **{
'sAttr': 'Att' })))
        if cl_condition.CheckHasSavedData(oTarget, oEventCB.GetCBLifeCycle(), '13532Bene'):
            if cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func784(*a, **{
'iCalOverflow': 0 }))) > cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func428(*a, **{
'sid': 33639 }) // 2)):
                cl_evact.EventCBSetCollectInfo(oTarget, oEventCB, 'AdditionWeaponGrade', (lambda *a: Func526(*a)), 0)
                cl_evact.EventCBSetTransInfo(oTarget, oEventCB, 'ReduceStrength', 1)
                if cl_evcon.EventCBGetMsgInfo(oTarget, oEventCB, 'NotReduceStrength') == 0:
                    cl_action.CommonAddStateCount(oTarget, oEventCB.GetCBLifeCycle(), 33639, -cl_evcon.EventCBGetTransInfo(oTarget, oEventCB, 'ReduceStrength', 1), 0)
                
            cl_evact.EventCBSetCollectInfo(oTarget, oEventCB, 'AdditionWeaponGrade', (lambda *a: Func526(*a)), 0)
            if cl_evcon.EventCBGetMsgInfo(oTarget, oEventCB, 'NotReduceStrength') == 0:
                cl_action.CommonAddStateCount(oTarget, oEventCB.GetCBLifeCycle(), 33639, -cl_evcon.EventCBGetTransInfo(oTarget, oEventCB, 'ReduceStrength', 1), 0)
            elif cl_evcon.EventCBGetMsgInfo(oTarget, oEventCB, 'NotReduceStrength') == 0:
                cl_action.CommonAddStateCount(oTarget, oEventCB.GetCBLifeCycle(), 33639, -cl_evcon.EventCBGetTransInfo(oTarget, oEventCB, 'ReduceStrength', 1), 0)


def CallBack4(oEventCB, oTarget):
    if cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func429(*a, **{
'sArg': 'StrengthLvRatio' }))):
        if cl_condition.CheckHasSavedData(oTarget, oEventCB.GetCBLifeCycle(), '13532Bene') and cl_condition.GetStateCount(oTarget, oEventCB.GetCBLifeCycle(), 33639) > cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func428(*a, **{
'sid': 33639 }) // 2)):
            cl_action.StateSetSelfCount(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func428(*a, **{
'sid': 33639 }) + Func428(*a, **{
'sid': 33639 }) // Func429(*a, **{
'sArg': 'StrengthLvRatio' })))
        else:
            cl_action.StateSetSelfCount(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func410(*a, **{
'sid': 33639 }) + Func410(*a, **{
'sid': 33639 }) // Func429(*a, **{
'sArg': 'StrengthLvRatio' })))
    elif cl_condition.CheckHasSavedData(oTarget, oEventCB.GetCBLifeCycle(), '13532Bene') and cl_condition.GetStateCount(oTarget, oEventCB.GetCBLifeCycle(), 33639) > cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func428(*a, **{
'sid': 33639 }) // 2)):
        cl_action.StateSetSelfCount(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func428(*a, **{
'sid': 33639 })))
    else:
        cl_action.StateSetSelfCount(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func410(*a, **{
'sid': 33639 })))


def CallBack7(oEventCB, oTarget):
    cl_action.CommonChangeWeaponExtGrade(oTarget, oEventCB.GetCBLifeCycle(), EXTGRADE_GROUP2, (lambda *a: Func404(*a)), MAIN_HOLD, 1)
    cl_action.CommonChangeWeaponAttr(oTarget, oEventCB.GetCBLifeCycle(), 'AttSpeed', 0, (lambda *a: Func437(*a, **{
'sKey': 'AttSpeedAdd' }) + Func437(*a, **{
'sKey': 'ExtraAttSpeedAdd' })), 0)
    cl_action.CommonChangeWeaponAttr(oTarget, oEventCB.GetCBLifeCycle(), 'AttSpeed', 0, (lambda *a: Func437(*a, **{
'sKey': 'AttSpeedAdd' }) + Func437(*a, **{
'sKey': 'ExtraAttSpeedAdd' })), -1)


def CallBack8(oEventCB, oTarget):
    if cl_evcon.EventCBGetMsgInfo(oTarget, oEventCB, 'StateSID') == 33639:
        if cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func429(*a, **{
'sArg': 'StrengthLvRatio' }))):
            if cl_condition.CheckHasSavedData(oTarget, oEventCB.GetCBLifeCycle(), '13532Bene') and cl_condition.GetStateCount(oTarget, oEventCB.GetCBLifeCycle(), 33639) > cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func428(*a, **{
'sid': 33639 }) // 2)):
                cl_action.StateSetSelfCount(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func428(*a, **{
'sid': 33639 }) + Func428(*a, **{
'sid': 33639 }) // Func429(*a, **{
'sArg': 'StrengthLvRatio' })))
            else:
                cl_action.StateSetSelfCount(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func410(*a, **{
'sid': 33639 }) + Func410(*a, **{
'sid': 33639 }) // Func429(*a, **{
'sArg': 'StrengthLvRatio' })))
        elif cl_condition.CheckHasSavedData(oTarget, oEventCB.GetCBLifeCycle(), '13532Bene') and cl_condition.GetStateCount(oTarget, oEventCB.GetCBLifeCycle(), 33639) > cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func428(*a, **{
'sid': 33639 }) // 2)):
            cl_action.StateSetSelfCount(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func428(*a, **{
'sid': 33639 })))
        else:
            cl_action.StateSetSelfCount(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func410(*a, **{
'sid': 33639 })))


def CallBack9(oEventCB, oTarget):
    if cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func429(*a, **{
'sArg': 'StrengthLvRatio' }))):
        if cl_condition.CheckHasSavedData(oTarget, oEventCB.GetCBLifeCycle(), '13532Bene') and cl_condition.GetStateCount(oTarget, oEventCB.GetCBLifeCycle(), 33639) > cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func428(*a, **{
'sid': 33639 }) // 2)):
            cl_action.StateSetSelfCount(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func428(*a, **{
'sid': 33639 }) + Func428(*a, **{
'sid': 33639 }) // Func429(*a, **{
'sArg': 'StrengthLvRatio' })))
        else:
            cl_action.StateSetSelfCount(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func410(*a, **{
'sid': 33639 }) + Func410(*a, **{
'sid': 33639 }) // Func429(*a, **{
'sArg': 'StrengthLvRatio' })))
    elif cl_condition.CheckHasSavedData(oTarget, oEventCB.GetCBLifeCycle(), '13532Bene') and cl_condition.GetStateCount(oTarget, oEventCB.GetCBLifeCycle(), 33639) > cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func428(*a, **{
'sid': 33639 }) // 2)):
        cl_action.StateSetSelfCount(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func428(*a, **{
'sid': 33639 })))
    else:
        cl_action.StateSetSelfCount(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func410(*a, **{
'sid': 33639 })))
    cl_action.CommonChangeWeaponExtGrade(oTarget, oEventCB.GetCBLifeCycle(), EXTGRADE_GROUP2, (lambda *a: Func404(*a)), MAIN_HOLD, 1)
    cl_action.CommonChangeWeaponAttr(oTarget, oEventCB.GetCBLifeCycle(), 'AttSpeed', 0, (lambda *a: Func437(*a, **{
'sKey': 'AttSpeedAdd' }) + Func437(*a, **{
'sKey': 'ExtraAttSpeedAdd' })), 0)
    cl_action.CommonChangeWeaponAttr(oTarget, oEventCB.GetCBLifeCycle(), 'AttSpeed', 0, (lambda *a: Func437(*a, **{
'sKey': 'AttSpeedAdd' }) + Func437(*a, **{
'sKey': 'ExtraAttSpeedAdd' })), -1)


def CallBack14(oEventCB, oTarget):
    if cl_evcon.CheckInPointPerform(oTarget, oEventCB, {
        1315: 1,
        1319: 1,
        8505: 1 }, 1, 0):
        if cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func784(*a, **{
'iCalOverflow': 0 }))) > cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func428(*a, **{
'sid': 33639 }) // 2)):
            cl_evact.EventCBSetCollectInfo(oTarget, oEventCB, 'AdditionWeaponGrade', (lambda *a: Func526(*a)), 0)
            cl_evact.EventCBSetTransInfo(oTarget, oEventCB, 'ReduceStrength', 1)
            if cl_evcon.EventCBGetMsgInfo(oTarget, oEventCB, 'NotReduceStrength') == 0:
                cl_action.CommonAddStateCount(oTarget, oEventCB.GetCBLifeCycle(), 33639, -cl_evcon.EventCBGetTransInfo(oTarget, oEventCB, 'ReduceStrength', 1), 0)
            else:
                cl_evact.EventCBSetCollectInfo(oTarget, oEventCB, 'AdditionWeaponGrade', (lambda *a: Func526(*a)), 0)
                if cl_evcon.EventCBGetMsgInfo(oTarget, oEventCB, 'NotReduceStrength') == 0:
                    cl_action.CommonAddStateCount(oTarget, oEventCB.GetCBLifeCycle(), 33639, -cl_evcon.EventCBGetTransInfo(oTarget, oEventCB, 'ReduceStrength', 1), 0)


class CState(cl_state.CState):
    m_SID = 1520
    m_Name = '镇妖'
    m_IsShow = 1
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
    m_ShowStateCnt = 1
    m_Action = (StateActAction, None)
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1,
        2: CallBack2,
        4: CallBack4,
        7: CallBack7,
        8: CallBack8,
        9: CallBack9,
        14: CallBack14 }

