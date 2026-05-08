# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_build/net.pyc
# RelativePath: clientlogic/cl_build/net.pyc
# Source Generated with Decompyle++
# File: net.pyc (Python 3.6)

from cl_commondefines import WARRIOR_BUILD
import cl_duonet.dn_cl_build_net as buildnet

def GS2CBuildGateStatus(pid, iBuildID, iStatus):
    netData = {
        'iBuildID': iBuildID,
        'iStatus': iStatus,
        'pid': pid }
    buildnet.DN_GS2CBuildGateStatus(netData)


def GS2CBuildInteractState(pid, iBuild, iState):
    netData = {
        'iState': iState,
        'iBuild': iBuild,
        'pid': pid }
    buildnet.DN_GS2CBuildInteractState(netData)


def GS2CPillarInfo(oGame, iBuild, iStartFrame, dLayerInfo, dPlayer):
    lstLayer = []
    for iLayer, dLayer in dLayerInfo.items():
        fVelocity = dLayer['Velocity']
        lstVent = []
        for iVent, iVentID in dLayer['Vents'].items():
            lstVent.append((iVent, iVentID))
        
        lstLayer.append((iLayer, fVelocity, lstVent))
    
    netData = {
        'oGame': oGame,
        'iBuild': iBuild,
        'iStartFrame': iStartFrame,
        'dPlayer': dPlayer,
        'lstLayer': lstLayer }
    buildnet.DN_GS2CPillarInfo(netData)


def GS2CPlankMove(iBuild, iStartFrame, fSpeed, fAcceSpeed, tStart, tEnd, dPlayer):
    netData = {
        'iBuild': iBuild,
        'iStartFrame': iStartFrame,
        'fSpeed': fSpeed,
        'fAcceSpeed': fAcceSpeed,
        'tStart': tStart,
        'tEnd': tEnd,
        'dPlayer': dPlayer }
    buildnet.DN_GS2CPlankMove(netData)


def GS2CGeyserInfo(oGame, iBuild, tCenter, tHalfExt, tDirection, iDistance, fShowHight, iEnableFrame, iEnablePreTime, fDropSpeedPercent, dPlayer):
    netData = {
        'oGame': oGame,
        'iBuild': iBuild,
        'tCenter': tCenter,
        'tHalfExt': tHalfExt,
        'tDirection': tDirection,
        'iDistance': iDistance,
        'fShowHight': fShowHight,
        'iEnableFrame': iEnableFrame,
        'iEnablePreTime': iEnablePreTime,
        'fDropSpeedPercent': fDropSpeedPercent,
        'dPlayer': dPlayer }
    buildnet.DN_GS2CGeyserInfo(netData)


def GS2CBuildMove(iBuild, tStart, tEnd, iMoveTime, dPlayer):
    netData = {
        'iBuild': iBuild,
        'tStart': tStart,
        'tEnd': tEnd,
        'iMoveTime': iMoveTime,
        'dPlayer': dPlayer }
    buildnet.DN_GS2CBuildMove(netData)


def C2GSBuildInteract(oHero, iBuild):
    oBuild = oHero.m_Game.GetObject(iBuild)
    if not oBuild or oBuild.m_FightType & WARRIOR_BUILD != WARRIOR_BUILD:
        return None
    oBuild.Interact(oHero)


def C2GSBuildStopInteract(oHero, iBuild):
    oBuild = oHero.m_Game.GetObject(iBuild)
    if not oBuild:
        return None
    oBuild.StopInteract(oHero)

