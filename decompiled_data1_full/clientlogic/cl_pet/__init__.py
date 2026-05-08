# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_pet/__init__.pyc
# RelativePath: clientlogic/cl_pet/__init__.pyc
# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.6)

from . import mobject, minipet, herosidepet
from cl_only import SendAlert, DeepCopy
from cl_commondefines import WARRIOR_PET_MINI, WARRIOR_PET_HEROSIDE
import cl_platformdata
g_PetClass = {
    WARRIOR_PET_HEROSIDE: herosidepet.CHeroSidePet,
    WARRIOR_PET_MINI: minipet.CMiniPet }

def CreatePet(oGame, oOwner, iPetSID, iPutWay, dAddData):
    clsData = cl_platformdata.GetPetClass(iPetSID)
    if not clsData:
        SendAlert('err', f'''妖灵{iPetSID}不存在''')
        return None
    nid = oGame.NewNPCID()
    if clsData.m_FightType in g_PetClass:
        oPet = g_PetClass[clsData.m_FightType](oGame, nid)
    else:
        oPet = mobject.CPet(oGame, nid)
    clsData.InitPetData(oPet)
    oPet.SetOwner(oOwner)
    oPet.InitPet(iPutWay, dAddData)
    oPet.OnCreated()
    return oPet


def LoadPet(oGame, oOwner, dData):
    if 'SID' not in dData:
        return None
    iPetSID = dData['SID']
    clsData = cl_platformdata.GetPetClass(iPetSID)
    if not clsData:
        SendAlert('err', f'''妖灵{iPetSID}不存在''')
        return None
    nid = oGame.NewNPCID()
    if clsData.m_FightType in g_PetClass:
        oPet = g_PetClass[clsData.m_FightType](oGame, nid)
    else:
        oPet = mobject.CPet(oGame, nid)
    clsData.InitPetData(oPet)
    oPet.SetOwner(oOwner)
    oPet.Load(dData)
    oPet.OnCreated()
    return oPet


def CreateCompanionPet(oGame, oOwner, dData):
    if 'SID' not in dData:
        return None
    iPetSID = dData['SID']
    clsData = cl_platformdata.GetPetClass(iPetSID)
    if not clsData:
        SendAlert('err', f'''妖灵{iPetSID}不存在''')
        return None
    nid = oGame.NewNPCID()
    if clsData.m_FightType in g_PetClass:
        oPet = g_PetClass[clsData.m_FightType](oGame, nid)
    else:
        oPet = mobject.CPet(oGame, nid)
    clsData.InitPetData(oPet)
    oPet.SetOwner(oOwner)
    oPet.LoadCompanionPet(dData)
    oPet.OnCreated()
    return oPet


def GetPutWayConfig(iPutWay):
    dReward = cl_platformdata.GetPetPutWayReward()
    if iPutWay in dReward:
        return DeepCopy(dReward[iPutWay])
    return { }


def GetPutWayPetWeight(iPutWay):
    dWeight = cl_platformdata.GetPetPutWayWeight()
    if iPutWay in dWeight:
        return dict(dWeight[iPutWay])
    return { }


def GetPetTypeWeight(iPutWay):
    dTypeWeight = cl_platformdata.GetPetTypeWeight()
    if iPutWay in dTypeWeight:
        return dict(dTypeWeight[iPutWay])
    return { }

