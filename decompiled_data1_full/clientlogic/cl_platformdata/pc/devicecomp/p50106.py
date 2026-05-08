# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/devicecomp/p50106.pyc
# RelativePath: clientlogic/cl_platformdata/pc/devicecomp/p50106.pyc
# Source Generated with Decompyle++
# File: p50106.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.devicecomp import CDeviceComp as CCustomPerform
from cl_commondefines import DEVICECOMP_TYPE_DEVICE
from cl_newformula import Func361

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50106, 'StateTime', (lambda *a: Func361(*a, **{
'sid': 50106,
'sArgs': 'Lv1StateTime' })), None)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50106, 'ExtendTime', (lambda *a: Func361(*a, **{
'sid': 50106,
'sArgs': 'Lv1ExtendTime' })), None)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 212) or cl_condition.CheckHero(oWarrior, oLifeCycle, 205) or cl_condition.CheckHero(oWarrior, oLifeCycle, 216) or cl_condition.CheckHero(oWarrior, oLifeCycle, 206) or cl_condition.CheckHero(oWarrior, oLifeCycle, 201) or cl_condition.CheckHero(oWarrior, oLifeCycle, 207):
        cl_action.CommonAddPerform(oWarrior, oLifeCycle, 50261)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 217):
        cl_action.CommonAddPerform(oWarrior, oLifeCycle, 50263)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 213):
        cl_action.CommonAddPerform(oWarrior, oLifeCycle, 50264)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 214):
        cl_action.CommonAddPerform(oWarrior, oLifeCycle, 50262)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 215):
        cl_action.CommonAddPerform(oWarrior, oLifeCycle, 50265)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50106, 'StateTime', (lambda *a: Func361(*a, **{
'sid': 50106,
'sArgs': 'Lv2StateTime' })), None)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50106, 'ExtendTime', (lambda *a: Func361(*a, **{
'sid': 50106,
'sArgs': 'Lv2ExtendTime' })), None)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 212) or cl_condition.CheckHero(oWarrior, oLifeCycle, 205) or cl_condition.CheckHero(oWarrior, oLifeCycle, 216) or cl_condition.CheckHero(oWarrior, oLifeCycle, 206) or cl_condition.CheckHero(oWarrior, oLifeCycle, 201) or cl_condition.CheckHero(oWarrior, oLifeCycle, 207):
        cl_action.CommonAddPerform(oWarrior, oLifeCycle, 50261)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 217):
        cl_action.CommonAddPerform(oWarrior, oLifeCycle, 50263)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 213):
        cl_action.CommonAddPerform(oWarrior, oLifeCycle, 50264)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 214):
        cl_action.CommonAddPerform(oWarrior, oLifeCycle, 50262)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 215):
        cl_action.CommonAddPerform(oWarrior, oLifeCycle, 50265)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50106, 'StateTime', (lambda *a: Func361(*a, **{
'sid': 50106,
'sArgs': 'Lv3StateTime' })), None)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50106, 'ExtendTime', (lambda *a: Func361(*a, **{
'sid': 50106,
'sArgs': 'Lv3ExtendTime' })), None)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 212) or cl_condition.CheckHero(oWarrior, oLifeCycle, 205) or cl_condition.CheckHero(oWarrior, oLifeCycle, 216) or cl_condition.CheckHero(oWarrior, oLifeCycle, 206) or cl_condition.CheckHero(oWarrior, oLifeCycle, 201) or cl_condition.CheckHero(oWarrior, oLifeCycle, 207):
        cl_action.CommonAddPerform(oWarrior, oLifeCycle, 50261)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 217):
        cl_action.CommonAddPerform(oWarrior, oLifeCycle, 50263)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 213):
        cl_action.CommonAddPerform(oWarrior, oLifeCycle, 50264)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 214):
        cl_action.CommonAddPerform(oWarrior, oLifeCycle, 50262)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 215):
        cl_action.CommonAddPerform(oWarrior, oLifeCycle, 50265)


class CPerform(CCustomPerform):
    m_SID = 50106
    m_Name = '特化模块'
    m_MaxLevel = 3
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = { }
    m_BaseArgData = {
        'Lv1ExtendTime': 50,
        'Lv2ExtendTime': 100,
        'Lv3ExtendTime': 150,
        'Lv1StateTime': 600,
        'Lv2StateTime': 800,
        'Lv3StateTime': 1500 }
    m_DieDisable = 0
    m_ExclusiveDevice = (1001,)
    m_ExclusiveHero = ()
    m_ExcludeComp = ()
    m_DropShape = 5560
    m_DeployActive = 0
    m_Type = DEVICECOMP_TYPE_DEVICE
    m_FirstChooseExtWeight = 35

