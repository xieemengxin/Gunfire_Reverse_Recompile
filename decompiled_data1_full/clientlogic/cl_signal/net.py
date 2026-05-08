# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_signal/net.pyc
# RelativePath: clientlogic/cl_signal/net.pyc
# Source Generated with Decompyle++
# File: net.pyc (Python 3.6)

from cl_only import SendAlert
import cl_duonet.dn_cl_signal_net as duonet
import cl_msgcenter

def GetSignalMgr(who):
    oGame = who.m_Game
    oWarMgr = oGame.m_WarMgr
    oSignalMgr = oWarMgr.GetComponent('SignalElement')
    if not oSignalMgr:
        SendAlert('err', '战场 %s 没有配置信号组件' % oWarMgr.m_SID)
    return oSignalMgr


def GS2CAddSignal(oGame, lstPlayer, dSignalObjs):
    lstSceneSignal = []
    lstObjSignal = []
    lstTeamInfoSignal = []
    for oSignal in dSignalObjs.get('Scene', []):
        lstInfo = oSignal.GetDesc()
        lstSceneSignal.append(lstInfo)
    
    for oSignal in dSignalObjs.get('Obj', []):
        lstInfo = oSignal.GetDesc()
        lstObjSignal.append(lstInfo)
    
    for oSignal in dSignalObjs.get('TeamInfo', []):
        lstInfo = oSignal.GetDesc()
        lstTeamInfoSignal.append(lstInfo)
    
    netdata = {
        'oGame': oGame,
        'lstSceneSignal': lstSceneSignal,
        'lstObjSignal': lstObjSignal,
        'lstTeamInfoSignal': lstTeamInfoSignal,
        'dPlayer': lstPlayer }
    duonet.DN_GS2CAddSignal(netdata)


def GS2CAddSignalByInfo(oGame, lstPlayer, lstSceneSignal, lstObjSignal, lstTeamInfoSignal):
    netdata = {
        'oGame': oGame,
        'lstSceneSignal': lstSceneSignal,
        'lstObjSignal': lstObjSignal,
        'lstTeamInfoSignal': lstTeamInfoSignal,
        'dPlayer': lstPlayer }
    duonet.DN_GS2CAddSignal(netdata)


def GS2CDelSignal(oGame, lstPlayer, lstSignal):
    netdata = {
        'oGame': oGame,
        'dPlayer': lstPlayer,
        'lstSignal': lstSignal }
    duonet.DN_GS2CDelSignal(netdata)


def GS2CSignInfo(oGame, dPlayer, iHero, iSignID):
    netdata = {
        'oGame': oGame,
        'dPlayer': dPlayer,
        'iHero': iHero,
        'iSignID': iSignID }
    duonet.DN_GS2CSignInfo(netdata)


def GS2CPhotoInfo(oGame, dPlayer, iHero, iSignID, tPos, tRotate):
    netdata = {
        'oGame': oGame,
        'dPlayer': dPlayer,
        'iHero': iHero,
        'iSignID': iSignID,
        'tPos': tPos,
        'tRotate': tRotate }
    duonet.DN_GS2CPhotoInfo(netdata)


def C2GSAddSceneSignal(who, sid, tPos):
    oSignalMgr = GetSignalMgr(who)
    if not oSignalMgr:
        return None
    pid = who.m_PlayerID
    dParam = {
        'Adder': pid,
        'AdderName': who.Name(),
        'SID': sid,
        'Pos': tPos }
    if oSignalMgr.ValidAddSceneSignal(pid, dParam):
        oSignalMgr.AddSignal(pid, dParam)


def C2GSAddObjSignal(who, sid, iAttach):
    oSignalMgr = GetSignalMgr(who)
    if not oSignalMgr:
        return None
    pid = who.m_PlayerID
    dParam = {
        'Adder': pid,
        'AdderName': who.Name(),
        'SID': sid,
        'Attach': iAttach }
    if oSignalMgr.ValidAddObjSignal(pid, dParam):
        oSignalMgr.AddSignal(pid, dParam)


def C2GSAddNotifySignal(who, sid):
    oSignalMgr = GetSignalMgr(who)
    if not oSignalMgr:
        return None
    pid = who.m_PlayerID
    dParam = {
        'Adder': pid,
        'AdderName': who.Name(),
        'SID': sid }
    if sid in who.Query('Illus')['Emotion'].values():
        oSignalMgr.AddEmotionNotify(pid, dParam)


def C2GSDelSignal(who, iSignal):
    oSignalMgr = GetSignalMgr(who)
    if not oSignalMgr:
        return None
    oSignalMgr.TimeOutRemoveSignal()
    oSignalMgr.RemoveSignal(iSignal)
    oSignalMgr.SetCDRecord(who.m_ID)


def C2GSTeamInfoSignal(who, iSignalSID, iObjectSID, sOwner, iObjectType, iOwnerID):
    oSignalMgr = GetSignalMgr(who)
    if not oSignalMgr:
        return None
    oOwner = who.m_Game.GetObject(iOwnerID)
    if not oOwner:
        return None
    pid = who.m_PlayerID
    dParam = {
        'Adder': pid,
        'AdderName': who.Name(),
        'Owner': oOwner.m_PlayerID,
        'OwnerName': sOwner,
        'SID': iSignalSID,
        'Attach': iObjectSID,
        'Type': iObjectType }
    if oSignalMgr.ValidAddObjSignal(pid, dParam):
        oSignalMgr.AddSignal(pid, dParam)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_SIGNALITEM, who, dParam)


def C2GSAddPhotoSignal(who, sid, tPos, tRotate):
    oSignalMgr = GetSignalMgr(who)
    if not oSignalMgr:
        return None
    pid = who.m_PlayerID
    dParam = {
        'Adder': pid,
        'AdderName': who.Name(),
        'SID': sid,
        'Pos': tPos,
        'Rotate': tRotate }
    if sid in who.Query('Illus')['Emotion'].values() and oSignalMgr.ValidAddPhotoSignal(pid, dParam):
        oSignalMgr.AddPhotoNotify(pid, dParam)

