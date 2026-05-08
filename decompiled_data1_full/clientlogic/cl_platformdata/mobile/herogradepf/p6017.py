# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/herogradepf/p6017.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/herogradepf/p6017.pyc
# Source Generated with Decompyle++
# File: p6017.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_npc import net
from cl_commondefines import NPC_CB_VALUE, NPC_CB_REFRESH
from cl_only import Functor, ShufferList
from cl_platformdata.custom.passive.customaction import CustomAction6017 as CustomAction
from . import CHeroGradePassive as CCustomPerform
from cl_commondefines import PLAYMODE_NEWSURVIVOR, PLAYMODE_SURVIVOR

def Action1(oWarrior, oLifeCycle):
    if cl_condition.CheckWarPlayMode(oWarrior, oLifeCycle, PLAYMODE_SURVIVOR) or cl_condition.CheckWarPlayMode(oWarrior, oLifeCycle, PLAYMODE_NEWSURVIVOR):
        cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)
    else:
        cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    CustomAction(oWarrior, oEventCB, {
        'Defensepf': {
            6021: 1,
            6022: 1,
            6023: 1,
            6024: 1 },
        'Weaponpf': {
            6031: 1,
            6032: 1,
            6033: 1,
            6034: 1 },
        'Skillpf': {
            6041: 1,
            6042: 1,
            6043: 1,
            6044: 1 },
        'Oncepf': 6031 })


def DoCallBackAction1(oEventCB, oWarrior):
    CustomAction(oWarrior, oEventCB, {
        'Defensepf': {
            6021: 1,
            6022: 1,
            6023: 1,
            6024: 1 },
        'Weaponpf': {
            6031: 1,
            6032: 1,
            6033: 1,
            6035: 1 },
        'Skillpf': {
            6041: 1,
            6042: 1,
            6043: 1,
            6044: 1 },
        'Oncepf': 6031 })


class CPerform(CCustomPerform):
    m_SID = 6017
    m_Name = '游侠lv.2'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0

