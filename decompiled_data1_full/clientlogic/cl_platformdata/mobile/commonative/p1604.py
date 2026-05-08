# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/commonative/p1604.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/commonative/p1604.pyc
# Source Generated with Decompyle++
# File: p1604.pyc (Python 3.6)

from cl_cscommondef.cs_other import PF_RS_WARSHOPBUY
import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon

def Action(skill):
    cl_action.AttackerAddState(skill, 1069, 200, 0, { })


def GetSkillCacheIndex():
    return []


def Halt(skill):
    pass


def End(skill):
    pass

from cl_perform.commonative import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 1604
    m_Name = '生命回复'
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
    
    def CanUse(self, oWarrior, dInfo):
        oReason = dInfo.get('RS', None)
        if (oWarrior.Query('AlwaysCure') or oReason) and oReason.GetStrReason() == PF_RS_WARSHOPBUY:
            return super(CPerform, self).CanUse(oWarrior, dInfo)
        iHPMax = oWarrior.QueryAttr('HPMax')
        if oWarrior.QuerySavedData('save.CanCureAll'):
            iShieldMax = oWarrior.QueryAttr('ShieldMax')
            iArmorMax = oWarrior.QueryAttr('ArmorMax')
            if iShieldMax == oWarrior.Shield() and iArmorMax == oWarrior.Armor() and iHPMax == oWarrior.HP():
                return 0
        if iHPMax == oWarrior.HP():
            return 0
        return super(CPerform, self).CanUse(oWarrior, dInfo)


