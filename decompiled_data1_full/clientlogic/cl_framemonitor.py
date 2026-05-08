# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_framemonitor.pyc
# RelativePath: clientlogic/cl_framemonitor.pyc
# Source Generated with Decompyle++
# File: cl_framemonitor.pyc (Python 3.6)

from cl_only import GAME_FRAME_INF, GAME_FRAME
from cl_object.logging import OptimizationLog
import time
import cllib.lib_flag
SECOND_RATIO = 1000
SECOND_1_AVG_FRAME = 1 * SECOND_RATIO
SECOND_10_AVG_FRAME = 10 * SECOND_RATIO
SECOND_30_AVG_FRAME = 30 * SECOND_RATIO
GAME_AVG_FRAME = int(GAME_FRAME_INF / GAME_FRAME) * SECOND_RATIO
INFO_TIME = 0
INFO_GAME_TIME = 1
INFO_LAST_FRAME = 2
INFO_AVG_FRAME = 3
INFO_MIN_AVG_FRAME = 4
ALERT_MIN_AVG_FRAME = 10
VALIUD_MIN_FRAME = 25

class CFrameMonitor(object):
    
    def __init__(self, oGame):
        self.m_Game = oGame
        iNowTime = int(time.time() * SECOND_RATIO)
        self.m_FrameRecord = { }
        for iType in (SECOND_1_AVG_FRAME, SECOND_10_AVG_FRAME, SECOND_30_AVG_FRAME, GAME_AVG_FRAME):
            self.m_FrameRecord[iType] = [
                iNowTime,
                0,
                0,
                0,
                []]
        
        self.m_Game.m_Timer.Logic_Call_Out(self.CheckFrame, 100, 'CheckGameFrame')
        self.m_GameStopped = False
        self.m_Game.m_Status.SetAfterStartHook('FrameMonitor', self.OnGameStartStep)

    
    def Release(self):
        self.m_FrameRecord = { }
        self.m_Game.m_Status.SetAfterStartHook('FrameMonitor', None)
        self.m_Game.m_Timer.Logic_Remove_Call_Out('CheckGameFrame')
        self.m_Game = None

    
    def OnGameStartStep(self):
        self.m_GameStopped = True

    
    def CheckFrame(self):
        if not cllib.lib_flag.g_OpenWarFrameCheck:
            return None
        self.m_Game.m_Timer.Logic_Call_Out(self.CheckFrame, 100, 'CheckGameFrame')
        iNowFrame = self.m_Game.GetFrameNum()
        iNowTime = int(time.time() * SECOND_RATIO)
        if not self.m_Game.m_Status.IsStoped():
            pass
        iGameStop = self.m_GameStopped
        self.m_GameStopped = False
        for iMonitorTime, lstInfo in self.m_FrameRecord.items():
            if not iGameStop:
                iGameTime = lstInfo[INFO_GAME_TIME] + iNowTime - lstInfo[INFO_TIME]
                lstInfo[INFO_GAME_TIME] = iGameTime
                lstInfo[INFO_TIME] = iNowTime
            else:
                lstInfo[INFO_TIME] = iNowTime
            if iGameTime >= iMonitorTime:
                iNewAvgFrame = int((iNowFrame - lstInfo[INFO_LAST_FRAME]) * SECOND_RATIO / iGameTime)
                lstMinAvgInfo = lstInfo[INFO_MIN_AVG_FRAME]
                if iNowFrame > 750:
                    if not lstMinAvgInfo or iNewAvgFrame < lstMinAvgInfo[0]:
                        lstInfo[INFO_MIN_AVG_FRAME] = (iNewAvgFrame, iNowFrame, iNowTime)
                        if iNewAvgFrame <= ALERT_MIN_AVG_FRAME:
                            oGame = self.m_Game
                            lstPlayer = oGame.m_WarMgr.GetAllPlayer()
                            iGameID = oGame.m_ID
                            OptimizationLog.Debug(f'''low avg frame {(iGameID, iGameTime, iNewAvgFrame, iMonitorTime // SECOND_RATIO, iNowFrame, lstPlayer)}''')
                lstInfo[INFO_AVG_FRAME] = iNewAvgFrame
                lstInfo[INFO_LAST_FRAME] = iNowFrame
                lstInfo[INFO_GAME_TIME] = 0
        

    
    def GetAllGameAvgFrame(self):
        iNowFrame = self.m_Game.GetFrameNum()
        if iNowFrame < VALIUD_MIN_FRAME:
            return 0
        lstInfo = self.m_FrameRecord[GAME_AVG_FRAME]
        return int((iNowFrame - lstInfo[INFO_LAST_FRAME]) * SECOND_RATIO / lstInfo[INFO_GAME_TIME])

    
    def GetFrameInfo(self):
        dInfo = { }
        for iMonitorTime, lstInfo in self.m_FrameRecord.items():
            if iMonitorTime == GAME_AVG_FRAME:
                continue
            dInfo[iMonitorTime] = list(lstInfo[INFO_MIN_AVG_FRAME])
        
        dInfo[GAME_AVG_FRAME] = self.GetAllGameAvgFrame()
        return dInfo


