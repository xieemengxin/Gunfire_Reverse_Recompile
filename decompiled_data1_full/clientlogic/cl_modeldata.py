# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_modeldata.pyc
# RelativePath: clientlogic/cl_modeldata.pyc
# Source Generated with Decompyle++
# File: cl_modeldata.pyc (Python 3.6)

from cl_commondefines import MODEL_TYPE_BOX, MODEL_TYPE_CAPSULE, MODEL_TYPE_SPHERE, MODEL_TYPE_CTRLAGENT, MODEL_TYPE_POINT, MODEL_TYPE_MESH, MODEL_TYPE_SCALECTRLAGENT
from cl_only import CELL_SPACESIZE, SendAlert
import cl_modeldefine
import cllib.lib_flag
import math

class CBaseModel(object):
    
    def __init__(self, dParam):
        self.m_ModelShape = dParam['Shape']
        self.m_ModelAngle = self.TransInt2Float(dParam['Angle'])
        self.m_ModelCenter = self.TransInt2Float(dParam['Center'])
        self.m_ModelScale = self.TransInt2Float(dParam['Scale'])
        self.m_ModelSize = self.TransInt2Float(dParam['Size'])
        self.m_ModelLocalAngle = self.TransInt2Float(dParam['LocalAngle']) if 'LocalAngle' in dParam else (0, 0, 0)
        self.OnInit(dParam)

    
    def OnInit(self, dParam):
        pass

    
    def GetClientData(self):
        dClientData = { }
        (a1, a2, a3) = self.TransPositiveAngle(self.m_ModelAngle)
        (s1, s2, s3) = self.m_ModelScale
        dClientData['Angle'] = (int(a1 * CELL_SPACESIZE), int(a2 * CELL_SPACESIZE), int(a3 * CELL_SPACESIZE))
        dClientData['Scale'] = (int(s1 * CELL_SPACESIZE), int(s2 * CELL_SPACESIZE), int(s3 * CELL_SPACESIZE))
        return dClientData

    
    def GetServerData(self):
        dServerData = { }
        return dServerData

    
    def GetModelHeight(self):
        return 1.7

    
    def GetModelRadius(self):
        return 0.3

    
    def TransInt2Float(self, tData):
        return (tData[0] * 1, tData[1] * 1, tData[2] * 1)

    
    def TransPositiveAngle(self, tAngle):
        return ((round(tAngle[0]) % 360) * 1, (round(tAngle[1]) % 360) * 1, (round(tAngle[2]) % 360) * 1)

    
    def SetModelAngle(self, tAngle):
        self.m_ModelAngle = tAngle



class CBoxModel(CBaseModel):
    
    def GetServerData(self):
        dServerData = { }
        (sz1, sz2, sz3) = self.m_ModelSize
        (c1, c2, c3) = self.m_ModelCenter
        (s1, s2, s3) = self.m_ModelScale
        (a1, a2, a3) = self.m_ModelAngle
        InvRa = math.pi / 180
        dServerData['HalfExt'] = (sz1 * s1 * 0.5, sz2 * s2 * 0.5, sz3 * s3 * 0.5)
        dServerData['Center'] = (c1 * s1, c2 * s2, c3 * s3)
        dServerData['Radians'] = (a1 * InvRa, a2 * InvRa, a3 * InvRa)
        dServerData['Shape'] = self.m_ModelShape
        return dServerData

    
    def GetModelHeight(self):
        return self.m_ModelSize[1] * self.m_ModelScale[1]

    
    def GetModelRadius(self):
        return max(self.m_ModelSize[0] * self.m_ModelScale[0], self.m_ModelSize[2] * self.m_ModelScale[2])



class CCapsuleModel(CBaseModel):
    
    def GetServerData(self):
        dServerData = { }
        (s1, s2, s3) = self.m_ModelScale
        (c1, c2, c3) = self.m_ModelCenter
        (a1, a2, a3) = self.m_ModelAngle
        (la1, la2, la3) = self.m_ModelLocalAngle
        InvRa = math.pi / 180
        fRadius = self.m_ModelSize[1] * s2
        dServerData['Height'] = self.m_ModelSize[0] * s1 - fRadius * 2
        dServerData['Radius'] = fRadius
        dServerData['Center'] = (c1 * s1, c2 * s2, c3 * s3)
        dServerData['Radians'] = (a1 * InvRa, a2 * InvRa, a3 * InvRa)
        dServerData['Shape'] = self.m_ModelShape
        dServerData['LocalRadians'] = (la1 * InvRa, la2 * InvRa, la3 * InvRa)
        return dServerData

    
    def GetModelHeight(self):
        return self.m_ModelSize[0] * self.m_ModelScale[0]

    
    def GetModelRadius(self):
        return self.m_ModelSize[1] * self.m_ModelScale[1]



class CSphereModel(CBaseModel):
    
    def GetServerData(self):
        dServerData = { }
        (s1, s2, s3) = self.m_ModelScale
        (c1, c2, c3) = self.m_ModelCenter
        (a1, a2, a3) = self.m_ModelAngle
        InvRa = math.pi / 180
        dServerData['Radius'] = self.m_ModelSize[0] * s1
        dServerData['Center'] = (c1 * s1, c2 * s2, c3 * s3)
        dServerData['Radians'] = (a1 * InvRa, a2 * InvRa, a3 * InvRa)
        dServerData['Shape'] = self.m_ModelShape
        return dServerData

    
    def GetModelHeight(self):
        return self.m_ModelSize[0] * self.m_ModelScale[0]

    
    def GetModelRadius(self):
        return self.m_ModelSize[0] * self.m_ModelScale[0]



class CCtrlCapsuleModel(CBaseModel):
    
    def __init__(self, dParam):
        iObjShape = dParam['ObjShape']
        lstModelArgs = cl_modeldefine.GetModelDefine(iObjShape, 'Physx')
        if not lstModelArgs:
            SendAlert('err', '未找到模型%d, 请重新导模型表' % iObjShape)
            return None
        self.m_ModelShape = dParam['Shape']
        self.m_ModelRadius = lstModelArgs[0]
        self.m_ModelHeight = lstModelArgs[1]

    
    def GetClientData(self):
        return { }

    
    def GetServerData(self):
        dServerData = { }
        dServerData['Radius'] = self.m_ModelRadius
        dServerData['Height'] = self.m_ModelHeight - self.m_ModelRadius * 2
        dServerData['Center'] = (0, self.m_ModelHeight * 0.5, 0)
        dServerData['Radians'] = (0, 0, 0)
        dServerData['Shape'] = MODEL_TYPE_CAPSULE
        return dServerData

    
    def GetModelHeight(self):
        return self.m_ModelHeight

    
    def GetModelRadius(self):
        return self.m_ModelRadius



class CScaleCtrlCapsuleModel(CCtrlCapsuleModel):
    
    def __init__(self, dParam):
        iObjShape = dParam['ObjShape']
        lstModelArgs = cl_modeldefine.GetModelDefine(iObjShape, 'Physx')
        if not lstModelArgs:
            SendAlert('err', '未找到模型%d, 请重新导模型表' % iObjShape)
            return None
        fScale = dParam['Scale']
        self.m_ModelShape = dParam['Shape']
        self.m_ModelRadius = lstModelArgs[0] * fScale
        self.m_ModelHeight = lstModelArgs[1] * fScale



class CPointModel(CBaseModel):
    
    def __init__(self, dParam):
        pass

    
    def GetClientData(self):
        return { }

    
    def GetServerData(self):
        dServerData = { }
        dServerData['Shape'] = MODEL_TYPE_POINT
        return dServerData

    
    def GetModelHeight(self):
        return 0

    
    def GetModelRadius(self):
        return 0



class CMeshModel(CBaseModel):
    
    def OnInit(self, dParam):
        self.m_ModeResIdx = dParam['SceneMap']
        self.m_GameID = dParam['GameID']
        self.m_SceneID = dParam['SceneID']
        self.m_ModelCookIdx = dParam['Prefab'] // 100
        if cllib.lib_flag.g_IsAuthorityRun:
            SendAlert('model', 'meshmodel used %s' % dParam)

    
    def GetServerData(self):
        dServerData = { }
        (sz1, sz2, sz3) = self.m_ModelSize
        (c1, c2, c3) = self.m_ModelCenter
        (s1, s2, s3) = self.m_ModelScale
        (a1, a2, a3) = self.m_ModelAngle
        InvRa = math.pi / 180
        dServerData['HalfExt'] = (sz1 * s1 * 0.5, sz2 * s2 * 0.5, sz3 * s3 * 0.5)
        dServerData['Center'] = (c1 * s1, c2 * s2, c3 * s3)
        dServerData['Radians'] = (a1 * InvRa, a2 * InvRa, a3 * InvRa)
        dServerData['Shape'] = self.m_ModelShape
        dServerData['ResIdx'] = self.m_ModeResIdx
        dServerData['GameID'] = self.m_GameID
        dServerData['SceneID'] = self.m_SceneID
        dServerData['CookIdx'] = self.m_ModelCookIdx
        return dServerData

    
    def GetModelHeight(self):
        return self.m_ModelSize[1] * self.m_ModelScale[1]

    
    def GetModelRadius(self):
        return max(self.m_ModelSize[0] * self.m_ModelScale[0], self.m_ModelSize[2] * self.m_ModelScale[2])



def GetModel(dParam):
    oCollider = None
    iShape = dParam['Shape']
    if iShape == MODEL_TYPE_CAPSULE:
        oCollider = CCapsuleModel(dParam)
    elif iShape == MODEL_TYPE_BOX:
        oCollider = CBoxModel(dParam)
    elif iShape == MODEL_TYPE_SPHERE:
        oCollider = CSphereModel(dParam)
    elif iShape == MODEL_TYPE_CTRLAGENT:
        oCollider = CCtrlCapsuleModel(dParam)
    elif iShape == MODEL_TYPE_POINT:
        oCollider = CPointModel(dParam)
    elif iShape == MODEL_TYPE_MESH:
        oCollider = CMeshModel(dParam)
    elif iShape == MODEL_TYPE_SCALECTRLAGENT:
        oCollider = CScaleCtrlCapsuleModel(dParam)
    return oCollider

