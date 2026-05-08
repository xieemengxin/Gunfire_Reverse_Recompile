# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/net.pyc
# RelativePath: clientlogic/cl_perform/net.pyc
# Source Generated with Decompyle++
# File: net.pyc (Python 3.6)

from cl_protocol import GS2C_SKILL_START, GS2C_SKILL_TRIGGER, GS2C_SKILL_THROUGHINFO, GS2C_CLIENT_SKILL_TRIGGER
from cl_commondefines import SKILLRET_FAIL, RUN_STEP_NORMAL, RUN_STEP_BELOW
from cl_duonet.netfunc import *
from cl_object.logging import SkillLog
from .cartoon import netdata as cartoondata
import cl_war
import cl_duonet.dn_cl_perform_net
import cl_perform.skillcache
import cllib.lib_flag as lib_flag
import cl_gamedebug
import time
if lib_flag.g_UseSkillID:
    
    def GS2CSkillStartCut(oSkill, dNet, lstPlayer):
        PacketPrepare(GS2C_SKILL_START)
        PacketAddI(oSkill.m_SkillID, 2)
        PacketAddI(oSkill.m_Base['AID'], 4)
        PacketAddI(oSkill.m_Base['pfid'], 2)
        PacketAddI(oSkill.m_Base['ActNum'], 2)
        PacketAddI(oSkill.m_Base['AttrObj'], 4)
        PacketAddI(oSkill.m_Base['VID'], 4)
        cartoondata.PacketSkill(dNet)
        cl_perform.skillcache.CacheInitSend(oSkill)
        SendToPlayers(lstPlayer)

    
    def GS2CSkillResend(oSkill, iPlayer, dNet):
        PacketPrepare(GS2C_SKILL_START)
        PacketAddI(oSkill.m_SkillID, 2)
        PacketAddI(oSkill.m_Base['AID'], 4)
        PacketAddI(oSkill.m_Base['pfid'], 2)
        PacketAddI(oSkill.m_Base['ActNum'], 2)
        PacketAddI(oSkill.m_Base['AttrObj'], 4)
        PacketAddI(oSkill.m_Base['VID'], 4)
        cartoondata.PacketSkill(dNet)
        cl_perform.skillcache.CacheInitSend(oSkill)
        DGamePacketSend(oSkill.m_Game, iPlayer)

    
    def GS2CSkillTriggerCut(oSkill, dNet, lstPlayer):
        PacketPrepare(GS2C_SKILL_TRIGGER)
        PacketAddI(oSkill.m_SkillID, 2)
        cartoondata.PacketSkill(dNet)
        SendToPlayers(lstPlayer)

    
    def GS2CSkillThroughInfo(oSkill, dNet, iExclude = 0):
        PacketPrepare(GS2C_SKILL_THROUGHINFO)
        PacketAddI(oSkill.m_SkillID, 2)
        cl_perform.skillcache.CacheChooseSend(oSkill, dNet['Choose'])
        DGameSceneBroadCastExclude(oSkill.m_Game, oSkill.m_Base['Scene'], iExclude)

    
    def GS2CClientSkillTrigger(oSKill, dNet, lstPlayer):
        PacketPrepare(GS2C_CLIENT_SKILL_TRIGGER)
        PacketAddI(oSKill.m_Base['ActNum'], 2)
        cartoondata.PacketSkill(dNet)
        SendToPlayers(lstPlayer)

else:
    
    def GS2CSkillStartCut(oSkill, dNet, lstPlayer):
        PacketPrepare(GS2C_SKILL_START)
        PacketAddI(oSkill.m_Base['AID'], 4)
        PacketAddI(oSkill.m_Base['pfid'], 2)
        PacketAddI(oSkill.m_Base['ActNum'], 2)
        PacketAddI(oSkill.m_Base['AttrObj'], 4)
        PacketAddI(oSkill.m_Base['VID'], 4)
        cartoondata.PacketSkill(dNet)
        cl_perform.skillcache.CacheInitSend(oSkill)
        SendToPlayers(lstPlayer)

    
    def GS2CSkillResend(oSkill, iPlayer, dNet):
        PacketPrepare(GS2C_SKILL_START)
        PacketAddI(oSkill.m_Base['AID'], 4)
        PacketAddI(oSkill.m_Base['pfid'], 2)
        PacketAddI(oSkill.m_Base['ActNum'], 2)
        PacketAddI(oSkill.m_Base['AttrObj'], 4)
        PacketAddI(oSkill.m_Base['VID'], 4)
        cartoondata.PacketSkill(dNet)
        cl_perform.skillcache.CacheInitSend(oSkill)
        DGamePacketSend(oSkill.m_Game, iPlayer)

    
    def GS2CSkillTriggerCut(oSkill, dNet, lstPlayer):
        PacketPrepare(GS2C_SKILL_TRIGGER)
        PacketAddI(oSkill.m_Base['AID'], 4)
        PacketAddI(oSkill.m_Base['ActNum'], 2)
        cartoondata.PacketSkill(dNet)
        SendToPlayers(lstPlayer)

    
    def GS2CSkillThroughInfo(oSkill, dNet, iExclude = 0):
        PacketPrepare(GS2C_SKILL_THROUGHINFO)
        PacketAddI(oSkill.m_Base['AID'], 4)
        PacketAddI(oSkill.m_Base['ActNum'], 2)
        cl_perform.skillcache.CacheChooseSend(oSkill, dNet['Choose'])
        DGameSceneBroadCastExclude(oSkill.m_Game, oSkill.m_Base['Scene'], iExclude)

    
    def GS2CClientSkillTrigger(oSKill, dNet, lstPlayer):
        pass


def GS2CSkillHalt(oSkill):
    oGame = oSkill.m_Game
    iScene = oSkill.m_Base['Scene']
    oScene = oGame.m_SceneMgr.GetScene(iScene)
    if not oScene:
        return None
    dPlayer = oScene.GetPlayers()
    netData = {
        'oGame': oSkill.m_Game,
        'iScene': iScene,
        'dPlayer': dPlayer,
        'AID': oSkill.m_Base['AID'],
        'ActNum': oSkill.m_Base['ActNum'] }
    cl_duonet.dn_cl_perform_net.DN_GS2CSkillHalt(netData)
    cl_war.SkillTryFallBackBullet(oSkill)


def GS2CSkillHaltCut(oSkill, lstPlayer):
    netData = {
        'oGame': oSkill.m_Game,
        'iScene': oSkill.m_Base['Scene'],
        'dPlayer': lstPlayer,
        'AID': oSkill.m_Base['AID'],
        'ActNum': oSkill.m_Base['ActNum'] }
    cl_duonet.dn_cl_perform_net.DN_GS2CSkillHalt(netData)


def GS2CSkillFail(oWarrior, iActNum):
    netData = {
        'oGame': oWarrior.m_Game,
        'pid': oWarrior.m_PlayerID,
        'AID': oWarrior.m_ID,
        'ActNum': iActNum }
    cl_duonet.dn_cl_perform_net.DN_GS2CSkillFail(netData)


def GS2CAddBulletChangeRule(oGame, oPerform, dPlayer):
    netData = {
        'iPerform': oPerform.m_ID,
        'iRuleSID': oPerform.m_SID,
        'iItemID': oPerform.m_Item,
        'iLevel': oPerform.m_Level,
        'oGame': oGame,
        'dPlayer': dPlayer }
    cl_duonet.dn_cl_perform_net.DN_GS2CAddBulletChangeRule(netData)


def GS2CDelBulletChangeRule(oGame, oPerform, dPlayer):
    netData = {
        'iPerform': oPerform.m_ID,
        'iRuleSID': oPerform.m_SID,
        'oGame': oGame,
        'dPlayer': dPlayer }
    cl_duonet.dn_cl_perform_net.DN_GS2CDelBulletChangeRule(netData)


def C2GSSkillStart(oGame, oWarrior):
    iPerform = UnpackInt(2)
    iActNum = UnpackInt(2)
    iAttrObj = UnpackInt(4)
    iVictim = UnpackInt(4)
    iWeapon = 0
    if iAttrObj:
        oItem = oWarrior.m_WieldCon.GetItemByID(iAttrObj)
        if oItem:
            iWeapon = iAttrObj
    pfobj = oWarrior.GetPerform(iPerform, iWeapon)
    if not pfobj:
        return None
    dNetData = cartoondata.UnpackSkill(oWarrior, pfobj.m_SID)
    oCacheData = cl_perform.skillcache.CacheInitPacket()
    dBulletData = { }
    iBulletTrigger = UnpackInt(1)
    if iBulletTrigger:
        dBulletData = cartoondata.UnpackBulletChange()
    dData = {
        'ActNum': iActNum,
        'Weapon': iWeapon,
        'AttrObj': iAttrObj,
        'VID': iVictim,
        'Net': dNetData,
        'CtrlCache': oCacheData,
        'BulletChange': dBulletData }
    iRlt = cl_war.UsePerform(oWarrior, pfobj, dData)
    if iRlt == SKILLRET_FAIL:
        GS2CSkillFail(oWarrior, iActNum)

if not (lib_flag.g_IsLogicLayer) and lib_flag.g_IsAuthorityRun:
    from cl_only import GAME_FRAME
    from cl_commondefines import WARRIOR_MONSTER
    g_SkillTriggerInfo = { }
    INTERVALFRAME = 10 * GAME_FRAME
    
    def C2GSSkillTrigger(oGame, oWarrior):
        iPreStateID = oGame.m_StateID
        iPreNpcID = oGame.m_NpcID
        iPreCartoonID = oGame.m_CartoonID
        iPreActNum = oWarrior.m_ActionNum
        iStart = time.time()
        iActNum = UnpackInt(2)
        if iActNum in oWarrior.m_FramingSkill:
            oSkill = None
        else:
            oSkill = oGame.m_SkillMgr.GetSkill(oWarrior.m_ID, iActNum)
        dNetData = cartoondata.UnpackSkill(oWarrior, oSkill)
        iBulletTrigger = UnpackInt(1)
        if iBulletTrigger:
            dBulletData = cartoondata.UnpackBulletChange()
            if oSkill:
                cl_war.TriggerBulletChange(oWarrior, oSkill, dBulletData)
            else:
                dNetData['BulletChange'] = dBulletData
        if oSkill:
            oSkill.NetTriggerUpdate(dNetData)
        elif iActNum in oWarrior.m_FramingSkill:
            oWarrior.CacheFramingSkill(iActNum, dNetData)
        else:
            oWarrior.CacheWaitingSkill(iActNum, dNetData)
        iEnd = time.time()
        if iEnd - iStart > 0.04:
            iGameID = oGame.m_ID
            iPlayer = oWarrior.m_PlayerID
            if iGameID not in g_SkillTriggerInfo:
                g_SkillTriggerInfo[iGameID] = { }
            if iPlayer not in g_SkillTriggerInfo:
                g_SkillTriggerInfo[iGameID][iPlayer] = { }
            dSkillTriggerInfo = g_SkillTriggerInfo[iGameID][iPlayer]
            iCurFrame = oGame.GetFrameNum()
            iSkill = 0
            if oSkill:
                iSkill = oSkill.m_Base.get('pfid', 0)
                if iSkill in dSkillTriggerInfo and iCurFrame - dSkillTriggerInfo[iSkill] < INTERVALFRAME:
                    return None
                dSkillTriggerInfo[iSkill] = iCurFrame
            iCurStateID = oGame.m_StateID
            iCurNpcID = oGame.m_NpcID
            iCurCartoonID = oGame.m_CartoonID
            iCurActNum = oWarrior.m_ActionNum
            sNpcInfo = ''
            for iNpcID in range(iPreNpcID + 1, iCurNpcID + 1):
                oNpc = oGame.GetObject(iNpcID)
                sNpcInfo += '%s:' % oNpc
                if oNpc and hasattr(oNpc, 'm_SID'):
                    sNpcInfo += '%s\n' % oNpc.m_SID
            
            sVictimInfo = ''
            iVictimNum = 0
            for dInfo in dNetData.values():
                lstHitInfo = dInfo.get('Ray', [])
                if not lstHitInfo:
                    continue
                iVictimNum += len(lstHitInfo)
                for _, _, iVictim, _ in lstHitInfo:
                    oVictim = oGame.GetObject(iVictim)
                    sVictimInfo += '%s:' % oVictim
                    if oVictim and hasattr(oVictim, 'm_SID'):
                        sVictimInfo += '%s' % oVictim.m_SID
                        if hasattr(oVictim, 'm_FightType') and oVictim.m_FightType & WARRIOR_MONSTER:
                            sVictimInfo += ' state: %s perform: %s\n' % (oVictim.m_State.m_StateBySid.keys(), oVictim.m_Perform.m_Perform.keys())
                        sVictimInfo += '\n'
                
            
            if oSkill:
                SkillLog.Alert('trigger pid:%d time:%.5f skill:%s state:%d npc:%d cartoon:%d prenum:%d curnum:%d victimnum:%s' % (oWarrior.m_PlayerID, iEnd - iStart, iSkill, iCurStateID - iPreStateID, iCurNpcID - iPreNpcID, iCurCartoonID - iPreCartoonID, iPreActNum, iCurActNum, iVictimNum))
                SkillLog.Debug('victiminfo:%s npcinfo:%s netdata:%s' % (sVictimInfo, sNpcInfo, dNetData))
            if iBulletTrigger:
                SkillLog.Alert('bullettrigger overtime:%s bulletData:%s' % (iEnd - iStart, dBulletData))

else:
    
    def C2GSSkillTrigger(oGame, oWarrior):
        iActNum = UnpackInt(2)
        if iActNum in oWarrior.m_FramingSkill:
            oSkill = None
        else:
            oSkill = oGame.m_SkillMgr.GetSkill(oWarrior.m_ID, iActNum)
        dNetData = cartoondata.UnpackSkill(oWarrior, oSkill)
        iBulletTrigger = UnpackInt(1)
        if iBulletTrigger:
            dBulletData = cartoondata.UnpackBulletChange()
            if oSkill:
                cl_war.TriggerBulletChange(oWarrior, oSkill, dBulletData)
            else:
                dNetData['BulletChange'] = dBulletData
        if oSkill:
            oSkill.NetTriggerUpdate(dNetData)
        elif iActNum in oWarrior.m_FramingSkill:
            oWarrior.CacheFramingSkill(iActNum, dNetData)
        else:
            oWarrior.CacheWaitingSkill(iActNum, dNetData)


def C2GSSkillDelegate(oGame, oWarrior):
    iActNum = UnpackInt(2)
    iAttack = UnpackInt(4)
    oSkill = oGame.m_SkillMgr.GetSkill(iAttack, iActNum)
    if oSkill:
        dNetData = cartoondata.UnpackSkill(oWarrior, oSkill)
        for dRecv in dNetData.values():
            dRecv['Source'] = oWarrior.m_ID
        
        oSkill.NetTriggerUpdate(dNetData)


def C2GSSkillThroughInfo(oGame, oWarrior):
    iActNum = UnpackInt(2)
    oSkill = oGame.m_SkillMgr.GetSkill(oWarrior.m_ID, iActNum)
    if not oSkill:
        return None
    lstChoose = cl_perform.skillcache.SyncClientCacheData(oSkill)
    GS2CSkillThroughInfo(oSkill, {
        'Choose': lstChoose }, oWarrior.m_PlayerID)


def C2GSSkillTriggerBulletChange(oGame, oWarrior):
    iPerform = UnpackInt(4)
    iGroup = UnpackInt(1)
    iMethod = UnpackInt(1)
    dNode = cartoondata.UnpackBulletItem()
    dData = {
        iPerform: {
            (iGroup, iMethod): dNode } }
    cl_war.TriggerBulletChange(oWarrior, None, dData)


def C2GSBulletRuleEnable(oWarrior, iBulletChange):
    oCon = oWarrior.m_BulletChangeCon
    oPerform = oCon.GetPerformByID(iBulletChange)
    if oPerform:
        oPerform.TrueEnable(oWarrior)


def C2GSBulletRuleDisable(oWarrior, iBulletChange):
    oCon = oWarrior.m_BulletChangeCon
    oPerform = oCon.GetPerformByID(iBulletChange)
    if oPerform:
        oPerform.TrueDisable(oWarrior)

