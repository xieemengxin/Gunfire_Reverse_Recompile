# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/relic/p5707.pyc
# RelativePath: clientlogic/cl_platformdata/pc/relic/p5707.pyc
# Source Generated with Decompyle++
# File: p5707.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import QUALITY_TYPE_NORMAL, RELIC_TYPE_NORMAL

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonSetCustomData(oWarrior, oLifeCycle, 'CanNoBulletUse', 1)
    cl_action.PassiveEnableBulletChangeRule(oWarrior, oLifeCycle, 11042, 1)
    cl_action.CommonForbidAutoFillBullet(oWarrior, oLifeCycle, 10)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonSetCustomData(oWarrior, oLifeCycle, 'CanNoBulletUse', 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonSetCustomData(oWarrior, oLifeCycle, 'CanNoBulletUse', 1)
    cl_action.PassiveEnableBulletChangeRule(oWarrior, oLifeCycle, 11042, 2)
    cl_action.CommonForbidAutoFillBullet(oWarrior, oLifeCycle, 10)


def DisableAction2(oWarrior, oLifeCycle):
    cl_action.CommonSetCustomData(oWarrior, oLifeCycle, 'CanNoBulletUse', 0)


class CPerform(CCustomPerform):
    m_SID = 5707
    m_Name = '浸血弹药'
    m_MaxLevel = 2
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2 }
    m_DisableActionInfo = {
        1: DisableAction1,
        2: DisableAction2 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = { }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_RelicType = RELIC_TYPE_NORMAL
    m_DropShape = 5524
    m_ValidRemove = 1
    m_BasePrice = 60
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_NORMAL

