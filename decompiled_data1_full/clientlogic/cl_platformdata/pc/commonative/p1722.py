# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/commonative/p1722.pyc
# RelativePath: clientlogic/cl_platformdata/pc/commonative/p1722.pyc
# Source Generated with Decompyle++
# File: p1722.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_commondefines import MONSTER_PART_UNTAGGED, SIGN_DAMAGE

def Action(skill):
    cl_action.SetDirectHitInfo(skill, cl_action.GetSkillVID(skill))
    cl_action.ModifySkillHitArea(skill, MONSTER_PART_UNTAGGED)
    cl_action.ModifySkillHitPos(skill, cl_action.CrtArgSkillEndPos(skill))
    cl_action.SetSkillServerCache(skill, 'ExShowTips', [
        SIGN_DAMAGE][0])
    cl_action.WeaponDamage(skill, {
        'Att': cl_action.GetSkillCustomData(skill, 'AttRatio', defaultValue = 200) }, { }, sendPFMsg = True)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return []


def GetOtherMonster():
    return []

from cl_perform.commonative import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 1722
    m_Name = '标记法杖标记引爆'
    m_ExtPerform = ()
    m_HaltInfo = { }
    m_IgnoreHalt = { }
    m_ActionInfo = {
        1: Action }
    m_HaltActionInfo = {
        1: Halt }
    m_EndActionInfo = {
        1: End }
    m_ElementType = DAM_TYPE_NORMAL
    m_BaseAttrData = {
        'ColdTime': 0,
        'AttDistance': 0,
        'ChargeTime': 0 }
    m_ClientNeed = 0
    m_UseCurWeapon = 0
    m_ForbidRule = 0

