# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/rewardpf/p16021.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/rewardpf/p16021.pyc
# Source Generated with Decompyle++
# File: p16021.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_VICTIM

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ASSISTKILL, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckMonsterType(oWarrior, oEventCB):
        CustomAction(oWarrior, oEventCB, {
            6151: {
                'State': 32549,
                'Time': 6000 },
            6152: {
                'State': 32550,
                'Time': 6000 },
            6153: {
                'State': 32551,
                'Time': 6000 },
            6154: {
                'State': 32552,
                'Time': 6000 },
            6155: {
                'State': 32553,
                'Time': 6000 },
            6156: {
                'State': 32554,
                'Time': 6000 },
            6157: {
                'State': 32555,
                'Time': 1000 },
            6158: {
                'State': 32556,
                'Time': 6000 },
            6159: {
                'State': 32613,
                'Time': 6000 },
            6160: {
                'State': 32614,
                'Time': 6000 },
            6162: {
                'State': 32680,
                'Time': 6000 },
            6165: {
                'State': 32681,
                'Time': 6000 },
            6251: {
                'State': 32557,
                'Time': 6000 },
            6252: {
                'State': 32558,
                'Time': 6000 },
            6253: {
                'State': 32559,
                'Time': 6000 },
            6254: {
                'State': 32560,
                'Time': 6000 } })


class CPerform(CCustomPerform):
    m_SID = 16021
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
    

