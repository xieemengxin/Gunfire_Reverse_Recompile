# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/bulletchange/p11111.pyc
# RelativePath: clientlogic/cl_perform/bulletchange/p11111.pyc
# Source Generated with Decompyle++
# File: p11111.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.bulletchange import CBulletChange as CCustomPerform
from . import action
from . import condition
from cl_newformula import Func309, Func410

def Action1(oWarrior, pfBulletChange):
    action.BulletChangeListenSnapshotMsg(oWarrior, pfBulletChange, cl_msgcenter.MSG_WAR_COSTBULLET, -1, 1, 0, 0)
    action.BulletChangeListenSnapshotMsg(oWarrior, pfBulletChange, cl_msgcenter.MSG_WAR_WEAPONPERFROM_COSTBULLET, -1, 9, 0, 0)


def Action2(oWarrior, pfBulletChange):
    action.BulletChangeListenSnapshotMsg(oWarrior, pfBulletChange, cl_msgcenter.MSG_WAR_COSTBULLET, -1, 2, 0, 0)
    action.BulletChangeListenSnapshotMsg(oWarrior, pfBulletChange, cl_msgcenter.MSG_WAR_WEAPONPERFROM_COSTBULLET, -1, 10, 0, 0)


def Action3(oWarrior, pfBulletChange):
    action.BulletChangeListenSnapshotMsg(oWarrior, pfBulletChange, cl_msgcenter.MSG_WAR_COSTBULLET, -1, 3, 0, 0)
    action.BulletChangeListenSnapshotMsg(oWarrior, pfBulletChange, cl_msgcenter.MSG_WAR_WEAPONPERFROM_COSTBULLET, -1, 11, 0, 0)


def DoCallBackAction0(oWarrior, pfBulletChange, oSkill, dClientInfo):
    if condition.CheckOwnServerState(oWarrior, pfBulletChange, oSkill, dClientInfo, 1446):
        action.BulletChangeRevertBulletBag(oWarrior, pfBulletChange, oSkill, dClientInfo)
    else:
        action.BulletChangeRevertBullet(oWarrior, pfBulletChange, oSkill, dClientInfo, (lambda *a: Func309(*a) * 1 + 0), 1010)


def DoCallBackAction1(oWarrior, pfBulletChange, oSkill, dClientInfo):
    if condition.CheckRandom(oWarrior, pfBulletChange, oSkill, dClientInfo, 10000, (lambda *a: Func410(*a, **{
'sid': 1009 }) * 500 + 0)):
        if condition.CheckOwnServerState(oWarrior, pfBulletChange, oSkill, dClientInfo, 1446):
            action.BulletChangeRevertBulletBag(oWarrior, pfBulletChange, oSkill, dClientInfo)
        else:
            action.BulletChangeRevertBullet(oWarrior, pfBulletChange, oSkill, dClientInfo, (lambda *a: Func309(*a) * 1 + 0), 1010)
    action.BulletChangeCBAddStateCount(oWarrior, pfBulletChange, oSkill, dClientInfo, 1008, (lambda *a: Func309(*a) * 1 + 0))
    if condition.CheckTargetStateGreaterCount(oWarrior, pfBulletChange, oSkill, dClientInfo):
        action.BulletChangeCBAddStateCount(oWarrior, pfBulletChange, oSkill, dClientInfo, 1008, -10)
        if condition.CheckOwnClientState(oWarrior, pfBulletChange, oSkill, dClientInfo, 1009):
            if condition.CheckSkillLevel(oWarrior, pfBulletChange, oSkill, dClientInfo):
                if condition.CheckTargetStateCount(oWarrior, pfBulletChange, oSkill, dClientInfo, 1009, 5):
                    action.BulletChangeAddServerStateCnt(oWarrior, pfBulletChange, oSkill, dClientInfo, 32521, 5, 300)
                else:
                    action.BulletChangeAddServerStateCnt(oWarrior, pfBulletChange, oSkill, dClientInfo, 32521, 1, 300)
            elif condition.CheckTargetStateCount(oWarrior, pfBulletChange, oSkill, dClientInfo, 1009, 3):
                action.BulletChangeAddServerStateCnt(oWarrior, pfBulletChange, oSkill, dClientInfo, 32521, 3, 300)
            else:
                action.BulletChangeAddServerStateCnt(oWarrior, pfBulletChange, oSkill, dClientInfo, 32521, 1, 300)
        else:
            action.BulletChangeAddServerState(oWarrior, pfBulletChange, oSkill, dClientInfo, 32521, 300, 1, 1)


def DoCallBackAction2(oWarrior, pfBulletChange, oSkill, dClientInfo):
    if condition.CheckRandom(oWarrior, pfBulletChange, oSkill, dClientInfo, 10000, (lambda *a: Func410(*a, **{
'sid': 1009 }) * 1000 + 0)):
        if condition.CheckOwnServerState(oWarrior, pfBulletChange, oSkill, dClientInfo, 1446):
            action.BulletChangeRevertBulletBag(oWarrior, pfBulletChange, oSkill, dClientInfo)
        else:
            action.BulletChangeRevertBullet(oWarrior, pfBulletChange, oSkill, dClientInfo, (lambda *a: Func309(*a) * 1 + 0), 1010)
    action.BulletChangeCBAddStateCount(oWarrior, pfBulletChange, oSkill, dClientInfo, 1008, (lambda *a: Func309(*a) * 1 + 0))
    if condition.CheckTargetStateGreaterCount(oWarrior, pfBulletChange, oSkill, dClientInfo):
        action.BulletChangeCBAddStateCount(oWarrior, pfBulletChange, oSkill, dClientInfo, 1008, -10)
        if condition.CheckOwnClientState(oWarrior, pfBulletChange, oSkill, dClientInfo, 1009):
            if condition.CheckSkillLevel(oWarrior, pfBulletChange, oSkill, dClientInfo):
                if condition.CheckTargetStateCount(oWarrior, pfBulletChange, oSkill, dClientInfo, 1009, 5):
                    action.BulletChangeAddServerStateCnt(oWarrior, pfBulletChange, oSkill, dClientInfo, 32521, 5, 300)
                else:
                    action.BulletChangeAddServerStateCnt(oWarrior, pfBulletChange, oSkill, dClientInfo, 32521, 1, 300)
            elif condition.CheckTargetStateCount(oWarrior, pfBulletChange, oSkill, dClientInfo, 1009, 3):
                action.BulletChangeAddServerStateCnt(oWarrior, pfBulletChange, oSkill, dClientInfo, 32521, 3, 300)
            else:
                action.BulletChangeAddServerStateCnt(oWarrior, pfBulletChange, oSkill, dClientInfo, 32521, 1, 300)
        else:
            action.BulletChangeAddServerState(oWarrior, pfBulletChange, oSkill, dClientInfo, 32521, 300, 1, 1)


def DoCallBackAction3(oWarrior, pfBulletChange, oSkill, dClientInfo):
    if condition.CheckRandom(oWarrior, pfBulletChange, oSkill, dClientInfo, 10000, (lambda *a: Func410(*a, **{
'sid': 1009 }) * 1500 + 0)):
        if condition.CheckOwnServerState(oWarrior, pfBulletChange, oSkill, dClientInfo, 1446):
            action.BulletChangeRevertBulletBag(oWarrior, pfBulletChange, oSkill, dClientInfo)
        else:
            action.BulletChangeRevertBullet(oWarrior, pfBulletChange, oSkill, dClientInfo, (lambda *a: Func309(*a) * 1 + 0), 1010)
    action.BulletChangeCBAddStateCount(oWarrior, pfBulletChange, oSkill, dClientInfo, 1008, (lambda *a: Func309(*a) * 1 + 0))
    if condition.CheckTargetStateGreaterCount(oWarrior, pfBulletChange, oSkill, dClientInfo):
        action.BulletChangeCBAddStateCount(oWarrior, pfBulletChange, oSkill, dClientInfo, 1008, -10)
        if condition.CheckOwnClientState(oWarrior, pfBulletChange, oSkill, dClientInfo, 1009):
            if condition.CheckSkillLevel(oWarrior, pfBulletChange, oSkill, dClientInfo):
                if condition.CheckTargetStateCount(oWarrior, pfBulletChange, oSkill, dClientInfo, 1009, 5):
                    action.BulletChangeAddServerStateCnt(oWarrior, pfBulletChange, oSkill, dClientInfo, 32521, 5, 300)
                else:
                    action.BulletChangeAddServerStateCnt(oWarrior, pfBulletChange, oSkill, dClientInfo, 32521, 1, 300)
            elif condition.CheckTargetStateCount(oWarrior, pfBulletChange, oSkill, dClientInfo, 1009, 3):
                action.BulletChangeAddServerStateCnt(oWarrior, pfBulletChange, oSkill, dClientInfo, 32521, 3, 300)
            else:
                action.BulletChangeAddServerStateCnt(oWarrior, pfBulletChange, oSkill, dClientInfo, 32521, 1, 300)
        else:
            action.BulletChangeAddServerState(oWarrior, pfBulletChange, oSkill, dClientInfo, 32521, 300, 1, 1)


def DoCallBackAction4(oWarrior, pfBulletChange, oSkill, dClientInfo):
    if condition.CheckTargetStateGreaterCount(oWarrior, pfBulletChange, oSkill, dClientInfo):
        action.BulletChangeCBAddStateCount(oWarrior, pfBulletChange, oSkill, dClientInfo, 1008, -10)
        if condition.CheckOwnClientState(oWarrior, pfBulletChange, oSkill, dClientInfo, 1009):
            if condition.CheckSkillLevel(oWarrior, pfBulletChange, oSkill, dClientInfo):
                if condition.CheckTargetStateCount(oWarrior, pfBulletChange, oSkill, dClientInfo, 1009, 5):
                    action.BulletChangeAddServerStateCnt(oWarrior, pfBulletChange, oSkill, dClientInfo, 32521, 5, 300)
                else:
                    action.BulletChangeAddServerStateCnt(oWarrior, pfBulletChange, oSkill, dClientInfo, 32521, 1, 300)
            elif condition.CheckTargetStateCount(oWarrior, pfBulletChange, oSkill, dClientInfo, 1009, 3):
                action.BulletChangeAddServerStateCnt(oWarrior, pfBulletChange, oSkill, dClientInfo, 32521, 3, 300)
            else:
                action.BulletChangeAddServerStateCnt(oWarrior, pfBulletChange, oSkill, dClientInfo, 32521, 1, 300)
        else:
            action.BulletChangeAddServerState(oWarrior, pfBulletChange, oSkill, dClientInfo, 32521, 300, 1, 1)


def DoCallBackAction5(oWarrior, pfBulletChange, oSkill, dClientInfo):
    if condition.CheckOwnClientState(oWarrior, pfBulletChange, oSkill, dClientInfo, 1009):
        if condition.CheckSkillLevel(oWarrior, pfBulletChange, oSkill, dClientInfo):
            if condition.CheckTargetStateCount(oWarrior, pfBulletChange, oSkill, dClientInfo, 1009, 5):
                action.BulletChangeAddServerStateCnt(oWarrior, pfBulletChange, oSkill, dClientInfo, 32521, 5, 300)
            else:
                action.BulletChangeAddServerStateCnt(oWarrior, pfBulletChange, oSkill, dClientInfo, 32521, 1, 300)
        elif condition.CheckTargetStateCount(oWarrior, pfBulletChange, oSkill, dClientInfo, 1009, 3):
            action.BulletChangeAddServerStateCnt(oWarrior, pfBulletChange, oSkill, dClientInfo, 32521, 3, 300)
        else:
            action.BulletChangeAddServerStateCnt(oWarrior, pfBulletChange, oSkill, dClientInfo, 32521, 1, 300)
    else:
        action.BulletChangeAddServerState(oWarrior, pfBulletChange, oSkill, dClientInfo, 32521, 300, 1, 1)


def DoCallBackAction6(oWarrior, pfBulletChange, oSkill, dClientInfo):
    if condition.CheckSkillLevel(oWarrior, pfBulletChange, oSkill, dClientInfo):
        if condition.CheckTargetStateCount(oWarrior, pfBulletChange, oSkill, dClientInfo, 1009, 5):
            action.BulletChangeAddServerStateCnt(oWarrior, pfBulletChange, oSkill, dClientInfo, 32521, 5, 300)
        else:
            action.BulletChangeAddServerStateCnt(oWarrior, pfBulletChange, oSkill, dClientInfo, 32521, 1, 300)
    elif condition.CheckTargetStateCount(oWarrior, pfBulletChange, oSkill, dClientInfo, 1009, 3):
        action.BulletChangeAddServerStateCnt(oWarrior, pfBulletChange, oSkill, dClientInfo, 32521, 3, 300)
    else:
        action.BulletChangeAddServerStateCnt(oWarrior, pfBulletChange, oSkill, dClientInfo, 32521, 1, 300)


def DoCallBackAction7(oWarrior, pfBulletChange, oSkill, dClientInfo):
    if condition.CheckTargetStateCount(oWarrior, pfBulletChange, oSkill, dClientInfo, 1009, 5):
        action.BulletChangeAddServerStateCnt(oWarrior, pfBulletChange, oSkill, dClientInfo, 32521, 5, 300)
    else:
        action.BulletChangeAddServerStateCnt(oWarrior, pfBulletChange, oSkill, dClientInfo, 32521, 1, 300)


def DoCallBackAction8(oWarrior, pfBulletChange, oSkill, dClientInfo):
    if condition.CheckTargetStateCount(oWarrior, pfBulletChange, oSkill, dClientInfo, 1009, 3):
        action.BulletChangeAddServerStateCnt(oWarrior, pfBulletChange, oSkill, dClientInfo, 32521, 3, 300)
    else:
        action.BulletChangeAddServerStateCnt(oWarrior, pfBulletChange, oSkill, dClientInfo, 32521, 1, 300)


def DoCallBackAction9(oWarrior, pfBulletChange, oSkill, dClientInfo):
    if condition.CheckRandom(oWarrior, pfBulletChange, oSkill, dClientInfo, 10000, (lambda *a: Func410(*a, **{
'sid': 1009 }) * 500 + 0)):
        if condition.CheckOwnServerState(oWarrior, pfBulletChange, oSkill, dClientInfo, 1446):
            action.BulletChangeRevertBulletBag(oWarrior, pfBulletChange, oSkill, dClientInfo)
        else:
            action.BulletChangeRevertBullet(oWarrior, pfBulletChange, oSkill, dClientInfo, (lambda *a: Func309(*a) * 1 + 0), 1010)
    action.BulletChangeCBAddStateCount(oWarrior, pfBulletChange, oSkill, dClientInfo, 1008, (lambda *a: Func309(*a) * 1 + 0))
    if condition.CheckTargetStateGreaterCount(oWarrior, pfBulletChange, oSkill, dClientInfo):
        action.BulletChangeCBAddStateCount(oWarrior, pfBulletChange, oSkill, dClientInfo, 1008, -10)
        if condition.CheckOwnClientState(oWarrior, pfBulletChange, oSkill, dClientInfo, 1009):
            if condition.CheckSkillLevel(oWarrior, pfBulletChange, oSkill, dClientInfo):
                if condition.CheckTargetStateCount(oWarrior, pfBulletChange, oSkill, dClientInfo, 1009, 5):
                    action.BulletChangeAddServerStateCnt(oWarrior, pfBulletChange, oSkill, dClientInfo, 32521, 5, 300)
                else:
                    action.BulletChangeAddServerStateCnt(oWarrior, pfBulletChange, oSkill, dClientInfo, 32521, 1, 300)
            elif condition.CheckTargetStateCount(oWarrior, pfBulletChange, oSkill, dClientInfo, 1009, 3):
                action.BulletChangeAddServerStateCnt(oWarrior, pfBulletChange, oSkill, dClientInfo, 32521, 3, 300)
            else:
                action.BulletChangeAddServerStateCnt(oWarrior, pfBulletChange, oSkill, dClientInfo, 32521, 1, 300)
        else:
            action.BulletChangeAddServerState(oWarrior, pfBulletChange, oSkill, dClientInfo, 32521, 300, 1, 1)


def DoCallBackAction10(oWarrior, pfBulletChange, oSkill, dClientInfo):
    if condition.CheckRandom(oWarrior, pfBulletChange, oSkill, dClientInfo, 10000, (lambda *a: Func410(*a, **{
'sid': 1009 }) * 1000 + 0)):
        if condition.CheckOwnServerState(oWarrior, pfBulletChange, oSkill, dClientInfo, 1446):
            action.BulletChangeRevertBulletBag(oWarrior, pfBulletChange, oSkill, dClientInfo)
        else:
            action.BulletChangeRevertBullet(oWarrior, pfBulletChange, oSkill, dClientInfo, (lambda *a: Func309(*a) * 1 + 0), 1010)
    action.BulletChangeCBAddStateCount(oWarrior, pfBulletChange, oSkill, dClientInfo, 1008, (lambda *a: Func309(*a) * 1 + 0))
    if condition.CheckTargetStateGreaterCount(oWarrior, pfBulletChange, oSkill, dClientInfo):
        action.BulletChangeCBAddStateCount(oWarrior, pfBulletChange, oSkill, dClientInfo, 1008, -10)
        if condition.CheckOwnClientState(oWarrior, pfBulletChange, oSkill, dClientInfo, 1009):
            if condition.CheckSkillLevel(oWarrior, pfBulletChange, oSkill, dClientInfo):
                if condition.CheckTargetStateCount(oWarrior, pfBulletChange, oSkill, dClientInfo, 1009, 5):
                    action.BulletChangeAddServerStateCnt(oWarrior, pfBulletChange, oSkill, dClientInfo, 32521, 5, 300)
                else:
                    action.BulletChangeAddServerStateCnt(oWarrior, pfBulletChange, oSkill, dClientInfo, 32521, 1, 300)
            elif condition.CheckTargetStateCount(oWarrior, pfBulletChange, oSkill, dClientInfo, 1009, 3):
                action.BulletChangeAddServerStateCnt(oWarrior, pfBulletChange, oSkill, dClientInfo, 32521, 3, 300)
            else:
                action.BulletChangeAddServerStateCnt(oWarrior, pfBulletChange, oSkill, dClientInfo, 32521, 1, 300)
        else:
            action.BulletChangeAddServerState(oWarrior, pfBulletChange, oSkill, dClientInfo, 32521, 300, 1, 1)


def DoCallBackAction11(oWarrior, pfBulletChange, oSkill, dClientInfo):
    if condition.CheckRandom(oWarrior, pfBulletChange, oSkill, dClientInfo, 10000, (lambda *a: Func410(*a, **{
'sid': 1009 }) * 1500 + 0)):
        if condition.CheckOwnServerState(oWarrior, pfBulletChange, oSkill, dClientInfo, 1446):
            action.BulletChangeRevertBulletBag(oWarrior, pfBulletChange, oSkill, dClientInfo)
        else:
            action.BulletChangeRevertBullet(oWarrior, pfBulletChange, oSkill, dClientInfo, (lambda *a: Func309(*a) * 1 + 0), 1010)
    action.BulletChangeCBAddStateCount(oWarrior, pfBulletChange, oSkill, dClientInfo, 1008, (lambda *a: Func309(*a) * 1 + 0))
    if condition.CheckTargetStateGreaterCount(oWarrior, pfBulletChange, oSkill, dClientInfo):
        action.BulletChangeCBAddStateCount(oWarrior, pfBulletChange, oSkill, dClientInfo, 1008, -10)
        if condition.CheckOwnClientState(oWarrior, pfBulletChange, oSkill, dClientInfo, 1009):
            if condition.CheckSkillLevel(oWarrior, pfBulletChange, oSkill, dClientInfo):
                if condition.CheckTargetStateCount(oWarrior, pfBulletChange, oSkill, dClientInfo, 1009, 5):
                    action.BulletChangeAddServerStateCnt(oWarrior, pfBulletChange, oSkill, dClientInfo, 32521, 5, 300)
                else:
                    action.BulletChangeAddServerStateCnt(oWarrior, pfBulletChange, oSkill, dClientInfo, 32521, 1, 300)
            elif condition.CheckTargetStateCount(oWarrior, pfBulletChange, oSkill, dClientInfo, 1009, 3):
                action.BulletChangeAddServerStateCnt(oWarrior, pfBulletChange, oSkill, dClientInfo, 32521, 3, 300)
            else:
                action.BulletChangeAddServerStateCnt(oWarrior, pfBulletChange, oSkill, dClientInfo, 32521, 1, 300)
        else:
            action.BulletChangeAddServerState(oWarrior, pfBulletChange, oSkill, dClientInfo, 32521, 300, 1, 1)


class CPerform(CCustomPerform):
    m_SID = 11111
    m_Name = '天赋2715子弹效果'
    m_MaxLevel = 3
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3 }
    m_DisableActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3,
        4: DoCallBackAction4,
        5: DoCallBackAction5,
        6: DoCallBackAction6,
        7: DoCallBackAction7,
        8: DoCallBackAction8,
        9: DoCallBackAction9,
        10: DoCallBackAction10,
        11: DoCallBackAction11 }

