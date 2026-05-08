# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/rewardpf/p6621.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/rewardpf/p6621.pyc
# Source Generated with Decompyle++
# File: p6621.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonSetCustomData(oWarrior, oLifeCycle, 'S6PacketDicePriceIncrease', 40)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonSetCustomData(oWarrior, oLifeCycle, 'S6PacketDicePriceIncrease', 100)


class CPerform(CCustomPerform):
    m_SID = 6621
    m_Name = '赛季6天赋0级'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = {
        1: DisableAction1 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = { }
    m_BaseArgData = { }
    m_DieDisable = 0

