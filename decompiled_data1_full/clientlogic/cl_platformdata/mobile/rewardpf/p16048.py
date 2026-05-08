# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/rewardpf/p16048.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/rewardpf/p16048.pyc
# Source Generated with Decompyle++
# File: p16048.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_newformula import Func509

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonSetCustomData(oWarrior, oLifeCycle, 'ExtraInscription', 1)
    cl_action.CommonSetOwnerWeaponExtraInscriptionCost(oWarrior, oLifeCycle, (lambda *a: Func509(*a, **{
'sAttr': 'ItemBaseGrade' }) * 200))


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonSetCustomData(oWarrior, oLifeCycle, 'ExtraInscription', 0)


class CPerform(CCustomPerform):
    m_SID = 16048
    m_Name = '鬼斧神工'
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

