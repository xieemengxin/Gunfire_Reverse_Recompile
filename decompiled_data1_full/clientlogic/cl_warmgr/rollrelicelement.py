# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_warmgr/rollrelicelement.pyc
# RelativePath: clientlogic/cl_warmgr/rollrelicelement.pyc
# Source Generated with Decompyle++
# File: rollrelicelement.pyc (Python 3.6)

from cl_warmgr.mobject import CBaseElement
from cl_commondefines import MG_SOURCE_RELIC, NWARRIOR_DROP_RELIC, RELIC_TYPE_CURSE, VIRTUAL_ITEM_RELIC, VIRTUAL_ITEM_DROP, DROP_REASON_GAMBLER_ROLLRELIC
import cl_reward
import cl_msgcenter
import cl_perform
ROLL_TYPE_DROP = 1
ROLL_TYPE_PERFORM = 2
ROLL_TYPE_EXTENDRELIC = 3

class CRollRelicElement(CBaseElement):
    
    def __init__(self, oGame, nid, oData):
        super().__init__(oGame, nid, oData)
        self.m_RelicDrop = self.m_Data.m_Config.get('RelicDrop', { })
        self.m_RelicPerform = self.m_Data.m_Config.get('RelicPerform', { })

    
    def RollMiniGameRelic(self, oHero, iLevel, iMiniGameSID, iOldRelic):
        iOld = oHero.GetRollRelicCnt()
        oHero.SetRollRelicCnt(iOld - 1)
        dMsgInfo = {
            'Perform': iOldRelic,
            'Level': iLevel }
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_GAMBLER_ROLL_RELIC, oHero, dMsgInfo)
        iHero = oHero.m_ID
        if dMsgInfo['Level'] != iLevel:
            dReward = {
                'item': VIRTUAL_ITEM_DROP,
                'info': {
                    'DropType': NWARRIOR_DROP_RELIC,
                    'DropInfo': [
                        iOldRelic],
                    'DropLevel': dMsgInfo['Level'] } }
            dExtInfo = {
                'Player': iHero,
                'Abandoner': iHero,
                'ExtStaticInfo': {
                    'RollNum': 1 } }
            cl_reward.RewardItem(self.m_Game, oHero, [
                dReward], 'RollSuperDrop%s' % iOldRelic, dExtInfo)
            return None
        iQuality = cl_perform.GetPerformClassAttr(iOldRelic, 'm_Quality')
        dExtInfo = {
            'CalOffset': 0,
            'CheckGoldenCup': 1,
            'CanReward': 1,
            'AutoReward': 1,
            'OnlyRewardAttack': 1,
            'DropLevel': iLevel,
            'Abandoner': oHero.m_ID,
            'RepeatReward': 1,
            'ExtStaticInfo': {
                'RollNum': 1 },
            'Exclude': [
                iOldRelic] }
        dMiniGame = {
            self.m_RelicDrop[iQuality]: (10000, 1) }
        cl_reward.RewardItemByMiniGame(oHero, iHero, dMiniGame, 'RollMiniGame%d' % iMiniGameSID, MG_SOURCE_RELIC, dExtInfo)

    
    def RollRelic(self, oHero, iDrop, iPerform, iRollType):
        if not oHero.m_Scene:
            return None
        if iRollType == ROLL_TYPE_DROP:
            self.RollRelicDrop(oHero, iDrop)
        elif iRollType == ROLL_TYPE_PERFORM:
            self.RollRelicPerform(oHero, iPerform)
        elif iRollType == ROLL_TYPE_EXTENDRELIC:
            self.RollExtendRelic(oHero, iPerform)

    
    def RollExtendRelic(self, oHero, iPerform):
        oRelicCon = oHero.m_RelicCon
        oPerform = oRelicCon.GetExtendRelic(iPerform)
        if not oPerform:
            return None
        if not self.ValidRollPerform(oHero, oPerform):
            return None
        iOld = oHero.GetRollRelicCnt()
        oHero.SetRollRelicCnt(iOld - 1)
        self.RewardPerform(oHero, oPerform, bExtend = True)

    
    def RollRelicPerform(self, oHero, iPerform):
        oRelicCon = oHero.m_RelicCon
        oPerform = oRelicCon.GetPerform(iPerform)
        if not oPerform:
            return None
        if not self.ValidRollPerform(oHero, oPerform):
            return None
        iOld = oHero.GetRollRelicCnt()
        oHero.SetRollRelicCnt(iOld - 1)
        self.RewardPerform(oHero, oPerform)

    
    def RemoveRelic(self, oHero, iPerform, sReason, bExtend = False):
        oRelicCon = oHero.m_RelicCon
        if bExtend:
            oRelicCon.RemoveExtendRelic(iPerform, sReason)
        else:
            oRelicCon.RemoveRelic(iPerform, sReason, 1)

    
    def ValidRollPerform(self, oHero, oPerform):
        if oHero.GetRollRelicCnt() <= 0:
            return 0
        if oPerform.m_RelicType == RELIC_TYPE_CURSE:
            return 0
        if oPerform.m_Source != oHero.m_PlayerID:
            return 0
        if oPerform.m_RollNum >= oHero.GetMaxRelicRollNum():
            return 0
        return 1

    
    def RollRelicDrop(self, oHero, iID):
        oDrop = self.m_Game.GetObject(iID)
        if not oDrop:
            return None
        iResult = self.ValidRollDrop(oHero, oDrop)
        if iResult:
            iOld = oHero.GetRollRelicCnt()
            oHero.SetRollRelicCnt(iOld - 1)
            oDrop.SetReleaseFlag(0)
            oDrop.Remove('RollRelicDrop')
            self.RewardDrop(oHero, oDrop)

    
    def ValidRollDrop(self, oHero, oDrop):
        if oHero.GetRollRelicCnt() <= 0:
            return 0
        if not oDrop.m_FightType == NWARRIOR_DROP_RELIC:
            return 0
        if not oDrop.ValidRoll(oHero):
            return 0
        if oDrop.m_Source != oHero.m_PlayerID:
            return 0
        if oDrop.m_RollNum >= oHero.GetMaxRelicRollNum():
            return 0
        return 1

    
    def RewardDrop(self, oHero, oDrop):
        iRollNum = oDrop.m_RollNum + 1
        iPerformSID = oDrop.m_DropInfo[0]
        iLevel = oDrop.m_Level
        dMsgInfo = {
            'Perform': iPerformSID,
            'Level': iLevel }
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_GAMBLER_ROLL_RELIC, oHero, dMsgInfo)
        iHero = oHero.m_ID
        if dMsgInfo['Level'] != iLevel:
            dReward = {
                'item': VIRTUAL_ITEM_DROP,
                'info': {
                    'DropType': NWARRIOR_DROP_RELIC,
                    'DropInfo': [
                        iPerformSID],
                    'DropLevel': dMsgInfo['Level'] } }
            dExtInfo = {
                'Player': iHero,
                'Abandoner': iHero,
                'ExtStaticInfo': {
                    'RollNum': iRollNum,
                    'OldDropID': oDrop.m_ID },
                'DropReason': DROP_REASON_GAMBLER_ROLLRELIC }
            cl_reward.RewardItem(self.m_Game, oHero, [
                dReward], 'RollSuperDrop%s' % iPerformSID, dExtInfo)
            return None
        iQuality = cl_perform.GetPerformClassAttr(iPerformSID, 'm_Quality')
        dExtInfo = {
            'CalOffset': 0,
            'CheckGoldenCup': 1,
            'CanReward': 1,
            'AutoReward': 1,
            'OnlyRewardAttack': 1,
            'DropLevel': iLevel,
            'ExtStaticInfo': {
                'RollNum': iRollNum,
                'OldDropID': oDrop.m_ID },
            'Abandoner': oHero.m_ID,
            'Exclude': [
                iPerformSID],
            'DropReason': DROP_REASON_GAMBLER_ROLLRELIC }
        dMiniGame = {
            self.m_RelicDrop[iQuality]: (10000, 1) }
        cl_reward.RewardItemByMiniGame(oHero, oHero.m_ID, dMiniGame, f'''Drop-{oDrop.m_ID}''', MG_SOURCE_RELIC, dExtInfo)

    
    def RewardPerform(self, oHero, oPerform, bExtend = False):
        iRollNum = oPerform.m_RollNum + 1
        iPerformSID = oPerform.m_SID
        iLevel = oPerform.m_Level
        dMsgInfo = {
            'Perform': iPerformSID,
            'Level': iLevel,
            'UpGrade': 0 }
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_GAMBLER_ROLL_RELIC, oHero, dMsgInfo)
        if dMsgInfo['Level'] != iLevel and dMsgInfo['UpGrade']:
            self.RemoveRelic(oHero, iPerformSID, 'RollRelicUpgrade', bExtend)
            dReward = {
                'item': VIRTUAL_ITEM_RELIC,
                'info': {
                    'sid': iPerformSID,
                    'amount': 1,
                    'level': dMsgInfo['Level'] } }
            dExtInfo = {
                'RollNum': iRollNum,
                'ExtendBag': bExtend }
            cl_reward.RewardItem(self.m_Game, oHero, [
                dReward], 'RollSuperRelic%s' % iPerformSID, dExtInfo)
            return None
        self.RemoveRelic(oHero, iPerformSID, 'RollRelicPerform', bExtend)
        iQuality = oPerform.m_Quality
        dMiniGame = {
            self.m_RelicPerform[iQuality]: (10000, 1) }
        dExtInfo = {
            'CheckGoldenCup': 1,
            'OnlyRewardAttack': 1,
            'Abandoner': oHero.m_ID,
            'RepeatReward': 1,
            'Level': dMsgInfo['Level'],
            'RollNum': iRollNum,
            'Exclude': [
                iPerformSID],
            'RepeatDrop': 1,
            'LimitQuality': 1,
            'ExtendBag': bExtend }
        cl_reward.RewardItemByMiniGame(oHero, oHero.m_ID, dMiniGame, 'RollRelicPerform%d' % iPerformSID, MG_SOURCE_RELIC, dExtInfo)



def GetComponentClass(oMgrManager):
    return CRollRelicElement

