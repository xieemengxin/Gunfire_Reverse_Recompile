# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/rewardpf/p15123.pyc
# RelativePath: clientlogic/cl_platformdata/pc/rewardpf/p15123.pyc
# Source Generated with Decompyle++
# File: p15123.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 212):
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 33446, 0, {
            'Att': 20,
            'Cache': 1 }, 1)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 205) or cl_condition.CheckHero(oWarrior, oLifeCycle, 206) or cl_condition.CheckHero(oWarrior, oLifeCycle, 215) or cl_condition.CheckHero(oWarrior, oLifeCycle, 216) or cl_condition.CheckHero(oWarrior, oLifeCycle, 218):
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 33446, 0, {
            'Att': 20 }, 1)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 201):
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 33447, 0, {
            'Att': 20 }, 1)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 207):
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 33450, 0, {
            'Att': 20 }, 1)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 213):
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 33452, 0, {
            'Att': 20 }, 1)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 217):
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 33453, 0, {
            'Att': 20 }, 1)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 219):
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 33454, 0, {
            'Att': 20 }, 1)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 214):
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 33455, 0, {
            'Att': 20 }, 1)
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 8608)


class CPerform(CCustomPerform):
    m_SID = 15123
    m_Name = '#NT#陨石秘法'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = { }
    m_BaseArgData = { }
    m_DieDisable = 0

