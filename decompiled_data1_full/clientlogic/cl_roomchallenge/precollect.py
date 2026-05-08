# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_roomchallenge/precollect.pyc
# RelativePath: clientlogic/cl_roomchallenge/precollect.pyc
# Source Generated with Decompyle++
# File: precollect.pyc (Python 3.6)

from cl_commondefines import CHALLENGE_ABERRANCE, CHALLENGE_BOXMONSTER, CHALLENGE_KILLSUMMON, SPAWN_ADDROOMCHALLENGE, CHALLENGE_ELITE, CHALLENGE_EXTRAMONSTER, CHALLENGE_EXTRAELITE

class CPreCollect(object):
    
    def __init__(self, oParent):
        self.m_Parent = oParent
        self.m_Game = oParent.m_Game
        self.m_MonterPreCollect = { }

    
    def Release(self):
        self.m_Parent = None
        self.m_Game = None

    
    def CollectOnLevelInit(self, iLevel):
        self.m_MonterPreCollect[iLevel] = []
        if self.m_Game.m_WarMgr.Query('AssignRoomChallenge'):
            iChallengeSID = self.m_Game.m_WarMgr.Query('AssignRoomChallenge')
            lstMonsterSID = self.CollectMonster(iChallengeSID)
            self.m_MonterPreCollect[iLevel].extend(lstMonsterSID)
        oLevelCtrl = self.m_Game.m_WarMgr.GetComponent('LevelCtrl')
        if not oLevelCtrl:
            return None
        oLevelNode = oLevelCtrl.GetLevelNode(iLevel)
        if not oLevelNode:
            return None
        iRound = self.m_Game.m_WarMgr.m_Round
        oLevelConfData = oLevelCtrl.m_LevelConfData
        for lstLine in oLevelNode.m_RoomList:
            for oLine in lstLine:
                lstSpawnRule = oLevelConfData.GetLineSpawnRule(iLevel, oLine.m_Name, iRound)
                for dSpawn in lstSpawnRule:
                    tAction = dSpawn['Action']
                    for dAction in tAction:
                        func = dAction['func']
                        if func != SPAWN_ADDROOMCHALLENGE:
                            continue
                        iChallengeSID = dAction['param'][0]
                        lstMonsterSID = self.CollectMonster(iChallengeSID)
                        self.m_MonterPreCollect[iLevel].extend(lstMonsterSID)
                    
                
            
        
        lstMonsterSID = self.m_MonterPreCollect[iLevel]
        self.m_MonterPreCollect[iLevel] = list(set(lstMonsterSID))

    
    def CollectOnChoose(self, iLevel, dChoose):
        for (iLevel, _), iChallengeSID in dChoose.items():
            lstMonsterSID = self.CollectMonster(iChallengeSID)
            self.m_MonterPreCollect[iLevel].extend(lstMonsterSID)
        
        lstMonsterSID = self.m_MonterPreCollect[iLevel]
        self.m_MonterPreCollect[iLevel] = list(set(lstMonsterSID))

    
    def CollectMonster(self, iChallengeSID):
        clsChallengeData = self.m_Game.m_WarData.GetChallengeData(iChallengeSID)
        lstBaseSID = []
        lstMonsterSID = []
        if clsChallengeData:
            tParam = clsChallengeData.m_Param
            if clsChallengeData.m_Type in (CHALLENGE_BOXMONSTER, CHALLENGE_EXTRAMONSTER, CHALLENGE_ELITE, CHALLENGE_ABERRANCE):
                lstMonsterSID = [
                    tParam[0]]
            elif clsChallengeData.m_Type in (CHALLENGE_KILLSUMMON,):
                lstMonsterSID = list(tParam[0].keys())
            elif clsChallengeData.m_Type == CHALLENGE_EXTRAELITE:
                for tChoose in tParam[2].keys():
                    for iMonsterSID in tChoose:
                        if iMonsterSID in lstMonsterSID:
                            continue
                        lstMonsterSID.append(iMonsterSID)
                    
                
            lstBaseSID = []
            for iMonsterSID in lstMonsterSID:
                clsMonsterData = self.m_Game.m_WarData.GetMonsterData(iMonsterSID)
                if not clsMonsterData:
                    continue
                iBaseSID = clsMonsterData.m_DataSID
                lstBaseSID.append(iBaseSID)
            
        return lstBaseSID

    
    def QueryMonsterCategory(self, iLevel):
        if iLevel in self.m_MonterPreCollect:
            return self.m_MonterPreCollect[iLevel]
        return []


