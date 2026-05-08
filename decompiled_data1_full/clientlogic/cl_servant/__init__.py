# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_servant/__init__.pyc
# RelativePath: clientlogic/cl_servant/__init__.pyc
# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.6)

from . import mobject, spare
from cl_commondefines import WARRIOR_MECH, WARRIOR_PLANT, WARRIOR_SPARE
g_ServantCls = {
    WARRIOR_SPARE: spare.CSpareServant,
    WARRIOR_PLANT: mobject.CPlantServant,
    WARRIOR_MECH: mobject.CMechServant }

def CreateServant(oGame, clsData, dAddData):
    if clsData.m_FightType not in g_ServantCls:
        return None
    nid = oGame.NewNPCID()
    clsServant = g_ServantCls[clsData.m_FightType]
    oServant = clsServant(oGame, nid)
    oServant.InitServant(clsData, dAddData)
    return oServant

