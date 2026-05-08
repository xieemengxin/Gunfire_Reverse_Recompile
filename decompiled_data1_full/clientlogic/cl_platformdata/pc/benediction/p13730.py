# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/benediction/p13730.pyc
# RelativePath: clientlogic/cl_platformdata/pc/benediction/p13730.pyc
# Source Generated with Decompyle++
# File: p13730.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.benediction import CBenediction as CCustomPerform
from cl_commondefines import OBJ_SELF, VIRTUAL_ITEM_WAND, VIRTUAL_ITEM_WANDCOMP, WANDCOMP_RARITY_NORMAL, WANDCOMP_RARITY_RARE, WANDCOMP_RARITY_TALE, WAND_QUALITY_TALE, WAND_SUBMSG_ADD, WAND_SUBMSG_UPGRADE

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WANDCHANGE, WAND_SUBMSG_ADD, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WANDCHANGE, WAND_SUBMSG_UPGRADE, 0, 0, 0)
    cl_action.CommonSetWandShopCompQuality(oWarrior, oLifeCycle, {
        1: WANDCOMP_RARITY_TALE })
    cl_action.CommonReplaceWandShopWandCompWeight(oWarrior, oLifeCycle, {
        1: {
            WANDCOMP_RARITY_RARE: 29,
            WANDCOMP_RARITY_NORMAL: 68,
            WANDCOMP_RARITY_TALE: 3 },
        2: {
            WANDCOMP_RARITY_RARE: 40,
            WANDCOMP_RARITY_NORMAL: 54,
            WANDCOMP_RARITY_TALE: 6 },
        3: {
            WANDCOMP_RARITY_RARE: 48,
            WANDCOMP_RARITY_NORMAL: 36,
            WANDCOMP_RARITY_TALE: 16 },
        4: {
            WANDCOMP_RARITY_RARE: 50,
            WANDCOMP_RARITY_NORMAL: 25,
            WANDCOMP_RARITY_TALE: 25 } })
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 2, 0, 0)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 3, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckItemQuality(oWarrior, oEventCB, WAND_QUALITY_TALE, VIRTUAL_ITEM_WAND) and cl_condition.CheckHasSavedData(oWarrior, oEventCB.GetCBLifeCycle(), '13730BeneReward') == 0:
        cl_evact.EventCBSetSavedData(oWarrior, oEventCB, '13730BeneReward', 1, 0)
        cl_evact.EventCBWandItemInBag(oWarrior, oEventCB, 2109, 3, 1, VIRTUAL_ITEM_WANDCOMP)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_condition.CommonCheckHasQualityWandItem(oWarrior, oEventCB.GetCBLifeCycle(), WAND_QUALITY_TALE, VIRTUAL_ITEM_WAND) and cl_condition.CheckHasSavedData(oWarrior, oEventCB.GetCBLifeCycle(), '13730BeneReward') == 0:
        cl_evact.EventCBSetSavedData(oWarrior, oEventCB, '13730BeneReward', 1, 0)
        cl_evact.EventCBWandItemInBag(oWarrior, oEventCB, 2109, 3, 1, VIRTUAL_ITEM_WANDCOMP)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.EventCBDelTargetCustomData(oWarrior, oEventCB, 'ChangeWandShopWandComp')
    cl_evact.EventCBDelTargetCustomData(oWarrior, oEventCB, 'ReplaceWandShopWandCompWeight')


class CPerform(CCustomPerform):
    m_SID = 13730
    m_Name = '天赐玄玉'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = {
        1: DisableAction1 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        2: DoCallBackAction2,
        3: DoCallBackAction3 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_Career = None

