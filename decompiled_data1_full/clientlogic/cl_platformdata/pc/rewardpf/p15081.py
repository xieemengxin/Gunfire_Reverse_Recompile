# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/rewardpf/p15081.pyc
# RelativePath: clientlogic/cl_platformdata/pc/rewardpf/p15081.pyc
# Source Generated with Decompyle++
# File: p15081.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import OBJ_SELF, PF_SUBMSG_CAREERPF
from cl_newformula import Func360, Func361

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_CAREERPF, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 1, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, -1, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.PassiveCheckInColdTime(oWarrior, oEventCB, 1) == 0 and cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1310, 0, 0):
        cl_evact.PassiveCBSetLiteCD(oWarrior, oEventCB, 200)
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventCBUsePerformEvtTarget(oWarrior, oEventCB, 1696, {
            'PerformAtt': (lambda *a: Func360(*a, **{
'sid': 1310,
'sAttr': 'Att' })),
            'Radius': (lambda *a: Func361(*a, **{
'sid': 15081,
'sArgs': 'Radius' })) }, None)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_condition.CheckCurLevel(oWarrior, oEventCB.GetCBLifeCycle(), 1101009) or cl_condition.CheckCurLevel(oWarrior, oEventCB.GetCBLifeCycle(), 1301002) or cl_condition.CheckCurLevel(oWarrior, oEventCB.GetCBLifeCycle(), 1101007):
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'Radius', 20)
    else:
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'Radius', 7)


class CPerform(CCustomPerform):
    m_SID = 15081
    m_Name = '合理冲撞'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0

