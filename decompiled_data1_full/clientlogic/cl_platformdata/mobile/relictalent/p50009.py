# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/relictalent/p50009.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/relictalent/p50009.pyc
# Source Generated with Decompyle++
# File: p50009.pyc (Python 3.6)

from cl_platformdata.custom.relictalent.customaction import CustomAction50009 as CustomAction
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relictalent import CRelicTalent as CCustomPerform
from cl_commondefines import PF_SUBMSG_COMMON
from cl_newformula import Func361, Func526

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 12022)
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 12020)
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 12021)
    cl_action.CommonSetPerformAttr(oWarrior, oLifeCycle, 12022, 'MaxCover', 4)
    cl_action.CommonSetPerformAttr(oWarrior, oLifeCycle, 12021, 'MaxCover', 6)
    cl_action.CommonSetPerformAttr(oWarrior, oLifeCycle, 12020, 'MaxCover', 2)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_COMMON, 0, 0, 1)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 12022)
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 12020)
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 12021)
    cl_action.CommonSetPerformAttr(oWarrior, oLifeCycle, 12022, 'MaxCover', 4)
    cl_action.CommonSetPerformAttr(oWarrior, oLifeCycle, 12021, 'MaxCover', 6)
    cl_action.CommonSetPerformAttr(oWarrior, oLifeCycle, 12020, 'MaxCover', 2)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_COMMON, 1, 0, 1)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 12022)
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 12020)
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 12021)
    cl_action.CommonSetPerformAttr(oWarrior, oLifeCycle, 12022, 'MaxCover', 6)
    cl_action.CommonSetPerformAttr(oWarrior, oLifeCycle, 12021, 'MaxCover', 9)
    cl_action.CommonSetPerformAttr(oWarrior, oLifeCycle, 12020, 'MaxCover', 3)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_COMMON, 2, 0, 1)
    cl_action.CommonSetPerformAttr(oWarrior, oLifeCycle, 12022, 'AttDistance', 1)
    cl_action.CommonSetPerformAttr(oWarrior, oLifeCycle, 12020, 'AttDistance', 6)


def DoCallBackAction0(oEventCB, oWarrior):
    CustomAction(oWarrior, oEventCB, {
        'FromPerform': 1908,
        12022: (lambda *a: Func361(*a, **{
'sid': 1908,
'sArgs': 'Att' }) * (1 + Func526(*a) * 0.3)),
        12021: (lambda *a: Func361(*a, **{
'sid': 1908,
'sArgs': 'Att' }) * 0.7 * (1 + Func526(*a) * 0.3)),
        12020: (lambda *a: Func361(*a, **{
'sid': 1908,
'sArgs': 'Att' }) * 0.5 * (1 + Func526(*a) * 0.3)),
        'AttExtFactor': 0,
        'FirePerform': 12022,
        'CorrisionPerform': 12020,
        'ThunderPerform': 12021 })


def DoCallBackAction1(oEventCB, oWarrior):
    CustomAction(oWarrior, oEventCB, {
        'FromPerform': 1908,
        12022: (lambda *a: Func361(*a, **{
'sid': 1908,
'sArgs': 'Att' }) * (1 + Func526(*a) * 0.3)),
        12021: (lambda *a: Func361(*a, **{
'sid': 1908,
'sArgs': 'Att' }) * 0.7 * (1 + Func526(*a) * 0.3)),
        12020: (lambda *a: Func361(*a, **{
'sid': 1908,
'sArgs': 'Att' }) * 0.5 * (1 + Func526(*a) * 0.3)),
        'AttExtFactor': 5000,
        'FirePerform': 12022,
        'CorrisionPerform': 12020,
        'ThunderPerform': 12021 })


def DoCallBackAction2(oEventCB, oWarrior):
    CustomAction(oWarrior, oEventCB, {
        'FromPerform': 1908,
        12022: (lambda *a: Func361(*a, **{
'sid': 1908,
'sArgs': 'Att' }) * (1 + Func526(*a) * 0.3)),
        12021: (lambda *a: Func361(*a, **{
'sid': 1908,
'sArgs': 'Att' }) * 0.7 * (1 + Func526(*a) * 0.3)),
        12020: (lambda *a: Func361(*a, **{
'sid': 1908,
'sArgs': 'Att' }) * 0.5 * (1 + Func526(*a) * 0.3)),
        'AttExtFactor': 10000,
        'FirePerform': 12022,
        'CorrisionPerform': 12020,
        'ThunderPerform': 12021 })


class CPerform(CCustomPerform):
    m_SID = 50009
    m_Name = '元素灵胚'
    m_MaxLevel = 3
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_GrowPF = []
    m_DamagePF = []

