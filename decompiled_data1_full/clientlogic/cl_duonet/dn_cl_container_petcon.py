# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_duonet/dn_cl_container_petcon.pyc
# RelativePath: clientlogic/cl_duonet/dn_cl_container_petcon.pyc
# Source Generated with Decompyle++
# File: dn_cl_container_petcon.pyc (Python 3.6)

import cl_duonet.netfunc
import cl_container.petcon

def DN_GS2CAddPet(netdata):
    cl_duonet.netfunc.PacketPrepare(107)
    cl_duonet.netfunc.PacketAddI(1, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iPetID'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iPetSID'], 2)
    cl_duonet.netfunc.PacketAttrOffset(netdata['dOffset'])
    cl_duonet.netfunc.PacketAttr(netdata['dInfo'])
    cl_duonet.netfunc.PacketAddI(len(netdata['lstAbility']), 1)
    for iPerform in netdata['lstAbility']:
        cl_duonet.netfunc.PacketAddI(iPerform, 2)
    
    cl_duonet.netfunc.PacketAddI(len(netdata['lstSealedAbility']), 1)
    for iPerform in netdata['lstSealedAbility']:
        cl_duonet.netfunc.PacketAddI(iPerform, 2)
    
    cl_duonet.netfunc.PacketAddI(netdata['iIsNew'], 1)
    cl_duonet.netfunc.PacketAddI(netdata['iLock'], 1)
    cl_duonet.netfunc.DGamePacketSend(netdata['oGame'], netdata['pid'])


def DN_GS2CRemovePet(netdata):
    cl_duonet.netfunc.PacketPrepare(107)
    cl_duonet.netfunc.PacketAddI(2, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iPetID'], 4)
    cl_duonet.netfunc.DGamePacketSend(netdata['oGame'], netdata['pid'])


def DN_GS2CSetCurPet(netdata):
    cl_duonet.netfunc.PacketPrepare(107)
    cl_duonet.netfunc.PacketAddI(3, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iPetID'], 4)
    cl_duonet.netfunc.DGamePacketSend(netdata['oGame'], netdata['pid'])


def DN_GS2CRefreshPetEggNum(netdata):
    cl_duonet.netfunc.PacketPrepare(107)
    cl_duonet.netfunc.PacketAddI(4, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iType'], 1)
    cl_duonet.netfunc.PacketAddI(netdata['iCount'], 2)
    cl_duonet.netfunc.DGamePacketSend(netdata['oGame'], netdata['pid'])


def DN_GS2CSetHatchEggType(netdata):
    cl_duonet.netfunc.PacketPrepare(107)
    cl_duonet.netfunc.PacketAddI(5, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iType'], 1)
    cl_duonet.netfunc.DGamePacketSend(netdata['oGame'], netdata['pid'])


def DN_GS2CCompanionPet(netdata):
    cl_duonet.netfunc.PacketPrepare(107)
    cl_duonet.netfunc.PacketAddI(6, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iPetID'], 4)
    cl_duonet.netfunc.DGameSendToPlayers(netdata['oGame'], netdata['dPlayer'])


def DN_GS2CPetAbility(netdata):
    cl_duonet.netfunc.PacketPrepare(107)
    cl_duonet.netfunc.PacketAddI(7, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iPetID'], 4)
    cl_duonet.netfunc.PacketAddI(len(netdata['lstAbility']), 1)
    for iPerform in netdata['lstAbility']:
        cl_duonet.netfunc.PacketAddI(iPerform, 2)
    
    cl_duonet.netfunc.PacketAddI(len(netdata['lstSealedAbility']), 1)
    for iPerform in netdata['lstSealedAbility']:
        cl_duonet.netfunc.PacketAddI(iPerform, 2)
    
    cl_duonet.netfunc.DGameSendToPlayers(netdata['oGame'], netdata['dPlayer'])


def DN_GS2CPetOptionCost(netdata):
    cl_duonet.netfunc.PacketPrepare(107)
    cl_duonet.netfunc.PacketAddI(8, 1)
    cl_duonet.netfunc.PacketAddI(len(netdata['dOption']), 1)
    for iOption, iCost in netdata['dOption'].items():
        cl_duonet.netfunc.PacketAddI(iOption, 1)
        cl_duonet.netfunc.PacketAddI(iCost, 4)
    
    cl_duonet.netfunc.DGamePacketSend(netdata['oGame'], netdata['pid'])


def DN_GS2CFuseResult(netdata):
    cl_duonet.netfunc.PacketPrepare(107)
    cl_duonet.netfunc.PacketAddI(9, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iResetTimes'], 1)
    cl_duonet.netfunc.PacketAddI(netdata['iResetCost'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iMainPetPos'], 1)
    cl_duonet.netfunc.PacketAddI(len(netdata['lstPet']), 1)
    for pos, sid, dOffset, attr, lstAbility in netdata['lstPet']:
        cl_duonet.netfunc.PacketAddI(pos, 1)
        cl_duonet.netfunc.PacketAddI(sid, 4)
        cl_duonet.netfunc.PacketAttrOffset(dOffset)
        cl_duonet.netfunc.PacketAttr(attr)
        cl_duonet.netfunc.PacketAddI(len(lstAbility), 1)
        for iPerform in lstAbility:
            cl_duonet.netfunc.PacketAddI(iPerform, 2)
        
    
    cl_duonet.netfunc.DGamePacketSend(netdata['oGame'], netdata['pid'])


def DN_GS2CPetAbilityMarkList(netdata):
    cl_duonet.netfunc.PacketPrepare(107)
    cl_duonet.netfunc.PacketAddI(10, 1)
    cl_duonet.netfunc.PacketAddI(len(netdata['lstAbility']), 1)
    for iPerform in netdata['lstAbility']:
        cl_duonet.netfunc.PacketAddI(iPerform, 2)
    
    cl_duonet.netfunc.DGamePacketSend(netdata['oGame'], netdata['pid'])


def DN_GS2CPetSpellStart(netdata):
    cl_duonet.netfunc.PacketPrepare(107)
    cl_duonet.netfunc.PacketAddI(11, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iSpellSID'], 2)
    cl_duonet.netfunc.PacketSend(netdata['pid'])


def DN_GS2CPetSpell(netdata):
    cl_duonet.netfunc.PacketPrepare(107)
    cl_duonet.netfunc.PacketAddI(12, 1)
    cl_duonet.netfunc.PacketAddI(len(netdata['lstSpell']), 1)
    for iSpellSID in netdata['lstSpell']:
        cl_duonet.netfunc.PacketAddI(iSpellSID, 2)
    
    cl_duonet.netfunc.PacketSend(netdata['pid'])


def DN_GS2CUpdateSealedAbilityProgress(netdata):
    cl_duonet.netfunc.PacketPrepare(107)
    cl_duonet.netfunc.PacketAddI(13, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iPetID'], 4)
    cl_duonet.netfunc.PacketAddI(len(netdata['lstAbility']), 1)
    for iPerform, iProgress in netdata['lstAbility']:
        cl_duonet.netfunc.PacketAddI(iPerform, 2)
        cl_duonet.netfunc.PacketAddI(iProgress, 1)
    
    cl_duonet.netfunc.PacketSend(netdata['pid'])


def DN_GS2CUpdatePetLock(netdata):
    cl_duonet.netfunc.PacketPrepare(107)
    cl_duonet.netfunc.PacketAddI(14, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iPetID'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iLock'], 1)
    cl_duonet.netfunc.PacketSend(netdata['pid'])


def DN_C2GSSetCurPet(who):
    iPetID = cl_duonet.netfunc.UnpackInt(4)
    cl_container.petcon.C2GSSetCurPet(who, iPetID)


def DN_C2GSSetHatchEggType(who):
    iType = cl_duonet.netfunc.UnpackInt(1)
    cl_container.petcon.C2GSSetHatchEggType(who, iType)


def DN_C2GSUnsetNewPet(who):
    lstPetID = []
    for _ in range(cl_duonet.netfunc.UnpackInt(1)):
        iPetID = cl_duonet.netfunc.UnpackInt(4)
        lstPetID.append(iPetID)
    
    cl_container.petcon.C2GSUnsetNewPet(who, lstPetID)


def DN_C2GSOpenPetBag(who):
    cl_container.petcon.C2GSOpenPetBag(who)


def DN_C2GSPetBagOption(who):
    iOption = cl_duonet.netfunc.UnpackInt(1)
    lstResult = []
    for _ in range(cl_duonet.netfunc.UnpackInt(1)):
        iResult = cl_duonet.netfunc.UnpackInt(4)
        lstResult.append(iResult)
    
    cl_container.petcon.C2GSPetBagOption(who, iOption, lstResult)


def DN_C2GSMarkPetAbility(who):
    iPerform = cl_duonet.netfunc.UnpackInt(2)
    iMark = cl_duonet.netfunc.UnpackInt(1)
    iTemplateID = cl_duonet.netfunc.UnpackInt(2)
    cl_container.petcon.C2GSMarkPetAbility(who, iPerform, iMark, iTemplateID)


def DN_C2GSHatchEggNum(who):
    iNormalEggNum = cl_duonet.netfunc.UnpackInt(2)
    iRareEggNum = cl_duonet.netfunc.UnpackInt(2)
    cl_container.petcon.C2GSHatchEggNum(who, iNormalEggNum, iRareEggNum)


def DN_C2GSChangePetLock(who):
    iPetID = cl_duonet.netfunc.UnpackInt(4)
    iLock = cl_duonet.netfunc.UnpackInt(1)
    cl_container.petcon.C2GSChangePetLock(who, iPetID, iLock)

