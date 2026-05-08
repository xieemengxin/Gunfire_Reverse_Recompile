# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/throw/p8015.pyc
# RelativePath: clientlogic/cl_platformdata/pc/throw/p8015.pyc
# Source Generated with Decompyle++
# File: p8015.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_commondefines import GARDENER_THROW_DAMAGE

def Action(skill):
    cl_action.SetSkillServerCache(skill, 'ExShowTips', [
        GARDENER_THROW_DAMAGE][0])
    cl_action.SetDirectHitInfo(skill, cl_action.GetSkillVID(skill))
    cl_action.SendParasiticTriggerMsg(skill, cl_action.GetSkillCustomData(skill, 'Mul', defaultValue = 1))
    cl_action.PerformDamage(skill, {
        'Att': cl_action.ToInt(skill, (skill.m_Cache['Att'] + cl_action.GetSkillCustomData(skill, 'Mul', defaultValue = 1) * (cl_action.GetPerformArgValue(skill, 'MulDam', iDefault = 0) * cl_action.GetPerformArgValue(skill, 'DamRatio', iDefault = 0) / 100)) * cl_action.GetPerformArgValue(skill, 'BaseDamRatio', iDefault = 0) / 100) })


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return []


def GetOtherMonster():
    return []

from cl_perform.throw import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_CORRISION

class CPerform(CCustomPerform):
    m_SID = 8015
    m_Name = '#NT#园丁单次Q技能伤害'
    m_ExtPerform = ()
    m_HaltInfo = { }
    m_IgnoreHalt = { }
    m_ActionInfo = {
        1: Action }
    m_HaltActionInfo = {
        1: Halt }
    m_EndActionInfo = {
        1: End }
    m_ElementType = DAM_TYPE_CORRISION
    m_BaseAttrData = {
        'ColdTime': 0,
        'AttDistance': 0,
        'MaxCover': 1,
        'BulletSID': 0,
        'Att': 25000,
        'CrazyEff': 0,
        'BulletSpeed': 45,
        'DebuffProb': 1500,
        'ExplodeDelay': 500,
        'Radius': 5,
        'BulletVerticalAcc': 0,
        'AddStateTime': 300,
        'KeepTime': 300,
        'DamInterval': 100,
        'Pierce': 0,
        'TriggerTimes': 1,
        'MinUseEnergy': 0 }
    m_ForbidRule = 0
    m_CheckForbid = 0
    m_BaseArgData = {
        'MulDam': 10000,
        'DamRatio': 100,
        'BaseDamRatio': 100 }
    m_UnCrtByOwnerSign = 1
    m_AIPerformDam = 2000

