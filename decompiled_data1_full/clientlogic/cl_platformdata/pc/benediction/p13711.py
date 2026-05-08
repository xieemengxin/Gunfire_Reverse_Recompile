# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/benediction/p13711.pyc
# RelativePath: clientlogic/cl_platformdata/pc/benediction/p13711.pyc
# Source Generated with Decompyle++
# File: p13711.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
import cl_object
import cl_state
from cl_commondefines import STATE_TIME_LIMIT, STATE_TIME_FOREVER
from cl_only import Time2Frame
from cl_perform.benediction import CBenediction as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_VICTIM

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ASSISTKILL, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckMonsterType(oWarrior, oEventCB):
        CustomAction(oWarrior, oEventCB, {
            6101: {
                'State': 32549,
                'Time': 6000 },
            6102: {
                'State': 32550,
                'Time': 6000 },
            6103: {
                'State': 32551,
                'Time': 6000 },
            6104: {
                'State': 32552,
                'Time': 6000 },
            6105: {
                'State': 32553,
                'Time': 6000 },
            6106: {
                'State': 32554,
                'Time': 6000 },
            6107: {
                'State': 32555,
                'Time': 1000 },
            6108: {
                'State': 32556,
                'Time': 6000 },
            6109: {
                'State': 32613,
                'Time': 6000 },
            6110: {
                'State': 32614,
                'Time': 6000 },
            6112: {
                'State': 32680,
                'Time': 6000 },
            6115: {
                'State': 32681,
                'Time': 6000 },
            6201: {
                'State': 32557,
                'Time': 6000 },
            6202: {
                'State': 32558,
                'Time': 6000 },
            6203: {
                'State': 32559,
                'Time': 6000 },
            6204: {
                'State': 32560,
                'Time': 6000 } })


class CPerform(CCustomPerform):
    m_SID = 13711
    m_Name = '狩猎季节'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_Career = None


def CustomAction(oWarrior, oEventCB, dArg):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'VID' not in dMsgInfo:
        return None
    iVictim = dMsgInfo['VID']
    oVictim = oWarrior.m_Game.GetObject(iVictim)
    if not oVictim:
        return None
    tSuperInfo = oVictim.Query('MonsterSuper', None)
    if not tSuperInfo:
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    oLifeCycle = dEventInfo['LifeCycle']
    for iSuperPF in tSuperInfo:
        if iSuperPF in dArg:
            dInfo = dArg[iSuperPF]
            iState = dInfo['State']
            iTime = dInfo['Time']
            oState = oWarrior.m_State.GetItemBySID(iState)
            if oState:
                oState.AddCount(oWarrior, 1)
                cl_evact.PassiveAddStateTime(oWarrior, oEventCB, iState, iTime, iTime)
                continue
            cl_action.PassiveAddState(oWarrior, oLifeCycle, iState, iTime, { }, 1)
    

