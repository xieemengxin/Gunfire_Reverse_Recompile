# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_monster/monsterdurability.pyc
# RelativePath: clientlogic/cl_monster/monsterdurability.pyc
# Source Generated with Decompyle++
# File: monsterdurability.pyc (Python 3.6)

import cl_monster.mobject
import cl_snetwar

class CMonsterDurability(cl_monster.mobject.CMonster):
    
    def HPModifyDam(self, iAttack, lstChange):
        oOwner = self.m_Game.GetObject(self.m_Owner)
        if oOwner:
            lstNewChange = []
            for iChange, oReason in lstChange:
                lstNewChange.append((iChange, oReason.ExtInfo({
                    'ShowTips': 0 })))
            
            (_, lstTrueChange, _) = oOwner.HPModifyDam(iAttack, lstNewChange)
            for iTrueChange, oReason in lstTrueChange:
                self.HPDirectModify('HP', iAttack, -iTrueChange, oReason)
            
            self.TipDam(iAttack, lstTrueChange)
        return ([
            0,
            0,
            0], [], [])

    
    def TipDam(self, iAttack, lstTrueChange):
        oGame = self.m_Game
        oAttack = oGame.GetObject(iAttack)
        iTargetPlayer = oAttack.m_OwnerPlayerID if oAttack and oAttack.m_OwnerPlayerID else self.m_PlayerID
        if not iTargetPlayer:
            return None
        for iDam, oReason in lstTrueChange:
            iDamType = oReason.Query('DamType', 0)
            iActNum = oReason.Query('ActNum', 0)
            oSkill = oGame.m_SkillMgr.GetSkill(iAttack, iActNum) if iActNum else None
            iBreakShield = 0
            iTriggerAbnormal = 0
            iInitDam = oReason.Query('InitDam')
            iWeaked = 1 if iInitDam > iDam else 0
            iLuckyHitEff = oReason.Query('LuckyHitEff', 1) if oSkill else 1
            iExInfo = 1 if oReason.Query('ExInfo', 1) != 0 else 0
            if oSkill and 'ExShowTips' in oSkill.m_Collect:
                iExShowTips = oSkill.m_Collect['ExShowTips']
            else:
                iExShowTips = 0
            iExInfo = iExInfo | iExShowTips
            cl_snetwar.GS2CWStatusHP(self, oSkill, iTargetPlayer, iAttack, iActNum, iDam, iDamType, iTriggerAbnormal, iBreakShield, iWeaked, iLuckyHitEff, iExInfo)
        


