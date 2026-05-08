# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p3202.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p3202.pyc
# Source Generated with Decompyle++
# File: p3202.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_newformula import Func543, Func568

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GAMBLER_GET_QUALITY, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GAMBLER_CLEAR_GROOVE, -1, 0, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 32757, 0, { }, 1)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 32903, 0, { }, 1)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 32757, (lambda *a: Func568(*a, **{
'sQuality': 'QUALITY_TYPE_LOW' }) * 10 + Func568(*a, **{
'sQuality': 'QUALITY_TYPE_NORMAL' }) * 15 + Func568(*a, **{
'sQuality': 'QUALITY_TYPE_HIGH' }) * 20 + Func568(*a, **{
'sQuality': 'QUALITY_TYPE_CURSE' }) * Func543(*a, **{
'dWeight': {
10: 1,
15: 1,
20: 1 } })))


class CPerform(CCustomPerform):
    m_SID = 3202
    m_Name = '福星高照'
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
    m_MaxUpgradeTimes = 0
    m_TalentType = 1
    m_IsRareTalent = 0
    m_Career = 113

