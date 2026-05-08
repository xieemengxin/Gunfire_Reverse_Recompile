# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_drop/__init__.pyc
# RelativePath: clientlogic/cl_drop/__init__.pyc
# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.6)

from cl_commondefines import NWARRIOR_DROP_EXPERIENCE, NWARRIOR_DROP_KEYITEM, NWARRIOR_DROP_EQUIP, NWARRIOR_DROP_BULLET, NWARRIOR_DROP, NWARRIOR_DROP_CASH, NWARRIOR_DROP_RELIC, NWARRIOR_DROP_TRIGGER, PF_TYPE_RELIC, NWARRIOR_DROP_KEY, NWARRIOR_DROP_RELIC_CURSE, NWARRIOR_DROP_TREASURE_DEAD, DROP_BULLETPICK_NORMAL, DROP_BULLETPICK_BULLETCLIP, DROP_BULLETPICK_CHANGE, NWARRIOR_DROP_DEMON, NWARRIOR_DROP_RELIFE, VIRTUAL_ITEM_MAGICPOWER, WARRIOR_MONSTER, VIRTUAL_ITEM_GOLDENCUP, VIRTUAL_ITEM_DROP, NWARRIOR_DROP_RAREITEM, NWARRIOR_DROP_AXE, NWARRIOR_DROP_ENCHANTING_BULLET, PF_TYPE_TRIGGERCLIENT, SKILLRET_SUCCESS, EXTRAPICKUPRULE_FROM_RELIC_5962, NWARRIOR_DROP_GSCASH, RELIC_TYPE_CURSE, STATE_TIME_LIMIT, STATE_TIME_FOREVER, PICK_RELIC, ANIMA_QUALITY, NORMAL_QUALITY, NWARRIOR_DROP_MAGIC_POWER, NWARRIOR_DROP_INKBEAD, NWARRIOR_DROP_DEVICECOMP, PF_TYPE_DEVICECOMP, PICK_CASH, PICK_BULLET, NWARRIOR_DROP_PETEGG, PET_EGG_NORMAL, DYNAMIC_DEMON_MONSTERRELIC, PICK_TYPE_NORMAL, PICK_TYPE_EXTEND, NWARRIOR_DROP_RELIC_BLANK, NWARRIOR_DROP_RELIC_MYSTERY, RELIC_TYPE_MYSTERY, NWARRIOR_DROP_NODISTANCEBULLET, NWARRIOR_DROP_MAGIC_WAND, NWARRIOR_DROP_WANDCOMP, NWARRIOR_DROP_DICE, NWARRIOR_DROP_COOKIES, WANDDROPSID_BY_QUALITY, NWARRIOR_DROP_DICESELECTIONPACKET, NWARRIOR_DROP_DICESPECIALITEM, TYPE_ASSEMBLE, NWARRIOR_DROP_S7MODULE, NWARRIOR_DROP_S7CRYSTAL, PICK_S7CRYSTAL, NWARRIOR_DROP_S8GEMITEM, NWARRIOR_DROP_S8THIRDITEM, GEMITEM_MASK, THIRDITEM_MASK, NWARRIOR_DROP_SUMMONSOUL, DROP_BULLETPICK_IGNOREMAX
from cl_only import Functor, Time2Frame, SendAlert, TraceLog
from cl_item.defines import EQUIP_MASK_WEAPON, EQUIP_MASK_DEF, EQUIP_TYPE_MAINWEAPON, KEYITEM_MASK, RAREITEM_MASK, WAND_MASK, DICE_MASK, MODULE_MASK, CRYSTAL_MASK
from cl_object.logging import WarobjLog
from cl_platformdata.custom.triggerpf.customaction import CheckTriggerPFCanUse
from cl_platformdata import GetCanRepickupRelic, GetAllDiceAbility
from cl_container.backpackcon import CRYSTAL_RAWMATERIAL_SID
import cl_item
import cl_world
import cl_netattr
import cl_perform
import cl_msgcenter
import cl_reward
import cl_snetwar
import cl_notify
import cl_war
import cl_state
import cl_object
import cl_propdata
import cl_math
import cl_gamedebug
import cl_wand
import cl_wand.net as wandnet
import cl_dice.net as dinednet
import cl_seasonplay.net as seasonplaynet
HIGHQUALITY_DROP = (NWARRIOR_DROP_RELIC, NWARRIOR_DROP_RELIC_CURSE, NWARRIOR_DROP_DEVICECOMP, NWARRIOR_DROP_PETEGG, NWARRIOR_DROP_MAGIC_WAND, NWARRIOR_DROP_DICE, NWARRIOR_DROP_S7CRYSTAL, NWARRIOR_DROP_S7MODULE)
g_commondrop = {
    5501: 5501,
    5502: 5502,
    5503: 5513,
    5504: 5513,
    5505: 5509,
    5507: 5504,
    5508: 4501,
    5509: 5513,
    5510: 5513,
    5511: 5513,
    5512: 5513,
    5513: 5513,
    5514: 5513,
    5515: 5513,
    5516: 5513,
    5517: 5511,
    5518: 5540,
    5519: 5512,
    5520: 5513,
    5521: 5513,
    5522: 5540,
    5523: 5513,
    5524: 5516,
    5525: 5543,
    5526: 5544,
    5527: 5545,
    5528: 5547,
    5529: 5548,
    5530: 5549,
    5531: 5552,
    5532: 5553,
    5533: 5547,
    5534: 5562,
    5535: 5564,
    5536: 5565,
    5537: 5566,
    5538: 5566,
    5539: 5540,
    5540: 5523,
    5541: 5513,
    5542: 5540,
    5543: 5572,
    5544: 7012,
    5545: 5501,
    5546: 5571,
    5547: 5570,
    5548: 5511,
    5549: 5574,
    5550: 5547,
    5551: 5548,
    5552: 5549,
    5553: 5543,
    5554: 5543,
    5555: 5575,
    5556: 5576,
    5557: 7052,
    5558: 7053,
    5559: 7054,
    5560: 5552,
    5561: 7054,
    5562: 7054 }
g_DelayPickTime = {
    5501: 50,
    5502: 50,
    5503: 0,
    5504: 50,
    5505: 50,
    5507: 50,
    5508: 0,
    5509: 50,
    5510: 50,
    5511: 50,
    5512: 50,
    5513: 50,
    5514: 50,
    5515: 50,
    5516: 50,
    5517: 50,
    5518: 75,
    5519: 50,
    5520: 50,
    5521: 50,
    5522: 0,
    5523: 50,
    5524: 50,
    5525: 0,
    5526: 0,
    5527: 0,
    5528: 0,
    5529: 0,
    5530: 0,
    5531: 50,
    5532: 50,
    5533: 0,
    5534: 50,
    5535: 0,
    5536: 0,
    5537: 0,
    5538: 50,
    5539: 50,
    5540: 0,
    5541: 0,
    5542: 50,
    5543: 0,
    5544: 0,
    5545: 50,
    5546: 0,
    5547: 0,
    5548: 50,
    5549: 0,
    5550: 0,
    5551: 0,
    5552: 0,
    5553: 0,
    5554: 0,
    5555: 0,
    5556: 0,
    5557: 0,
    5558: 0,
    5559: 0,
    5560: 50,
    5561: 0,
    5562: 0 }
g_SurvivalTime = {
    5501: 0,
    5502: 0,
    5503: 0,
    5504: 0,
    5505: 0,
    5507: 0,
    5508: 1500,
    5509: 0,
    5510: 0,
    5511: 0,
    5512: 0,
    5513: 0,
    5514: 0,
    5515: 0,
    5516: 0,
    5517: 400,
    5518: 0,
    5519: 0,
    5520: 0,
    5521: 0,
    5522: 0,
    5523: 0,
    5524: 0,
    5525: 0,
    5526: 100,
    5527: 0,
    5528: 0,
    5529: 0,
    5530: 0,
    5531: 0,
    5532: 0,
    5533: 0,
    5534: 0,
    5535: 0,
    5536: 0,
    5537: 0,
    5538: 0,
    5539: 0,
    5540: 0,
    5541: 0,
    5542: 0,
    5543: 0,
    5544: 0,
    5545: 0,
    5546: 0,
    5547: 0,
    5548: 1000,
    5549: 0,
    5550: 0,
    5551: 0,
    5552: 0,
    5553: 0,
    5554: 0,
    5555: 0,
    5556: 0,
    5557: 0,
    5558: 0,
    5559: 0,
    5560: 0,
    5561: 0,
    5562: 0 }
g_SID2Info = {
    5501: [
        NWARRIOR_DROP_BULLET,
        10],
    5502: [
        NWARRIOR_DROP_CASH,
        10],
    5503: [
        NWARRIOR_DROP_RELIC,
        0],
    5504: [
        NWARRIOR_DROP_TRIGGER,
        10],
    5505: [
        NWARRIOR_DROP_KEY,
        10],
    5507: [
        NWARRIOR_DROP_GSCASH,
        10],
    5508: [
        NWARRIOR_DROP_KEYITEM,
        0],
    5509: [
        NWARRIOR_DROP_RELIC,
        0],
    5510: [
        NWARRIOR_DROP_RELIC,
        0],
    5511: [
        NWARRIOR_DROP_RELIC,
        0],
    5512: [
        NWARRIOR_DROP_RELIC,
        0],
    5513: [
        NWARRIOR_DROP_RELIC,
        0],
    5514: [
        NWARRIOR_DROP_RELIC,
        0],
    5515: [
        NWARRIOR_DROP_RELIC_CURSE,
        10],
    5516: [
        NWARRIOR_DROP_RELIC,
        0],
    5517: [
        NWARRIOR_DROP_TREASURE_DEAD,
        6],
    5518: [
        NWARRIOR_DROP_DEMON,
        0],
    5519: [
        NWARRIOR_DROP_RELIFE,
        6],
    5520: [
        NWARRIOR_DROP_RELIC,
        0],
    5521: [
        NWARRIOR_DROP_RELIC,
        0],
    5522: [
        NWARRIOR_DROP_DEMON,
        0],
    5523: [
        NWARRIOR_DROP_RELIC_CURSE,
        0],
    5524: [
        NWARRIOR_DROP_EXPERIENCE,
        10],
    5525: [
        NWARRIOR_DROP_RAREITEM,
        0],
    5526: [
        NWARRIOR_DROP_AXE,
        2],
    5527: [
        NWARRIOR_DROP_ENCHANTING_BULLET,
        0],
    5528: [
        NWARRIOR_DROP_MAGIC_POWER,
        0],
    5529: [
        NWARRIOR_DROP_MAGIC_POWER,
        0],
    5530: [
        NWARRIOR_DROP_MAGIC_POWER,
        0],
    5531: [
        NWARRIOR_DROP_INKBEAD,
        3],
    5532: [
        NWARRIOR_DROP_INKBEAD,
        3],
    5533: [
        NWARRIOR_DROP_DEVICECOMP,
        0],
    5534: [
        NWARRIOR_DROP_TRIGGER,
        10],
    5535: [
        NWARRIOR_DROP_PETEGG,
        0],
    5536: [
        NWARRIOR_DROP_PETEGG,
        0],
    5537: [
        NWARRIOR_DROP_PETEGG,
        0],
    5538: [
        NWARRIOR_DROP_PETEGG,
        10],
    5539: [
        NWARRIOR_DROP_RELIC,
        0],
    5540: [
        NWARRIOR_DROP_RELIC_BLANK,
        0],
    5541: [
        NWARRIOR_DROP_RELIC_MYSTERY,
        0],
    5542: [
        NWARRIOR_DROP_RELIC,
        0],
    5543: [
        NWARRIOR_DROP_MAGIC_WAND,
        0],
    5544: [
        NWARRIOR_DROP_WANDCOMP,
        0],
    5545: [
        NWARRIOR_DROP_NODISTANCEBULLET,
        999],
    5546: [
        NWARRIOR_DROP_MAGIC_WAND,
        0],
    5547: [
        NWARRIOR_DROP_MAGIC_WAND,
        0],
    5548: [
        NWARRIOR_DROP_COOKIES,
        6],
    5549: [
        NWARRIOR_DROP_DICE,
        0],
    5550: [
        NWARRIOR_DROP_DICESELECTIONPACKET,
        0],
    5551: [
        NWARRIOR_DROP_DICESELECTIONPACKET,
        0],
    5552: [
        NWARRIOR_DROP_DICESELECTIONPACKET,
        0],
    5553: [
        NWARRIOR_DROP_DICESPECIALITEM,
        0],
    5554: [
        0,
        0],
    5555: [
        NWARRIOR_DROP_DICE,
        0],
    5556: [
        NWARRIOR_DROP_DICE,
        0],
    5557: [
        NWARRIOR_DROP_S7MODULE,
        0],
    5558: [
        NWARRIOR_DROP_S7CRYSTAL,
        0],
    5559: [
        NWARRIOR_DROP_S7CRYSTAL,
        0],
    5560: [
        NWARRIOR_DROP_SUMMONSOUL,
        3],
    5561: [
        NWARRIOR_DROP_S8THIRDITEM,
        0],
    5562: [
        NWARRIOR_DROP_S8GEMITEM,
        0] }

def GetCommondrop(iSID):
    return g_commondrop.get(iSID, 0)


def CheckBulletClip(oHero, dInfo):
    lstWeapon = oHero.m_WieldCon.GetAllItemByType(EQUIP_TYPE_MAINWEAPON)
    for oWeapon in lstWeapon:
        oBulletCom = oWeapon.GetComponent('Bullet')
        if not oBulletCom:
            continue
        if oBulletCom.Bullet() < oBulletCom.MaxBullet():
            return 1
    
    oBulletCon = oHero.m_BulletCon
    for iBulletSID in dInfo:
        if oBulletCon.Bullet(iBulletSID) < oBulletCon.GetMaxBullet(iBulletSID):
            return 1
    
    return 0


def CheckBulletChange(oHero, dInfo):
    oBulletCon = oHero.m_BulletCon
    lstType = cl_item.load.GetAllWeaponBulletType()
    for iBulletSID in lstType:
        if oBulletCon.Bullet(iBulletSID) < oBulletCon.GetMaxBullet(iBulletSID):
            return 1
    
    return 0


def CheckIgnoreMax(oHero, dInfo):
    oBulletCon = oHero.m_BulletCon
    dBulletPickIgnoreMax = oHero.Query('BulletPickIgnoreMax', { })
    for iBulletSID in dInfo:
        if iBulletSID in dBulletPickIgnoreMax and dBulletPickIgnoreMax[iBulletSID]:
            return 1
        if oBulletCon.Bullet(iBulletSID) < oBulletCon.GetMaxBullet(iBulletSID):
            return 1
    
    return 0

g_PickFunc = {
    DROP_BULLETPICK_IGNOREMAX: CheckIgnoreMax,
    DROP_BULLETPICK_CHANGE: CheckBulletChange,
    DROP_BULLETPICK_BULLETCLIP: CheckBulletClip }

def GetCheckPickFunc(idx):
    if idx in g_PickFunc:
        return g_PickFunc[idx]


def CheckRelicSourceHero(oDrop, oHero):
    if oDrop.m_FightType == NWARRIOR_DROP_RELIC:
        iSource = oDrop.m_Source
        if iSource and iSource == oHero.m_PlayerID:
            return 1
        if oDrop.Query('Abandoner', 0) == oHero.m_ID:
            return 1
        return 0
    return 1

EXTRAPICKUPRULE_FUNC = {
    EXTRAPICKUPRULE_FROM_RELIC_5962: CheckRelicSourceHero }

class CDrop(cl_world.CSceneObject):
    m_Type = 'Drop'
    m_FightType = NWARRIOR_DROP
    m_SubPickMsg = -1
    
    def __init__(self, oGame, nid):
        super(CDrop, self).__init__(oGame, nid)
        self.m_Level = 1
        self.m_DropInfo = { }
        self.m_Pick = 0
        self.m_Owner = 0
        self.m_Source = 0
        self.m_SourceReason = 0
        self.m_ShareInfo = { }
        self.m_DelayPickTime = g_DelayPickTime[self.m_SID] if self.m_SID in g_DelayPickTime else 0
        self.DropDisappear()

    
    def Release(self):
        self.Remove_Call_Out('SurvivalTime')
        super().Release()

    
    def Shape(self):
        return 0

    
    def MapSendPacket(self, dPlayer):
        cl_netattr.MakeDropAddPacket(self, dPlayer)

    
    def SetFacing(self, tFace, iTurnTime = 8):
        pass

    
    def SetOwner(self, iOwner):
        self.m_Owner = iOwner

    
    def SetPicker(self, oHero):
        if not self.m_Pick:
            self.m_Pick = oHero.m_ID

    
    def InitSource(self, iSource):
        if self.m_Source:
            return None
        if not self.m_Game.m_WarMgr.Query('RecycleSelf', 1):
            iSource = 0
        self.m_Source = iSource
        self.GS2CPropChange('Source', iSource)

    
    def SyncDropSource(self, iType, iOwner):
        if iType == NWARRIOR_DROP_EQUIP:
            oItem = self.m_DropInfo[0]
            oHero = self.m_Game.GetObject(iOwner)
            if not oHero:
                return None
            oItem.InitSource(oHero.m_PlayerID)

    
    def ResetPicker(self):
        self.m_Pick = 0

    
    def DropReason(self):
        return self.Query('DropReason', 0)

    
    def Abandoner(self):
        return self.Query('Abandoner', 0)

    
    def SetAbandoner(self, iAbandoner):
        self.Set('Abandoner', iAbandoner)

    
    def ValidPick(self, oHero, iPickType = PICK_TYPE_NORMAL):
        if self.m_Scene != oHero.m_Scene:
            return 0
        iHero = oHero.m_ID
        if self.m_Owner and self.m_Owner != iHero:
            return 0
        if self.m_Pick and self.m_Pick != iHero:
            return 0
        if self.m_ReleaseFlag:
            return 0
        if oHero.IsDead():
            return 0
        if oHero.m_ExtraPickUpRule:
            for iRule in oHero.m_ExtraPickUpRule:
                if not EXTRAPICKUPRULE_FUNC[iRule](self, oHero):
                    return 0
            
        return 1

    
    def ValidRoll(self, oHero):
        return 0

    
    def SetDropData(self, lstDropData, dStaticInfo):
        if 'ShareInfo' in dStaticInfo:
            dShareInfo = dStaticInfo['ShareInfo']
            self.m_ShareInfo = dShareInfo
        if 'DropLevel' in dStaticInfo:
            self.m_Level = dStaticInfo['DropLevel']
        if 'DropSource' in dStaticInfo:
            self.InitSource(dStaticInfo['DropSource'])
        if 'SourceReason' in dStaticInfo:
            self.m_SourceReason = dStaticInfo['SourceReason']
        for idx, dDropData in enumerate(lstDropData):
            self.m_DropInfo[idx] = dDropData
        
        self.OnSetDropData(lstDropData)

    
    def CheckMerge(self, tPos, dExtraInfo, dStaticInfo):
        return False

    
    def MergeDropData(self, lstDropData):
        SendAlert('err', '掉落物类型 %s 暂未支持合并功能，请在子类中重写' % self.m_FightType)

    
    def GetPickMsgInfo(self, oHero, iPos = 0):
        dInfo = { }
        dInfo['Picker'] = oHero.m_ID
        dInfo['Type'] = self.m_FightType
        dInfo['Item'] = self.m_DropInfo[iPos]
        return dInfo

    
    def GetDropMsgInfo(self, iPos = 0):
        dInfo = { }
        dInfo['Drop'] = self.m_ID
        dInfo['Type'] = self.m_FightType
        dInfo['Item'] = self.m_DropInfo[iPos]
        return dInfo

    
    def GetGetDisappearMsgInfo(self, iPos = 0):
        dInfo = { }
        dInfo['Type'] = self.m_FightType
        dInfo['Item'] = self.m_DropInfo[iPos]
        return dInfo

    
    def GetSourceReason(self, iPos = 0):
        dInfo = { }
        dInfo['Mode'] = self.m_SourceReason
        dInfo['Item'] = self.m_DropInfo[iPos]
        return dInfo

    
    def DelayPick(self, oHero, iPos = 0, iPickType = PICK_TYPE_NORMAL):
        if not self.ValidPick(oHero, iPickType):
            cl_snetwar.GS2CPickFail(self.m_Game, self.m_Scene, self.m_Pick, self.m_ID)
            return None
        self.SetPicker(oHero)
        self.OnPickUp(oHero)
        if not self.m_DelayPickTime:
            self.Pick(oHero.m_ID, iPos, iPickType)
        else:
            self.Call_Out(Functor(self.Pick, oHero.m_ID, iPos, iPickType), Time2Frame(self.m_DelayPickTime), 'DelayPick')
            self.OnDelayPickBegin()

    
    def OnPickUp(self, oHero):
        cl_snetwar.GS2CPickUp(self.m_Game, self.m_Scene, oHero.m_ID, self.m_ID)

    
    def Pick(self, iHero, iPos = 0, iPickType = PICK_TYPE_NORMAL):
        oHero = self.m_Game.GetObject(iHero)
        if not oHero or not self.ValidPick(oHero):
            self.OnPickFail()
            return 0
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_PICK, oHero, self.GetPickMsgInfo(oHero), iSub = self.m_SubPickMsg)
        self.OnPick(oHero, iPos, iPickType)
        return 1

    
    def OnPick(self, oHero, iPos, iPickType = PICK_TYPE_NORMAL):
        pass

    
    def OnDelayPickBegin(self):
        pass

    
    def OnPickFail(self):
        cl_snetwar.GS2CPickFail(self.m_Game, self.m_Scene, self.m_Pick, self.m_ID)
        self.ResetPicker()

    
    def OnSetDropData(self, lstDropData):
        pass

    
    def EachDropInfo(self, oDropItem):
        return {
            'Type': cl_netattr.PROP_ITEM,
            'Attr': [] }

    
    def DropDesc(self):
        lstDropDesc = []
        for oDropItem in self.m_DropInfo.values():
            lstDropDesc.append(self.EachDropInfo(oDropItem))
        
        return lstDropDesc

    
    def NetAddTo(self, dPlayer):
        if self.m_Owner:
            oHero = self.m_Game.GetObject(self.m_Owner)
            if not oHero or oHero.m_PlayerID not in dPlayer:
                return None
            dPlayer = {
                oHero.m_PlayerID: 1 }
        super().NetAddTo(dPlayer)

    
    def DropIn(self):
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_DROP, self.m_Game.m_WarMgr, self.GetDropMsgInfo())

    
    def DropDisappear(self):
        iTime = g_SurvivalTime.get(self.m_SID, 0)
        if iTime:
            self.Call_Out(Functor(self.OnDisappear), Time2Frame(iTime), 'SurvivalTime')

    
    def OnDisappear(self):
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_DROPDISAPPEAR, self.m_Game.m_WarMgr, self.GetGetDisappearMsgInfo())
        self.Remove('SurvivalTime')

    
    def OnInitToScene(self, tPos):
        self.DropIn()

    
    def ResetDisappearTime(self, iTime):
        self.Remove_Call_Out('SurvivalTime')
        self.Call_Out(self.OnDisappear, Time2Frame(iTime), 'SurvivalTime')

    
    def VaildCanShare(self):
        return True



class CEquipDrop(CDrop):
    m_FightType = NWARRIOR_DROP_EQUIP
    
    def __init__(self, oGame, nid):
        super(CEquipDrop, self).__init__(oGame, nid)
        self.m_MonsterDrop = 0
        self.m_AnimaDrop = NORMAL_QUALITY
        self.m_CheckedPlayer = { }

    
    def Release(self):
        for oItem in self.m_DropInfo.values():
            oItem.Release()
        
        self.m_DropInfo = { }
        self.m_CheckedPlayer = { }
        super(CEquipDrop, self).Release()

    
    def Shape(self):
        return self.m_DropInfo[0].m_Shape

    
    def OnPick(self, oHero, iPos = 0, iPickType = PICK_TYPE_NORMAL):
        oItem = self.m_DropInfo[iPos]
        oItem.Set('OneWeaponNotChange', self.m_MonsterDrop)
        lstContainer = oItem.GetTargetContainer(oHero)
        sReason = 'Pick:%d-%d' % (oItem.Type(), oItem.m_SID)
        if oItem.PutToContainer(lstContainer, sReason):
            oItem.UpdateCheckedPlayer(self.m_CheckedPlayer)
            self.m_DropInfo.pop(iPos)
            self.Remove(sReason)
        oItem.Set('OneWeaponNotChange', 0)

    
    def OnSetDropData(self, lstDropData):
        oDropItem = lstDropData[0]
        self.m_SID = oDropItem.m_SID
        iInjectOwner = oDropItem.Query('InjectOwner', 0)
        if iInjectOwner:
            self.m_AnimaDrop = ANIMA_QUALITY

    
    def GetDropItemPropType(self, oEquip):
        if oEquip.m_Type & EQUIP_TYPE_MAINWEAPON == EQUIP_TYPE_MAINWEAPON:
            return cl_netattr.PROP_DROPITEM_MAINWEAPON
        return 0

    
    def EachDropInfo(self, oDropItem):
        lstAttrInfo = []
        iPropType = self.GetDropItemPropType(oDropItem)
        if not iPropType:
            raise Exception('未定义的类型')
        for sAttr in cl_netattr.INFO_OBJECT_INIT[iPropType]:
            (iIdx, _, iType, iLen, iMode) = cl_netattr.INFO_PROP_NAME[sAttr]
            if sAttr == 'Quality':
                iValue = self.m_AnimaDrop
            else:
                iValue = cl_netattr.GetPropValue(oDropItem, sAttr, iMode)
            if iValue is None:
                continue
            lstAttrInfo.append((iIdx, iType, iLen, iValue))
        
        return {
            'Type': iPropType,
            'Attr': lstAttrInfo }

    
    def ReplaceWeapon(self, oHero, iFromPos, iToPos):
        if not self.ValidPick(oHero):
            return None
        oItem = self.m_DropInfo[iFromPos]
        if oItem.m_Type & EQUIP_TYPE_MAINWEAPON != EQUIP_TYPE_MAINWEAPON:
            return None
        cl_snetwar.GS2CPickUp(self.m_Game, self.m_Scene, oHero.m_ID, self.m_ID)
        sReason = 'Pick:%d-%d' % (oItem.Type(), oItem.m_SID)
        if oItem.ReplaceToContainer(oHero.m_WieldCon, iToPos, sReason):
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_DROPREPLACE, oHero, self.GetPickMsgInfo(oHero))
            oItem.UpdateCheckedPlayer(self.m_CheckedPlayer)
            self.m_DropInfo.pop(iFromPos)
            self.Remove(sReason)

    
    def SetAbandoner(self, iAbandoner):
        super(CEquipDrop, self).SetAbandoner(iAbandoner)
        oGame = self.m_Game
        bSet = False
        lstHero = oGame.GetWarMgr().GetLiveHero()
        for iHero in lstHero:
            oHero = oGame.GetObject(iHero)
            if not oHero:
                continue
            if oHero.Query('OpenAutoDrop', 0):
                bSet = True
                break
        
        if not bSet:
            return None
        oAbandoner = oGame.GetObject(iAbandoner)
        if not oAbandoner:
            return None
        if oAbandoner.m_FightType & WARRIOR_MONSTER == WARRIOR_MONSTER:
            self.m_MonsterDrop = 1

    
    def SetCheckedPlayer(self, oHero):
        pid = oHero.m_PlayerID
        self.m_CheckedPlayer[pid] = 1



class CRelicDrop(CDrop):
    m_SID = 5503
    m_FightType = NWARRIOR_DROP_RELIC
    m_SubPickMsg = PICK_RELIC
    
    def __init__(self, oGame, nid):
        super(CRelicDrop, self).__init__(oGame, nid)
        self.m_RollNum = 0
        self.m_RollOldDrop = 0
        self.m_Share = 1
        self.m_OwnerInfo = { }
        self.m_NotifyType = 0
        self.m_Reason = ''

    
    def Shape(self):
        iShape = g_commondrop.get(self.m_SID, 0)
        iPerformSID = self.m_DropInfo[0]
        clsPerform = cl_perform.GetPerformModule(iPerformSID)
        if not clsPerform:
            return iShape
        iShape = clsPerform.m_DropShape
        return iShape

    
    def ValidPick(self, oHero, iPickType = PICK_TYPE_NORMAL):
        if iPickType == PICK_TYPE_NORMAL:
            return self.ValidPickNormal(oHero)
        if iPickType == PICK_TYPE_EXTEND:
            return self.ValidPickExtend(oHero)
        return 0

    
    def GetReward(self):
        return self.m_DropInfo[0]

    
    def ValidPickNormal(self, oHero):
        iPerformSID = self.m_DropInfo[0]
        pfobj = oHero.m_RelicCon.GetPerform(iPerformSID)
        setCanRepickup = set(GetCanRepickupRelic())
        if pfobj and pfobj.m_Level == self.m_Level and iPerformSID not in setCanRepickup:
            cl_notify.SendCommonNotify(oHero.m_Game, [
                oHero.m_PlayerID], 2117, { })
            return 0
        if pfobj and pfobj.m_Level > self.m_Level and not pfobj.ValidRemove():
            cl_notify.SendCommonNotify(oHero.m_Game, [
                oHero.m_PlayerID], 7242, { })
            return 0
        return super(CRelicDrop, self).ValidPick(oHero)

    
    def ValidPickExtend(self, oHero):
        iRelicSID = self.m_DropInfo[0]
        oRelicCon = oHero.m_RelicCon
        if not oRelicCon.IsOpenExtendBag():
            return 0
        if oRelicCon.IsExtendBagFull():
            cl_notify.SendCommonNotify(oHero.m_Game, [
                oHero.m_PlayerID], 2422, { })
            return 0
        oPerform = oRelicCon.GetExtendRelic(iRelicSID)
        if oPerform:
            cl_notify.SendCommonNotify(oHero.m_Game, [
                oHero.m_PlayerID], 2117, { })
            return 0
        return super(CRelicDrop, self).ValidPick(oHero)

    
    def ValidRoll(self, oHero):
        return super(CRelicDrop, self).ValidPick(oHero)

    
    def SetDropData(self, lstDropData, dStaticInfo):
        if 'RollNum' in dStaticInfo:
            self.m_RollNum = dStaticInfo['RollNum']
        if 'OldDropID' in dStaticInfo:
            self.m_RollOldDrop = dStaticInfo['OldDropID']
        if 'Share' in dStaticInfo:
            self.m_Share = dStaticInfo['Share']
        if 'OwnerInfo' in dStaticInfo:
            self.m_OwnerInfo = dStaticInfo['OwnerInfo']
        if 'NotifyType' in dStaticInfo:
            self.m_NotifyType = dStaticInfo['NotifyType']
        if 'Reason' in dStaticInfo:
            self.m_Reason = dStaticInfo['Reason']
        dMsgInfo = {
            'Drop': self.m_ID,
            'StaticInfo': dStaticInfo,
            'Operate': 'SetDropData' }
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_SURVIVOR_HANDLE_RELIC, self.m_Game.GetWarMgr(), dMsgInfo)
        super(CRelicDrop, self).SetDropData(lstDropData, dStaticInfo)

    
    def OnSetDropData(self, lstDropData):
        oHero = self.m_Game.GetObject(self.m_Owner)
        if oHero:
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_GENERATE_RELIC, oHero, {
                'Relic': lstDropData,
                'Drop': self.m_ID })

    
    def Pick(self, iHero, iPos = 0, iPickType = PICK_TYPE_NORMAL):
        oHero = self.m_Game.GetObject(iHero)
        if not oHero or not self.ValidPick(oHero, iPickType):
            self.OnPickFail()
            return 0
        dInfo = self.GetPickMsgInfo(oHero)
        dInfo['Drop'] = self.m_ID
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_PICK, oHero, dInfo, iSub = self.m_SubPickMsg)
        self.OnPick(oHero, iPos, iPickType)
        return 1

    
    def OnPick(self, oHero, iPos = 0, iPickType = PICK_TYPE_NORMAL):
        iPerformSID = self.m_DropInfo[iPos]
        oRelicCon = oHero.m_RelicCon
        dExtInfo = {
            'RollNum': self.m_RollNum,
            'Share': self.m_Share,
            'OwnerInfo': self.m_OwnerInfo,
            'NotifyType': self.m_NotifyType,
            'Reason': self.m_Reason,
            'SourceReason': self.m_SourceReason }
        if iPickType == PICK_TYPE_NORMAL:
            oPickRelic = oRelicCon.AddRelic(iPerformSID, 'pick', self.m_Level, dExtInfo = dExtInfo, iSource = self.m_Source)
        else:
            oPickRelic = oRelicCon.AddExtendRelic(iPerformSID, 'pick', self.m_Level, dExtInfo = dExtInfo, iSource = self.m_Source)
        if oPickRelic:
            dMsgInfo = {
                'Relic': oPickRelic.m_SID,
                'Drop': self.m_ID,
                'Hero': oHero.m_ID,
                'Operate': 'PickRelic' }
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_SURVIVOR_HANDLE_RELIC, self.m_Game.GetWarMgr(), dMsgInfo)
            oPickRelic.UploadPickInfo(self.m_ShareInfo)
        self.Remove('Pick')

    
    def EachDropInfo(self, iSID):
        clsPerform = cl_perform.GetPerformModule(iSID)
        lstAttrInfo = []
        iPropType = cl_netattr.PROP_DROPITEM_RELIC
        for sAttr in cl_netattr.INFO_OBJECT_INIT[iPropType]:
            (iIdx, _, iType, iLen, iMode) = cl_netattr.INFO_PROP_NAME[sAttr]
            if sAttr == 'Level':
                iValue = self.m_Level
            elif sAttr == 'RollNum':
                iValue = self.m_RollNum
            elif sAttr == 'Share':
                iValue = self.m_Share
            else:
                iValue = cl_netattr.GetPropValue(clsPerform, sAttr, iMode, self.m_Game)
            if iValue is None:
                continue
            lstAttrInfo.append((iIdx, iType, iLen, iValue))
        
        return {
            'Type': iPropType,
            'Attr': lstAttrInfo }



class CCurseRelicDrop(CRelicDrop):
    m_SID = 5515
    m_FightType = NWARRIOR_DROP_RELIC_CURSE
    m_EnablePick = 0
    
    def __init__(self, oGame, nid):
        super(CCurseRelicDrop, self).__init__(oGame, nid)

    
    def DelayPick(self, oHero, iPos = 0, iPickType = PICK_TYPE_NORMAL):
        if not self.m_EnablePick:
            return None
        if not self.ValidPick(oHero, iPickType):
            cl_snetwar.GS2CPickFail(self.m_Game, self.m_Scene, self.m_Pick, self.m_ID)
            return None
        self.SetPicker(oHero)
        self.Pick(oHero.m_ID, iPos)

    
    def EnterScene(self, iOldScene):
        super(CCurseRelicDrop, self).EnterScene(iOldScene)
        oHero = self.m_Game.GetObject(self.m_Owner)
        if not oHero or not self.ValidPick(oHero):
            cl_snetwar.GS2CPickFail(self.m_Game, self.m_Scene, self.m_Pick, self.m_ID)
            return None
        self.SetPicker(oHero)
        cl_snetwar.GS2CPickUp(self.m_Game, self.m_Scene, oHero.m_ID, self.m_ID)
        self.Call_Out(Functor(self.Pick, oHero.m_ID), Time2Frame(self.m_DelayPickTime), 'DelayPick')

    
    def SetDropData(self, lstDropData, dStaticInfo):
        super().SetDropData(lstDropData, dStaticInfo)
        if 'DelayPickTime' in dStaticInfo:
            self.m_DelayPickTime = dStaticInfo['DelayPickTime']
        if 'EnablePick' in dStaticInfo:
            self.m_EnablePick = dStaticInfo['EnablePick']



class CBulletDrop(CDrop):
    m_SID = 5501
    m_FightType = NWARRIOR_DROP_BULLET
    m_SubPickMsg = PICK_BULLET
    
    def NetAddTo(self, dPlayer):
        dInfo = self.m_DropInfo[0]
        if not dInfo:
            return None
        super().NetAddTo(dPlayer)

    
    def Shape(self):
        dInfo = self.m_DropInfo[0]
        iSID = list(dInfo.keys())[0]
        clsItem = cl_item.GetItemCls(iSID)
        if clsItem:
            return clsItem.m_Shape
        iShape = g_commondrop.get(self.m_SID, 0)
        return iShape

    
    def OnPick(self, oHero, iPos = 0, iPickType = PICK_TYPE_NORMAL):
        dInfo = self.m_DropInfo[iPos]
        oBulletCon = oHero.m_BulletCon
        for iBulletSID, iCnt in dInfo.items():
            oBulletCon.BulletModify(iBulletSID, iCnt, 'Pick')
        
        self.Remove('Pick')

    
    def OnSetDropData(self, lstDropData):
        iAlert = 0
        sAlertText = ''
        for dDropData in lstDropData:
            for iBulletSID, iCnt in dDropData.items():
                if iCnt < 0:
                    iAlert = 1
                    sAlertText += f''' {iBulletSID} {iCnt}'''
            
        
        if iAlert:
            sAlertText = 'bullet amount err' + sAlertText
            SendAlert('err', sAlertText)
            TraceLog('err', sAlertText)

    
    def ValidPick(self, oHero, iPickType = PICK_TYPE_NORMAL):
        if not super(CBulletDrop, self).ValidPick(oHero):
            return 0
        iDropModule = self.GetTrueDropModule(oHero)
        dInfo = self.m_DropInfo[0]
        oBulletCon = oHero.m_BulletCon
        if iDropModule <= DROP_BULLETPICK_NORMAL:
            for iBulletSID in dInfo:
                if oBulletCon.Bullet(iBulletSID) < oBulletCon.GetMaxBullet(iBulletSID):
                    return 1
            
        else:
            for iPickTpye in g_PickFunc:
                if iPickTpye & iDropModule == iPickTpye and GetCheckPickFunc(iPickTpye)(oHero, dInfo):
                    return 1
            
        return 0

    
    def GetTrueDropModule(self, oHero):
        dInfo = self.m_DropInfo[0]
        oBulletCon = oHero.m_BulletCon
        iDropModule = oBulletCon.m_DropModule
        if iDropModule == DROP_BULLETPICK_IGNOREMAX:
            return iDropModule
        if iDropModule > DROP_BULLETPICK_NORMAL:
            oCurWeapon = oHero.m_WieldCon.GetCurWeapon()
            if oCurWeapon and oCurWeapon.m_Type & EQUIP_TYPE_MAINWEAPON != EQUIP_TYPE_MAINWEAPON:
                return DROP_BULLETPICK_NORMAL
            oThrowPerform = oHero.GetThrowPerform()
            iThrowBulletSID = oThrowPerform.CalAttr('BulletSID')
            for iBulletSID in dInfo:
                if iBulletSID != iThrowBulletSID:
                    return iDropModule
            
            return DROP_BULLETPICK_NORMAL
        return iDropModule

    
    def DropDesc(self):
        return []



class CWandDrop(CDrop):
    m_SID = 5543
    m_FightType = NWARRIOR_DROP_MAGIC_WAND
    
    def MapSendPacket(self, dPlayer):
        super().MapSendPacket(dPlayer)
        oWand = self.m_DropInfo[0]
        wandnet.GS2CDropWandAbilities(self.m_Game, self.m_ID, oWand.GetWandAbilityInfo(), dPlayer)

    
    def Shape(self):
        iShape = g_commondrop.get(self.m_SID, 0)
        return iShape

    
    def ValidPick(self, oHero, iPickType = PICK_TYPE_NORMAL):
        if not oHero.m_WandCon.ValidAddWand():
            return 0
        return super().ValidPick(oHero)

    
    def OnPick(self, oHero, iPos = 0, iPickType = PICK_TYPE_NORMAL):
        oWandCon = oHero.m_WandCon
        if oWandCon:
            oWand = self.m_DropInfo[iPos]
            if oWand.QueryTmp('MGDrop', 0):
                oWand.SetTmp('MGDrop', 0)
                oWand.Set('InitComp', 1)
            sReason = 'Pick'
            self.m_DropInfo.pop(iPos)
            self.Remove(sReason)
            oWandCon.AddWandToContainer(oWand, sReason = sReason)

    
    def OnSetDropData(self, lstDropData):
        oWand = lstDropData[0]
        if oWand and oWand.m_Quality in WANDDROPSID_BY_QUALITY:
            self.m_SID = WANDDROPSID_BY_QUALITY[oWand.m_Quality]

    
    def EachDropInfo(self, oDropItem):
        lstAttrInfo = []
        iPropType = cl_netattr.PROP_ITEM
        for sAttr in cl_netattr.INFO_OBJECT_INIT[iPropType]:
            (iIdx, _, iType, iLen, iMode) = cl_netattr.INFO_PROP_NAME[sAttr]
            iValue = cl_netattr.GetPropValue(oDropItem, sAttr, iMode)
            if iValue is None:
                continue
            lstAttrInfo.append((iIdx, iType, iLen, iValue))
        
        return {
            'Type': iPropType,
            'Attr': lstAttrInfo }



class CWandCompDrop(CDrop):
    m_SID = 5544
    m_FightType = NWARRIOR_DROP_WANDCOMP
    m_WandCompSID = 0
    m_WandCompLevel = 0
    
    def Shape(self):
        iShape = g_commondrop.get(self.m_SID, 0)
        return iShape

    
    def ValidPick(self, oHero, iPickType = PICK_TYPE_NORMAL):
        if not self.m_WandCompSID:
            return 0
        return super().ValidPick(oHero)

    
    def OnPick(self, oHero, iPos = 0, iPickType = PICK_TYPE_NORMAL):
        oWandCon = oHero.m_WandCon
        if oWandCon:
            self.Remove('Pick')
            oWandCon.AddBagComp(self.m_WandCompSID, self.m_WandCompLevel, 1, 'Pick')

    
    def OnSetDropData(self, lstDropData):
        dDropData = lstDropData[0]
        if 'WandCompSID' in dDropData:
            self.m_WandCompSID = dDropData['WandCompSID']
        if 'WandCompLevel' in dDropData:
            self.m_WandCompLevel = dDropData['WandCompLevel']

    
    def EachDropInfo(self, oDropItem):
        lstAttrInfo = []
        iPropType = cl_netattr.PROP_WANDCOMP
        for sAttr in cl_netattr.INFO_OBJECT_INIT[iPropType]:
            (iIdx, _, iType, iLen, _) = cl_netattr.INFO_PROP_NAME[sAttr]
            if sAttr == 'Level':
                iValue = self.m_WandCompLevel
            elif sAttr == 'SID':
                iValue = self.m_WandCompSID
            
            lstAttrInfo.append((iIdx, iType, iLen, iValue))
        
        return {
            'Type': iPropType,
            'Attr': lstAttrInfo }

    
    def Name(self):
        clsWandComp = cl_wand.GetWandCompCls(self.m_WandCompSID)
        if not clsWandComp:
            return '无名'
        return clsWandComp.m_Name



class CNoDistanceBulletDrop(CBulletDrop):
    m_SID = 5545
    m_FightType = NWARRIOR_DROP_NODISTANCEBULLET


class CDiceDrop(CDrop):
    m_SID = 5549
    m_FightType = NWARRIOR_DROP_DICE
    
    def Shape(self):
        iShape = g_commondrop.get(self.m_SID, 0)
        return iShape

    
    def OnPick(self, oHero, iPos = 0, iPickType = PICK_TYPE_NORMAL):
        
        def SetDicePointCBFunc(oHero, iDropID, iPoints):
            dinednet.GS2CDiceDropRollInfo(oHero.m_PlayerID, iDropID, iPoints)

        oDiceCon = oHero.m_DiceCon
        if not oDiceCon:
            return 0
        if iPickType == PICK_TYPE_NORMAL:
            oDice = self.m_DropInfo[iPos]
            sReason = 'NormalPick'
            self.m_DropInfo.pop(iPos)
            self.Remove(sReason)
            oDiceCon.AddDiceToContainer(oDice, sReason = sReason)
            oDiceCon.CheckAndReplaceAssembleDice(oDice)
        elif iPickType == PICK_TYPE_EXTEND:
            oDice = self.m_DropInfo[iPos]
            sReason = 'LongPressPick'
            self.m_DropInfo.pop(iPos)
            self.Remove(sReason)
            oDiceCon.AddDiceToContainer(oDice, sReason = sReason)
            dResult = oDiceCon.RollDice(oDice.m_ID, sReason, cbfunc = Functor(SetDicePointCBFunc, oHero, self.m_ID), dExtraInfo = {
                'LongPressSkipChoose': 1 })
            if not dResult:
                return None
            if len(dResult) > 1:
                iRollPoint = max(dResult.values())
                dinednet.GS2CDiceDropRollInfo(oHero.m_PlayerID, self.m_ID, iRollPoint)
                oDiceCon.SetDicePoint(oDice.m_ID, iRollPoint, sReason, bAddDiceEnergy = True)
            oDiceCon.CheckAndReplaceAssembleDice(oDice)

    
    def OnSetDropData(self, lstDropData):
        oDiceElement = self.m_Game.m_WarMgr.GetDiceElement()
        if not oDiceElement:
            return None
        dDiceShape = oDiceElement.GetDropDiceShape()
        oDice = lstDropData[0]
        iQuality = oDice.m_Quality
        if iQuality in dDiceShape:
            self.m_SID = dDiceShape[iQuality]

    
    def EachDropInfo(self, oDropItem):
        lstAttrInfo = []
        iPropType = cl_netattr.PROP_DICE
        for sAttr in cl_netattr.INFO_OBJECT_INIT[iPropType]:
            (iIdx, _, iType, iLen, iMode) = cl_netattr.INFO_PROP_NAME[sAttr]
            if sAttr == 'PointRange':
                iValue = []
                for iQuality, lstRange in oDropItem.GetPointRange().items():
                    if not lstRange:
                        continue
                    iLen = len(lstRange)
                    iValue.extend([ iQuality for _ in range(iLen) ])
                
            else:
                iValue = cl_netattr.GetPropValue(oDropItem, sAttr, iMode)
            if iValue is None:
                continue
            lstAttrInfo.append((iIdx, iType, iLen, iValue))
        
        return {
            'Type': iPropType,
            'Attr': lstAttrInfo }

    
    def ValidPick(self, oHero, iPickType = PICK_TYPE_NORMAL):
        if iPickType == PICK_TYPE_NORMAL:
            return self.ValidPickNormal(oHero)
        if iPickType == PICK_TYPE_EXTEND:
            return self.ValidPickExtend(oHero)
        return 0

    
    def ValidPickNormal(self, oHero):
        oDice = self.m_DropInfo[0]
        if not oDice:
            return 0
        if oDice.m_SID not in GetAllDiceAbility():
            return 0
        return super(CDiceDrop, self).ValidPick(oHero)

    
    def ValidPickExtend(self, oHero):
        oDice = self.m_DropInfo[0]
        if not oDice:
            return 0
        if oDice.m_SID not in GetAllDiceAbility():
            return 0
        if oDice.GetRollType():
            return 0
        return super(CDiceDrop, self).ValidPick(oHero)



class CExperienceBallDrop(CDrop):
    m_SID = 5524
    m_FightType = NWARRIOR_DROP_EXPERIENCE
    
    def Shape(self):
        dInfo = self.m_DropInfo[0]
        iShape = g_commondrop.get(self.m_SID, 0)
        if dInfo['DropModel']:
            iShape = dInfo['DropModel']
        return iShape

    
    def OnPick(self, oHero, iPos = 0, iPickType = PICK_TYPE_NORMAL):
        oSurvivorElement = self.m_Game.m_WarMgr.GetComponent('SurvivorElement')
        if oSurvivorElement:
            dInfo = self.m_DropInfo[iPos]
            iExperience = dInfo['Experience']
            self.Remove('Pick')
            oSurvivorElement.m_UpgradeMgr.AddExperience(iExperience)

    
    def DropDesc(self):
        return []



class CRareItemDrop(CDrop):
    m_SID = 5525
    m_FightType = NWARRIOR_DROP_RAREITEM
    
    def Shape(self):
        return self.m_DropInfo[0].m_Shape

    
    def OnPick(self, oHero, iPos = 0, iPickType = PICK_TYPE_NORMAL):
        oItem = self.m_DropInfo[iPos]
        lstContainer = oItem.GetTargetContainer(oHero)
        sReason = 'Pick:%d-%d' % (oItem.Type(), oItem.m_SID)
        if oItem.PutToContainer(lstContainer, sReason):
            self.m_DropInfo.pop(iPos)
            self.Remove(sReason)

    
    def EachDropInfo(self, oDropItem):
        lstAttrInfo = []
        iPropType = cl_netattr.PROP_ITEM
        for sAttr in cl_netattr.INFO_OBJECT_INIT[iPropType]:
            (iIdx, _, iType, iLen, iMode) = cl_netattr.INFO_PROP_NAME[sAttr]
            iValue = cl_netattr.GetPropValue(oDropItem, sAttr, iMode)
            if iValue is None:
                continue
            lstAttrInfo.append((iIdx, iType, iLen, iValue))
        
        return {
            'Type': iPropType,
            'Attr': lstAttrInfo }



class CAxeDrop(CDrop):
    m_SID = 5526
    m_FightType = NWARRIOR_DROP_AXE
    
    def Shape(self):
        iShape = g_commondrop.get(self.m_SID, 0)
        return iShape

    
    def OnPick(self, oHero, iPos = 0, iPickType = PICK_TYPE_NORMAL):
        dInfo = self.m_DropInfo[iPos]
        iWeapon = dInfo['Item']
        dArgs = {
            'AID': oHero.m_ID,
            'RS': cl_object.reason.CStrReason('PickAxe%d-%d' % (self.m_SID, self.m_ID), None, {
                'Item': iWeapon }),
            'arg': { } }
        iTimeType = STATE_TIME_LIMIT
        if not dInfo['StateTime']:
            iTimeType = STATE_TIME_FOREVER
        oState = cl_state.AddState(oHero, dInfo['StateSID'], iTimeType, Time2Frame(dInfo['StateTime']), dArgs)
        if oState:
            oState.Enable(oHero)
        self.Remove('Pick')

    
    def DropDesc(self):
        return []

    
    def OnSetDropData(self, lstDropData):
        iTime = g_SurvivalTime.get(self.m_SID, 0)
        dInfo = lstDropData[0]
        iExtTime = dInfo['ExtTime']
        iTime += iExtTime
        if iTime:
            iFrame = Time2Frame(iTime)
            self.Set('SurvivalFrame', self.m_Game.GetFrameNum() + iFrame)
            self.Call_Out(Functor(self.OnDisappear), iFrame, 'SurvivalTime')

    
    def DropDisappear(self):
        pass

    
    def GetPickMsgInfo(self, oHero, iPos = 0):
        dInfo = super().GetPickMsgInfo(oHero, iPos)
        dInfo['SurvivalFrame'] = self.Query('SurvivalFrame', 0)
        if 'Item' in self.m_DropInfo[iPos]:
            dInfo['ItemID'] = self.m_DropInfo[iPos]['Item']
        dInfo['VID'] = self.Abandoner()
        return dInfo



class CEnchantingBulletDrop(CDrop):
    m_SID = 5527
    m_FightType = NWARRIOR_DROP_ENCHANTING_BULLET
    
    def Shape(self):
        iShape = g_commondrop.get(self.m_SID, 0)
        return iShape

    
    def OnPick(self, oHero, iPos = 0, iPickType = PICK_TYPE_NORMAL):
        dInfo = self.m_DropInfo[iPos]
        for iPerform, iAmount in dInfo.items():
            for _ in range(iAmount):
                oPerform = oHero.GetPerform(iPerform)
                if not oPerform or oPerform.m_PFType != PF_TYPE_TRIGGERCLIENT:
                    SendAlert('err', '技能%s类型不是客户端主动，请检查配置' % iPerform)
                    continue
                oPerform.AddCanUseCount()
            
        
        self.Remove('Pick')

    
    def DropDesc(self):
        return []



class CCashDrop(CDrop):
    m_SID = 5502
    m_FightType = NWARRIOR_DROP_CASH
    m_SubPickMsg = PICK_CASH
    
    def Shape(self):
        iShape = g_commondrop.get(self.m_SID, 0)
        return iShape

    
    def Pick(self, iHero, iPos = 0, iPickType = PICK_TYPE_NORMAL):
        oHero = self.m_Game.GetObject(iHero)
        if not oHero or not self.ValidPick(oHero):
            self.OnPickFail()
            return 0
        if iPos != 0:
            WarobjLog.Alert('%s pick cash pos err %s %s' % (self.m_Game.m_ID, self.m_ID, iPos))
        for iPickPos in list(self.m_DropInfo):
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_PICK, oHero, self.GetPickMsgInfo(oHero, iPickPos), iSub = self.m_SubPickMsg)
            self.OnPick(oHero, iPickPos)
        
        self.Remove('Pick')
        return 1

    
    def OnPick(self, oHero, iPos = 0, iPickType = PICK_TYPE_NORMAL):
        dInfo = self.m_DropInfo[iPos]
        iCash = dInfo['Cash']
        oHero.AddCash(iCash, 'Pick', iSendMsg = 1, iLog = 0)

    
    def DropDesc(self):
        return []

    
    def MergeDropData(self, lstDropData):
        iIdx = len(self.m_DropInfo)
        for dDropData in lstDropData:
            self.m_DropInfo[iIdx] = dDropData
            iIdx += 1
        

    
    def CheckMerge(self, tPos, dExtraInfo, dStaticInfo):
        iDropSource = dStaticInfo['DropSource'] if 'DropSource' in dStaticInfo else 0
        if self.m_Source != iDropSource:
            return False
        iAbandoner = dExtraInfo['Abandoner'] if 'Abandoner' in dExtraInfo else 0
        if self.Query('Abandoner') != iAbandoner:
            return False
        if not cl_math.CheckDistance3D(self.m_Pos, tPos, 0.5):
            return False
        return True



class CGSCashDrop(CDrop):
    m_SID = 5507
    m_FightType = NWARRIOR_DROP_GSCASH
    
    def Shape(self):
        iShape = g_commondrop.get(self.m_SID, 0)
        return iShape

    
    def OnPick(self, oHero, iPos = 0, iPickType = PICK_TYPE_NORMAL):
        dInfo = self.m_DropInfo[iPos]
        iGSCash = dInfo['GSCash']
        oHero.AddGSCash(iGSCash, 'Pick')
        self.Remove('Pick')

    
    def DropDesc(self):
        return []



class CKeyDrop(CDrop):
    m_SID = 5505
    m_FightType = NWARRIOR_DROP_KEY
    
    def Shape(self):
        iShape = g_commondrop.get(self.m_SID, 0)
        return iShape

    
    def OnPick(self, oHero, iPos = 0, iPickType = PICK_TYPE_NORMAL):
        dKey = self.m_DropInfo[iPos]
        oHero.AddKey(dKey, 'Pick')
        self.Remove('Pick')

    
    def DropDesc(self):
        return []



class CTriggerDrop(CDrop):
    m_SID = 5504
    m_FightType = NWARRIOR_DROP_TRIGGER
    
    def OnSetDropData(self, lstDropData):
        self.m_WaitPickFrame = 0
        dInfo = self.m_DropInfo[0]
        for iPerformSID in dInfo:
            clsTriggerPerform = cl_perform.GetPerformModule(iPerformSID)
            self.m_WaitPickFrame = Time2Frame(clsTriggerPerform.m_WaitPickTime)
        
        if self.m_WaitPickFrame:
            self.Call_Out(self.NonePick, self.m_WaitPickFrame, 'WaitPick')

    
    def OnDelayPickBegin(self):
        self.Remove_Call_Out('WaitPick')

    
    def OnPickFail(self):
        super(CTriggerDrop, self).OnPickFail()
        if self.m_WaitPickFrame:
            self.Call_Out(self.NonePick, self.m_WaitPickFrame, 'WaitPick')

    
    def Shape(self):
        iShape = g_commondrop.get(self.m_SID, 0)
        dInfo = self.m_DropInfo[0]
        for iPerformSID in dInfo:
            clsTriggerPerform = cl_perform.GetPerformModule(iPerformSID)
            if not clsTriggerPerform:
                return iShape
            iShape = clsTriggerPerform.m_DropShape
        
        return iShape

    
    def OnPick(self, oHero, iPos = 0, iPickType = PICK_TYPE_NORMAL):
        dInfo = self.m_DropInfo[iPos]
        self.Remove('Pick')
        for iPerform, iAmount in dInfo.items():
            for _ in range(iAmount):
                dReward = { }
                dRewardInfo = {
                    'sid': iPerform,
                    'data': { } }
                dReward['info'] = dRewardInfo
                cl_reward.RewardAutoPerform(oHero.m_Game, oHero, dReward, 'pick', { })
            
        

    
    def ValidPick(self, oHero, iPickType = PICK_TYPE_NORMAL):
        if not super(CTriggerDrop, self).ValidPick(oHero):
            return 0
        dInfo = self.m_DropInfo[0]
        for iPerform in dInfo:
            if not CheckTriggerPFCanUse(oHero, iPerform):
                continue
            oPerform = oHero.GetPerformIfNoThenNew(iPerform)
            dData = {
                'VID': oHero.m_ID }
            iCanUse = oPerform.CanUse(oHero, dData)
            if iCanUse == SKILLRET_SUCCESS:
                return 1
            oHero.RemovePerform(iPerform)
        
        return 0

    
    def DropDesc(self):
        return []

    
    def NonePick(self):
        self.Remove('NonePick')



class CKeyItemDrop(CDrop):
    m_SID = 5508
    m_FightType = NWARRIOR_DROP_KEYITEM
    
    def Release(self):
        WarobjLog.Debug('%d release keyitem %d' % (self.m_Game.m_ID, self.m_ID))
        self.m_DropInfo = { }
        super().Release()

    
    def Shape(self):
        return self.m_DropInfo[0].m_Shape

    
    def OnPick(self, oHero, iPos = 0, iPickType = PICK_TYPE_NORMAL):
        oItem = self.m_DropInfo[iPos]
        lstContainer = oItem.GetTargetContainer(oHero)
        sReason = 'Pick:%d-%d' % (oItem.Type(), oItem.m_SID)
        oItem.AddAmount(1, 'PickDrop')
        if oItem.PutToContainer(lstContainer, sReason):
            self.m_DropInfo.pop(iPos)
            self.Remove(sReason)

    
    def OnInitToScene(self, tPos):
        WarobjLog.Debug('%d drop keyitem %d %s' % (self.m_Game.m_ID, self.m_ID, tPos))
        super().OnInitToScene(tPos)

    
    def DropDesc(self):
        return []



class CTreasureDeadDrop(CDrop):
    m_SID = 5517
    m_FightType = NWARRIOR_DROP_TREASURE_DEAD
    
    def __init__(self, oGame, nid):
        super(CTreasureDeadDrop, self).__init__(oGame, nid)

    
    def Shape(self):
        iShape = g_commondrop.get(self.m_SID, 0)
        return iShape

    
    def OnPick(self, oHero, iPos, iPickType = PICK_TYPE_NORMAL):
        self.Remove('Pick')

    
    def GetPickMsgInfo(self, oHero, iPos = 0):
        dInfo = { }
        dInfo['Picker'] = oHero.m_ID
        dInfo['Type'] = self.m_FightType
        dInfo['Item'] = self.m_DropInfo[iPos]
        dInfo['Drop'] = self.m_ID
        dInfo['DropPos'] = self.m_DropPos
        return dInfo

    
    def GetDropMsgInfo(self, iPos = 0):
        dInfo = { }
        dInfo['Type'] = self.m_FightType
        dInfo['Item'] = self.m_DropInfo[iPos]
        dInfo['Drop'] = self.m_ID
        dInfo['DropPos'] = self.m_DropPos
        dInfo['Delaytime'] = self.m_Delaytime
        return dInfo

    
    def GetGetDisappearMsgInfo(self, iPos = 0):
        dInfo = { }
        dInfo['Type'] = self.m_FightType
        dInfo['Item'] = self.m_DropInfo[iPos]
        dInfo['Drop'] = self.m_ID
        dInfo['DropPos'] = self.m_DropPos
        dInfo['Scene'] = self.m_Scene
        return dInfo

    
    def OnSetDropData(self, lstDropData):
        if 'DropPos' in lstDropData[0]:
            self.m_DropPos = lstDropData[0]['DropPos']
        if 'Delaytime' in lstDropData[0]:
            self.m_Delaytime = lstDropData[0]['Delaytime']

    
    def DropDesc(self):
        return []

    
    def OnDelayPickBegin(self):
        self.Remove_Call_Out('SurvivalTime')



def GetMonsterRelicDemonReward(oDrop, oHero):
    oElement = oDrop.m_Game.m_WarMgr.GetComponent('MonsterRelicElement')
    if not oElement:
        return { }
    return oElement.GetMonsterRelicDemonReward(oDrop, oHero)

g_DynamicRewardFunc = {
    DYNAMIC_DEMON_MONSTERRELIC: GetMonsterRelicDemonReward }

class CDemonDrop(CDrop):
    m_SID = 5522
    m_FightType = NWARRIOR_DROP_DEMON
    m_Quality2SID = {
        0: 5522,
        1: 5518,
        2: 5539 }
    
    def __init__(self, oGame, nid):
        super(CDemonDrop, self).__init__(oGame, nid)
        self.m_Quality = 0
        self.m_MGInfo = { }
        self.m_DynamicReward = 0

    
    def Shape(self):
        iShape = g_commondrop.get(self.m_SID, 0)
        return iShape

    
    def Release(self):
        self.m_MGInfo = { }
        super().Release()

    
    def OnPick(self, oHero, iPos = 0, iPickType = PICK_TYPE_NORMAL):
        oTarget = self.m_Game.GetObject(self.m_Owner)
        if self.m_DynamicReward:
            dReward = g_DynamicRewardFunc[self.m_DynamicReward](self, oTarget)
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_DEMON_DYNAMIC_REWARD, oHero, {
                'Reward': dReward }, iSub = self.m_DynamicReward)
            self.m_MGInfo = dReward
        for iMiniGame, lstInfo in self.m_MGInfo.items():
            (iSID, lstReward, dExtInfo) = lstInfo
            for dReward in lstReward:
                if dReward['item'] == VIRTUAL_ITEM_GOLDENCUP and 'DropPos' in dReward['info']:
                    continue
                dReward['info']['DropPos'] = self.GetPos()
            
            dExtInfo['Abandoner'] = self.m_ID
            cl_reward.RewardItem(self.m_Game, oTarget, lstReward, 'MiniGame%s-%s' % (iSID, iMiniGame), dExtInfo)
        
        self.Remove('Pick')

    
    def EachDropInfo(self, oDropItem):
        lstAttrInfo = []
        iPropType = cl_netattr.PROP_DROPITEM_DEMON
        for sAttr in cl_netattr.INFO_OBJECT_INIT[iPropType]:
            (iIdx, _, iType, iLen, _) = cl_netattr.INFO_PROP_NAME[sAttr]
            if sAttr == 'Quality':
                iValue = self.m_Quality
            elif sAttr == 'SID':
                iValue = self.m_SID
            
            lstAttrInfo.append((iIdx, iType, iLen, iValue))
        
        return {
            'Type': iPropType,
            'Attr': lstAttrInfo }

    
    def OnSetDropData(self, lstDropData):
        if not self.m_DynamicReward:
            self.m_MGInfo = lstDropData[0]
            if self.m_Quality < 1:
                for tInfo in self.m_MGInfo.values():
                    (_, lstReward, _) = tInfo
                    for dReward in lstReward:
                        iRewardItem = dReward['item'] if 'item' in dReward else 0
                        if iRewardItem in [
                            VIRTUAL_ITEM_GOLDENCUP,
                            VIRTUAL_ITEM_MAGICPOWER]:
                            self.m_Quality = 1
                            break
                        if iRewardItem == VIRTUAL_ITEM_DROP:
                            iDropType = dReward.get('info', { }).get('DropType', 0)
                            if iDropType in HIGHQUALITY_DROP:
                                self.m_Quality = 1
                                break
                    
                
        self.m_SID = self.m_Quality2SID[self.m_Quality]
        self.m_DelayPickTime = g_DelayPickTime[self.m_SID]

    
    def SetDropData(self, lstDropData, dStaticInfo):
        if 'PhaseChallenge' in dStaticInfo:
            self.Set('PhaseChallenge', dStaticInfo['PhaseChallenge'])
        if 'Quality' in dStaticInfo:
            self.m_Quality = dStaticInfo['Quality']
        if 'DynamicReward' in dStaticInfo:
            self.m_DynamicReward = dStaticInfo['DynamicReward']
        super().SetDropData(lstDropData, dStaticInfo)

    
    def GetPickMsgInfo(self, oHero, iPos = 0):
        dInfo = super().GetPickMsgInfo(oHero, iPos)
        dPhaseChallenge = self.Query('PhaseChallenge')
        if dPhaseChallenge:
            dInfo['PhaseChallenge'] = dPhaseChallenge
        return dInfo



class CRelifeDrop(CDrop):
    m_SID = 5519
    m_FightType = NWARRIOR_DROP_RELIFE
    
    def Shape(self):
        iShape = g_commondrop.get(self.m_SID, 0)
        return iShape

    
    def OnPick(self, oHero, iPos = 0, iPickType = PICK_TYPE_NORMAL):
        oPerform = oHero.GetPerformIfNoThenNew(self.m_Perform)
        oPerform.AddCanUseCount()
        cl_war.UsePerform(oHero, oPerform, { })
        cl_notify.SendCommonNotify(oHero.m_Game, [
            oHero.m_PlayerID], 9285, { })
        self.Remove('Pick')

    
    def OnSetDropData(self, lstDropData):
        self.m_Perform = lstDropData[0]['PerformID']

    
    def DropDesc(self):
        return []



class CMagicPowerDrop(CDrop):
    m_SID = 5528
    m_Group = 0
    m_FightType = NWARRIOR_DROP_MAGIC_POWER
    
    def Shape(self):
        return g_commondrop.get(self.m_SID, 0)

    
    def OnPickUp(self, oHero):
        pass

    
    def OnPick(self, oHero, iPos = 0, iPickType = PICK_TYPE_NORMAL):
        oRelicTalentCon = oHero.m_RelicTalentCon
        if self.m_Option or self.m_MagicPower:
            oRelicTalentCon.RewardByDrop(oHero, self, self.m_Option, self.m_MagicPower, 'MagicJade')
        else:
            self.Remove('Pick')

    
    def Remove(self, sReason):
        self.m_Game.m_WarMgr.RemoveDropGroup(self.m_Group, self.m_Owner)
        self.m_Option = 0
        self.m_MagicPower = 0
        super().Remove(sReason)

    
    def OnSetDropData(self, lstDropData):
        dInfo = lstDropData[0]
        self.m_Option = dInfo['Option']
        self.m_MagicPower = dInfo['MagicPower']
        if 'Group' in dInfo:
            self.m_Group = dInfo['Group']
            self.m_Game.m_WarMgr.SetDropGroup(self, self.m_Group)
        if 'SID' in dInfo:
            self.m_SID = dInfo['SID']

    
    def DropDesc(self):
        return []



class CInkBeadDrop(CDrop):
    m_SID = 5531
    m_FightType = NWARRIOR_DROP_INKBEAD
    m_AddInkValue = 0
    
    def Shape(self):
        return g_commondrop.get(self.m_SID, 0)

    
    def Pick(self, iHero, iPos = 0, iPickType = PICK_TYPE_NORMAL):
        oHero = self.m_Game.GetObject(iHero)
        if not oHero or not self.ValidPick(oHero):
            self.OnPickFail()
            return 0
        dDropInfo = self.m_DropInfo[iPos]
        dInfo = self.GetPickMsgInfo(oHero)
        dInfo['InkBeadReward'] = dDropInfo['AddInkValue']
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_PICK, oHero, dInfo, iSub = dDropInfo['InkBeadType'])
        self.m_AddInkValue = dInfo['InkBeadReward']
        self.OnPick(oHero, iPos)
        return 1

    
    def OnPick(self, oHero, iPos = 0, iPickType = PICK_TYPE_NORMAL):
        oInkCon = oHero.m_InkCon
        oInkCon.ModifyInkValue(self.m_AddInkValue, 'Pick')
        oInkCon.RemoveInkBead(self, 'Pick')

    
    def OnSetDropData(self, lstDropData):
        dDropData = lstDropData[0]
        self.m_SID = dDropData['SID']

    
    def DropDesc(self):
        return []



class CDeviceCompDrop(CDrop):
    m_SID = 5533
    m_FightType = NWARRIOR_DROP_DEVICECOMP
    
    def Shape(self):
        iShape = g_commondrop.get(self.m_SID, 0)
        iPerformSID = self.m_DropInfo[0]
        clsPerform = cl_perform.GetPerformModule(iPerformSID)
        if not clsPerform:
            return iShape
        iShape = clsPerform.m_DropShape
        return iShape

    
    def OnPick(self, oHero, iPos = 0, iPickType = PICK_TYPE_NORMAL):
        iSID = self.m_DropInfo[0]
        self.Remove('Pick')
        oHero.m_DevicePerformCon.PickComponent(iSID, 'Pick')

    
    def ValidPick(self, oHero, iPickType = PICK_TYPE_NORMAL):
        iSID = self.m_DropInfo[0]
        if not oHero.m_DevicePerformCon.ValidPickComponent(iSID, 'Pick'):
            return 0
        return super().ValidPick(oHero)

    
    def EachDropInfo(self, iSID):
        clsPerform = cl_perform.GetPerformModule(iSID)
        lstAttrInfo = []
        iPropType = cl_propdata.PROP_DROPITEM_DEVICECOMP
        for sAttr in cl_netattr.INFO_OBJECT_INIT[iPropType]:
            (iIdx, _, iType, iLen, iMode) = cl_netattr.INFO_PROP_NAME[sAttr]
            iValue = cl_netattr.GetPropValue(clsPerform, sAttr, iMode, self.m_Game)
            if iValue is None:
                continue
            lstAttrInfo.append((iIdx, iType, iLen, iValue))
        
        return {
            'Type': iPropType,
            'Attr': lstAttrInfo }



class CPetEggDrop(CDrop):
    m_SID = 5535
    m_FightType = NWARRIOR_DROP_PETEGG
    m_EggType = PET_EGG_NORMAL
    m_Group = 0
    
    def Shape(self):
        return g_commondrop.get(self.m_SID, 0)

    
    def ValidPick(self, oHero, iPickType = PICK_TYPE_NORMAL):
        if oHero.m_PetCon.CheckIsFull():
            cl_notify.SendCommonNotify(oHero.m_Game, [
                oHero.m_PlayerID], 9591, { })
            return 0
        return super().ValidPick(oHero)

    
    def OnPick(self, oHero, iPos = 0, iPickType = PICK_TYPE_NORMAL):
        self.Remove('Pick')
        oHero.m_PetCon.AddPetEgg(self.m_EggType)

    
    def Remove(self, sReason):
        self.m_Game.m_WarMgr.RemoveDropGroup(self.m_Group, self.m_Owner)
        super().Remove(sReason)

    
    def OnSetDropData(self, lstDropData):
        dDropData = lstDropData[0]
        self.m_EggType = dDropData['Type']
        if 'SID' in dDropData:
            self.m_SID = dDropData['SID']
        if 'Group' in dDropData:
            self.m_Group = dDropData['Group']
            self.m_Game.m_WarMgr.SetDropGroup(self, self.m_Group)

    
    def DropDesc(self):
        return []



class CBlankRelicDrop(CDrop):
    m_SID = 5540
    m_FightType = NWARRIOR_DROP_RELIC_BLANK
    
    def Shape(self):
        return g_commondrop.get(self.m_SID, 0)

    
    def OnPick(self, oHero, iPos = 0, iPickType = PICK_TYPE_NORMAL):
        self.Remove('Pick')
        oHero.m_RelicCon.ChangeBlankRelicNum(1, 'Pick')

    
    def DropDesc(self):
        return []



class CMysteryRelicDrop(CRelicDrop):
    m_SID = 5541
    m_FightType = NWARRIOR_DROP_RELIC_MYSTERY


class CCookiesDrop(CDrop):
    m_SID = 5548
    m_FightType = NWARRIOR_DROP_COOKIES
    
    def Shape(self):
        iShape = g_commondrop.get(self.m_SID, 0)
        return iShape

    
    def Release(self):
        cl_msgcenter.DoneAttention(self, self.m_Owner, cl_msgcenter.MSG_WAR_WANDDISABLE, 'RemoveSelf')
        super().Release()

    
    def SetOwner(self, iOwner):
        super().SetOwner(iOwner)
        cl_msgcenter.AddAttentionFunc(self, iOwner, cl_msgcenter.MSG_WAR_WANDDISABLE, self.RemoveSelf, 'RemoveSelf')

    
    def RemoveSelf(self, oListener, oTarget, dMsgInfo):
        self.Remove('RemoveSelf')

    
    def OnPick(self, oHero, iPos, iPickType = PICK_TYPE_NORMAL):
        dInfo = self.m_DropInfo[iPos]
        oWand = oHero.m_WandCon.GetWandByID(dInfo['Item'])
        if oWand and oWand.m_Enable:
            self.Remove('Pick')
            oWand.TriggerPointPosActionComp(dInfo['TriggerPos'])



class CDiceSelectionPacketDrop(CDrop):
    m_SID = 5550
    m_Group = 0
    m_FightType = NWARRIOR_DROP_DICESELECTIONPACKET
    
    def Shape(self):
        return g_commondrop.get(self.m_SID, 0)

    
    def OnPickUp(self, oHero):
        pass

    
    def OnPick(self, oHero, iPos = 0, iPickType = PICK_TYPE_NORMAL):
        oDiceCon = oHero.m_DiceCon
        if oDiceCon:
            oDiceCon.RewardDiceSelectionPacket(oHero, self, 'SelectionPacket%s' % self.m_SID)
        else:
            self.Remove('Pick')

    
    def OnSetDropData(self, lstDropData):
        dInfo = lstDropData[0]
        self.m_SID = dInfo['SID']
        self.m_Quality = dInfo['Quality']

    
    def DropDesc(self):
        return []



class CDiceSpecialItemDrop(CDrop):
    m_SID = 5553
    m_Group = 0
    m_FightType = NWARRIOR_DROP_DICESPECIALITEM
    
    def Shape(self):
        return g_commondrop.get(self.m_SID, 0)

    
    def OnPickUp(self, oHero):
        pass

    
    def OnPick(self, oHero, iPos = 0, iPickType = PICK_TYPE_NORMAL):
        self.Remove('Pick')

    
    def OnSetDropData(self, lstDropData):
        pass

    
    def EachDropInfo(self, dInfo):
        lstAttrInfo = []
        iPropType = cl_netattr.PROP_DROPITEM_DICESPECIALITEM
        for sAttr in cl_netattr.INFO_OBJECT_INIT[iPropType]:
            (iIdx, _, iType, iLen, _) = cl_netattr.INFO_PROP_NAME[sAttr]
            if sAttr not in dInfo:
                continue
            iValue = dInfo[sAttr]
            lstAttrInfo.append((iIdx, iType, iLen, iValue))
        
        return {
            'Type': iPropType,
            'Attr': lstAttrInfo }



class CS7ModuleDrop(CDrop):
    m_SID = 5557
    m_FightType = NWARRIOR_DROP_S7MODULE
    
    def Shape(self):
        return g_commondrop.get(self.m_SID, 0)

    
    def OnPick(self, oHero, iPos = 0, iPickType = PICK_TYPE_NORMAL):
        oBackpackCon = oHero.m_BackpackCon
        if not oBackpackCon or iPos not in self.m_DropInfo:
            return None
        iNeedEquip = 0
        if iPickType == PICK_TYPE_NORMAL:
            sReason = 'NormalPick'
        elif iPickType == PICK_TYPE_EXTEND:
            sReason = 'ExtendPick'
            iNeedEquip = 1
        else:
            return None
        oModule = self.m_DropInfo.pop(iPos)
        self.Remove(sReason)
        oBackpackCon.AddS7Item(oModule, sReason = sReason)
        if iNeedEquip:
            iPlayer = oHero.m_PlayerID
            lstCanEquipPos = oBackpackCon.GetAllCanEquipPos(iCheckHasEquip = 1)
            if not lstCanEquipPos:
                cl_notify.SendCommonNotify(oHero.m_Game, [
                    iPlayer], 2553, { })
                return None
            if oBackpackCon.CheckModuleEquipNumMax(oModule.m_SID):
                cl_notify.SendCommonNotify(oHero.m_Game, [
                    iPlayer], 2523, { })
                return None
            tChoosePos = max(lstCanEquipPos, key = (lambda tPos: oBackpackCon.GetPosPoint(*tPos)))
            oBackpackCon.EquipS7Item(*tChoosePos, oModule.m_ID)
            cl_notify.SendCommonNotify(oHero.m_Game, [
                iPlayer], 2552, { })

    
    def EachDropInfo(self, oDropItem):
        lstAttrInfo = []
        iPropType = cl_propdata.PROP_DROPITEM_S7MODULE
        for sAttr in cl_propdata.INFO_OBJECT_INIT[iPropType]:
            (iIdx, _, iType, iLen, iMode) = cl_propdata.INFO_PROP_NAME[sAttr]
            iValue = cl_netattr.GetPropValue(oDropItem, sAttr, iMode)
            if iValue is None:
                continue
            lstAttrInfo.append((iIdx, iType, iLen, iValue))
        
        return {
            'Type': iPropType,
            'Attr': lstAttrInfo }



class CS7CrystalDrop(CDrop):
    m_SID = 5558
    m_FightType = NWARRIOR_DROP_S7CRYSTAL
    m_SubPickMsg = PICK_S7CRYSTAL
    
    def Shape(self):
        if self.m_DropInfo:
            oCrystal = self.m_DropInfo[0]
            if oCrystal.m_SID == CRYSTAL_RAWMATERIAL_SID:
                return g_commondrop.get(5559, 0)
        return g_commondrop.get(self.m_SID, 0)

    
    def MapSendPacket(self, dPlayer):
        super().MapSendPacket(dPlayer)
        oCrystal = self.m_DropInfo[0]
        seasonplaynet.GS2CS7CrystalDropInfo(self.m_ID, oCrystal, dPlayer)

    
    def OnPick(self, oHero, iPos = 0, iPickType = PICK_TYPE_NORMAL):
        oBackpackCon = oHero.m_BackpackCon
        if not oBackpackCon or iPos not in self.m_DropInfo:
            return None
        oCrystal = self.m_DropInfo[iPos]
        self.m_DropInfo.pop(iPos)
        sReason = 'NormalPick'
        self.Remove(sReason)
        oBackpackCon.AddS7Item(oCrystal, sReason = sReason)

    
    def EachDropInfo(self, oDropItem):
        lstAttrInfo = []
        iPropType = cl_propdata.PROP_DROPITEM_S7CRYSTAL
        for sAttr in cl_propdata.INFO_OBJECT_INIT[iPropType]:
            (iIdx, _, iType, iLen, iMode) = cl_propdata.INFO_PROP_NAME[sAttr]
            iValue = cl_netattr.GetPropValue(oDropItem, sAttr, iMode)
            if iValue is None:
                continue
            lstAttrInfo.append((iIdx, iType, iLen, iValue))
        
        return {
            'Type': iPropType,
            'Attr': lstAttrInfo }

    
    def VaildCanShare(self):
        if not self.m_DropInfo:
            return False
        oCrystal = self.m_DropInfo[0]
        if not oCrystal:
            return False
        if oCrystal.m_SID == CRYSTAL_RAWMATERIAL_SID:
            return False
        return True



class CSummonSoulDrop(CDrop):
    m_SID = 5560
    m_FightType = NWARRIOR_DROP_SUMMONSOUL
    
    def Shape(self):
        return g_commondrop.get(self.m_SID, 0)

    
    def OnPick(self, oHero, iPos = 0, iPickType = PICK_TYPE_NORMAL):
        self.Remove('Pick')
        dInfo = self.m_DropInfo[iPos]
        iAdd = dInfo['AddSoulValue']
        if not iAdd:
            return None
        iWeapon = dInfo['Item']
        oPerform = oHero.GetPerform(dInfo['Perform'], iWeapon)
        if oPerform:
            oPerform.AddPFBullet(iAdd)



class CS8ThirdItemDrop(CDrop):
    m_SID = 5561
    m_FightType = NWARRIOR_DROP_S8THIRDITEM
    
    def Shape(self):
        return g_commondrop.get(self.m_SID, 0)

    
    def MapSendPacket(self, dPlayer):
        super().MapSendPacket(dPlayer)
        oThirdItem = self.m_DropInfo.get(0, None)
        if not oThirdItem:
            return None
        seasonplaynet.GS2CThirdItemDropInfo(self.m_ID, oThirdItem, dPlayer)

    
    def OnPick(self, oHero, iPos = 0, iPickType = PICK_TYPE_NORMAL):
        oS8Con = oHero.m_S8Con
        if not oS8Con or iPos not in self.m_DropInfo:
            return None
        oThirdItem = self.m_DropInfo.pop(iPos, None)
        if not oThirdItem:
            return None
        sReason = 'NormalPick'
        self.Remove(sReason)
        oS8Con.AddThirdItem(oThirdItem, sReason)

    
    def EachDropInfo(self, oDropItem):
        lstAttrInfo = []
        iPropType = cl_propdata.PROP_DROPITEM_S8THITDPFITEM
        for sAttr in cl_propdata.INFO_OBJECT_INIT[iPropType]:
            (iIdx, _, iType, iLen, iMode) = cl_propdata.INFO_PROP_NAME[sAttr]
            iValue = cl_netattr.GetPropValue(oDropItem, sAttr, iMode)
            if iValue is None:
                continue
            lstAttrInfo.append((iIdx, iType, iLen, iValue))
        
        return {
            'Type': iPropType,
            'Attr': lstAttrInfo }



class CS8GemItemDrop(CDrop):
    m_SID = 5562
    m_FightType = NWARRIOR_DROP_S8GEMITEM
    
    def Shape(self):
        return g_commondrop.get(self.m_SID, 0)

    
    def OnPick(self, oHero, iPos = 0, iPickType = PICK_TYPE_NORMAL):
        oS8Con = oHero.m_S8Con
        if not oS8Con or iPos not in self.m_DropInfo:
            return None
        oGemItem = self.m_DropInfo.pop(iPos, None)
        if not oGemItem:
            return None
        sReason = 'NormalPick'
        self.Remove(sReason)
        oS8Con.AddGemItem(oGemItem, sReason)

    
    def EachDropInfo(self, oDropItem):
        lstAttrInfo = []
        iPropType = cl_propdata.PROP_DROPITEM_S8GEMITEM
        for sAttr in cl_propdata.INFO_OBJECT_INIT[iPropType]:
            (iIdx, _, iType, iLen, iMode) = cl_propdata.INFO_PROP_NAME[sAttr]
            iValue = cl_netattr.GetPropValue(oDropItem, sAttr, iMode)
            if iValue is None:
                continue
            lstAttrInfo.append((iIdx, iType, iLen, iValue))
        
        return {
            'Type': iPropType,
            'Attr': lstAttrInfo }


g_DropType = {
    NWARRIOR_DROP_S8GEMITEM: CS8GemItemDrop,
    NWARRIOR_DROP_S8THIRDITEM: CS8ThirdItemDrop,
    NWARRIOR_DROP_SUMMONSOUL: CSummonSoulDrop,
    NWARRIOR_DROP_S7CRYSTAL: CS7CrystalDrop,
    NWARRIOR_DROP_S7MODULE: CS7ModuleDrop,
    NWARRIOR_DROP_DICESPECIALITEM: CDiceSpecialItemDrop,
    NWARRIOR_DROP_DICESELECTIONPACKET: CDiceSelectionPacketDrop,
    NWARRIOR_DROP_COOKIES: CCookiesDrop,
    NWARRIOR_DROP_DICE: CDiceDrop,
    NWARRIOR_DROP_WANDCOMP: CWandCompDrop,
    NWARRIOR_DROP_MAGIC_WAND: CWandDrop,
    NWARRIOR_DROP_RELIC_MYSTERY: CMysteryRelicDrop,
    NWARRIOR_DROP_RELIC_BLANK: CBlankRelicDrop,
    NWARRIOR_DROP_PETEGG: CPetEggDrop,
    NWARRIOR_DROP_DEVICECOMP: CDeviceCompDrop,
    NWARRIOR_DROP_INKBEAD: CInkBeadDrop,
    NWARRIOR_DROP_MAGIC_POWER: CMagicPowerDrop,
    NWARRIOR_DROP_ENCHANTING_BULLET: CEnchantingBulletDrop,
    NWARRIOR_DROP_AXE: CAxeDrop,
    NWARRIOR_DROP_RAREITEM: CRareItemDrop,
    NWARRIOR_DROP_EXPERIENCE: CExperienceBallDrop,
    NWARRIOR_DROP_RELIFE: CRelifeDrop,
    NWARRIOR_DROP_DEMON: CDemonDrop,
    NWARRIOR_DROP_TREASURE_DEAD: CTreasureDeadDrop,
    NWARRIOR_DROP_KEYITEM: CKeyItemDrop,
    NWARRIOR_DROP_GSCASH: CGSCashDrop,
    NWARRIOR_DROP_KEY: CKeyDrop,
    NWARRIOR_DROP_TRIGGER: CTriggerDrop,
    NWARRIOR_DROP_RELIC_CURSE: CCurseRelicDrop,
    NWARRIOR_DROP_RELIC: CRelicDrop,
    NWARRIOR_DROP_CASH: CCashDrop,
    NWARRIOR_DROP_NODISTANCEBULLET: CNoDistanceBulletDrop,
    NWARRIOR_DROP_BULLET: CBulletDrop,
    NWARRIOR_DROP_EQUIP: CEquipDrop }
g_ItemType2DropType = {
    GEMITEM_MASK: NWARRIOR_DROP_S8GEMITEM,
    THIRDITEM_MASK: NWARRIOR_DROP_S8THIRDITEM,
    CRYSTAL_MASK: NWARRIOR_DROP_S7CRYSTAL,
    MODULE_MASK: NWARRIOR_DROP_S7MODULE,
    DICE_MASK: NWARRIOR_DROP_DICE,
    WAND_MASK: NWARRIOR_DROP_MAGIC_WAND }

def GetRealDropType(oGame, iType, lstPropData, iValid, iOwner):
    if iType == NWARRIOR_DROP_RELIC and lstPropData:
        iPerformSID = lstPropData[0]
        clsPerform = cl_perform.GetPerformModule(iPerformSID)
        if clsPerform.m_RelicType == RELIC_TYPE_CURSE and not iValid:
            oHero = oGame.GetObject(iOwner)
            if oHero and not oHero.m_RelicCon.GetPerform(iPerformSID):
                return NWARRIOR_DROP_RELIC_CURSE
        if clsPerform.m_RelicType == RELIC_TYPE_MYSTERY:
            return NWARRIOR_DROP_RELIC_MYSTERY
    return iType


def NewDrop(oGame, iType):
    iDropID = oGame.NewNPCID()
    if iType not in g_DropType:
        return None
    oDrop = g_DropType[iType](oGame, iDropID)
    return oDrop


def DropItem(oHero, oItem, bFly = False):
    iSource = oItem.m_Source
    dChecked = { }
    iItemType = oItem.Type()
    if iItemType & (EQUIP_MASK_DEF | EQUIP_MASK_WEAPON):
        lstDropData = [
            oItem]
        iDropType = NWARRIOR_DROP_EQUIP
        dChecked = oItem.UpdateCheckedPlayer({
            oHero.m_PlayerID: 1 })
    elif iItemType & KEYITEM_MASK:
        if not oItem.m_ID:
            lstDropData = [
                oItem]
        else:
            oTemp = cl_item.GetTemp(oItem.m_SID)
            oTemp.AddAmount(oItem.Amount(), 'Drop')
            oItem.Release()
            lstDropData = [
                oTemp]
        iDropType = NWARRIOR_DROP_KEYITEM
    elif iItemType & RAREITEM_MASK:
        lstDropData = [
            oItem]
        iDropType = NWARRIOR_DROP_RAREITEM
    elif iItemType in g_ItemType2DropType:
        lstDropData = [
            oItem]
        iDropType = g_ItemType2DropType[iItemType]
    else:
        return None
    iOwner = 0
    dStaticInfo = {
        'DropSource': iSource }
    if iDropType == NWARRIOR_DROP_EQUIP:
        iInjectOwner = oItem.Query('InjectOwner', 0)
        if iInjectOwner and iInjectOwner == oHero.m_PlayerID:
            iOwner = oHero.m_ID
    Drop(oHero, iDropType, lstDropData, bFly, dStaticInfo, iOwner, dPlayer = dChecked)


def DropPerform(oHero, iPerform, dStaticInfo, bFly = False, iShare = 1):
    clsPerform = cl_perform.GetPerformModule(iPerform)
    if not clsPerform:
        return None
    if clsPerform.m_PFType & PF_TYPE_RELIC == PF_TYPE_RELIC:
        iDropType = NWARRIOR_DROP_RELIC
        lstDropData = [
            iPerform]
    elif clsPerform.m_PFType == PF_TYPE_DEVICECOMP:
        iDropType = NWARRIOR_DROP_DEVICECOMP
        lstDropData = [
            iPerform]
    else:
        return None
    iOwner = 0
    if not iShare:
        iOwner = oHero.m_ID
    Drop(oHero, iDropType, lstDropData, bFly, dStaticInfo, iOwner)


def Drop(oHero, iDropType, lstDropData, bFly, dStaticInfo, iOwner = 0, dPlayer = None):
    oResMgr = oHero.m_Game.m_ResMgr
    dExtraInfo = { }
    if iDropType == NWARRIOR_DROP_RELIC:
        dExtraInfo['ValidRemoveCurseRelic'] = oHero.GetRemoveCurseRelicValid()
    if bFly:
        dExtraInfo['Abandoner'] = oHero.m_ID
        oDrop = oResMgr.CreateDrop(oHero.m_Scene, iDropType, oHero.GetPos(), lstDropData, dExtraInfo, dStaticInfo, iOwner)
        if iDropType not in (NWARRIOR_DROP_RELIC, NWARRIOR_DROP_MAGIC_WAND):
            oDrop.Delete('Abandoner')
        else:
            oDrop = oResMgr.CreateDrop(oHero.m_Scene, iDropType, oHero.GetPos(), lstDropData, dExtraInfo, dStaticInfo, iOwner)
    if None == NWARRIOR_DROP_EQUIP and dPlayer:
        cl_snetwar.GS2CRefreshItemChecked(oHero.m_Game, dPlayer, oDrop.m_ID)

