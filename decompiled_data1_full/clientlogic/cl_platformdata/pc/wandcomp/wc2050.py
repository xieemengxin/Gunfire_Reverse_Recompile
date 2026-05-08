# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wandcomp/wc2050.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wandcomp/wc2050.pyc
# Source Generated with Decompyle++
# File: wc2050.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_platformdata.custom.wandcomp.customaction import CustomAction2050 as CustomAction
from cl_wand.mobject import CWandComp as CBaseComp
from cl_commondefines import CHARGECARTOON_SUBMSG_END, CHARGECARTOON_SUBMSG_START, WANDTAG_OTHER, WAND_ACTCOMP_INSTANT, WAND_COMP_TYPE_ACTION
from cl_newformula import Func308

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHARGECARTOON_TRIGGER, CHARGECARTOON_SUBMSG_START, 0, 0, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHARGECARTOON_TRIGGER, CHARGECARTOON_SUBMSG_END, 1, 0, 0)


def TriggerAction1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 2, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHARGECARTOON_TRIGGER, CHARGECARTOON_SUBMSG_START, 0, 0, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHARGECARTOON_TRIGGER, CHARGECARTOON_SUBMSG_END, 1, 0, 0)


def TriggerAction2(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 2, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHARGECARTOON_TRIGGER, CHARGECARTOON_SUBMSG_START, 0, 0, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHARGECARTOON_TRIGGER, CHARGECARTOON_SUBMSG_END, 1, 0, 0)


def TriggerAction3(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBRecordSkill(oWarrior, oEventCB, 'Charge')


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventCBDelRecordSkill(oWarrior, oEventCB, 'Charge')


def DoCallBackAction2(oEventCB, oWarrior):
    CustomAction(oWarrior, oEventCB, {
        'StateSID': 33603,
        'RecordKey': 'Charge',
        'AddCount': 1,
        'AddDamRatio': (lambda *a: 2000 * Func308(*a)) })


class CWandComp(CBaseComp):
    m_SID = 2050
    m_Name = '蓄力一击'
    m_Type = WAND_COMP_TYPE_ACTION
    m_Tag = (WANDTAG_OTHER,)
    m_ActionInfo = {
        1: (Action1, None),
        2: (Action2, None),
        3: (Action3, None) }
    m_TriggerActionInfo = {
        1: TriggerAction1,
        2: TriggerAction2,
        3: TriggerAction3 }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2 }
    m_TriggerType = WAND_ACTCOMP_INSTANT

