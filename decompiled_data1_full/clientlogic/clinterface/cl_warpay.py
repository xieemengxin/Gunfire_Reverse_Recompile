# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/clinterface/cl_warpay.pyc
# RelativePath: clientlogic/clinterface/cl_warpay.pyc
# Source Generated with Decompyle++
# File: cl_warpay.pyc (Python 3.6)

from cl_commondefines import WARPAY_ERR_REWARD, WARPAY_ERR_NOGOLD, WARPAY_ERR_NOGAME, WARPAY_SUCCESS
from cl_only import GetServerIndex, RaiseError, Functor
from cl_object.logging import WarpayLog
import cllib.lib_server as librpc
import cl_framegame
import cl_notify

class CWarPayManager(object):
    
    def __init__(self, oGame):
        self.m_Game = oGame
        self.m_Note = { }
        self.m_CurPay = { }

    
    def Release(self):
        self.m_Game = None

    
    def PayGold(self, iPlayer, iGold, sReason, RewardFunc):
        iGS = self.m_Game.m_WarMgr.GetPlayerLGS(iPlayer)
        if not iGS:
            return None
        if iPlayer in self.m_CurPay:
            return None
        self.m_CurPay[iPlayer] = 1
        resFunc = librpc.RPC_Functor(RES_PayGold, T_PayGold, self.m_Game.m_ID, iPlayer, iGS, iGold, sReason, RewardFunc)
        tRoomKey = (self.m_Game.m_ID, GetServerIndex())
        librpc.CallFunc(iGS, 'warpay.R_WarPayGold', [
            tRoomKey,
            iPlayer,
            iGold,
            sReason], resFunc, 20)

    
    def NotePay(self, iPlayer, iGold, sReason, sPayKey, iCode):
        if iPlayer not in self.m_Note:
            self.m_Note[iPlayer] = { }
        dPlayerNote = self.m_Note[iPlayer]
        if sPayKey in dPlayerNote and dPlayerNote[sPayKey]:
            RaiseError('WarPayErr Repeat %d %d' % (iPlayer, iCode))
        WarpayLog.Info('%d %d %d %s %s' % (iPlayer, iGold, iCode, sReason, sPayKey))
        self.m_Note[iPlayer][sPayKey] = iCode
        iGS = self.m_Game.m_WarMgr.GetPlayerLGS(iPlayer)
        if iCode != WARPAY_SUCCESS:
            librpc.CallFunc(iGS, 'warpay.R_WarPayRewardFail', [
                iPlayer,
                sPayKey,
                iCode], None)

    
    def GetPlayerPayNote(self, iPlayer):
        if iPlayer in self.m_Note:
            return self.m_Note[iPlayer]
        return { }



def RES_PayGold(iGame, iPlayer, iGS, iGold, sReason, RewardFunc, iResCode, sPayKey):
    oGame = cl_framegame.GetGame(iGame)
    if not oGame:
        librpc.CallFunc(iGS, 'warpay.R_WarPayRewardFail', [
            iPlayer,
            sPayKey,
            WARPAY_ERR_NOGAME], None)
        return None
    oGame.m_WarPayMgr.m_CurPay.pop(iPlayer)
    if iResCode != WARPAY_SUCCESS:
        if iResCode == WARPAY_ERR_NOGOLD:
            cl_notify.SendCommonNotify(oGame, [
                iPlayer], 7008, { })
            return None
        cl_notify.SendCommonNotify(oGame, [
            iPlayer], 7009, { })
        return None
    oGame.m_WarPayMgr.NotePay(iPlayer, iGold, sReason, sPayKey, WARPAY_SUCCESS)
    ret = RewardFunc(oGame, iPlayer)
    if ret is None:
        if isinstance(RewardFunc, Functor):
            sFuncName = RewardFunc.__func.__name__
        else:
            sFuncName = RewardFunc.__name__
        WarpayLog.Error('RewardFunc %s none return' % sFuncName)
    elif not ret:
        oGame.m_WarPayMgr.NotePay(iPlayer, iGold, sReason, sPayKey, WARPAY_ERR_REWARD)


def T_PayGold(iGame, iPlayer, iGS, iGold, sReason, RewardFunc):
    oGame = cl_framegame.GetGame(iGame)
    if not oGame:
        return None
    oGame.m_WarPayMgr.m_CurPay.pop(iPlayer)
    cl_notify.SendCommonNotify(oGame, [
        iPlayer], 7009, { })


def R_CheckGameActive(resFunc, iPlayer, iGame):
    oGame = cl_framegame.GetGame(iGame)
    if not oGame or iPlayer not in oGame.m_WarMgr.GetAllPlayer():
        iRes = 0
    else:
        iRes = 1
    resFunc(iRes)

