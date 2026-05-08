# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_action/ac_common.pyc
# RelativePath: clientlogic/cl_action/ac_common.pyc
# Source Generated with Decompyle++
# File: ac_common.pyc (Python 3.6)

from cl_only import Functor, GAME_FRAME
from cl_commondefines import CHECKTYPE_CLIENTBEHAVIOR
from cllib.lib_only import RunMobileData
import cl_perform
import cl_snetwar

def HaltCasting(oTarget, iActNum, sReason):
    oSkill = oTarget.m_Game.m_SkillMgr.GetSkill(oTarget.m_ID, iActNum)
    if oSkill:
        oSkill.Halt()
    else:
        oTarget.HaltWaitSkill(iActNum)


def HaltAllCasting(oTarget, sReason):
    for iActNum in list(oTarget.m_CastingSkill.keys()):
        HaltCasting(oTarget, iActNum, sReason)
    


def CastingForbid(oTarget, oSkill):
    iPerform = oSkill.m_Base['pfid']
    iRule = cl_perform.GetPerformClassAttr(iPerform, 'm_ForbidRule')
    if iRule:
        sKey = oSkill.m_Base['PFKey']
        iWeapon = oSkill.m_Base['Weapon']
        if iWeapon:
            oForbidObj = oTarget.m_WieldCon.GetItemByID(iWeapon)
        else:
            oForbidObj = oTarget
        if not oForbidObj:
            return None
        oForbidObj.Forbid(iRule, sKey)
        oTarget.SetCastingEndFunc(oSkill, Functor(CastingForbidEnd, iRule, sKey, iWeapon))


def CastingForbidEnd(iRule, sKey, iWeapon, oAttack):
    if iWeapon:
        oForbidObj = oAttack.m_WieldCon.GetItemByID(iWeapon)
        if not oForbidObj:
            return None
    oForbidObj = oAttack
    oForbidObj.UnForbid(iRule, sKey)

