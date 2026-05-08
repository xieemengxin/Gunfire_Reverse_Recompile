# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_npc/tasknpccondition.pyc
# RelativePath: clientlogic/cl_npc/tasknpccondition.pyc
# Source Generated with Decompyle++
# File: tasknpccondition.pyc (Python 3.6)

from cl_item.defines import WEAPON_ACTION_INSC_ALL_NOR2RARE, WEAPON_ACTION_INSC_ONE_NOR2RARE, WEAPON_ACTION_INSC_ONE_NORRARE2EXCLU
from cl_cscommondef.cs_itemdef import EQUIP_TYPE_MAINWEAPON

def TaskCheckUpgradeInscription(oHero, oNpc, tArgs):
    iActionType = tArgs[0]
    lstWeapon = oHero.m_WieldCon.GetAllItemByType(EQUIP_TYPE_MAINWEAPON)
    iResult = 0
    for oWeapon in lstWeapon:
        oInscriptionCom = oWeapon.GetComponent('Inscription')
        if not oInscriptionCom:
            continue
        if oInscriptionCom.ValidUpgradeActionType(iActionType):
            iResult = 1
            break
    
    return iResult

g_TaskOptionCondition = {
    1011: {
        'Func': TaskCheckUpgradeInscription,
        'Args': (WEAPON_ACTION_INSC_ONE_NOR2RARE,) },
    1111: {
        'Func': TaskCheckUpgradeInscription,
        'Args': (WEAPON_ACTION_INSC_ALL_NOR2RARE,) },
    1211: {
        'Func': TaskCheckUpgradeInscription,
        'Args': (WEAPON_ACTION_INSC_ONE_NORRARE2EXCLU,) } }

def GetTaskOptionCondition():
    return g_TaskOptionCondition

