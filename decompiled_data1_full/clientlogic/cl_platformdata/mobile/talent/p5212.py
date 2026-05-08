# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/talent/p5212.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/talent/p5212.pyc
# Source Generated with Decompyle++
# File: p5212.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_newformula import Func304, Func423

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PREDICTDAMED, -1, 0, 0, 36)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func423(*a))) <= cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: (Func304(*a, **{
'sAttr': 'ShieldMax' }) + Func304(*a, **{
'sAttr': 'ArmorMax' })) * 0.3)) and cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func304(*a, **{
'sAttr': 'HP' }) + Func304(*a, **{
'sAttr': 'Armor' }) + Func304(*a, **{
'sAttr': 'Shield' }))) >= cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: (Func304(*a, **{
'sAttr': 'ArmorMax' }) + Func304(*a, **{
'sAttr': 'ShieldMax' })) * 0.3)):
        cl_evact.EventSetLimitDamage(oWarrior, oEventCB, 0)


class CPerform(CCustomPerform):
    m_SID = 5212
    m_Name = '缓冲装置'
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
    m_TalentType = 4
    m_IsRareTalent = 1
    m_Career = 0

