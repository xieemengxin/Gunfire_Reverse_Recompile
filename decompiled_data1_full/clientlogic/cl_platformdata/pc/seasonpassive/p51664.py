# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51664.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51664.pyc
# Source Generated with Decompyle++
# File: p51664.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_newformula import Func859

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_REVTOTALDAM, -1, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_REVTOTALDAM, -1, 0, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_REVTOTALDAM, -1, 0, 0, 0)


def Action4(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_REVTOTALDAM, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 39734, (lambda *a: Func859(*a, **{
'sAttr': 'Time' })), {
        'Resistance': (lambda *a: Func859(*a, **{
'sAttr': 'Resistance' })) }, 1)
    if cl_evcon.PassiveCheckInColdTime(oWarrior, oEventCB, 1) and cl_evcon.CheckRandom(oWarrior, oEventCB, 100, (lambda *a: Func859(*a, **{
'sAttr': 'Prob' }))):
        cl_action.CommonAddCareerPfTempUseTimes(oWarrior, oEventCB.GetCBLifeCycle(), 1, 1, 1, 1)
        cl_evact.PassiveCBSetLiteCD(oWarrior, oEventCB, (lambda *a: Func859(*a, **{
'sAttr': 'CDTime' })))


class CPerform(CCustomPerform):
    m_SID = 51664
    m_Name = '生存-硬化外壳'
    m_MaxLevel = 4
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3,
        4: Action4 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_BaseLevelArgData = {
        1: {
            'CDTime': 600,
            'Prob': 30,
            'Resistance': 1000,
            'Time': 300 },
        2: {
            'CDTime': 500,
            'Prob': 40,
            'Resistance': 2000,
            'Time': 300 },
        3: {
            'CDTime': 400,
            'Prob': 50,
            'Resistance': 3000,
            'Time': 300 },
        4: {
            'CDTime': 300,
            'Prob': 60,
            'Resistance': 4000,
            'Time': 400 } }

