# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_npc/__init__.pyc
# RelativePath: clientlogic/cl_npc/__init__.pyc
# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.6)

from cl_commondefines import NWARRIOR_NPC_WEAPONSTORE, NWARRIOR_NPC_RAREGOLDENCUP, NWARRIOR_NPC_SHOP, NWARRIOR_NPC_TRANSFER, NWARRIOR_NPC_GSCASHSHOP, NWARRIOR_NPC_ITEMBOX, NWARRIOR_NPC_BENEDICTION, NWARRIOR_NPC_INITBOX, NWARRIOR_NPC_ROOMCHALLENGE, NWARRIOR_NPC_CANNON, NWARRIOR_NPC_REFRESH, NWARRIOR_NPC_CAR, NWARRIOR_NPC_LOCKEDBOX, NWARRIOR_NPC_BONFIRE, NWARRIOR_NPC_MAGICBOX, NWARRIOR_NPC_EVENT, NWARRIOR_NPC_SMITH, NWARRIOR_NPC_GOLDENCUP, NWARRIOR_NPC_PASSBOX, NWARRIOR_NPC_TRANSFERPOS, NWARRIOR_NPC_LIMITGOLDENCUP, NWARRIOR_NPC_EXCHANGEGOLDENCUP, NWARRIOR_NPC_CONNECTTRANSFER, NWARRIOR_NPC_RELIC, NWARRIOR_NPC_PHASESHOP, NWARRIOR_NPC_PHASESMITH, NWARRIOR_NPC_PHASEGOLDENCUP, NWARRIOR_NPC_TASKNPC, NWARRIOR_NPC_HOOKROPE, NWARRIOR_NPC_PETSHOP, NWARRIOR_NPC_RELICROLLBOX, NWARRIOR_NPC_RELICLOTTERY, NWARRIOR_NPC_WANDSHOP, NWARRIOR_NPC_DICESHOP, NWARRIOR_NPC_S7SHOP, NWARRIOR_NPC_S8SHOP
from . import mobject
from . import shopnpc
from . import leveltransfernpc
from . import passboxnpc
from . import goldencupnpc
from . import lockedboxnpc
from . import smithnpc
from . import magicbox
from . import eventnpc
from . import bonfirenpc
from . import carnpc
from . import refreshnpc
from . import npceventdata
from . import benedictionnpc
from . import transfernpc
from . import connecttransfernpc
from . import relicnpc
from . import weaponstorenpc
from . import tasknpc
from . import hookropenpc
from . import petshopnpc
from . import relicrollboxnpc
from . import reliclotterynpc
from . import wandshopnpc
from . import diceshopnpc
from . import s7shopnpc
from . import s8shopnpc
g_NpcClass = {
    NWARRIOR_NPC_S8SHOP: s8shopnpc.CS8ShopNpc,
    NWARRIOR_NPC_S7SHOP: s7shopnpc.CS7ShopNpc,
    NWARRIOR_NPC_DICESHOP: diceshopnpc.CDiceShopNpc,
    NWARRIOR_NPC_WANDSHOP: wandshopnpc.CWandShopNpc,
    NWARRIOR_NPC_RELICLOTTERY: reliclotterynpc.CRelicLotteryNpc,
    NWARRIOR_NPC_RELICROLLBOX: relicrollboxnpc.CRelicRollBoxNPC,
    NWARRIOR_NPC_PETSHOP: petshopnpc.CPetShopNpc,
    NWARRIOR_NPC_HOOKROPE: hookropenpc.CHookRopeNPC,
    NWARRIOR_NPC_EXCHANGEGOLDENCUP: goldencupnpc.CGoldenCupNpc,
    NWARRIOR_NPC_TASKNPC: tasknpc.CTaskNPC,
    NWARRIOR_NPC_PHASEGOLDENCUP: goldencupnpc.CPhaseGoldenCupNpc,
    NWARRIOR_NPC_PHASESMITH: smithnpc.CPhaseSmithNpc,
    NWARRIOR_NPC_PHASESHOP: shopnpc.CPhaseShopNpc,
    NWARRIOR_NPC_WEAPONSTORE: weaponstorenpc.CWeaponStoreNPC,
    NWARRIOR_NPC_RELIC: relicnpc.CRelicNPC,
    NWARRIOR_NPC_RAREGOLDENCUP: goldencupnpc.CRareGoldenCupNpc,
    NWARRIOR_NPC_CONNECTTRANSFER: connecttransfernpc.CConnectTransferNPC,
    NWARRIOR_NPC_LIMITGOLDENCUP: goldencupnpc.CLimitGoldenCupNpc,
    NWARRIOR_NPC_TRANSFERPOS: transfernpc.CTransferNPC,
    NWARRIOR_NPC_GSCASHSHOP: shopnpc.CGSCashShopNpc,
    NWARRIOR_NPC_BENEDICTION: benedictionnpc.CBenedictionNPC,
    NWARRIOR_NPC_ITEMBOX: magicbox.CItemBoxNPC,
    NWARRIOR_NPC_INITBOX: magicbox.CMagicBoxNPC,
    NWARRIOR_NPC_ROOMCHALLENGE: passboxnpc.CRoomChallengeNpc,
    NWARRIOR_NPC_CANNON: lockedboxnpc.CLockedBoxNpc,
    NWARRIOR_NPC_REFRESH: refreshnpc.CRefreshNPC,
    NWARRIOR_NPC_CAR: carnpc.CCarNPC,
    NWARRIOR_NPC_BONFIRE: bonfirenpc.CBonfireNpc,
    NWARRIOR_NPC_EVENT: eventnpc.CEventNPC,
    NWARRIOR_NPC_MAGICBOX: magicbox.CMagicBoxNPC,
    NWARRIOR_NPC_SMITH: smithnpc.CSmithNpc,
    NWARRIOR_NPC_GOLDENCUP: goldencupnpc.CGoldenCupNpc,
    NWARRIOR_NPC_LOCKEDBOX: lockedboxnpc.CLockedBoxNpc,
    NWARRIOR_NPC_TRANSFER: leveltransfernpc.CLevelTransferNPC,
    NWARRIOR_NPC_PASSBOX: passboxnpc.CLevelGoalBoxNpc,
    NWARRIOR_NPC_SHOP: shopnpc.CShopNpc }

def NewNPC(oGame, clsData, dAddData):
    iNpcID = oGame.NewNPCID()
    if clsData.m_FightType in g_NpcClass:
        oNpc = g_NpcClass[clsData.m_FightType](oGame, iNpcID)
    else:
        oNpc = mobject.CNPC(oGame, iNpcID)
    oNpc.InitCustomAttr(clsData, dAddData)
    return oNpc


def GetNpcEventData(iSID):
    if iSID in npceventdata.g_AllEvent:
        return npceventdata.g_AllEvent[iSID]

