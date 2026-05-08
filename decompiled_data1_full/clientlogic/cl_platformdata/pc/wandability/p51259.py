# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wandability/p51259.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wandability/p51259.pyc
# Source Generated with Decompyle++
# File: p51259.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.wandability import CWandAbility as CCustomPerform
from cl_commondefines import ABILITY_TYPE_EXCLUSIVE
from cl_newformula import Func717

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 1970)
    cl_action.CommonAddPerformArgsValue(oWarrior, oLifeCycle, 1970, 'Count', 4, 0)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1970, 'Att', (lambda *a: Func717(*a, **{
'sArg': 'AttMul' })), 0)
    cl_action.CommonSendMessage(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOM_PERFORMINFO_CHANGE, -1, {
        'pfid': 1970 })


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonAddPerformArgsValue(oWarrior, oLifeCycle, 1970, 'Count', -4, 0)
    cl_action.CommonSendMessage(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOM_PERFORMINFO_CHANGE, -1, {
        'pfid': 1970 })


class CPerform(CCustomPerform):
    m_SID = 51259
    m_Name = '星轨令牌专属词条'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = {
        1: DisableAction1 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = { }
    m_BaseArgData = {
        'AttMul': -4000 }
    m_DieDisable = 0
    m_QualityValue = { }
    m_AbilityType = ABILITY_TYPE_EXCLUSIVE
    m_BaseValue = 100
    m_IsReverseFloting = 0

