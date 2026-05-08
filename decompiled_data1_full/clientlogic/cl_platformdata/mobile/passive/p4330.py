# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p4330.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p4330.pyc
# Source Generated with Decompyle++
# File: p4330.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL
from cl_newformula import Func717

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 1)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 9215, 1, 0) and cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'NotDrop', 0) == 0 and cl_evcon.CheckHitWeakness(oWarrior, oEventCB, 0):
        if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('ExtraDrop') and cl_condition.RandomTrigger(oWarrior, oEventCB.GetCBLifeCycle(), 100, 50):
            cl_evact.RepeatTriggerGroup(oWarrior, oEventCB, 3, 2, None)
        else:
            CustomAction(oWarrior, oEventCB, {
                'StateSID': (lambda *a: Func717(*a, **{
'sArg': 'StateSID' })),
                'StateTime': (lambda *a: Func717(*a, **{
'sArg': 'StateTime' })),
                'DistanceParam1': (lambda *a: Func717(*a, **{
'sArg': 'DistanceParam1' })),
                'DistanceParam2': (lambda *a: Func717(*a, **{
'sArg': 'DistanceParam2' })),
                'MinFlyTime': (lambda *a: Func717(*a, **{
'sArg': 'MinFlyTime' })),
                'MaxFlyTime': (lambda *a: Func717(*a, **{
'sArg': 'MaxFlyTime' })),
                'MinFlyDis': (lambda *a: Func717(*a, **{
'sArg': 'MinFlyDis' })),
                'MaxFlyDis': (lambda *a: Func717(*a, **{
'sArg': 'MaxFlyDis' })),
                'Angle': (lambda *a: Func717(*a, **{
'sArg': 'Angle' })),
                'ExtTime': (lambda *a: Func717(*a, **{
'sArg': 'ExtTime' })),
                'BossStoneSID': (lambda *a: Func717(*a, **{
'sArg': 'BossStoneSID' })),
                'AirWallLen': (lambda *a: Func717(*a, **{
'sArg': 'AirWallLen' })),
                'ShiftRadius': (lambda *a: Func717(*a, **{
'sArg': 'ShiftRadius' })) })


def DoCallBackAction3(oEventCB, oWarrior):
    CustomAction(oWarrior, oEventCB, {
        'StateSID': (lambda *a: Func717(*a, **{
'sArg': 'StateSID' })),
        'StateTime': (lambda *a: Func717(*a, **{
'sArg': 'StateTime' })),
        'DistanceParam1': (lambda *a: Func717(*a, **{
'sArg': 'DistanceParam1' })),
        'DistanceParam2': (lambda *a: Func717(*a, **{
'sArg': 'DistanceParam2' })),
        'MinFlyTime': (lambda *a: Func717(*a, **{
'sArg': 'MinFlyTime' })),
        'MaxFlyTime': (lambda *a: Func717(*a, **{
'sArg': 'MaxFlyTime' })),
        'MinFlyDis': (lambda *a: Func717(*a, **{
'sArg': 'MinFlyDis' })),
        'MaxFlyDis': (lambda *a: Func717(*a, **{
'sArg': 'MaxFlyDis' })),
        'Angle': (lambda *a: Func717(*a, **{
'sArg': 'Angle' })),
        'ExtTime': (lambda *a: Func717(*a, **{
'sArg': 'ExtTime' })),
        'BossStoneSID': (lambda *a: Func717(*a, **{
'sArg': 'BossStoneSID' })),
        'AirWallLen': (lambda *a: Func717(*a, **{
'sArg': 'AirWallLen' })),
        'ShiftRadius': (lambda *a: Func717(*a, **{
'sArg': 'ShiftRadius' })) })


class CPerform(CCustomPerform):
    m_SID = 4330
    m_Name = '飞斧攻击技能被动'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        3: DoCallBackAction3 }
    m_BaseArgData = {
        'StateSID': 1909,
        'StateTime': 800,
        'DistanceParam1': 50,
        'DistanceParam2': 3,
        'MinFlyTime': 50,
        'MaxFlyTime': 80,
        'MinFlyDis': 15,
        'MaxFlyDis': 30,
        'Angle': 45,
        'ExtTime': 100,
        'BossStoneSID': 39091,
        'AirWallLen': 17,
        'ShiftRadius': 2 }
    m_DieDisable = 0

