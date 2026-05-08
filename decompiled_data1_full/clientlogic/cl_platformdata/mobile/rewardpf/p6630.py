# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/rewardpf/p6630.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/rewardpf/p6630.pyc
# Source Generated with Decompyle++
# File: p6630.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import SEASONSHOP_INITGOODSBEFORE

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddSeasonShopNpcRefreshTimes(oWarrior, oLifeCycle, 1, 'ModulePacketRefreshTimes')
    cl_action.CommonAddSeasonShopNpcRefreshTimes(oWarrior, oLifeCycle, 1, 'CrystalPacketRefreshTimes')
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_SEASONSHOP, SEASONSHOP_INITGOODSBEFORE, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBSetCrystalPacketInfo(oWarrior, oEventCB, {
        1: {
            1: {
                1205: 100 },
            2: {
                1205: 100 },
            3: {
                1205: 100 },
            4: {
                1205: 100 } },
        2: {
            1: {
                1206: 100 },
            2: {
                1206: 100 },
            3: {
                1206: 100 } },
        3: {
            1: {
                1207: 100 },
            2: {
                1207: 100 },
            3: {
                1207: 100 } },
        4: {
            1: {
                1208: 100 },
            2: {
                1208: 100 } } })


class CPerform(CCustomPerform):
    m_SID = 6630
    m_Name = '赛季7天赋10级'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0

