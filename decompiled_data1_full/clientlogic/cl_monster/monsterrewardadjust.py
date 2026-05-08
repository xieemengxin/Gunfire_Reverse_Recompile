# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_monster/monsterrewardadjust.pyc
# RelativePath: clientlogic/cl_monster/monsterrewardadjust.pyc
# Source Generated with Decompyle++
# File: monsterrewardadjust.pyc (Python 3.6)

import cl_formula

class CBaseRewardAdjust(object):
    
    def DoneAllRewardAdjust(self, obj):
        oWarMgr = obj.m_Game.m_WarMgr
        oRoundElement = oWarMgr.GetComponent('RoundElement')
        dCycleRewardInfo = oRoundElement.m_CycleMonsterRewardAdjust if oRoundElement else { }
        self.AddRewardRatio(obj, dCycleRewardInfo)

    
    def AddRewardRatio(self, obj, dCycleRewardInfo):
        iRound = obj.m_Game.m_WarMgr.m_Round
        if iRound not in obj.m_Reward:
            return None
        dReward = obj.m_Reward[iRound]
        for iRewardSID, tReward in dReward.items():
            if iRewardSID in dCycleRewardInfo:
                iRatio = cl_formula.GetFormulaResult(obj, tReward[0], { })
                if iRatio > 0:
                    iAddRatio = cl_formula.GetFormulaResult(obj, dCycleRewardInfo[iRewardSID], { })
                    iNewRatio = iRatio + iAddRatio
                    dReward[iRewardSID] = (iNewRatio, tReward[1])
        


