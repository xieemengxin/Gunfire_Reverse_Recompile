# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p2313.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p2313.pyc
# Source Generated with Decompyle++
# File: p2313.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL
from cl_newformula import Func425

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1412, 'Att', 10000, 0)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1413, 'Att', 10000, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1412, 'Att', 20000, 0)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1413, 'Att', 20000, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1412, 'Att', 30000, 0)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1413, 'Att', 30000, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PREDICTDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1412, 1, None) or cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1413, 1, None):
        CustomAction(oWarrior, oEventCB, { })
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32277, 0, { }, 0, 0, None)
        cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 32277, (lambda *a: Func425(*a)), 0)
        if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 32278, 0, 0, None):
            cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 32278, 1, 0)
        else:
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32278, 0, { }, 0, 0, None)
            cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 32278, 1, 0)


class CPerform(CCustomPerform):
    m_SID = 2313
    m_Name = '强效电流'
    m_MaxLevel = 3
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 3
    m_IsRareTalent = 0
    m_Career = 104


def CustomAction(oWarrior, oEventCB, dInfo):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dTransInfo = oEventCB.GetCBTransInfo()
    oSkill = dMsgInfo['Skill']
    iActNum = oSkill.m_Base['ActNum']
    dMonster = oWarrior.Query('dFristMonster', { })
    lstTar = []
    if iActNum not in dMonster.keys():
        dMonster = { }
        dMonster[iActNum] = dMsgInfo['VID']
        oWarrior.Set('dFristMonster', dMonster)
        lstTar.append(dMonster[iActNum])
    else:
        lstTar.append(dMonster[iActNum])
    dTransInfo['TargetList'] = lstTar

