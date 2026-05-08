# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/clinterface/cllib/lib_server.pyc
# RelativePath: clientlogic/clinterface/cllib/lib_server.pyc
# Source Generated with Decompyle++
# File: lib_server.pyc (Python 3.6)

import cllib.lib_flag
if cllib.lib_flag.g_IsLogicLayer:
    if cllib.lib_flag.g_IsStandalone or cllib.lib_flag.g_IsConsole or cllib.lib_flag.g_IsMobile:
        from rpc import CallOtherLogic
        from cli_player import GetPlayer
        
        def L2SPlayerLevelReport(iLGS, iGameID, pid, dInfo):
            CallOtherLogic(pid, 'roomsub.playerop.R_ServerWarLevelReport', (0, iGameID, pid, dInfo), None)

        
        def L2SPlayerWeaponStoreSave(iLGS, iGameID, pid, dInfo):
            CallOtherLogic(pid, 'roomsub.playerop.R_WeaponStoreSave', (0, iGameID, pid, dInfo), None)

        
        def L2SPlayerUnWarSetInfo(iLGS, iGameID, pid, dInfo):
            CallOtherLogic(pid, 'roomsub.playerop.R_UnWarSetInfo', (0, iGameID, pid, dInfo), None)

        
        def L2SPlayerWarEndBigData(iLGS, iGameID, pid, dInfo):
            CallOtherLogic(pid, 'roomsub.playerop.R_WarEndBigData', (0, iGameID, pid, dInfo), None)

        
        def L2SPlayerSurvivoUpGradeBigData(iLGS, iGameID, pid, dInfo):
            CallOtherLogic(pid, 'roomsub.playerop.R_SurvivoUpGradeBigData', (0, iGameID, pid, dInfo), None)

        
        def L2SPlayerPhaseEndBigData(iLGS, iGameID, pid, dInfo):
            CallOtherLogic(pid, 'roomsub.playerop.R_PhaseEndBigData', (0, iGameID, pid, dInfo), None)

        
        def L2SPlayerIntervalPhaseBigData(iLGS, iGameID, pid, dInfo):
            CallOtherLogic(pid, 'roomsub.playerop.R_IntervalPhaseBigData', (0, iGameID, pid, dInfo), None)

        
        def L2SDeviceChallengeBigData(iLGS, iGameID, pid, dInfo):
            CallOtherLogic(pid, 'roomsub.playerop.R_DeviceChallengeBigData', (0, iGameID, pid, dInfo), None)

        
        def L2SPlayerLevelBigData(iLGS, iGameID, pid, dInfo):
            CallOtherLogic(pid, 'roomsub.playerop.R_WarLevelBigData', (0, iGameID, pid, dInfo), None)

        
        def L2SPlayerReport(iLGS, iGameID, pid, dInfo):
            CallOtherLogic(pid, 'roomsub.playerop.R_ServerWarEndReport', (0, iGameID, pid, dInfo), None)

        
        def L2SPlayerBuyItemReport(iLGS, iGameID, pid, dInfo):
            CallOtherLogic(pid, 'roomsub.playerop.R_WarBuyItemReport', (0, iGameID, pid, dInfo), None)

        
        def L2SPlayerAchievement(iLGS, iGameID, pid, dInfo):
            CallOtherLogic(pid, 'roomsub.playerop.R_AchievementReport', (0, iGameID, pid, dInfo), None)

        
        def L2SPlayerSeasonTask(iLGS, iGameID, pid, dInfo):
            CallOtherLogic(pid, 'roomsub.playerop.R_SeasonTaskReport', (0, iGameID, pid, dInfo), None)

        
        def L2SPlayerUnlockProgress(iLGS, iGameID, pid, dInfo):
            CallOtherLogic(pid, 'roomsub.playerop.R_UnlockProgress', (0, iGameID, pid, dInfo), None)

        
        def L2SPlayerNewUnlockProgress(iLGS, iGameID, pid, dInfo):
            CallOtherLogic(pid, 'roomsub.playerop.R_NewUnlockProgress', (0, iGameID, pid, dInfo), None)

        
        def L2SPlayerRecord(iLGS, iGameID, pid, dInfo):
            CallOtherLogic(pid, 'roomsub.playerop.R_Record', (0, iGameID, pid, dInfo), None)

        
        def L2STempReport(iLGS, iGameID, pid, dInfo):
            CallOtherLogic(pid, 'roomsub.playerop.R_TempReport', (0, iGameID, pid, dInfo), None)

        
        def L2SChangeCash(iLGS, iGameID, pid, dInfo):
            CallOtherLogic(pid, 'roomsub.playerop.R_ChangeCash', (0, iGameID, pid, dInfo), None)

        
        def CtrlWarRelease(iGameID, sReason):
            import cl_interface
            cl_interface.ReleaseLogicGame(iGameID, sReason)

        
        def L2SPartyReward(iLGS, iGameID, pid, cbFunc):
            resfunc = RPC_Functor(cbFunc, None)
            SendSvrMsg(iLGS, 'playway.partyreward.R_GetPartyReward', (0, iGameID, pid), resfunc)

        
        def L2SMasterTransfer(iLGS, iGameID, pid, dInfo):
            CallOtherLogic(pid, 'roomsub.playerop.R_MasterTransfer', (0, iGameID, pid, dInfo), None)

        
        def L2SSendReloadFightRecord(iLGS, iGameID, pid, dInfo):
            CallOtherLogic(pid, 'roomsub.playerop.R_ReloadRecord', (0, iGameID, pid, dInfo), None)

        
        def L2SReSendCacheReport(iLGS, iGameID, pid, dInfo):
            CallOtherLogic(pid, 'reportcache.R_ReSendCacheReport', (0, iGameID, pid, dInfo), None)

        
        def L2SReSendSeasonInfo(iLGS, iGameID, pid, dInfo):
            CallOtherLogic(pid, 'roomsub.playerop.R_ReSendSeasonInfo', (0, iGameID, pid, dInfo), None)

        
        def WarEnd(iGameID, lstPlayer):
            pass

        
        def LogicKickOut(iGameID, pid, iNowDisconnect):
            who = GetPlayer(pid)
            if who:
                iLeaveGame = 1
                who.KickOut(iGameID, iLeaveGame, iNowDisconnect)

        
        def L2SRealDieBigData(iLGS, iGameID, pid, dInfo):
            CallOtherLogic(pid, 'roomsub.playerop.R_RealDieBigData', (0, iGameID, pid, dInfo), None)

    elif cllib.lib_flag.g_IsTradition:
        from cl_only import Functor
        from clclient.clc_rpc import SendSvrMsg, CallFunc
        from cllib.lib_rpc import RPC_Functor
        from cli_player import GetPlayer
        
        def L2SPlayerLevelReport(iLGS, iGameID, pid, dInfo):
            dPacket = {
                'StartFunc': Functor(PacketSendWarp, iLGS, 'roomsub.playerop.R_LogicWarLevelReport', (0, iGameID, pid), None),
                'LGS': iLGS,
                'pid': pid,
                'Data': dInfo }
            GetPlayer(pid).m_PacketSender.AddPacket(dPacket)

        
        def L2SPlayerWeaponStoreSave(iLGS, iGameID, pid, dInfo):
            dPacket = {
                'StartFunc': Functor(PacketSendWarp, iLGS, 'roomsub.playerop.R_WeaponStoreSave', (0, iGameID, pid), None),
                'LGS': iLGS,
                'pid': pid,
                'Data': dInfo }
            GetPlayer(pid).m_PacketSender.AddPacket(dPacket)

        
        def L2SPlayerUnWarSetInfo(iLGS, iGameID, pid, dInfo):
            dPacket = {
                'StartFunc': Functor(PacketSendWarp, iLGS, 'roomsub.playerop.R_UnWarSetInfo', (0, iGameID, pid), None),
                'LGS': iLGS,
                'pid': pid,
                'Data': dInfo }
            GetPlayer(pid).m_PacketSender.AddPacket(dPacket)

        
        def L2SPlayerWarEndBigData(iLGS, iGameID, pid, dInfo):
            dPacket = {
                'StartFunc': Functor(PacketSendWarp, iLGS, 'roomsub.playerop.R_LogicWarEndBigData', (0, iGameID, pid), None),
                'LGS': iLGS,
                'pid': pid,
                'Data': dInfo }
            GetPlayer(pid).m_PacketSender.AddPacket(dPacket)

        
        def L2SPlayerSurvivoUpGradeBigData(iLGS, iGameID, pid, dInfo):
            pass

        
        def L2SPlayerPhaseEndBigData(iLGS, iGameID, pid, dInfo):
            pass

        
        def L2SPlayerIntervalPhaseBigData(iLGS, iGameID, pid, dInfo):
            pass

        
        def L2SDeviceChallengeBigData(iLGS, iGameID, pid, dInfo):
            pass

        
        def L2SPlayerLevelBigData(iLGS, iGameID, pid, dInfo):
            dPacket = {
                'StartFunc': Functor(PacketSendWarp, iLGS, 'roomsub.playerop.R_LogicWarLevelBigData', (0, iGameID, pid), None),
                'LGS': iLGS,
                'pid': pid,
                'Data': dInfo }
            GetPlayer(pid).m_PacketSender.AddPacket(dPacket)

        
        def L2SPlayerReport(iLGS, iGameID, pid, dInfo):
            dPacket = {
                'StartFunc': Functor(PacketSendWarp, iLGS, 'roomsub.playerop.R_LogicWarEndReport', (0, iGameID, pid), None),
                'LGS': iLGS,
                'pid': pid,
                'Data': dInfo }
            GetPlayer(pid).m_PacketSender.AddPacket(dPacket)

        
        def PacketSendWarp(iLGS, sFunc, lstArgs, resfunc, sKey, iPacketID):
            lstArgs = list(lstArgs)
            lstArgs.append(sKey)
            lstArgs.append(iPacketID)
            SendSvrMsg(iLGS, sFunc, lstArgs, resfunc)

        
        def L2SPacketContent(iLGS, pid, sKey, iPacketID, sData):
            SendSvrMsg(iLGS, 'packetreceiver.R_PacketContent', (pid, sKey, iPacketID, sData), None)

        
        def L2SPacketEnd(iLGS, pid, sKey, iPacketID):
            SendSvrMsg(iLGS, 'packetreceiver.R_PacketEnd', (pid, sKey, iPacketID), RPC_Functor(Res_PacketEnd, None, pid, sKey, iPacketID))

        
        def Res_PacketEnd(pid, sKey, iPacketID):
            GetPlayer(pid).m_PacketSender.ResPacketEnd(sKey, iPacketID)

        
        def L2SPlayerBuyItemReport(iLGS, iGameID, pid, dInfo):
            SendSvrMsg(iLGS, 'roomsub.playerop.R_WarBuyItemReport', (0, iGameID, pid, dInfo), None)

        
        def L2SPlayerAchievement(iLGS, iGameID, pid, dInfo):
            SendSvrMsg(iLGS, 'roomsub.playerop.R_AchievementReport', (0, iGameID, pid, dInfo), None)

        
        def L2SPlayerSeasonTask(iLGS, iGameID, pid, dInfo):
            SendSvrMsg(iLGS, 'roomsub.playerop.R_SeasonTaskReport', (0, iGameID, pid, dInfo), None)

        
        def L2SPlayerUnlockProgress(iLGS, iGameID, pid, dInfo):
            SendSvrMsg(iLGS, 'roomsub.playerop.R_UnlockProgress', (0, iGameID, pid, dInfo), None)

        
        def L2SPlayerNewUnlockProgress(iLGS, iGameID, pid, dInfo):
            SendSvrMsg(iLGS, 'roomsub.playerop.R_NewUnlockProgress', (0, iGameID, pid, dInfo), None)

        
        def L2SPlayerRecord(iLGS, iGameID, pid, dInfo):
            dPacket = {
                'StartFunc': Functor(PacketSendWarp, iLGS, 'roomsub.playerop.R_Record', (0, iGameID, pid), None),
                'LGS': iLGS,
                'pid': pid,
                'Data': dInfo }
            GetPlayer(pid).m_PacketSender.AddPacket(dPacket)

        
        def L2STempReport(iLGS, iGameID, pid, dInfo):
            pass

        
        def L2SChangeCash(iLGS, iGameID, pid, dInfo):
            pass

        
        def CtrlWarRelease(iGameID, sReason):
            import cl_interface
            cl_interface.ReleaseLogicGame(iGameID, sReason)

        
        def L2SPartyReward(iLGS, iGameID, pid, cbFunc):
            resfunc = RPC_Functor(cbFunc, None)
            SendSvrMsg(iLGS, 'playway.partyreward.R_GetPartyReward', (0, iGameID, pid), resfunc)

        
        def L2SReSendSeasonInfo(iLGS, iGameID, pid, dInfo):
            pass

        
        def WarEnd(iGameID, lstPlayer):
            pass

        
        def LogicKickOut(iGameID, pid, iNowDisconnect):
            who = GetPlayer(pid)
            if who:
                iLeaveGame = 1
                who.KickOut(iGameID, iLeaveGame, iNowDisconnect)

        
        def L2SRealDieBigData(iLGS, iGameID, pid, dInfo):
            pass

    else:
        raise Exception('unknown platform flag.')
if cllib.lib_flag.g_IsMobile:
    import servicefight.rpccli
    import cli_player
    from cl_only import GetServerIndex, GetServerNum
    from rpc import RPC_Functor
    
    def L2SPlayerLevelReport(iLGS, iGameID, pid, dInfo):
        who = cli_player.GetPlayer(pid, iGameID)
        if who:
            pid = who.m_ID
            servicefight.rpccli.CallClientLogic(pid, 'roomsub.playerop.R_ServerWarLevelReport', (GetServerIndex(), iGameID, pid, dInfo), None)

    
    def L2SPlayerWeaponStoreSave(iLGS, iGameID, pid, dInfo):
        who = cli_player.GetPlayer(pid, iGameID)
        if who:
            pid = who.m_ID
            servicefight.rpccli.CallClientLogic(pid, 'roomsub.playerop.R_WeaponStoreSave', (GetServerIndex(), iGameID, pid, dInfo), None)

    
    def L2SPlayerUnWarSetInfo(iLGS, iGameID, pid, dInfo):
        who = cli_player.GetPlayer(pid, iGameID)
        if who:
            pid = who.m_ID
            servicefight.rpccli.CallClientLogic(pid, 'roomsub.playerop.R_UnWarSetInfo', (GetServerIndex(), iGameID, pid, dInfo), None)

    
    def L2SPlayerWarEndBigData(iLGS, iGameID, pid, dInfo):
        who = cli_player.GetPlayer(pid, iGameID)
        if who:
            pid = who.m_ID
            dInfo['CombatServer'] = GetServerNum()
            servicefight.rpccli.CallClientLogic(pid, 'roomsub.playerop.R_WarEndBigData', (GetServerIndex(), iGameID, pid, dInfo), None)

    
    def L2SPlayerSurvivoUpGradeBigData(iLGS, iGameID, pid, dInfo):
        who = cli_player.GetPlayer(pid, iGameID)
        if who:
            pid = who.m_ID
            dInfo['CombatServer'] = GetServerNum()
            servicefight.rpccli.CallClientLogic(pid, 'roomsub.playerop.R_SurvivoUpGradeBigData', (GetServerIndex(), iGameID, pid, dInfo), None)

    
    def L2SPlayerPhaseEndBigData(iLGS, iGameID, pid, dInfo):
        who = cli_player.GetPlayer(pid, iGameID)
        if who:
            pid = who.m_ID
            dInfo['CombatServer'] = GetServerNum()
            servicefight.rpccli.CallClientLogic(pid, 'roomsub.playerop.R_PhaseEndBigData', (GetServerIndex(), iGameID, pid, dInfo), None)

    
    def L2SPlayerIntervalPhaseBigData(iLGS, iGameID, pid, dInfo):
        who = cli_player.GetPlayer(pid, iGameID)
        if who:
            pid = who.m_ID
            dInfo['CombatServer'] = GetServerNum()
            servicefight.rpccli.CallClientLogic(pid, 'roomsub.playerop.R_IntervalPhaseBigData', (GetServerIndex(), iGameID, pid, dInfo), None)

    
    def L2SDeviceChallengeBigData(iLGS, iGameID, pid, dInfo):
        who = cli_player.GetPlayer(pid, iGameID)
        if who:
            pid = who.m_ID
            servicefight.rpccli.CallClientLogic(pid, 'roomsub.playerop.R_DeviceChallengeBigData', (GetServerIndex(), iGameID, pid, dInfo), None)

    
    def L2SPlayerLevelBigData(iLGS, iGameID, pid, dInfo):
        who = cli_player.GetPlayer(pid, iGameID)
        if who:
            pid = who.m_ID
            servicefight.rpccli.CallClientLogic(pid, 'roomsub.playerop.R_WarLevelBigData', (GetServerIndex(), iGameID, pid, dInfo), None)

    
    def L2SPlayerReport(iLGS, iGameID, pid, dInfo):
        who = cli_player.GetPlayer(pid, iGameID)
        if who:
            pid = who.m_ID
            resfunc = RPC_Functor(RES_L2SPlayerReport, T_L2SPlayerReport, iGameID, pid)
            servicefight.rpccli.CallClientLogic(pid, 'roomsub.playerop.R_ServerWarEndReport', (GetServerIndex(), iGameID, pid, dInfo), resfunc)

    
    def RES_L2SPlayerReport(iGameID, pid):
        who = cli_player.GetPlayer(pid, iGameID)
        if who:
            who.KickOut(iGameID, 1, 0, 'reportok')

    
    def T_L2SPlayerReport(iGameID, pid):
        who = cli_player.GetPlayer(pid, iGameID)
        if who:
            who.KickOut(iGameID, 1, 0, 'reporttimeout')

    
    def L2SPlayerBuyItemReport(iLGS, iGameID, pid, dInfo):
        who = cli_player.GetPlayer(pid, iGameID)
        if who:
            pid = who.m_ID
            servicefight.rpccli.CallClientLogic(pid, 'roomsub.playerop.R_WarBuyItemReport', (GetServerIndex(), iGameID, pid, dInfo), None)

    
    def L2SPlayerAchievement(iLGS, iGameID, pid, dInfo):
        who = cli_player.GetPlayer(pid, iGameID)
        if who:
            pid = who.m_ID
            servicefight.rpccli.CallClientLogic(pid, 'roomsub.playerop.R_AchievementReport', (GetServerIndex(), iGameID, pid, dInfo), None)

    
    def L2SPlayerSeasonTask(iLGS, iGameID, pid, dInfo):
        who = cli_player.GetPlayer(pid, iGameID)
        if who:
            pid = who.m_ID
            servicefight.rpccli.CallClientLogic(pid, 'roomsub.playerop.R_SeasonTaskReport', (GetServerIndex(), iGameID, pid, dInfo), None)

    
    def L2SPlayerUnlockProgress(iLGS, iGameID, pid, dInfo):
        who = cli_player.GetPlayer(pid, iGameID)
        if who:
            pid = who.m_ID
            servicefight.rpccli.CallClientLogic(pid, 'roomsub.playerop.R_UnlockProgress', (GetServerIndex(), iGameID, pid, dInfo), None)

    
    def L2SPlayerNewUnlockProgress(iLGS, iGameID, pid, dInfo):
        who = cli_player.GetPlayer(pid, iGameID)
        if who:
            pid = who.m_ID
            servicefight.rpccli.CallClientLogic(pid, 'roomsub.playerop.R_NewUnlockProgress', (GetServerIndex(), iGameID, pid, dInfo), None)

    
    def L2SPlayerRecord(iLGS, iGameID, pid, dInfo):
        who = cli_player.GetPlayer(pid, iGameID)
        if who:
            pid = who.m_ID
            servicefight.rpccli.CallClientLogic(pid, 'roomsub.playerop.R_Record', (GetServerIndex(), iGameID, pid, dInfo), None)

    
    def L2STempReport(iLGS, iGameID, pid, dInfo):
        pass

    
    def L2SChangeCash(iLGS, iGameID, pid, dInfo):
        pass

    
    def CtrlWarRelease(iGameID, sReason):
        import logicctrl
        logicctrl.WarRelease(iGameID, sReason)

    
    def L2SPartyReward(iLGS, iGameID, pid, cbFunc):
        who = cli_player.GetPlayer(pid, iGameID)
        if who:
            pid = who.m_ID
            resfunc = RPC_Functor(cbFunc, None)
            servicefight.rpccli.CallClientLogic(pid, 'playway.partyreward.R_GetPartyReward', (GetServerIndex(), iGameID, pid), resfunc)

    
    def L2SReSendSeasonInfo(iLGS, iGameID, pid, dInfo):
        who = cli_player.GetPlayer(pid, iGameID)
        if who:
            pid = who.m_ID
            servicefight.rpccli.CallClientLogic(pid, 'roomsub.playerop.R_ReSendSeasonInfo', (GetServerIndex(), iGameID, pid, dInfo), None)

    
    def WarEnd(iGameID, lstPlayer):
        for pid in lstPlayer:
            who = cli_player.GetPlayer(pid, iGameID)
            if who:
                who.SetOverStatus(iGameID)
        

    
    def LogicKickOut(iGameID, pid, iNowDisconnect):
        pass

    
    def L2SRealDieBigData(iLGS, iGameID, pid, dInfo):
        pass

elif cllib.lib_flag.g_IsPCRunFight:
    from only import RPC_Functor
    from cl_only import GetServerIndex
    import servicefight.fightlogic.rpccli as rpccli
    import cli_player
    
    def L2SPlayerLevelReport(iLGS, iGameID, pid, dInfo):
        who = cli_player.GetPlayer(pid, iGameID)
        if who:
            pid = who.m_ID
            iAccount = who.m_AccountID
            rpccli.CallClientLogic(pid, 'roomsub.playerop.R_ServerWarLevelReport', (GetServerIndex(), iGameID, iAccount, dInfo), None)

    
    def L2SPlayerWeaponStoreSave(iLGS, iGameID, pid, dInfo):
        who = cli_player.GetPlayer(pid, iGameID)
        if who:
            pid = who.m_ID
            iAccount = who.m_AccountID
            rpccli.CallClientLogic(pid, 'roomsub.playerop.R_WeaponStoreSave', (GetServerIndex(), iGameID, iAccount, dInfo), None)

    
    def L2SPlayerUnWarSetInfo(iLGS, iGameID, pid, dInfo):
        who = cli_player.GetPlayer(pid, iGameID)
        if who:
            pid = who.m_ID
            iAccount = who.m_AccountID
            rpccli.CallClientLogic(pid, 'roomsub.playerop.R_UnWarSetInfo', (GetServerIndex(), iGameID, iAccount, dInfo), None)

    
    def L2SPlayerWarEndBigData(iLGS, iGameID, pid, dInfo):
        who = cli_player.GetPlayer(pid, iGameID)
        if who:
            pid = who.m_ID
            iAccount = who.m_AccountID
            rpccli.CallClientLogic(pid, 'roomsub.playerop.R_WarEndBigData', (GetServerIndex(), iGameID, iAccount, dInfo), None)

    
    def L2SPlayerSurvivoUpGradeBigData(iLGS, iGameID, pid, dInfo):
        who = cli_player.GetPlayer(pid, iGameID)
        if who:
            pid = who.m_ID
            iAccount = who.m_AccountID
            rpccli.CallClientLogic(pid, 'roomsub.playerop.R_SurvivoUpGradeBigData', (GetServerIndex(), iGameID, iAccount, dInfo), None)

    
    def L2SPlayerPhaseEndBigData(iLGS, iGameID, pid, dInfo):
        who = cli_player.GetPlayer(pid, iGameID)
        if who:
            pid = who.m_ID
            iAccount = who.m_AccountID
            rpccli.CallClientLogic(pid, 'roomsub.playerop.R_PhaseEndBigData', (GetServerIndex(), iGameID, iAccount, dInfo), None)

    
    def L2SPlayerIntervalPhaseBigData(iLGS, iGameID, pid, dInfo):
        who = cli_player.GetPlayer(pid, iGameID)
        if who:
            pid = who.m_ID
            iAccount = who.m_AccountID
            rpccli.CallClientLogic(pid, 'roomsub.playerop.R_IntervalPhaseBigData', (GetServerIndex(), iGameID, iAccount, dInfo), None)

    
    def L2SDeviceChallengeBigData(iLGS, iGameID, pid, dInfo):
        who = cli_player.GetPlayer(pid, iGameID)
        if who:
            pid = who.m_ID
            iAccount = who.m_AccountID
            rpccli.CallClientLogic(pid, 'roomsub.playerop.R_DeviceChallengeBigData', (GetServerIndex(), iGameID, iAccount, dInfo), None)

    
    def L2SPlayerLevelBigData(iLGS, iGameID, pid, dInfo):
        who = cli_player.GetPlayer(pid, iGameID)
        if who:
            pid = who.m_ID
            iAccount = who.m_AccountID
            rpccli.CallClientLogic(pid, 'roomsub.playerop.R_WarLevelBigData', (GetServerIndex(), iGameID, iAccount, dInfo), None)

    
    def L2SPlayerReport(iLGS, iGameID, pid, dInfo):
        who = cli_player.GetPlayer(pid, iGameID)
        if who:
            who.SendWarReport(iGameID, dInfo)

    
    def L2SPlayerBuyItemReport(iLGS, iGameID, pid, dInfo):
        who = cli_player.GetPlayer(pid, iGameID)
        if who:
            pid = who.m_ID
            iAccount = who.m_AccountID
            rpccli.CallClientLogic(pid, 'roomsub.playerop.R_WarBuyItemReport', (GetServerIndex(), iGameID, iAccount, dInfo), None)

    
    def L2SPlayerAchievement(iLGS, iGameID, pid, dInfo):
        who = cli_player.GetPlayer(pid, iGameID)
        if who:
            pid = who.m_ID
            iAccount = who.m_AccountID
            rpccli.CallClientLogic(pid, 'roomsub.playerop.R_AchievementReport', (GetServerIndex(), iGameID, iAccount, dInfo), None)

    
    def L2SPlayerSeasonTask(iLGS, iGameID, pid, dInfo):
        who = cli_player.GetPlayer(pid, iGameID)
        if who:
            pid = who.m_ID
            iAccount = who.m_AccountID
            rpccli.CallClientLogic(pid, 'roomsub.playerop.R_SeasonTaskReport', (GetServerIndex(), iGameID, iAccount, dInfo), None)

    
    def L2SPlayerUnlockProgress(iLGS, iGameID, pid, dInfo):
        who = cli_player.GetPlayer(pid, iGameID)
        if who:
            pid = who.m_ID
            iAccount = who.m_AccountID
            rpccli.CallClientLogic(pid, 'roomsub.playerop.R_UnlockProgress', (GetServerIndex(), iGameID, iAccount, dInfo), None)

    
    def L2SPlayerNewUnlockProgress(iLGS, iGameID, pid, dInfo):
        who = cli_player.GetPlayer(pid, iGameID)
        if who:
            pid = who.m_ID
            iAccount = who.m_AccountID
            rpccli.CallClientLogic(pid, 'roomsub.playerop.R_NewUnlockProgress', (GetServerIndex(), iGameID, iAccount, dInfo), None)

    
    def L2SPlayerRecord(iLGS, iGameID, pid, dInfo):
        who = cli_player.GetPlayer(pid, iGameID)
        if who:
            pid = who.m_ID
            iAccount = who.m_AccountID
            rpccli.CallClientLogic(pid, 'roomsub.playerop.R_Record', (GetServerIndex(), iGameID, iAccount, dInfo), None)

    
    def L2STempReport(iLGS, iGameID, pid, dInfo):
        pass

    
    def L2SChangeCash(iLGS, iGameID, pid, dInfo):
        pass

    
    def CtrlWarRelease(iGameID, sReason):
        import servicefight.logicctrl
        servicefight.logicctrl.WarRelease(iGameID, sReason)

    
    def L2SPartyReward(iLGS, iGameID, pid, cbFunc):
        who = cli_player.GetPlayer(pid, iGameID)
        if who:
            pid = who.m_ID
            iAccount = who.m_AccountID
            resfunc = RPC_Functor(cbFunc, None)
            rpccli.CallClientLogic(pid, 'playway.partyreward.R_GetPartyReward', (GetServerIndex(), iGameID, iAccount), resfunc)

    
    def L2SReSendSeasonInfo(iLGS, iGameID, pid, dInfo):
        who = cli_player.GetPlayer(pid, iGameID)
        if who:
            pid = who.m_ID
            iAccount = who.m_AccountID
            rpccli.CallClientLogic(pid, 'roomsub.playerop.R_ReSendSeasonInfo', (GetServerIndex(), iGameID, iAccount, dInfo), None)

    
    def WarEnd(iGameID, lstPlayer):
        pass

    
    def LogicKickOut(iGameID, pid, iNowDisconnect):
        pass

    
    def L2SRealDieBigData(iLGS, iGameID, pid, dInfo):
        who = cli_player.GetPlayer(pid, iGameID)
        if who:
            pid = who.m_ID
            iAccount = who.m_AccountID
            rpccli.CallClientLogic(pid, 'roomsub.playerop.R_RealDieBigData', (GetServerIndex(), iGameID, iAccount, dInfo), None)

elif cllib.lib_flag.g_IsTradition:
    from cl_only import GetServerIndex
    from rpc import SendSvrMsg, CallFunc, RPC_Functor
    import cli_player
    
    def L2SPlayerLevelReport(iLGS, iGameID, pid, dInfo):
        SendSvrMsg(iLGS, 'roomsub.playerop.R_ServerWarLevelReport', (GetServerIndex(), iGameID, pid, dInfo), None)

    
    def L2SPlayerWeaponStoreSave(iLGS, iGameID, pid, dInfo):
        SendSvrMsg(iLGS, 'roomsub.playerop.R_WeaponStoreSave', (GetServerIndex(), iGameID, pid, dInfo), None)

    
    def L2SPlayerUnWarSetInfo(iLGS, iGameID, pid, dInfo):
        SendSvrMsg(iLGS, 'roomsub.playerop.R_UnWarSetInfo', (GetServerIndex(), iGameID, pid, dInfo), None)

    
    def L2SPlayerWarEndBigData(iLGS, iGameID, pid, dInfo):
        SendSvrMsg(iLGS, 'roomsub.playerop.R_WarEndBigData', (GetServerIndex(), iGameID, pid, dInfo), None)

    
    def L2SPlayerSurvivoUpGradeBigData(iLGS, iGameID, pid, dInfo):
        SendSvrMsg(iLGS, 'roomsub.playerop.R_SurvivoUpGradeBigData', (GetServerIndex(), iGameID, pid, dInfo), None)

    
    def L2SPlayerPhaseEndBigData(iLGS, iGameID, pid, dInfo):
        SendSvrMsg(iLGS, 'roomsub.playerop.R_PhaseEndBigData', (GetServerIndex(), iGameID, pid, dInfo), None)

    
    def L2SPlayerIntervalPhaseBigData(iLGS, iGameID, pid, dInfo):
        SendSvrMsg(iLGS, 'roomsub.playerop.R_IntervalPhaseBigData', (GetServerIndex(), iGameID, pid, dInfo), None)

    
    def L2SDeviceChallengeBigData(iLGS, iGameID, pid, dInfo):
        pass

    
    def L2SPlayerLevelBigData(iLGS, iGameID, pid, dInfo):
        SendSvrMsg(iLGS, 'roomsub.playerop.R_WarLevelBigData', (GetServerIndex(), iGameID, pid, dInfo), None)

    
    def L2SPlayerReport(iLGS, iGameID, pid, dInfo):
        SendSvrMsg(iLGS, 'roomsub.playerop.R_ServerWarEndReport', (GetServerIndex(), iGameID, pid, dInfo), None)

    
    def L2SPlayerBuyItemReport(iLGS, iGameID, pid, dInfo):
        SendSvrMsg(iLGS, 'roomsub.playerop.R_WarBuyItemReport', (GetServerIndex(), iGameID, pid, dInfo), None)

    
    def L2SPlayerAchievement(iLGS, iGameID, pid, dInfo):
        SendSvrMsg(iLGS, 'roomsub.playerop.R_AchievementReport', (GetServerIndex(), iGameID, pid, dInfo), None)

    
    def L2SPlayerSeasonTask(iLGS, iGameID, pid, dInfo):
        SendSvrMsg(iLGS, 'roomsub.playerop.R_SeasonTaskReport', (GetServerIndex(), iGameID, pid, dInfo), None)

    
    def L2SPlayerUnlockProgress(iLGS, iGameID, pid, dInfo):
        SendSvrMsg(iLGS, 'roomsub.playerop.R_UnlockProgress', (GetServerIndex(), iGameID, pid, dInfo), None)

    
    def L2SPlayerNewUnlockProgress(iLGS, iGameID, pid, dInfo):
        SendSvrMsg(iLGS, 'roomsub.playerop.R_NewUnlockProgress', (GetServerIndex(), iGameID, pid, dInfo), None)

    
    def L2SPlayerRecord(iLGS, iGameID, pid, dInfo):
        SendSvrMsg(iLGS, 'roomsub.playerop.R_Record', (GetServerIndex(), iGameID, pid, dInfo), None)

    
    def L2STempReport(iLGS, iGameID, pid, dInfo):
        pass

    
    def L2SChangeCash(iLGS, iGameID, pid, dInfo):
        pass

    
    def CtrlWarRelease(iGameID, sReason):
        import logicctrl
        logicctrl.WarRelease(iGameID, sReason)

    
    def L2SPartyReward(iLGS, iGameID, pid, cbFunc):
        resfunc = RPC_Functor(cbFunc, None)
        SendSvrMsg(iLGS, 'playway.partyreward.R_GetPartyReward', (GetServerIndex(), iGameID, pid), resfunc)

    
    def L2SReSendSeasonInfo(iLGS, iGameID, pid, dInfo):
        pass

    
    def WarEnd(iGameID, lstPlayer):
        pass

    
    def LogicKickOut(iGameID, pid, iNowDisconnect):
        who = cli_player.GetPlayer(pid)
        if who:
            iLeaveGame = 1
            who.KickOut(iGameID, iLeaveGame, iNowDisconnect)

    
    def L2SRealDieBigData(iLGS, iGameID, pid, dInfo):
        pass

elif cllib.lib_flag.g_IsStandalone:
    pass
else:
    raise Exception('unknown platform flag.')
