# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_minigame/mg_goldencup.pyc
# RelativePath: clientlogic/cl_minigame/mg_goldencup.pyc
# Source Generated with Decompyle++
# File: mg_goldencup.pyc (Python 3.6)

from cl_only import ChooseKey, DeepCopy
from cl_commondefines import VIRTUAL_ITEM_GOLDENCUP, MG_GOLDENCUP
from cl_pxlayer import PXMASK_MOVEBLK
from cl_object.logging import WarrewardLog
from .mobject import CDropGame, CBaseGameData
import cl_math

class CRewardGoldenCupGameData(CBaseGameData):
    m_SID = 0
    m_Type = MG_GOLDENCUP
    m_ChooseWeight = { }
    
    def InitMiniGame(cls, oMiniGame):
        oMiniGame.m_ChooseWeight = DeepCopy(cls.m_ChooseWeight)

    InitMiniGame = classmethod(InitMiniGame)
    
    def GetGameClass(cls):
        return CRewardGoldenCupGame

    GetGameClass = classmethod(GetGameClass)


class CRewardGoldenCupGame(CDropGame):
    m_MaxGoundDistance = 12
    
    def GetRewardInfo(self):
        oGame = self.m_Game
        oOwner = oGame.GetObject(self.m_Owner)
        if not oOwner:
            return []
        iTime = self.Query('Times', 1)
        lstReward = []
        iScene = oOwner.m_Scene
        if self.Query('CalOffset', 1):
            vPos = cl_math.Vec3Add(oOwner.GetPos(), (0, oOwner.m_ModelHeight * 1.5 - 0.5, 0))
        else:
            vPos = (0, 0, 0)
        for _ in range(iTime):
            iNpc = ChooseKey(self.m_Game, self.m_ChooseWeight)
            if not self.Query('CalOffset', 1):
                vPos = self.GetDropBasePos()
                vPos = (vPos[0], vPos[1] + 1.2, vPos[2])
                fGroundDis = oGame.Scene_GroundDistance(iScene, vPos, self.m_MaxGoundDistance, PXMASK_MOVEBLK, self.m_Owner)
                vPos = (vPos[0], vPos[1] - fGroundDis, vPos[2])
                if fGroundDis >= self.m_MaxGoundDistance:
                    WarrewardLog.Alert('%d goldencup %d drop at %s height %.2f' % (oGame.m_ID, oOwner.m_SID, vPos, fGroundDis))
            dReward = {
                'item': VIRTUAL_ITEM_GOLDENCUP,
                'info': {
                    'sid': iNpc,
                    'DropPos': vPos,
                    'Scene': iScene } }
            lstReward.append(dReward)
        
        return lstReward


