# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/petability.pyc
# RelativePath: clientlogic/cl_perform/petability.pyc
# Source Generated with Decompyle++
# File: petability.pyc (Python 3.6)

from cl_perform.passive import CPerform
from cl_commondefines import PF_TYPE_PETABILITY, PET_ABILITY_LOW, PET_HATE_START, WARRIOR_PET_MINICLONE, WARRIOR_PET_MINI, PET_ABILITY_TYPE_ONLYMAIN, PET_ABILITY_TYPE_ONLYCLONE
from cl_propdata import BASIC_PROP_NAME
from cl_only import Time2Frame
import cl_msgcenter
ENABLE_TYPE_MAP = {
    PET_ABILITY_TYPE_ONLYCLONE: WARRIOR_PET_MINICLONE,
    PET_ABILITY_TYPE_ONLYMAIN: WARRIOR_PET_MINI }

class CPetAbility(CPerform):
    m_PFType = PF_TYPE_PETABILITY
    m_Quality = PET_ABILITY_LOW
    m_LimitPet = ()
    m_ExcludePet = ()
    m_Weight = 0
    m_SpellPower = 0
    m_AutoCDCallBack = 0
    m_SkillIntervalAttr = 'SkillInterval'
    m_NeedLockTarget = 0
    m_DieDisable = 0
    m_AIMemberPetDisable = False
    m_EnableType = 0
    
    def OnInit(self):
        self.m_ExtCover = 0

    
    def AddExtCover(self):
        if self.m_ExtCover:
            return None
        self.m_ExtCover = 1

    
    def Enable(self, oWarrior, iNotify = 0):
        if self.m_Enable:
            return None
        if oWarrior.m_FightType in (WARRIOR_PET_MINI, WARRIOR_PET_MINICLONE) and self.m_EnableType in ENABLE_TYPE_MAP and oWarrior.m_FightType != ENABLE_TYPE_MAP[self.m_EnableType]:
            return None
        if self.m_DieDisable and oWarrior.IsDead():
            if oWarrior.m_DieDisablePassive is None:
                oWarrior.m_DieDisablePassive = []
            oWarrior.m_DieDisablePassive.append(self.m_SID)
            return None
        self.SpellEnable(oWarrior)
        if self.m_NeedLockTarget:
            cl_msgcenter.AddFunction(oWarrior, cl_msgcenter.MSG_WAR_PET_UPDATE_HATE, self.OnLockEnemy, self.m_Key, iSub = PET_HATE_START, iOnce = 0)
        super().Enable(oWarrior, iNotify)

    
    def Disable(self, oWarrior, iNotify = 1, iReleaseFlag = 0):
        if not self.m_Enable:
            return None
        self.SpellDisable(oWarrior)
        if self.m_NeedLockTarget:
            cl_msgcenter.DoneEvent(oWarrior, cl_msgcenter.MSG_WAR_PET_UPDATE_HATE, self.m_Key, iSub = PET_HATE_START)
        super().Disable(oWarrior, iNotify, iReleaseFlag)

    
    def OnLockEnemy(self, oWarrior, dMsgInfo):
        if self.InColdTime() and not (self.m_ExtCover):
            return None
        oOwner = self.GetOwner()
        self.TrueCDCallBack(oOwner)

    
    def CDCallBack(self, oWarrior):
        oContainer = self.m_Container
        oContainer.DelColdTime(self.m_SID)
        if self.m_NeedLockTarget:
            if not (oWarrior.m_Agent) or not oWarrior.m_Agent.GetLockEnemy():
                return None
        self.TrueCDCallBack(oWarrior)

    
    def TrueCDCallBack(self, oWarrior):
        if not self.m_Enable:
            return None
        if self.m_Level not in self.m_LifeCycleLevel:
            return None
        if self.m_ExtCover:
            self.m_ExtCover = 0
            self.m_LifeCycleLevel[self.m_Level].CallFunc('ColdDown', oWarrior)
            self.OnLockEnemy(oWarrior, { })
            return None
        self.m_LifeCycleLevel[self.m_Level].CallFunc('ColdDown', oWarrior)
        if not self.m_AutoCDCallBack:
            return None
        self.SetCDTime(oWarrior, self.GetArgValue('SpellCDTime'))
        dMsgInfo = {
            'Perform': self.m_SID,
            'Owner': self.m_Owner }
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_PET_PASSIVESPELL_SETCD, oWarrior, dMsgInfo, iSub = -1)

    
    def SpellEnable(self, oWarrior):
        if not self.CheckIsSpell():
            return None
        self.SetSpellCDTime(oWarrior, dMsgInfo = None)
        iSub = BASIC_PROP_NAME[self.m_SkillIntervalAttr][0]
        oWarrior.AddRefreshAttr(self.m_SkillIntervalAttr)
        cl_msgcenter.AddFunction(oWarrior, cl_msgcenter.MSG_WAR_ATTR_CHANGE, self.SetSpellCDTime, self.m_Key, iSub = iSub, iOnce = 0)
        self.SetCDTime(oWarrior, self.GetArgValue('SpellCDTime'))
        oWarrior.AddEnableSpell(self.m_SID)

    
    def SpellDisable(self, oWarrior):
        if not self.CheckIsSpell():
            return None
        iSub = BASIC_PROP_NAME[self.m_SkillIntervalAttr][0]
        oWarrior.DelRefreshAttr(self.m_SkillIntervalAttr)
        cl_msgcenter.DoneEvent(oWarrior, cl_msgcenter.MSG_WAR_ATTR_CHANGE, self.m_Key, iSub = iSub)
        oWarrior.RemoveEnableSpell(self.m_SID)

    
    def SetSpellCDTime(self, oTarget, dMsgInfo):
        self.SetArgValue('SpellCDTime', self.GetSpellCDFrame(oTarget))

    
    def GetSpellCDFrame(self, oWarrior):
        iTime = oWarrior.QueryAttr(self.m_SkillIntervalAttr) * self.m_SpellPower // 100
        return Time2Frame(iTime)

    
    def CheckIsSpell(self):
        if self.m_SpellPower > 0:
            return 1
        return 0

    
    def CheckIsAIMemberPetDisable(self):
        return self.m_AIMemberPetDisable


