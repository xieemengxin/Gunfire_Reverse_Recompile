# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51730.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51730.pyc
# Source Generated with Decompyle++
# File: p51730.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_commondefines import S8THIRDACTIVE_REFRESH_MAXENERGY
from cl_newformula import Func859, Func862

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_S8THIRDACTIVE_ATT_REFRESH, S8THIRDACTIVE_REFRESH_MAXENERGY, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_S8THIRDACTIVE_ATT_REFRESH, S8THIRDACTIVE_REFRESH_MAXENERGY, 0, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_S8THIRDACTIVE_ATT_REFRESH, S8THIRDACTIVE_REFRESH_MAXENERGY, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveChangeAttr(oWarrior, oEventCB, 'DebuffFactor', 0, (lambda *a: min(Func859(*a, **{
'sAttr': 'MaxProb' }), (Func862(*a, **{
'sAttr': 'MaxEnergy' }) // Func859(*a, **{
'sAttr': 'PerAddMaxEnergy' })) * Func859(*a, **{
'sAttr': 'AddDebuffProb' }))))


class CPerform(CCustomPerform):
    m_SID = 51730
    m_Name = '元素异常几率'
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
            'PerAddMaxEnergy': 10,
            'AddDebuffProb': 200,
            'MaxProb': 3000 },
        2: {
            'PerAddMaxEnergy': 10,
            'AddDebuffProb': 400,
            'MaxProb': 6000 },
        3: {
            'PerAddMaxEnergy': 10,
            'AddDebuffProb': 800,
            'MaxProb': 12000 } }

