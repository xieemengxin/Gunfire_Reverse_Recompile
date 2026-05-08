# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/commonative/p1723.pyc
# RelativePath: clientlogic/cl_platformdata/pc/commonative/p1723.pyc
# Source Generated with Decompyle++
# File: p1723.pyc (Python 3.6)

from cl_platformdata.custom.commonative.customaction import CommonAddToxicCount
import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon

def Action(skill):
    cl_action.SetDirectHitInfo(skill, cl_action.GetSkillVID(skill))
    cl_action.CustomPerformAction(skill, 1723, 'AddToxicCount', { })
    cl_action.CustomPerformAction(skill, 7204, 'ToxicDam', { })


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return []


def GetOtherMonster():
    return []

from cl_perform.commonative import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_CORRISION

class CPerform(CCustomPerform):
    m_SID = 1723
    m_Name = '毒气装置-桃专属组件技能'
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
        'ChargeTime': 0 }
    m_ClientNeed = 0
    m_UseCurWeapon = 0
    m_ForbidRule = 0
    m_BaseArgData = {
        'DebuffProb': 3000,
        'AddCount': 1 }
    
    def CanUse(self, oWarrior, dInfo):
        if self.GetArgValue('UseCount', 0) < 1:
            return 0
        return super().CanUse(oWarrior, dInfo)

    
    def UsePerform(self, oWarrior, oSkill):
        self.AddArgValue('UseCount', -1)
        super().UsePerform(oWarrior, oSkill)



def AddToxicCount(oSkill, *args):
    if 'CurVID' not in oSkill.m_Update:
        return None
    iTarget = oSkill.m_Update['CurVID']
    oTarget = oSkill.m_Game.GetObject(iTarget)
    if not oTarget:
        return None
    iAttack = oSkill.m_Base['AID']
    dData = {
        'AddCount': oSkill.m_Cache['AddCount'] }
    CommonAddToxicCount(oTarget, iAttack, dCustomData = dData)

