# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/bulletchange/p11139.pyc
# RelativePath: clientlogic/cl_perform/bulletchange/p11139.pyc
# Source Generated with Decompyle++
# File: p11139.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.bulletchange import CBulletChange as CCustomPerform
from . import action
from . import condition
from cl_commondefines import PF_SUBMSG_THROW
from cl_newformula import Func343

def Action1(oWarrior, pfBulletChange):
    action.BulletChangeListenMsgCallBack(oWarrior, pfBulletChange, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_THROW, 0, 0, 0)


def Action2(oWarrior, pfBulletChange):
    action.BulletChangeListenMsgCallBack(oWarrior, pfBulletChange, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_THROW, 2, 0, 0)


def Action3(oWarrior, pfBulletChange):
    action.BulletChangeListenMsgCallBack(oWarrior, pfBulletChange, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_THROW, 4, 0, 0)


def Action4(oWarrior, pfBulletChange):
    action.BulletChangeListenMsgCallBack(oWarrior, pfBulletChange, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_THROW, 6, 0, 0)


def DoCallBackAction0(oWarrior, pfBulletChange, oSkill, dClientInfo):
    if condition.CheckFromPointPerforms(oWarrior, pfBulletChange, dClientInfo, {
        1: 1436,
        2: 1409,
        4: 1429,
        5: 1410,
        6: 1431 }) and condition.CheckThrowBulletCntUpperLimit(oWarrior, pfBulletChange, 0):
        action.BulletChangeCBTriggerGroup(oWarrior, pfBulletChange, oSkill, dClientInfo, {
            1: 1000 })


def DoCallBackAction1(oWarrior, pfBulletChange, oSkill, dClientInfo):
    if condition.CheckThrowBulletCntUpperLimit(oWarrior, pfBulletChange, 3):
        action.BulletChangeExtBulletUse(oWarrior, pfBulletChange, oSkill, dClientInfo, 3)
        action.BulletChangeCBSetSkillCacheChange(oWarrior, pfBulletChange, oSkill, dClientInfo, 'TriggerTimes', 0, 30000)
    else:
        action.BulletChangeExtBulletUse(oWarrior, pfBulletChange, oSkill, dClientInfo, (lambda *a: Func343(*a, **{
'sid': 4508 }) * 1))
        action.BulletChangeCBSetSkillCacheChange(oWarrior, pfBulletChange, oSkill, dClientInfo, 'TriggerTimes', 0, (lambda *a: Func343(*a, **{
'sid': 4508 }) * 10000))
    action.BulletChangeSetCollectInfo(oWarrior, pfBulletChange, oSkill, dClientInfo, 'FirstCostBulletFromContainer', 1, 0)


def DoCallBackAction2(oWarrior, pfBulletChange, oSkill, dClientInfo):
    if condition.CheckFromPointPerforms(oWarrior, pfBulletChange, dClientInfo, {
        1: 1436,
        2: 1409,
        4: 1429,
        5: 1410,
        6: 1431 }) and condition.CheckThrowBulletCntUpperLimit(oWarrior, pfBulletChange, 0):
        action.BulletChangeCBTriggerGroup(oWarrior, pfBulletChange, oSkill, dClientInfo, {
            3: 2000 })


def DoCallBackAction3(oWarrior, pfBulletChange, oSkill, dClientInfo):
    if condition.CheckThrowBulletCntUpperLimit(oWarrior, pfBulletChange, 3):
        action.BulletChangeExtBulletUse(oWarrior, pfBulletChange, oSkill, dClientInfo, 3)
        action.BulletChangeCBSetSkillCacheChange(oWarrior, pfBulletChange, oSkill, dClientInfo, 'TriggerTimes', 0, 30000)
    else:
        action.BulletChangeExtBulletUse(oWarrior, pfBulletChange, oSkill, dClientInfo, (lambda *a: Func343(*a, **{
'sid': 4508 }) * 1))
        action.BulletChangeCBSetSkillCacheChange(oWarrior, pfBulletChange, oSkill, dClientInfo, 'TriggerTimes', 0, (lambda *a: Func343(*a, **{
'sid': 4508 }) * 10000))
    action.BulletChangeSetCollectInfo(oWarrior, pfBulletChange, oSkill, dClientInfo, 'FirstCostBulletFromContainer', 1, 0)


def DoCallBackAction4(oWarrior, pfBulletChange, oSkill, dClientInfo):
    if condition.CheckFromPointPerforms(oWarrior, pfBulletChange, dClientInfo, {
        1: 1436,
        2: 1409,
        4: 1429,
        5: 1410,
        6: 1431 }) and condition.CheckThrowBulletCntUpperLimit(oWarrior, pfBulletChange, 0):
        action.BulletChangeCBTriggerGroup(oWarrior, pfBulletChange, oSkill, dClientInfo, {
            5: 2000 })


def DoCallBackAction5(oWarrior, pfBulletChange, oSkill, dClientInfo):
    if condition.CheckThrowBulletCntUpperLimit(oWarrior, pfBulletChange, 5):
        action.BulletChangeExtBulletUse(oWarrior, pfBulletChange, oSkill, dClientInfo, 5)
        action.BulletChangeCBSetSkillCacheChange(oWarrior, pfBulletChange, oSkill, dClientInfo, 'TriggerTimes', 0, 50000)
    else:
        action.BulletChangeExtBulletUse(oWarrior, pfBulletChange, oSkill, dClientInfo, (lambda *a: Func343(*a, **{
'sid': 4508 }) * 1))
        action.BulletChangeCBSetSkillCacheChange(oWarrior, pfBulletChange, oSkill, dClientInfo, 'TriggerTimes', 0, (lambda *a: Func343(*a, **{
'sid': 4508 }) * 10000))
    action.BulletChangeSetCollectInfo(oWarrior, pfBulletChange, oSkill, dClientInfo, 'FirstCostBulletFromContainer', 1, 0)


def DoCallBackAction6(oWarrior, pfBulletChange, oSkill, dClientInfo):
    if condition.CheckFromPointPerforms(oWarrior, pfBulletChange, dClientInfo, {
        1: 1436,
        2: 1409,
        4: 1429,
        5: 1410,
        6: 1431 }) and condition.CheckThrowBulletCntUpperLimit(oWarrior, pfBulletChange, 0):
        action.BulletChangeCBTriggerGroup(oWarrior, pfBulletChange, oSkill, dClientInfo, {
            7: 3000 })


def DoCallBackAction7(oWarrior, pfBulletChange, oSkill, dClientInfo):
    if condition.CheckThrowBulletCntUpperLimit(oWarrior, pfBulletChange, 5):
        action.BulletChangeExtBulletUse(oWarrior, pfBulletChange, oSkill, dClientInfo, 5)
        action.BulletChangeCBSetSkillCacheChange(oWarrior, pfBulletChange, oSkill, dClientInfo, 'TriggerTimes', 0, 50000)
    else:
        action.BulletChangeExtBulletUse(oWarrior, pfBulletChange, oSkill, dClientInfo, (lambda *a: Func343(*a, **{
'sid': 4508 }) * 1))
        action.BulletChangeCBSetSkillCacheChange(oWarrior, pfBulletChange, oSkill, dClientInfo, 'TriggerTimes', 0, (lambda *a: Func343(*a, **{
'sid': 4508 }) * 10000))
    action.BulletChangeSetCollectInfo(oWarrior, pfBulletChange, oSkill, dClientInfo, 'FirstCostBulletFromContainer', 1, 0)


class CPerform(CCustomPerform):
    m_SID = 11139
    m_Name = 'S7多重施法'
    m_MaxLevel = 4
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3,
        4: Action4 }
    m_DisableActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3,
        4: DoCallBackAction4,
        5: DoCallBackAction5,
        6: DoCallBackAction6,
        7: DoCallBackAction7 }

