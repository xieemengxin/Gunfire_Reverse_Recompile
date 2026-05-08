# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_minigame/mg_equip.pyc
# RelativePath: clientlogic/cl_minigame/mg_equip.pyc
# Source Generated with Decompyle++
# File: mg_equip.pyc (Python 3.6)

from cl_commondefines import VIRTUAL_ITEM_DROP, NWARRIOR_DROP_EQUIP, DEFAULT_DROP_RADIUS, MG_EQUIP, VIRTUAL_ITEM_EQUIP, LEVEL_TYPE_BOSS, PLAYER_CHOOSE_EQUIP
from cl_cscommondef import ITEM_SOURCE_CHOOSE, ITEM_SOURCE_DROP, ITEM_SOURCE_SURVIVOR, EQUIP_TYPE_MAINWEAPON
from cl_reward import GetWeaponRewardGrade, RewardItem
from cl_minigame import MiniGameAttrInfo
from cl_only import ChooseKey, Functor, DeepCopy
from cl_object.logging import ErrLog
from .mobject import CDropGame, CBaseGameData, CRewardChooseGame, CDropChoose
import cl_npc.net as npcnet
import cl_item
import cl_math
import cl_netattr
import cl_msgcenter
import cl_item.defines as itemdef

def ReSendRewardInfo(iMiniGame, oOwner, oTarget, dInfo):
    oMiniGame = oOwner.m_Game.m_MiniGameMgr.GetMiniGame(iMiniGame)
    if not oMiniGame:
        return None
    if not oOwner or oTarget.m_Scene != oOwner.m_Scene:
        return None
    if oTarget.m_ID == oMiniGame.m_Player:
        oMiniGame.SendChoose()


def PlayerChooseEquip(oMiniGame, who, iAnswer):
    lstReward = oMiniGame.Query('Reward', [])
    oMiniGame.Set('Reward', [])
    oGame = who.m_Game
    for iEquip, dInfo in lstReward:
        if iAnswer == iEquip:
            dEquipReward = {
                'item': VIRTUAL_ITEM_EQUIP,
                'info': {
                    'sid': iAnswer,
                    'item': dInfo['Item'],
                    'data': { },
                    'Owner': oMiniGame.m_Owner } }
            RewardItem(oGame, who, [
                dEquipReward], 'PlayerChoose%s' % iAnswer, None)
            break
    
    oGame.DoneGlobalAttention(oMiniGame.m_Owner, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, 'PlayReEnter%d' % oMiniGame.m_ID)
    oMiniGame.End()


def GetWeaponDropInfo(oLevelCtrl, iType):
    oGame = oLevelCtrl.m_Game
    oWarData = oGame.m_WarData
    if iType == LEVEL_TYPE_BOSS:
        iLayer = oLevelCtrl.m_LayerNum + 1
        iGrade = oWarData.GetWeaponGrade(iLayer, 1, oGame)
        iNewInscriptionNum = oWarData.GetInscriptionNum(iLayer, 1, oLevelCtrl)
        return (iGrade, iNewInscriptionNum)
    return (0, 0)


class CEquipDropChoose(CDropChoose):
    
    def Filter(cls, oPlayer, dWeight):
        lstUnlock = oPlayer.Query('Illus')['Weapon']
        dEquipWeight = { }
        dEquipWeight.update(dWeight)
        for iEquip in list(dEquipWeight):
            if iEquip not in lstUnlock:
                dEquipWeight.pop(iEquip)
        
        return dEquipWeight

    Filter = classmethod(Filter)
    
    def Choose(cls, oPlayer, dWeight):
        oGame = oPlayer.m_Game
        dWeight = cls.Filter(oPlayer, dWeight)
        iEquip = oGame.m_RandomMgr.ChooseKey('weapon%d' % oPlayer.m_ID, {
            'Select': dWeight })
        if not iEquip:
            return []
        return [
            iEquip]

    Choose = classmethod(Choose)


class CDropEquipGameData(CBaseGameData):
    m_SID = 0
    m_Type = MG_EQUIP
    m_ChooseWeight = { }
    m_FilterList = []
    m_FlagDifferBullet = 1
    
    def InitMiniGame(cls, oMiniGame):
        oMiniGame.m_ChooseWeight = DeepCopy(cls.m_ChooseWeight)

    InitMiniGame = classmethod(InitMiniGame)
    
    def GetGameClass(cls):
        return CDropEquipGame

    GetGameClass = classmethod(GetGameClass)
    
    def GetChooseClass(cls):
        return CEquipDropChoose

    GetChooseClass = classmethod(GetChooseClass)
    
    def GetChooseWeight(cls, oHero):
        if cls.m_ChooseWeight:
            return dict(cls.m_ChooseWeight)
        dWeight = dict.fromkeys(oHero.Query('Illus')['Weapon'], 1)
        for iSID in cls.m_FilterList:
            if iSID in dWeight:
                dWeight.pop(iSID)
        
        return dWeight

    GetChooseWeight = classmethod(GetChooseWeight)
    
    def GetChooseWeightByBullet(cls, oHero, iBulletType):
        dCache = oHero.Query('MGWeightCache%d' % cls.m_SID, { })
        if iBulletType in dCache:
            dWeight = dCache[iBulletType]
        else:
            dWeight = { }
            dChooseWeight = cls.GetChooseWeight(oHero)
            for iSID in dChooseWeight:
                clsWeapon = cl_item.GetItemCls(iSID)
                if not clsWeapon:
                    continue
                if clsWeapon.GetBulletType() == iBulletType:
                    dWeight[iSID] = 1
            
            dCache[iBulletType] = dWeight
            oHero.Set('MGWeightCache%d' % cls.m_SID, dCache)
        return dWeight

    GetChooseWeightByBullet = classmethod(GetChooseWeightByBullet)


class CDropEquipGame(CDropGame):
    
    def GetRewardInfo(self):
        lstReward = []
        oGame = self.m_Game
        oOwner = oGame.GetObject(self.m_Owner)
        if not oOwner:
            return lstReward
        oScene = oGame.m_SceneMgr.GetScene(oOwner.m_Scene)
        oChoosePool = oScene.m_ScenePreLoad.GetSceneChoosePool(self.m_Player)
        if not oChoosePool:
            return lstReward
        iTime = self.Query('Times', 1)
        iGrade = GetWeaponRewardGrade(oGame)
        oTarget = oGame.GetObject(self.m_Player)
        dWeaponInfo = self.Query('WeaponInfo', { })
        if oTarget and 'SyncGrade' in dWeaponInfo:
            iWeaponBaseGrade = 0
            lstWeapon = oTarget.m_WieldCon.GetAllItemByType(EQUIP_TYPE_MAINWEAPON)
            for oWeapon in lstWeapon:
                if oWeapon.m_BaseGrade > iWeaponBaseGrade:
                    iWeaponBaseGrade = oWeapon.m_BaseGrade
            
            iGrade = max(iWeaponBaseGrade, iGrade)
        oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
        oLevelNode = oLevelCtrl.m_CurNode
        iNewInscriptionNum = 0
        if oLevelNode.m_LevelType == LEVEL_TYPE_BOSS:
            (iGrade, iNewInscriptionNum) = GetWeaponDropInfo(oLevelCtrl, oLevelNode.m_LevelType)
        for _ in range(iTime):
            lstEquip = oChoosePool.QueryChoose(self.m_SID)
            if not lstEquip:
                break
            iEquip = lstEquip[0]
            dCopyWeaponInfo = DeepCopy(dWeaponInfo)
            oEquip = cl_item.CreateEquip(oGame, iEquip, iGrade, oOwner = oTarget, iSource = ITEM_SOURCE_DROP, dExtraAttr = dCopyWeaponInfo)
            if oEquip.Type() & EQUIP_TYPE_MAINWEAPON:
                oBulletcom = oEquip.GetComponent('Bullet')
                if oBulletcom:
                    oBulletcom.BulletModify(oBulletcom.MaxBullet())
                oInscriptionCom = oEquip.GetComponent('Inscription')
                if oInscriptionCom and iNewInscriptionNum:
                    oInscriptionCom.m_InscriptionNum = iNewInscriptionNum
                    oInscriptionCom.AddInscription()
            dInfo = { }
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_GREATEDROPWEAPON, oTarget, dInfo)
            if 'Enhance' in dInfo:
                oEquip.AddEnhance(dInfo['Enhance'], dInfo['Reason'])
            dReward = {
                'item': VIRTUAL_ITEM_DROP,
                'info': {
                    'DropType': NWARRIOR_DROP_EQUIP,
                    'DropInfo': [
                        oEquip],
                    'DropPos': self.GetDropBasePos() } }
            lstReward.append(dReward)
        
        return lstReward



class CMultipleEquipDropChoose(CEquipDropChoose):
    m_MaxChooseLen = 4
    
    def Choose(cls, oPlayer, dWeight):
        oGame = oPlayer.m_Game
        dEquipWeight = cls.Filter(oPlayer, dWeight)
        lstEquip = []
        for _ in range(cls.m_MaxChooseLen):
            iEquip = oGame.m_RandomMgr.ChooseKey('weapon%d' % oPlayer.m_ID, {
                'Select': dEquipWeight })
            if not iEquip:
                break
            lstEquip.append(iEquip)
            dEquipWeight.pop(iEquip)
        
        return lstEquip

    Choose = classmethod(Choose)


class CRewardChooseEquipGameData(CBaseGameData):
    m_SID = 0
    m_Type = MG_EQUIP
    m_ChooseWeight = { }
    m_FilterList = []
    m_FlagDifferBullet = 1
    
    def InitMiniGame(cls, oMiniGame):
        oMiniGame.m_ChooseWeight = DeepCopy(cls.m_ChooseWeight)

    InitMiniGame = classmethod(InitMiniGame)
    
    def GetGameClass(cls):
        return CRewardChooseEquipGame

    GetGameClass = classmethod(GetGameClass)
    
    def GetChooseClass(cls):
        return CMultipleEquipDropChoose

    GetChooseClass = classmethod(GetChooseClass)
    
    def GetChooseWeight(cls, oHero):
        if cls.m_ChooseWeight:
            return dict(cls.m_ChooseWeight)
        dWeight = dict.fromkeys(oHero.Query('Illus')['Weapon'], 1)
        for iSID in cls.m_FilterList:
            if iSID in dWeight:
                dWeight.pop(iSID)
        
        return dWeight

    GetChooseWeight = classmethod(GetChooseWeight)


class CRewardChooseEquipGame(CRewardChooseGame):
    m_C2GSOPFunc = {
        PLAYER_CHOOSE_EQUIP: PlayerChooseEquip }
    
    def GetChooseWeight(self):
        return self.m_ChooseWeight

    
    def GetEquipGrade(self):
        return GetWeaponRewardGrade(self.m_Game)

    
    def GetRewardInfo(self):
        lstReward = []
        oGame = self.m_Game
        oOwner = oGame.GetObject(self.m_Owner)
        if not oOwner:
            return lstReward
        oScene = oGame.m_SceneMgr.GetScene(oOwner.m_Scene)
        oChoosePool = oScene.m_ScenePreLoad.GetSceneChoosePool(self.m_Player)
        if not oChoosePool:
            return lstReward
        dChooseCnt = self.Query('ChooseCnt', { })
        iChooseCnt = ChooseKey(oGame, dChooseCnt)
        if not iChooseCnt:
            return lstReward
        iStartIdx = 0
        iTotalIdx = iChooseCnt
        iGrade = self.GetEquipGrade()
        vPos = self.GetDropBasePos()
        vFace = oOwner.GetFacing()
        vVertical = (-vFace[2], 0, vFace[0])
        fHeight = oOwner.m_ModelData.GetModelHeight()
        vPos = (vPos[0], vPos[1] + 1.5 * fHeight, vPos[2])
        fInterval = DEFAULT_DROP_RADIUS * 2
        lstEquip = oChoosePool.QueryChoose(self.m_SID)
        if lstEquip:
            lstUse = lstEquip[:iChooseCnt] if len(lstEquip) >= iChooseCnt else lstEquip
            for idx, iEquip in enumerate(lstUse):
                oEquip = cl_item.CreateEquip(oGame, iEquip, iGrade, oOwner = oGame.GetObject(self.m_Player), iSource = ITEM_SOURCE_CHOOSE)
                if oEquip.Type() & EQUIP_TYPE_MAINWEAPON:
                    oBulletcom = oEquip.GetComponent('Bullet')
                    if oBulletcom:
                        oBulletcom.BulletModify(oBulletcom.MaxBullet())
                vDropPos = cl_math.Vec3DisplaceDir(vPos, vVertical, fInterval * (iStartIdx + idx - (iTotalIdx - 1) / 2))
                lstAttr = MiniGameAttrInfo(oEquip, cl_netattr.PROP_DROPITEM_MAINWEAPON)
                lstReward.append([
                    oEquip.m_SID,
                    {
                        'Item': oEquip,
                        'Pos': vDropPos,
                        'Attr': lstAttr,
                        'Type': VIRTUAL_ITEM_EQUIP }])
            
        oGame.AddGlobalAttention(oOwner.m_ID, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, Functor(ReSendRewardInfo, self.m_ID), 'PlayReEnter%d' % self.m_ID)
        return lstReward

    
    def SendChoose(self):
        lstReward = self.Query('Reward', [])
        oPlayer = self.m_Game.GetObject(self.m_Player)
        if oPlayer:
            npcnet.GS2CNpcChooseReward(oPlayer, self.m_Owner, lstReward, self.m_ID, PLAYER_CHOOSE_EQUIP)
        self.Leave()



class CInitEquipDropChoose(CMultipleEquipDropChoose):
    
    def GetPlayerInitDropChoose(cls, oPlayer):
        dInitWeaponDrop = oPlayer.Query('InitWeaponDrop', { })
        if not dInitWeaponDrop:
            return { }
        dChoose = { }
        lstUnlockWeapon = oPlayer.Query('Illus')['Weapon']
        for iWeapon in lstUnlockWeapon:
            clsWeapon = cl_item.GetItemCls(iWeapon)
            iBulletType = clsWeapon.GetBulletType()
            if iBulletType in dInitWeaponDrop and dInitWeaponDrop[iBulletType] and clsWeapon.m_Type & itemdef.EQUIP_TYPE_MAINWEAPON == itemdef.EQUIP_TYPE_MAINWEAPON:
                dChoose[iWeapon] = 1
        
        return dChoose

    GetPlayerInitDropChoose = classmethod(GetPlayerInitDropChoose)
    
    def Filter(cls, oPlayer, dWeight):
        dEquipWeight = super(CInitEquipDropChoose, cls).Filter(oPlayer, dWeight)
        lstValidInitDrop = cls.GetPlayerInitDropChoose(oPlayer)
        lstKey = list(dEquipWeight.keys())
        for iEquip in lstKey:
            if iEquip not in lstValidInitDrop:
                dEquipWeight.pop(iEquip)
        
        return dEquipWeight

    Filter = classmethod(Filter)


class CRewardChooseInitWeaponGameData(CRewardChooseEquipGameData):
    
    def GetGameClass(cls):
        return CRewardChooseInitWeaponGame

    GetGameClass = classmethod(GetGameClass)
    
    def GetChooseClass(cls):
        return CInitEquipDropChoose

    GetChooseClass = classmethod(GetChooseClass)


class CRewardChooseInitWeaponGame(CRewardChooseEquipGame):
    
    def GetEquipGrade(self):
        return 0

    
    def GetRewardInfo(self):
        oPlayer = self.m_Game.GetObject(self.m_Player)
        dInitWeaponDrop = oPlayer.Query('InitWeaponDrop', { })
        if not dInitWeaponDrop:
            return { }
        oPlayer.Set('InitWeaponDrop', { })
        return super(CRewardChooseInitWeaponGame, self).GetRewardInfo()

    
    def OnInit(self):
        super(CRewardChooseInitWeaponGame, self).OnInit()
        oPlayer = self.m_Game.GetObject(self.m_Player)
        oPlayer.Set('InitWeaponDrop', { })



class CRewardSurvivorInitWeaponGameData(CRewardChooseEquipGameData):
    
    def GetGameClass(cls):
        return CRewardSurvivorInitWeaponGame

    GetGameClass = classmethod(GetGameClass)
    
    def GetChooseClass(cls):
        return CMultipleEquipDropChoose

    GetChooseClass = classmethod(GetChooseClass)


class CRewardSurvivorInitWeaponGame(CRewardChooseEquipGame):
    
    def GetEquipInfo(self):
        oSurvivorElement = self.m_Game.m_WarMgr.GetComponent('NewSurvivorElement')
        if oSurvivorElement:
            return oSurvivorElement.GetInitEquipInfo()
        return (0, 1)

    
    def SendChoose(self):
        dReward = self.Query('Reward', { })
        oHero = self.m_Game.GetObject(self.m_Player)
        if oHero:
            oSurvivorElement = self.m_Game.m_WarMgr.GetComponent('NewSurvivorElement')
            if oSurvivorElement:
                oSurvivorElement.m_RewardMgr.AddInitWeapon(oHero, dReward)
        self.Leave()

    
    def GetRewardInfo(self):
        dReward = { }
        oGame = self.m_Game
        oOwner = oGame.GetObject(self.m_Owner)
        if not oOwner:
            return dReward
        oScene = oGame.m_SceneMgr.GetScene(oOwner.m_Scene)
        oChoosePool = oScene.m_ScenePreLoad.GetSceneChoosePool(self.m_Player)
        if not oChoosePool:
            return dReward
        iChooseCnt = self.Query('ChooseCnt', 0)
        if not iChooseCnt:
            return dReward
        (iGrade, iInscriptionNum) = self.GetEquipInfo()
        lstEquip = oChoosePool.QueryChoose(self.m_SID)
        if lstEquip:
            lstUse = lstEquip[:iChooseCnt] if len(lstEquip) >= iChooseCnt else lstEquip
            for iEquip in lstUse:
                oEquip = cl_item.CreateEquip(oGame, iEquip, iGrade, oOwner = oOwner, iSource = ITEM_SOURCE_CHOOSE, dExtraAttr = {
                    'InscriptionNum': iInscriptionNum })
                if oEquip.Type() & EQUIP_TYPE_MAINWEAPON:
                    oBulletcom = oEquip.GetComponent('Bullet')
                    if oBulletcom:
                        oBulletcom.BulletModify(oBulletcom.MaxBullet())
                lstAttr = MiniGameAttrInfo(oEquip, cl_netattr.PROP_DROPITEM_MAINWEAPON)
                dReward[oEquip.m_SID] = {
                    'Item': oEquip,
                    'Attr': lstAttr }
            
        return dReward



class CUpgradeChooseWeaponGameData(CRewardChooseEquipGameData):
    
    def GetGameClass(cls):
        return CUpgradeChooseWeaponGame

    GetGameClass = classmethod(GetGameClass)
    
    def GetChooseClass(cls):
        return CMultipleEquipDropChoose

    GetChooseClass = classmethod(GetChooseClass)


class CUpgradeChooseWeaponGame(CRewardChooseGame):
    
    def GetEquipInfo(self):
        oSurvivor = self.m_Game.m_WarMgr.GetComponent('SurvivorElement')
        if oSurvivor:
            iPhase = self.Query('Phase', 0)
            iGrade = oSurvivor.GetWeaponGrade(dData = {
                'Phase': iPhase })
            iInscriptionNum = oSurvivor.GetInscriptionNum(iPhase = iPhase)
        else:
            iGrade = GetWeaponRewardGrade(self.m_Game)
            iInscriptionNum = 0
        return (iGrade, iInscriptionNum)

    
    def GetRewardInfo(self):
        dReward = { }
        oGame = self.m_Game
        oOwner = oGame.GetObject(self.m_Owner)
        if not oOwner:
            return dReward
        iChooseCnt = self.Query('ChooseCnt', 0)
        if not iChooseCnt:
            return dReward
        (iGrade, iInscriptionNum) = self.GetEquipInfo()
        oScene = oGame.m_SceneMgr.GetScene(oOwner.m_Scene)
        oChoosePool = oScene.m_ScenePreLoad.GetSceneChoosePool(self.m_Player)
        if not oChoosePool:
            return dReward
        lstEquip = oChoosePool.QueryChoose(self.m_SID)
        if lstEquip:
            lstUse = lstEquip[:iChooseCnt] if len(lstEquip) >= iChooseCnt else lstEquip
            for iEquip in lstUse:
                oEquip = cl_item.CreateEquip(oGame, iEquip, iGrade, oOwner = oGame.GetObject(self.m_Player), iSource = ITEM_SOURCE_SURVIVOR, dExtraAttr = {
                    'InscriptionNum': iInscriptionNum })
                if oEquip.Type() & EQUIP_TYPE_MAINWEAPON:
                    oBulletcom = oEquip.GetComponent('Bullet')
                    if oBulletcom:
                        oBulletcom.BulletModify(oBulletcom.MaxBullet())
                lstAttr = MiniGameAttrInfo(oEquip, cl_netattr.PROP_DROPITEM_MAINWEAPON)
                dReward[oEquip.m_SID] = {
                    'Item': oEquip,
                    'Attr': lstAttr }
            
        return dReward

    
    def SendChoose(self):
        oHero = self.m_Game.GetObject(self.m_Player)
        if oHero:
            dReward = self.Query('Reward', { })
            oSurvivorElement = self.m_Game.m_WarMgr.GetComponent('SurvivorElement')
            if oSurvivorElement:
                dExtInfo = self.Query('ExtInfo', { })
                oSurvivorElement.m_UpgradeMgr.AddRewardInfo(oHero, VIRTUAL_ITEM_EQUIP, dReward, 'UpGradeMiniGame', dExtInfo)
        self.End()


