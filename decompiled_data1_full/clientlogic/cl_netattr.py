# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_netattr.pyc
# RelativePath: clientlogic/cl_netattr.pyc
# Source Generated with Decompyle++
# File: cl_netattr.pyc (Python 3.6)

from cl_propdata import PROP_DROPITEM_DEMON, PROP_DROPITEM_MAINWEAPON, PROP_DROPITEM_RELIC, PROP_SHOOTPERFORM, PROP_PERFORM, PROP_FILLPERFORM, PROP_CAREERPERFORM, PROP_THROWPERFORM, MONSTER_PROP_INIT, INFO_PROP_NAME, INFO_OBJECT_INIT, PROP_ITEM, PROP_MAINWEAPON, BUILD_PROP_INIT, PROP_HERO, PROP_NONE, HERO_PROP_INIT, HERO_PROP_EXT, PC_SEND_SELF, BASIC_OBJECT_EXT, TYPE_INTD100, TYPE_LONGD100, BASIC_OBJECT_INIT, PROP_CLIENTACTIVEPERFORM, PROP_COMMONACTIVEPERFORM, PROP_DEVICEACTIVEPERFORM, PROP_PETACTIVEPERFORM, PROP_SUITACTIVEPERFORM, PROP_WANDCOMP, PROP_WATCHACTIVEPERFORM, PROP_DROPITEM_DICESPECIALITEM, PROP_PLANT, PROP_AIRFOLLOWEFFECT, PROP_S8THIRDACTIVEPERFORM
from cl_propdata import BASIC_PROP_NAME, PROP_BEACONSUMMON, QUERYATTR_FORECAST, OTHER_GET, QUERYATTR_NETGET, ATTRBASE_GET, QUERYATTR_GET, ATTR_GET, FUNC_GET, QUERY_GET, PROP_STONEBUILD, PROP_BUILD, PROP_EQUIPDROPS, PROP_DROPS, PROP_GOLDENCUP, PROP_CARNPC, PROP_NPC, PROP_SUMMON, PROP_MONSTER, BASIC_PROP_DICT, ITEM_BROADCAST_PROP, WEAPON_SHARE_PROP, CLASS_GET, PROP_SERVANT, SERVANT_PROP_INIT, SPECIALATTR_GET, PROP_DROPITEM_MAGICPOWER, PROP_RELIC, PROP_DEVICE, PROP_POISON_DEVICE, PROP_BARRIER_DEVICE, PROP_PET_SHOW, PET_PROP_INIT, PROP_PET, PROP_HOOKROPECUP, PROP_PET_FINISHWAR, INFO_OBJECT_FINISHWAR, PROP_DICE
from cl_commondefines import NWARRIOR_NPC_RAREGOLDENCUP, SCENEOBJ_TYPE, WARRIOR_TRAP_STONE, WARRIOR_BEACON, WARRIOR_BUILD, WARRIOR_HERO, WARRIOR_PERFORM, NWARRIOR_NPC_CAR, NWARRIOR_NPC, WARRIOR_SUMMON, WARRIOR_MONSTER, NWARRIOR_NPC_GOLDENCUP, NWARRIOR_NPC_LIMITGOLDENCUP, NWARRIOR_NPC_EXCHANGEGOLDENCUP, NWARRIOR_DROP_EQUIP, NWARRIOR_DROP, WARRIOR_SERVANT, WARRIOR_DEVICE, WARRIOR_DEVICE_POISON, WARRIOR_DEVICE_BARRIER, WARRIOR_PET, NWARRIOR_NPC_HOOKROPE, WARRIOR_PET_MINI, WARRIOR_PLANT, WARRIOR_SUMMON_AIRFOLLOWEFFECT
from cl_object.logging import OtherLog
import cl_item.defines as itemdef
import cl_cscommondef.cs_perform as performdef
import cl_duonet.dn_cl_netattr as attrnet
PACKET_PROP_INIT = 0
FIGHTTYPE_TO_PROP = {
    WARRIOR_SUMMON_AIRFOLLOWEFFECT: PROP_AIRFOLLOWEFFECT,
    WARRIOR_PLANT: PROP_PLANT,
    WARRIOR_PET: PROP_PET,
    NWARRIOR_NPC_EXCHANGEGOLDENCUP: PROP_GOLDENCUP,
    WARRIOR_DEVICE_BARRIER: PROP_BARRIER_DEVICE,
    WARRIOR_DEVICE_POISON: PROP_POISON_DEVICE,
    WARRIOR_DEVICE: PROP_DEVICE,
    WARRIOR_SERVANT: PROP_SERVANT,
    WARRIOR_TRAP_STONE: PROP_STONEBUILD,
    WARRIOR_BEACON: PROP_BEACONSUMMON,
    WARRIOR_BUILD: PROP_BUILD,
    NWARRIOR_DROP_EQUIP: PROP_EQUIPDROPS,
    NWARRIOR_DROP: PROP_DROPS,
    NWARRIOR_NPC_HOOKROPE: PROP_HOOKROPECUP,
    NWARRIOR_NPC_RAREGOLDENCUP: PROP_GOLDENCUP,
    NWARRIOR_NPC_LIMITGOLDENCUP: PROP_GOLDENCUP,
    NWARRIOR_NPC_GOLDENCUP: PROP_GOLDENCUP,
    NWARRIOR_NPC_CAR: PROP_CARNPC,
    NWARRIOR_NPC: PROP_NPC,
    WARRIOR_SUMMON: PROP_SUMMON,
    WARRIOR_MONSTER: PROP_MONSTER,
    WARRIOR_HERO: PROP_HERO }
FIGHTTYPE_TO_PROPFINISHWAR = {
    WARRIOR_PET_MINI: PROP_PET_FINISHWAR,
    WARRIOR_PET: PROP_PET_FINISHWAR }
PFTYPE_TO_PROP = {
    performdef.PF_TYPE_S8THIRDACTIVE: PROP_S8THIRDACTIVEPERFORM,
    performdef.PF_TYPE_WATCHACTIVE: PROP_WATCHACTIVEPERFORM,
    performdef.PF_TYPE_SUITACTIVE: PROP_SUITACTIVEPERFORM,
    performdef.PF_TYPE_PETACTIVE: PROP_PETACTIVEPERFORM,
    performdef.PF_TYPE_DEVICEACTIVE: PROP_DEVICEACTIVEPERFORM,
    performdef.PF_TYPE_COMMON: PROP_COMMONACTIVEPERFORM,
    performdef.PF_TYPE_TRIGGERCLIENT: PROP_CLIENTACTIVEPERFORM,
    performdef.PF_TYPE_FILLBULLET: PROP_FILLPERFORM,
    performdef.PF_TYPE_CAREERPF: PROP_CAREERPERFORM,
    performdef.PF_TYPE_THROW: PROP_THROWPERFORM,
    performdef.PF_TYPE_CHARGE: PROP_SHOOTPERFORM,
    performdef.PF_TYPE_CONSHOOT: PROP_SHOOTPERFORM,
    performdef.PF_TYPE_SHOOT: PROP_SHOOTPERFORM }

def GetPropType(iFightType):
    if iFightType in FIGHTTYPE_TO_PROP:
        return FIGHTTYPE_TO_PROP[iFightType]
    if iFightType & SCENEOBJ_TYPE in FIGHTTYPE_TO_PROP:
        return FIGHTTYPE_TO_PROP[iFightType & SCENEOBJ_TYPE]
    return PROP_NONE


def GetPropValue(obj, sAttr, iMode, oGame = None):
    if iMode == QUERY_GET:
        return obj.Query(sAttr)
    if iMode == ATTR_GET:
        return getattr(obj, 'm_%s' % sAttr)
    if iMode == FUNC_GET:
        func = getattr(obj, sAttr)
        return func()
    if iMode == QUERYATTR_GET:
        return obj.QueryAttr(sAttr)
    if iMode == ATTRBASE_GET:
        return obj.QueryAttrBase(sAttr)
    if iMode == QUERYATTR_NETGET:
        return obj.QueryAttrNet(sAttr)
    if iMode == OTHER_GET:
        return obj.CustomAttrValue(sAttr)
    if iMode == QUERYATTR_FORECAST:
        return obj.QueryAttrForecast(sAttr)
    if iMode == SPECIALATTR_GET:
        return obj.QueryAttrSpecial(sAttr)
    if iMode == CLASS_GET:
        if oGame:
            oWarMgr = oGame.m_WarMgr
            return oWarMgr.GetPropValue(sAttr, obj.m_SID)
        return []


def GS2CPropChange(obj, sAttr, iVal = None, lstPlayer = None):
    (iIdx, _, iType, iLen, iMode) = BASIC_PROP_NAME[sAttr]
    if iVal is None or iMode in (FUNC_GET, QUERYATTR_FORECAST):
        iVal = GetPropValue(obj, sAttr, iMode)
    if iVal is None:
        return None
    iPropType = obj.m_PropType
    if sAttr in BASIC_OBJECT_INIT[iPropType]:
        dPropInfo = {
            'Send': obj.m_PropChangeBCType,
            'Attr': [
                (iIdx, iType, iLen, iVal)] }
        if iType == TYPE_LONGD100 or iType == TYPE_INTD100:
            iVal = (iVal + 99) // 100
        elif iPropType in BASIC_OBJECT_EXT and sAttr in BASIC_OBJECT_EXT[iPropType]:
            dPropInfo = {
                'Send': PC_SEND_SELF,
                'Attr': [
                    (iIdx, iType, iLen, iVal)] }
        else:
            return None
    dPropInfo['Player'] = lstPlayer
    attrnet.DN_GS2CPropChange(obj.m_ID, dPropInfo, obj.m_Game, obj.m_Scene, obj.m_OwnerPlayerID)


def GS2CPetPropChange(obj, sAttr, iVal = None, lstPlayer = None):
    (iIdx, _, iType, iLen, iMode) = BASIC_PROP_NAME[sAttr]
    if iVal is None or iMode in (FUNC_GET, QUERYATTR_FORECAST):
        iVal = GetPropValue(obj, sAttr, iMode)
    if iVal is None:
        return None
    if sAttr in PET_PROP_INIT:
        dPropInfo = {
            'Send': obj.m_PropChangeBCType,
            'Attr': [
                (iIdx, iType, iLen, iVal)] }
        if iType == TYPE_LONGD100 or iType == TYPE_INTD100:
            iVal = (iVal + 99) // 100
        else:
            return None
    dPropInfo['Player'] = lstPlayer
    attrnet.DN_GS2CPetPropChange(obj.m_ID, dPropInfo, obj.m_Game, obj.m_Scene, obj.m_OwnerPlayerID)


def MakeHeroAddPacket(oHero, dPlayer):
    iHero = oHero.m_ID
    lstPropInfo = GetHeroBaseProp(oHero)
    (ix, iy, iz) = oHero.GetPixelPosition()
    (dx, dy, dz) = oHero.GetNetFacing()
    dPropInfo = {
        'Attr': lstPropInfo }
    attrnet.DN_MakeHeroAddPacket(iHero, oHero.m_FightType, ix, iy, iz, dx, dy, dz, dPropInfo, dPlayer)


def ExtHeroProp(oHero):
    lstPropInfo = []
    for sAttr in HERO_PROP_EXT:
        (iIdx, _, iType, iLen, iMode) = BASIC_PROP_NAME[sAttr]
        lstPropInfo.append((iIdx, iType, iLen, GetPropValue(oHero, sAttr, iMode)))
    
    dPropInfo = {
        'Attr': lstPropInfo }
    attrnet.DN_ExtHeroProp(oHero.m_ID, dPropInfo, oHero.m_PlayerID)


def GetHeroBaseProp(oHero):
    lstPropInfo = []
    for sAttr in HERO_PROP_INIT:
        (iIdx, _, iType, iLen, iMode) = BASIC_PROP_NAME[sAttr]
        lstPropInfo.append((iIdx, iType, iLen, GetPropValue(oHero, sAttr, iMode)))
    
    return lstPropInfo


def MakeDropAddPacket(oDrop, dPlayer):
    lstPropInfo = []
    iFightType = oDrop.m_FightType
    iPropType = GetPropType(iFightType)
    if iPropType == PROP_NONE:
        return None
    for sAttr in BASIC_OBJECT_INIT[iPropType]:
        (iIdx, _, iType, iLen, iMode) = BASIC_PROP_NAME[sAttr]
        iVal = GetPropValue(oDrop, sAttr, iMode)
        if iVal is None:
            continue
        lstPropInfo.append((iIdx, iType, iLen, iVal))
    
    iDrop = oDrop.m_ID
    (ix, iy, iz) = oDrop.GetPixelPosition()
    dPropInfo = {
        'Attr': lstPropInfo }
    lstDesc = oDrop.DropDesc()
    attrnet.DN_MakeDropAddPacket(iFightType, iDrop, ix, iy, iz, dPropInfo, lstDesc, dPlayer)


def MakeSummonAddPacket(oSummon, dPlayer):
    lstPropInfo = []
    iFightType = oSummon.m_FightType
    iPropType = GetPropType(iFightType)
    if iPropType == PROP_NONE:
        return None
    for sAttr in BASIC_OBJECT_INIT[iPropType]:
        (iIdx, _, iType, iLen, iMode) = BASIC_PROP_NAME[sAttr]
        lstPropInfo.append((iIdx, iType, iLen, GetPropValue(oSummon, sAttr, iMode)))
    
    iSummon = oSummon.m_ID
    (ix, iy, iz) = oSummon.GetPixelPosition()
    dParam = oSummon.m_ModelData.GetClientData()
    (sx, sy, sz) = dParam['Scale'] if 'Scale' in dParam else (100, 100, 100)
    (ax, ay, az) = dParam['Angle'] if 'Angle' in dParam else (0, 0, 0)
    dPropInfo = {
        'Attr': lstPropInfo }
    attrnet.DN_MakeSummonAddPacket(iFightType, iSummon, ix, iy, iz, sx, sy, sz, ax, ay, az, oSummon.m_ClientOwner, dPropInfo, oSummon.m_BodyPart, dPlayer)


def MakeBuildAddPacket(oBuild, dPlayer):
    lstPropInfo = []
    iFightType = oBuild.m_FightType
    iPropType = GetPropType(iFightType)
    if iPropType == PROP_NONE:
        return None
    for sAttr in BASIC_OBJECT_INIT[iPropType]:
        (iIdx, _, iType, iLen, iMode) = BASIC_PROP_NAME[sAttr]
        lstPropInfo.append((iIdx, iType, iLen, GetPropValue(oBuild, sAttr, iMode)))
    
    iArea = 0
    if oBuild.m_ClientGlobalArea:
        iArea = 99
    elif oBuild.m_LineIdx:
        oGame = oBuild.m_Game
        oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
        oLine = oLevelCtrl.GetLineNode(oBuild.m_LineIdx)
        iArea = oLine.m_Area
    (ix, iy, iz) = oBuild.GetPixelPosition()
    dParam = oBuild.m_ModelData.GetClientData()
    (sx, sy, sz) = dParam['Scale']
    (ax, ay, az) = dParam['Angle']
    iObstacle = oBuild.m_ID
    dPropInfo = {
        'Attr': lstPropInfo }
    attrnet.DN_MakeBuildAddPacket(iFightType, iObstacle, ix, iy, iz, sx, sy, sz, ax, ay, az, oBuild.m_Prefab, iArea, dPropInfo, dPlayer)


def MakeMonsterAddPacket(oMonster, dPlayer):
    lstPropInfo = []
    for sAttr in MONSTER_PROP_INIT:
        (iIdx, _, iType, iLen, iMode) = BASIC_PROP_NAME[sAttr]
        lstPropInfo.append((iIdx, iType, iLen, GetPropValue(oMonster, sAttr, iMode)))
    
    (ix, iy, iz) = oMonster.GetPixelPosition()
    (dx, dy, dz) = oMonster.GetNetFacing()
    iMonster = oMonster.m_ID
    dPropInfo = {
        'Attr': lstPropInfo }
    attrnet.DN_MakeMonsterAddPacket(oMonster.m_FightType, iMonster, ix, iy, iz, dx, dy, dz, dPropInfo, dPlayer)


def MakeServantAddPacket(oServant, dPlayer):
    lstPropInfo = []
    iPropType = GetPropType(oServant.m_FightType)
    if iPropType == PROP_NONE:
        return None
    for sAttr in BASIC_OBJECT_INIT[iPropType]:
        (iIdx, _, iType, iLen, iMode) = BASIC_PROP_NAME[sAttr]
        lstPropInfo.append((iIdx, iType, iLen, GetPropValue(oServant, sAttr, iMode)))
    
    (ix, iy, iz) = oServant.GetPixelPosition()
    (dx, dy, dz) = oServant.GetNetFacing()
    iServant = oServant.m_ID
    dPropInfo = {
        'Attr': lstPropInfo }
    attrnet.DN_MakeServantAddPacket(oServant.m_FightType, iServant, ix, iy, iz, dx, dy, dz, oServant.m_Owner, dPropInfo, dPlayer)


def MakeDeviceAddPacket(oDevice, dPlayer):
    iFightType = oDevice.m_FightType
    iPropType = GetPropType(iFightType)
    if iPropType == PROP_NONE:
        return None
    lstPropInfo = []
    for sAttr in BASIC_OBJECT_INIT[iPropType]:
        (iIdx, _, iType, iLen, iMode) = BASIC_PROP_NAME[sAttr]
        lstPropInfo.append((iIdx, iType, iLen, GetPropValue(oDevice, sAttr, iMode)))
    
    (ix, iy, iz) = oDevice.GetPixelPosition()
    (dx, dy, dz) = oDevice.GetNetFacing()
    dParam = oDevice.m_ModelData.GetClientData()
    (sx, sy, sz) = dParam['Scale'] if 'Scale' in dParam else (100, 100, 100)
    iDevice = oDevice.m_ID
    dPropInfo = {
        'Attr': lstPropInfo }
    attrnet.DN_MakeDeviceAddPacket(iFightType, iDevice, ix, iy, iz, dx, dy, dz, sx, sy, sz, dPropInfo, dPlayer)


def MapMonsterAndPart(oMonsterPart, dPlayer):
    attrnet.DN_MapMonsterAndPart(oMonsterPart.m_ID, oMonsterPart.m_Owner, dPlayer)


def MakeNpcAddPacket(oNpc, dPlayer):
    lstPropInfo = []
    iFightType = oNpc.m_FightType
    iPropType = GetPropType(iFightType)
    if iPropType == PROP_NONE:
        return None
    for sAttr in BASIC_OBJECT_INIT[iPropType]:
        (iIdx, _, iType, iLen, iMode) = BASIC_PROP_NAME[sAttr]
        lstPropInfo.append((iIdx, iType, iLen, GetPropValue(oNpc, sAttr, iMode)))
    
    (ix, iy, iz) = oNpc.GetPixelPosition()
    (dx, dy, dz) = oNpc.GetNetFacing()
    iNpc = oNpc.m_ID
    dPropInfo = {
        'Attr': lstPropInfo }
    attrnet.DN_MakeNpcAddPacket(iFightType, iNpc, ix, iy, iz, dx, dy, dz, dPropInfo, dPlayer)


def MakePetAddPacket(oPet, dPlayer):
    lstPropInfo = []
    for sAttr in PET_PROP_INIT:
        (iIdx, _, iType, iLen, iMode) = BASIC_PROP_NAME[sAttr]
        lstPropInfo.append((iIdx, iType, iLen, GetPropValue(oPet, sAttr, iMode)))
    
    (ix, iy, iz) = oPet.GetPixelPosition()
    (dx, dy, dz) = oPet.GetNetFacing()
    iPetID = oPet.m_ID
    dPropInfo = {
        'Attr': lstPropInfo }
    dOffset = oPet.GetAttrOffsetPacketInfo()
    lstAbility = oPet.Ability()
    attrnet.DN_MakePetAddPacket(oPet.m_FightType, iPetID, ix, iy, iz, dx, dy, dz, oPet.m_Owner, dPropInfo, dOffset, lstAbility, dPlayer)


def MakePetShowAddPacket(oPet):
    lstPropInfo = []
    lstPropInit = INFO_OBJECT_INIT[PROP_PET_SHOW]
    for sAttr in lstPropInit:
        (iIdx, _, iType, iLen, iMode) = BASIC_PROP_NAME[sAttr]
        iValue = GetPropValue(oPet, sAttr, iMode)
        if iValue is None:
            continue
        lstPropInfo.append((iIdx, iType, iLen, iValue))
    
    return {
        'Attr': lstPropInfo }


def MakeFinshWarShowAddPacket(obj):
    if obj.m_FightType not in FIGHTTYPE_TO_PROPFINISHWAR:
        return None
    lstPropInfo = []
    iShowProp = FIGHTTYPE_TO_PROPFINISHWAR[obj.m_FightType]
    lstPropFinshWar = INFO_OBJECT_FINISHWAR[iShowProp]
    for sAttr in lstPropFinshWar:
        (iIdx, _, iType, iLen, iMode) = BASIC_PROP_NAME[sAttr]
        iValue = GetPropValue(obj, sAttr, iMode)
        if iValue is None:
            continue
        lstPropInfo.append((iIdx, iType, iLen, iValue))
    
    return {
        'Attr': lstPropInfo }


def GetItemPropType(obj):
    if obj.m_Type & itemdef.EQUIP_TYPE_MAINWEAPON == itemdef.EQUIP_TYPE_MAINWEAPON:
        return PROP_MAINWEAPON
    if obj.m_Type & itemdef.EQUIP_TYPE_FUNDAMENTALWEAPON == itemdef.EQUIP_TYPE_FUNDAMENTALWEAPON:
        return PROP_MAINWEAPON
    return PROP_ITEM


def MakeItemAddPacket(oItem):
    lstPropInfo = []
    iPropType = GetItemPropType(oItem)
    lstPropInit = INFO_OBJECT_INIT[iPropType]
    for sAttr in lstPropInit:
        (iIdx, _, iType, iLen, iMode) = INFO_PROP_NAME[sAttr]
        iValue = GetPropValue(oItem, sAttr, iMode)
        if iValue is None:
            continue
        lstPropInfo.append((iIdx, iType, iLen, iValue))
    
    for sAttr in oItem.m_SpecialAttr:
        (iIdx, _, iType, iLen, _) = INFO_PROP_NAME[sAttr]
        iCurValue = oItem.GetSpecialAttr(sAttr)
        lstPropInfo.append((iIdx, iType, iLen, iCurValue))
    
    return {
        'Attr': lstPropInfo }


def GS2CItemPropChange(oItem, sAttr, iVal = 0, iPerform = 0, dPlayer = None):
    oGame = oItem.m_Game
    if not oGame:
        return None
    if iPerform:
        dPlayer = oGame.m_LinkMgr.m_OnlineLink
    if not dPlayer:
        if sAttr in ITEM_BROADCAST_PROP:
            dPlayer = oGame.GetRealPlayers()
        else:
            oOwner = oGame.GetObject(oItem.m_Owner)
            if not oOwner or not (oOwner.m_PlayerID):
                return None
            dPlayer = {
                oOwner.m_PlayerID: 1 }
    (iIdx, _, iType, iLen, iMode) = INFO_PROP_NAME[sAttr]
    if not iVal or iMode in (FUNC_GET, QUERYATTR_FORECAST):
        iVal = GetPropValue(oItem, sAttr, iMode)
    if iVal is None:
        return None
    lstPropInfo = []
    lstPropInfo.append((iIdx, iType, iLen, iVal))
    dPropInfo = {
        'Attr': lstPropInfo }
    attrnet.DN_GS2CItemPropChange(oItem.m_ID, dPropInfo, dPlayer)


def GetPerformPropType(obj):
    iPFType = obj.m_PFType
    if iPFType in PFTYPE_TO_PROP:
        return PFTYPE_TO_PROP[iPFType]
    return PROP_PERFORM


def MakePerformAddPacket(oPerform):
    lstPropInfo = []
    iPropType = GetPerformPropType(oPerform)
    lstPropInit = INFO_OBJECT_INIT[iPropType]
    for sAttr in lstPropInit:
        (iIdx, _, iType, iLen, iMode) = INFO_PROP_NAME[sAttr]
        iValue = GetPropValue(oPerform, sAttr, iMode)
        if iValue is None:
            continue
        lstPropInfo.append((iIdx, iType, iLen, iValue))
    
    return {
        'Attr': lstPropInfo }


def SyncWeaponProp(oWeapon, dPlayer):
    if not dPlayer:
        return None
    lstPropInfo = []
    for sAttr in WEAPON_SHARE_PROP:
        (iIdx, _, iType, iLen, iMode) = INFO_PROP_NAME[sAttr]
        iValue = GetPropValue(oWeapon, sAttr, iMode)
        if iValue is None:
            continue
        lstPropInfo.append((iIdx, iType, iLen, iValue))
    
    if not lstPropInfo:
        return None
    dPropInfo = {
        'Attr': lstPropInfo }
    attrnet.DN_GS2CItemPropChange(oWeapon.m_ID, dPropInfo, dPlayer)

