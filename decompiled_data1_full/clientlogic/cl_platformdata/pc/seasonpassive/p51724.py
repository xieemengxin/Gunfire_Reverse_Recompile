# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51724.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51724.pyc
# Source Generated with Decompyle++
# File: p51724.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_newformula import Func859, Func862

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_S8THIRDACTIVE_ATT_REFRESH, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_S8_CONTAINER_OPERATION, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_SWITCH_CAREER_PERFORM, -1, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_S8THIRDACTIVE_ATT_REFRESH, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_S8_CONTAINER_OPERATION, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_SWITCH_CAREER_PERFORM, -1, 0, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_S8THIRDACTIVE_ATT_REFRESH, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_S8_CONTAINER_OPERATION, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_SWITCH_CAREER_PERFORM, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.CommonChangeCareerPerformAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'MaxCover', 0, (lambda *a: min(Func859(*a, **{
'sAttr': 'MaxCnt' }), Func862(*a, **{
'sAttr': 'MaxEnergy' }) // Func859(*a, **{
'sAttr': 'Point' }))), 0)


class CPerform(CCustomPerform):
    m_SID = 51724
    m_Name = '主要技能使用次数'
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
    m_BaseLevelArgData = {
        1: {
            'Point': 120,
            'MaxCnt': 2 },
        2: {
            'Point': 60,
            'MaxCnt': 4 },
        3: {
            'Point': 30,
            'MaxCnt': 6 } }

