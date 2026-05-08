# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/relictalent/p50018.pyc
# RelativePath: clientlogic/cl_platformdata/pc/relictalent/p50018.pyc
# Source Generated with Decompyle++
# File: p50018.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relictalent import CRelicTalent as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def DisableAction2(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def DisableAction3(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_condition.CheckHero(oWarrior, oEventCB.GetCBLifeCycle(), 201):
        cl_action.CommonAddPerform(oWarrior, oEventCB.GetCBLifeCycle(), 7000)
    if cl_condition.CheckHero(oWarrior, oEventCB.GetCBLifeCycle(), 207):
        cl_action.CommonAddPerform(oWarrior, oEventCB.GetCBLifeCycle(), 7003)
    if cl_condition.CheckHero(oWarrior, oEventCB.GetCBLifeCycle(), 205):
        cl_action.CommonAddPerform(oWarrior, oEventCB.GetCBLifeCycle(), 7001)
    if cl_condition.CheckHero(oWarrior, oEventCB.GetCBLifeCycle(), 212):
        cl_action.CommonAddPerform(oWarrior, oEventCB.GetCBLifeCycle(), 7004)
    if cl_condition.CheckHero(oWarrior, oEventCB.GetCBLifeCycle(), 215):
        cl_action.CommonAddPerform(oWarrior, oEventCB.GetCBLifeCycle(), 7007)
    if cl_condition.CheckHero(oWarrior, oEventCB.GetCBLifeCycle(), 216):
        cl_action.CommonAddPerform(oWarrior, oEventCB.GetCBLifeCycle(), 7008)
    if cl_condition.CheckHero(oWarrior, oEventCB.GetCBLifeCycle(), 217):
        cl_action.CommonAddPerform(oWarrior, oEventCB.GetCBLifeCycle(), 7009)
    if cl_condition.CheckHero(oWarrior, oEventCB.GetCBLifeCycle(), 206):
        cl_action.CommonAddPerform(oWarrior, oEventCB.GetCBLifeCycle(), 7002)
    if cl_condition.CheckHero(oWarrior, oEventCB.GetCBLifeCycle(), 213):
        cl_action.CommonAddPerform(oWarrior, oEventCB.GetCBLifeCycle(), 7005)
    if cl_condition.CheckHero(oWarrior, oEventCB.GetCBLifeCycle(), 214):
        cl_action.CommonAddPerform(oWarrior, oEventCB.GetCBLifeCycle(), 7006)
    if cl_condition.CheckHero(oWarrior, oEventCB.GetCBLifeCycle(), 218):
        cl_action.CommonAddPerform(oWarrior, oEventCB.GetCBLifeCycle(), 7017)
    if cl_condition.CheckHero(oWarrior, oEventCB.GetCBLifeCycle(), 219):
        cl_action.CommonAddPerform(oWarrior, oEventCB.GetCBLifeCycle(), 7018)
    if cl_condition.CheckHero(oWarrior, oEventCB.GetCBLifeCycle(), 220):
        cl_action.CommonAddPerform(oWarrior, oEventCB.GetCBLifeCycle(), 7019)
    if cl_condition.CheckHero(oWarrior, oEventCB.GetCBLifeCycle(), 221):
        cl_action.CommonAddPerform(oWarrior, oEventCB.GetCBLifeCycle(), 7019)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_condition.CheckHero(oWarrior, oEventCB.GetCBLifeCycle(), 201):
        cl_action.CommonRemovePerform(oWarrior, oEventCB.GetCBLifeCycle(), 7000)
    if cl_condition.CheckHero(oWarrior, oEventCB.GetCBLifeCycle(), 207):
        cl_action.CommonRemovePerform(oWarrior, oEventCB.GetCBLifeCycle(), 7003)
    if cl_condition.CheckHero(oWarrior, oEventCB.GetCBLifeCycle(), 205):
        cl_action.CommonRemovePerform(oWarrior, oEventCB.GetCBLifeCycle(), 7001)
    if cl_condition.CheckHero(oWarrior, oEventCB.GetCBLifeCycle(), 212):
        cl_action.CommonRemovePerform(oWarrior, oEventCB.GetCBLifeCycle(), 7004)
    if cl_condition.CheckHero(oWarrior, oEventCB.GetCBLifeCycle(), 215):
        cl_action.CommonRemovePerform(oWarrior, oEventCB.GetCBLifeCycle(), 7007)
    if cl_condition.CheckHero(oWarrior, oEventCB.GetCBLifeCycle(), 216):
        cl_action.CommonRemovePerform(oWarrior, oEventCB.GetCBLifeCycle(), 7008)
    if cl_condition.CheckHero(oWarrior, oEventCB.GetCBLifeCycle(), 217):
        cl_action.CommonRemovePerform(oWarrior, oEventCB.GetCBLifeCycle(), 7009)
    if cl_condition.CheckHero(oWarrior, oEventCB.GetCBLifeCycle(), 206):
        cl_action.CommonRemovePerform(oWarrior, oEventCB.GetCBLifeCycle(), 7002)
    if cl_condition.CheckHero(oWarrior, oEventCB.GetCBLifeCycle(), 213):
        cl_action.CommonRemovePerform(oWarrior, oEventCB.GetCBLifeCycle(), 7005)
    if cl_condition.CheckHero(oWarrior, oEventCB.GetCBLifeCycle(), 214):
        cl_action.CommonRemovePerform(oWarrior, oEventCB.GetCBLifeCycle(), 7006)
    if cl_condition.CheckHero(oWarrior, oEventCB.GetCBLifeCycle(), 218):
        cl_action.CommonRemovePerform(oWarrior, oEventCB.GetCBLifeCycle(), 7017)
    if cl_condition.CheckHero(oWarrior, oEventCB.GetCBLifeCycle(), 219):
        cl_action.CommonRemovePerform(oWarrior, oEventCB.GetCBLifeCycle(), 7018)
    if cl_condition.CheckHero(oWarrior, oEventCB.GetCBLifeCycle(), 220):
        cl_action.CommonRemovePerform(oWarrior, oEventCB.GetCBLifeCycle(), 7019)
    if cl_condition.CheckHero(oWarrior, oEventCB.GetCBLifeCycle(), 221):
        cl_action.CommonRemovePerform(oWarrior, oEventCB.GetCBLifeCycle(), 7019)


class CPerform(CCustomPerform):
    m_SID = 50018
    m_Name = '针衍万法'
    m_MaxLevel = 3
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3 }
    m_DisableActionInfo = {
        1: DisableAction1,
        2: DisableAction2,
        3: DisableAction3 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_GrowPF = []
    m_DamagePF = []

