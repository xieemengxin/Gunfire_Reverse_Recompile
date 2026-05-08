# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/commonative/p1972.pyc
# RelativePath: clientlogic/cl_platformdata/pc/commonative/p1972.pyc
# Source Generated with Decompyle++
# File: p1972.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import TimerCartoon
from cl_commondefines import CRT_CHECK_SERVER, SKILLCACHE_LSTPOS

class CCartoon1(TimerCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        pass

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        if len(cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTPOS)) > 0:
            cl_action.CreateMonsterHinder(skill, 1213, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTPOS)[0], cl_action.GetOneListFromRandonList(skill, [
                [
                    1,
                    4,
                    5,
                    7,
                    9],
                [
                    1,
                    4,
                    7,
                    8,
                    9],
                [
                    2,
                    3,
                    4,
                    6,
                    7,
                    9],
                [
                    2,
                    5,
                    7,
                    8,
                    9],
                [
                    4,
                    6,
                    7,
                    8,
                    9],
                [
                    5,
                    7,
                    8,
                    9],
                [
                    4,
                    5,
                    6,
                    7,
                    9],
                [
                    1,
                    4,
                    5,
                    6,
                    9],
                [
                    3,
                    5,
                    6,
                    7,
                    9],
                [
                    1,
                    4,
                    5,
                    6,
                    7,
                    9],
                [
                    3,
                    5,
                    6,
                    7,
                    8,
                    9],
                [
                    2,
                    4,
                    5,
                    6,
                    7,
                    8],
                [
                    2,
                    4,
                    5,
                    7,
                    9],
                [
                    1,
                    2,
                    4,
                    6,
                    7,
                    8,
                    9],
                [
                    1,
                    2,
                    3,
                    4,
                    6,
                    7]]), { })
            cl_action.MonsterResumeAgent(skill)
        else:
            cl_action.MonsterResumeAgent(skill)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 100, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.MonsterPauseAgent(skill)
    cl_action.StopMove(skill)
    cl_action.SetSkillCacheData(skill, SKILLCACHE_LSTPOS, cl_action.RandomPointSectorInMeshList(skill, cl_action.CrtArgWarriorPos(skill, cl_action.GetSkillVID(skill)), cl_math.Vec3Minus(cl_action.CrtArgSelfPos(skill), cl_action.CrtArgWarriorPos(skill, cl_action.GetSkillVID(skill))), 3, 10, 0, 20, 1))
    cl_action.ServerSendSkillCache(skill, [
        SKILLCACHE_LSTPOS])
    cartoon = { }
    CCartoon1.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    cl_action.MonsterResumeAgent(skill)


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_LSTPOS]


def GetOtherMonster():
    return []

from cl_perform.commonative import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_FIRE

class CPerform(CCustomPerform):
    m_SID = 1972
    m_Name = '明雷法师怪被动阻挡物召唤'
    m_ExtPerform = ()
    m_HaltInfo = { }
    m_IgnoreHalt = { }
    m_ActionInfo = {
        1: Action }
    m_HaltActionInfo = {
        1: Halt }
    m_EndActionInfo = {
        1: End }
    m_ElementType = DAM_TYPE_FIRE
    m_BaseAttrData = {
        'ColdTime': 0,
        'AttDistance': 99,
        'ChargeTime': 0 }
    m_ClientNeed = 0
    m_UseCurWeapon = 0
    m_ForbidRule = 0

