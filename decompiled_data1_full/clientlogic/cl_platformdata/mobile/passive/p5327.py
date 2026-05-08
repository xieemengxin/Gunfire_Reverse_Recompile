# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p5327.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p5327.pyc
# Source Generated with Decompyle++
# File: p5327.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL
from cl_newformula import Func517, Func717

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonHeroSwitchPerform(oWarrior, oLifeCycle, 'Career', 1329)
    cl_action.CommonHeroSwitchPerform(oWarrior, oLifeCycle, 'Throw', 1434)
    cl_action.CommonDisablePF(oWarrior, oLifeCycle, 1334, 0)
    cl_action.CommonDisablePF(oWarrior, oLifeCycle, 1435, 0)
    cl_action.CommonDisablePF(oWarrior, oLifeCycle, 1332, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 3, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 5, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_MAXBULLETCHANGE, -1, 5, 0, 0)


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.CheckFromWeapon(oWarrior, oEventCB, 0) and cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, '5327HitOver', 0) == 0:
        cl_evact.EventCBAddCollectInfo(oWarrior, oEventCB, '5327HitOver', 1, 0)
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'HitCount', 1)
        if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'HitCount') >= cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'HitCountMax'):
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'HitCount', 0)
            cl_action.CommonChangeEnergy(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: 100 + Func717(*a, **{
'sArg': 'RepeatHitExtEnergy' })), 0)


def DoCallBackAction5(oEventCB, oWarrior):
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'HitCount', 0)
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'HitCountMax', (lambda *a: max(2, Func517(*a) // 4)))


class CPerform(CCustomPerform):
    m_SID = 5327
    m_Name = '#NT#浩克变身被动'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        3: DoCallBackAction3,
        5: DoCallBackAction5 }
    m_BaseArgData = { }
    m_DieDisable = 0

