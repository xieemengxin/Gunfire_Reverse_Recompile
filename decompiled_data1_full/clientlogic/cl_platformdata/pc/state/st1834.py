# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st1834.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st1834.pyc
# Source Generated with Decompyle++
# File: st1834.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import DAM_USE_ARMOR, DAM_USE_HP, DAM_USE_SHIELD, DEFEND_TREND_ARMOR, DEFEND_TREND_SHIELD, OBJ_SELF, STATE_ADD_SYNC, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func16, Func347, Func403, Func404

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 9, -1, 0)


def CallBack0(oEventCB, oTarget):
    if cl_condition.CheckHasRelic(oTarget, oEventCB.GetCBLifeCycle(), 5764):
        if cl_condition.CheckHasRelic(oTarget, oEventCB.GetCBLifeCycle(), 5806):
            cl_evact.StateSetSelfCount(oTarget, oEventCB, 150)
            if oTarget.HP() >= oTarget.QueryAttr('HPMax'):
                if cl_condition.CheckTargetDefendTrend(oTarget, oEventCB.GetCBLifeCycle(), DEFEND_TREND_SHIELD):
                    cl_action.StateCureByAtive(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func404(*a) * Func403(*a, **{
'sAttr': 'ShieldMax' }) / 100), 1, DAM_USE_SHIELD)
                elif cl_condition.CheckTargetDefendTrend(oTarget, oEventCB.GetCBLifeCycle(), DEFEND_TREND_ARMOR):
                    cl_action.StateCureByAtive(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func404(*a) * Func403(*a, **{
'sAttr': 'ArmorMax' }) / 100), 1, DAM_USE_ARMOR)
                
            cl_action.StateCureByAtive(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func404(*a) * Func403(*a, **{
'sAttr': 'HPMax' }) / 100), 1, DAM_USE_HP)
        else:
            cl_evact.StateSetSelfCount(oTarget, oEventCB, 100)
            if oTarget.HP() >= oTarget.QueryAttr('HPMax'):
                if cl_condition.CheckTargetDefendTrend(oTarget, oEventCB.GetCBLifeCycle(), DEFEND_TREND_SHIELD):
                    cl_action.StateCureByAtive(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func404(*a) * Func403(*a, **{
'sAttr': 'ShieldMax' }) / 100), 1, DAM_USE_SHIELD)
                elif cl_condition.CheckTargetDefendTrend(oTarget, oEventCB.GetCBLifeCycle(), DEFEND_TREND_ARMOR):
                    cl_action.StateCureByAtive(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func404(*a) * Func403(*a, **{
'sAttr': 'ArmorMax' }) / 100), 1, DAM_USE_ARMOR)
                else:
                    cl_action.StateCureByAtive(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func404(*a) * Func403(*a, **{
'sAttr': 'HPMax' }) / 100), 1, DAM_USE_HP)
        if None.GetRelicGrade(oTarget, oEventCB.GetCBLifeCycle(), 5764) == 2:
            cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 1476, 2000, { }, None)
    elif cl_condition.CheckHasRelic(oTarget, oEventCB.GetCBLifeCycle(), 5806):
        if cl_condition.CheckHasRelic(oTarget, oEventCB.GetCBLifeCycle(), 5950) or cl_condition.HasState(oTarget, oEventCB.GetCBLifeCycle(), 33357):
            cl_evact.StateSetSelfCount(oTarget, oEventCB, (lambda *a: 1.5 * Func16(*a, **{
'a': 1,
'b': 40 })))
            if oTarget.HP() >= oTarget.QueryAttr('HPMax'):
                if cl_condition.CheckTargetDefendTrend(oTarget, oEventCB.GetCBLifeCycle(), DEFEND_TREND_SHIELD):
                    cl_action.StateCureByAtive(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func404(*a) * Func403(*a, **{
'sAttr': 'ShieldMax' }) / 100), 1, DAM_USE_SHIELD)
                elif cl_condition.CheckTargetDefendTrend(oTarget, oEventCB.GetCBLifeCycle(), DEFEND_TREND_ARMOR):
                    cl_action.StateCureByAtive(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func404(*a) * Func403(*a, **{
'sAttr': 'ArmorMax' }) / 100), 1, DAM_USE_ARMOR)
                else:
                    cl_action.StateCureByAtive(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func404(*a) * Func403(*a, **{
'sAttr': 'HPMax' }) / 100), 1, DAM_USE_HP)
            else:
                cl_evact.StateSetSelfCount(oTarget, oEventCB, 45)
                if oTarget.HP() >= oTarget.QueryAttr('HPMax'):
                    if cl_condition.CheckTargetDefendTrend(oTarget, oEventCB.GetCBLifeCycle(), DEFEND_TREND_SHIELD):
                        cl_action.StateCureByAtive(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func404(*a) * Func403(*a, **{
'sAttr': 'ShieldMax' }) / 100), 1, DAM_USE_SHIELD)
                    elif cl_condition.CheckTargetDefendTrend(oTarget, oEventCB.GetCBLifeCycle(), DEFEND_TREND_ARMOR):
                        cl_action.StateCureByAtive(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func404(*a) * Func403(*a, **{
'sAttr': 'ArmorMax' }) / 100), 1, DAM_USE_ARMOR)
                    else:
                        cl_action.StateCureByAtive(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func404(*a) * Func403(*a, **{
'sAttr': 'HPMax' }) / 100), 1, DAM_USE_HP)
                elif cl_condition.CheckHasRelic(oTarget, oEventCB.GetCBLifeCycle(), 5950) or cl_condition.HasState(oTarget, oEventCB.GetCBLifeCycle(), 33357):
                    cl_evact.StateSetSelfCount(oTarget, oEventCB, (lambda *a: Func16(*a, **{
'a': 1,
'b': 40 })))
                    if oTarget.HP() >= oTarget.QueryAttr('HPMax'):
                        if cl_condition.CheckTargetDefendTrend(oTarget, oEventCB.GetCBLifeCycle(), DEFEND_TREND_SHIELD):
                            cl_action.StateCureByAtive(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func404(*a) * Func403(*a, **{
'sAttr': 'ShieldMax' }) / 100), 1, DAM_USE_SHIELD)
                        elif cl_condition.CheckTargetDefendTrend(oTarget, oEventCB.GetCBLifeCycle(), DEFEND_TREND_ARMOR):
                            cl_action.StateCureByAtive(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func404(*a) * Func403(*a, **{
'sAttr': 'ArmorMax' }) / 100), 1, DAM_USE_ARMOR)
                        else:
                            cl_action.StateCureByAtive(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func404(*a) * Func403(*a, **{
'sAttr': 'HPMax' }) / 100), 1, DAM_USE_HP)
                    else:
                        cl_evact.StateSetSelfCount(oTarget, oEventCB, 30)
                        if oTarget.HP() >= oTarget.QueryAttr('HPMax'):
                            if cl_condition.CheckTargetDefendTrend(oTarget, oEventCB.GetCBLifeCycle(), DEFEND_TREND_SHIELD):
                                cl_action.StateCureByAtive(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func404(*a) * Func403(*a, **{
'sAttr': 'ShieldMax' }) / 100), 1, DAM_USE_SHIELD)
                            elif cl_condition.CheckTargetDefendTrend(oTarget, oEventCB.GetCBLifeCycle(), DEFEND_TREND_ARMOR):
                                cl_action.StateCureByAtive(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func404(*a) * Func403(*a, **{
'sAttr': 'ArmorMax' }) / 100), 1, DAM_USE_ARMOR)
                            else:
                                cl_action.StateCureByAtive(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func404(*a) * Func403(*a, **{
'sAttr': 'HPMax' }) / 100), 1, DAM_USE_HP)


def CallBack9(oEventCB, oTarget):
    cl_evact.EventAddBagBullet(oTarget, oEventCB, 4502, (lambda *a: Func347(*a, **{
'sid': 4502 }) * 0.3))
    cl_evact.EventAddBagBullet(oTarget, oEventCB, 4503, (lambda *a: Func347(*a, **{
'sid': 4503 }) * 0.3))
    cl_evact.EventAddBagBullet(oTarget, oEventCB, 4504, (lambda *a: Func347(*a, **{
'sid': 4504 }) * 0.3))
    cl_evact.EventAddBagBullet(oTarget, oEventCB, 4508, (lambda *a: Func347(*a, **{
'sid': 4508 }) * 0.3))
    if cl_condition.CheckHasRelic(oTarget, oEventCB.GetCBLifeCycle(), 5764):
        if cl_condition.CheckHasRelic(oTarget, oEventCB.GetCBLifeCycle(), 5806):
            cl_evact.StateSetSelfCount(oTarget, oEventCB, 150)
            if oTarget.HP() >= oTarget.QueryAttr('HPMax'):
                if cl_condition.CheckTargetDefendTrend(oTarget, oEventCB.GetCBLifeCycle(), DEFEND_TREND_SHIELD):
                    cl_action.StateCureByAtive(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func404(*a) * Func403(*a, **{
'sAttr': 'ShieldMax' }) / 100), 1, DAM_USE_SHIELD)
                elif cl_condition.CheckTargetDefendTrend(oTarget, oEventCB.GetCBLifeCycle(), DEFEND_TREND_ARMOR):
                    cl_action.StateCureByAtive(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func404(*a) * Func403(*a, **{
'sAttr': 'ArmorMax' }) / 100), 1, DAM_USE_ARMOR)
                
            cl_action.StateCureByAtive(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func404(*a) * Func403(*a, **{
'sAttr': 'HPMax' }) / 100), 1, DAM_USE_HP)
        else:
            cl_evact.StateSetSelfCount(oTarget, oEventCB, 100)
            if oTarget.HP() >= oTarget.QueryAttr('HPMax'):
                if cl_condition.CheckTargetDefendTrend(oTarget, oEventCB.GetCBLifeCycle(), DEFEND_TREND_SHIELD):
                    cl_action.StateCureByAtive(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func404(*a) * Func403(*a, **{
'sAttr': 'ShieldMax' }) / 100), 1, DAM_USE_SHIELD)
                elif cl_condition.CheckTargetDefendTrend(oTarget, oEventCB.GetCBLifeCycle(), DEFEND_TREND_ARMOR):
                    cl_action.StateCureByAtive(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func404(*a) * Func403(*a, **{
'sAttr': 'ArmorMax' }) / 100), 1, DAM_USE_ARMOR)
                else:
                    cl_action.StateCureByAtive(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func404(*a) * Func403(*a, **{
'sAttr': 'HPMax' }) / 100), 1, DAM_USE_HP)
        if None.GetRelicGrade(oTarget, oEventCB.GetCBLifeCycle(), 5764) == 2:
            cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 1476, 2000, { }, None)
    elif cl_condition.CheckHasRelic(oTarget, oEventCB.GetCBLifeCycle(), 5806):
        if cl_condition.CheckHasRelic(oTarget, oEventCB.GetCBLifeCycle(), 5950) or cl_condition.HasState(oTarget, oEventCB.GetCBLifeCycle(), 33357):
            cl_evact.StateSetSelfCount(oTarget, oEventCB, (lambda *a: 1.5 * Func16(*a, **{
'a': 1,
'b': 40 })))
            if oTarget.HP() >= oTarget.QueryAttr('HPMax'):
                if cl_condition.CheckTargetDefendTrend(oTarget, oEventCB.GetCBLifeCycle(), DEFEND_TREND_SHIELD):
                    cl_action.StateCureByAtive(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func404(*a) * Func403(*a, **{
'sAttr': 'ShieldMax' }) / 100), 1, DAM_USE_SHIELD)
                elif cl_condition.CheckTargetDefendTrend(oTarget, oEventCB.GetCBLifeCycle(), DEFEND_TREND_ARMOR):
                    cl_action.StateCureByAtive(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func404(*a) * Func403(*a, **{
'sAttr': 'ArmorMax' }) / 100), 1, DAM_USE_ARMOR)
                else:
                    cl_action.StateCureByAtive(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func404(*a) * Func403(*a, **{
'sAttr': 'HPMax' }) / 100), 1, DAM_USE_HP)
            else:
                cl_evact.StateSetSelfCount(oTarget, oEventCB, 45)
                if oTarget.HP() >= oTarget.QueryAttr('HPMax'):
                    if cl_condition.CheckTargetDefendTrend(oTarget, oEventCB.GetCBLifeCycle(), DEFEND_TREND_SHIELD):
                        cl_action.StateCureByAtive(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func404(*a) * Func403(*a, **{
'sAttr': 'ShieldMax' }) / 100), 1, DAM_USE_SHIELD)
                    elif cl_condition.CheckTargetDefendTrend(oTarget, oEventCB.GetCBLifeCycle(), DEFEND_TREND_ARMOR):
                        cl_action.StateCureByAtive(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func404(*a) * Func403(*a, **{
'sAttr': 'ArmorMax' }) / 100), 1, DAM_USE_ARMOR)
                    else:
                        cl_action.StateCureByAtive(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func404(*a) * Func403(*a, **{
'sAttr': 'HPMax' }) / 100), 1, DAM_USE_HP)
                elif cl_condition.CheckHasRelic(oTarget, oEventCB.GetCBLifeCycle(), 5950) or cl_condition.HasState(oTarget, oEventCB.GetCBLifeCycle(), 33357):
                    cl_evact.StateSetSelfCount(oTarget, oEventCB, (lambda *a: Func16(*a, **{
'a': 1,
'b': 40 })))
                    if oTarget.HP() >= oTarget.QueryAttr('HPMax'):
                        if cl_condition.CheckTargetDefendTrend(oTarget, oEventCB.GetCBLifeCycle(), DEFEND_TREND_SHIELD):
                            cl_action.StateCureByAtive(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func404(*a) * Func403(*a, **{
'sAttr': 'ShieldMax' }) / 100), 1, DAM_USE_SHIELD)
                        elif cl_condition.CheckTargetDefendTrend(oTarget, oEventCB.GetCBLifeCycle(), DEFEND_TREND_ARMOR):
                            cl_action.StateCureByAtive(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func404(*a) * Func403(*a, **{
'sAttr': 'ArmorMax' }) / 100), 1, DAM_USE_ARMOR)
                        else:
                            cl_action.StateCureByAtive(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func404(*a) * Func403(*a, **{
'sAttr': 'HPMax' }) / 100), 1, DAM_USE_HP)
                    else:
                        cl_evact.StateSetSelfCount(oTarget, oEventCB, 30)
                        if oTarget.HP() >= oTarget.QueryAttr('HPMax'):
                            if cl_condition.CheckTargetDefendTrend(oTarget, oEventCB.GetCBLifeCycle(), DEFEND_TREND_SHIELD):
                                cl_action.StateCureByAtive(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func404(*a) * Func403(*a, **{
'sAttr': 'ShieldMax' }) / 100), 1, DAM_USE_SHIELD)
                            elif cl_condition.CheckTargetDefendTrend(oTarget, oEventCB.GetCBLifeCycle(), DEFEND_TREND_ARMOR):
                                cl_action.StateCureByAtive(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func404(*a) * Func403(*a, **{
'sAttr': 'ArmorMax' }) / 100), 1, DAM_USE_ARMOR)
                            else:
                                cl_action.StateCureByAtive(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func404(*a) * Func403(*a, **{
'sAttr': 'HPMax' }) / 100), 1, DAM_USE_HP)


class CState(cl_state.CState):
    m_SID = 1834
    m_Name = '#NT#补充状态'
    m_DieRemove = 1
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_SYNC
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
        9: CallBack9 }

