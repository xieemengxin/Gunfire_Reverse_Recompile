# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/rewardpf/p6620.pyc
# RelativePath: clientlogic/cl_platformdata/pc/rewardpf/p6620.pyc
# Source Generated with Decompyle++
# File: p6620.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import OBJ_SELF, VIRTUAL_ITEM_WAND, VIRTUAL_ITEM_WANDCOMP

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddWandShopGoodsNum(oWarrior, oLifeCycle, VIRTUAL_ITEM_WAND, 1)
    cl_action.CommonAddWandShopGoodsNum(oWarrior, oLifeCycle, VIRTUAL_ITEM_WANDCOMP, 2)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.EventCBDelTargetCustomData(oWarrior, oEventCB, 'AddWandShopGoodsExtraGoodsNum')


class CPerform(CCustomPerform):
    m_SID = 6620
    m_Name = '赛季5天赋1024'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = {
        1: DisableAction1 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0

