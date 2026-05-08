# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_engphyobj.pyc
# RelativePath: clientlogic/cl_engphyobj.pyc
# Source Generated with Decompyle++
# File: cl_engphyobj.pyc (Python 3.6)

from C_component import ComPhyController, ComPhyCollider
from cl_world import CSceneObject
from cl_commondefines import PAMOD_TYPE_TRDYNA, PAMOD_TYPE_DYING, PAMOD_TYPE_QUERRY, NWARRIOR_VIRTUAL_REALBULLET, SCENE_EVT_ENTER, SCENE_EVT_LEAVE, NWARRIOR_VIRTUAL_DYNCEVENT, PAMOD_TYPE_DYNA, PAMOD_TYPE_CTRL
from cl_pxlayer import PXLAYER_DEVENT
import cl_math

class CCtrlController(ComPhyController):
    
    def __init__(self, oOwner, iLayer, dParam):
        self.m_Owner = oOwner
        dArgs = {
            'layer': iLayer,
            'HalfHeight': dParam['Height'] / 2,
            'Radius': dParam['Radius'],
            'StepOffset': 0.35 }
        super().__init__(oOwner.m_Game.m_ID, oOwner.m_ID, 'CtrlCCT', dArgs)

    
    def SetCtrlFlag(self, iFlags, iSet):
        self.E_SetFlags(iFlags, iSet)



class CKinematicModel(ComPhyCollider):
    
    def __init__(self, oOwner, iLayer, dParam):
        self.m_Owner = oOwner
        dArgs = {
            'layer': iLayer,
            'EnableSimulation': 1,
            'EnableSceneQuery': 1,
            'IsTrigger': 0 }
        dArgs.update(dParam)
        super().__init__(oOwner.m_Game.m_ID, oOwner.m_ID, 'Obstacle', dParam['Shape'], dArgs)
        self.rigidbody.E_SetKinematic(1)
        if 'LocalRadians' in dArgs and not cl_math.IsZero(dArgs['LocalRadians']):
            self.E_SetLocalPose(dArgs['Center'], dArgs['LocalRadians'])

    
    def SetCtrlFlag(self, iFlags, iSet):
        self.E_SetFlags(iFlags, iSet)

    
    def C_OnContact(self, *args):
        pass



class CSceneQueryModel(ComPhyCollider):
    
    def __init__(self, oOwner, iLayer, dParam):
        self.m_Owner = oOwner
        dArgs = {
            'layer': iLayer,
            'EnableSimulation': 1,
            'EnableSceneQuery': 1,
            'IsTrigger': 0 }
        dArgs.update(dParam)
        super().__init__(oOwner.m_Game.m_ID, oOwner.m_ID, 'Obstacle', dParam['Shape'], dArgs)

    
    def SetCtrlFlag(self, iFlags, iSet):
        self.E_SetFlags(iFlags, iSet)

    
    def C_OnContact(self, *args):
        pass



class CDyingModel(ComPhyController):
    
    def __init__(self, oOwner, iLayer, dParam):
        self.m_Owner = oOwner
        dArgs = {
            'layer': iLayer,
            'HalfHeight': dParam['Height'] / 2,
            'Radius': dParam['Radius'],
            'StepOffset': 0.35 }
        super().__init__(oOwner.m_Game.m_ID, oOwner.m_ID, 'Dying', dArgs)

    
    def SetCtrlFlag(self, iFlags, iSet):
        self.E_SetFlags(iFlags, iSet)

    
    def C_OnContact(self, *args):
        pass



class CTriggerKinematicModel(CKinematicModel):
    
    def C_OnContact(self, iTarget, dArgs):
        self.m_Owner.OnContact(iTarget, dArgs)

    
    def SetEnableSimulation(self, iValue):
        self.E_SetEnableSimulation(iValue)

    
    def SetEnableSceneQuery(self, iValue):
        self.E_SetEnableSceneQuery(iValue)

    
    def SetRigidbodyEnableSimulation(self, iValue):
        self.rigidbody.E_SetEnableSimulation(iValue)

    
    def SetTrigger(self, iValue):
        self.E_SetTrigger(iValue)

    
    def C_OnTrigger(self, iTriType, oTarget):
        if iTriType == SCENE_EVT_ENTER:
            self.m_Owner.OnTriggerEnter(oTarget)
        else:
            self.m_Owner.OnTriggerLeave(oTarget)

    
    def C_OnTriggerStatic(self):
        pass



def CreatePhyModel(oOwner, iPaType, iLayer, dParam):
    if iPaType == PAMOD_TYPE_CTRL:
        return CCtrlController(oOwner, iLayer, dParam)
    if iPaType == PAMOD_TYPE_DYNA:
        return CKinematicModel(oOwner, iLayer, dParam)
    if iPaType == PAMOD_TYPE_QUERRY:
        return CSceneQueryModel(oOwner, iLayer, dParam)
    if iPaType == PAMOD_TYPE_DYING:
        return CDyingModel(oOwner, iLayer, dParam)
    if iPaType == PAMOD_TYPE_TRDYNA:
        return CTriggerKinematicModel(oOwner, iLayer, dParam)


class CDynamicEventObject(CSceneObject, ComPhyCollider):
    m_Type = 'DyncEvent'
    m_FightType = NWARRIOR_VIRTUAL_DYNCEVENT
    
    def __init__(self, oGame, nid, dParam):
        CSceneObject.__init__(self, oGame, nid)
        dArgs = {
            'layer': PXLAYER_DEVENT,
            'EnableSimulation': 0,
            'EnableSceneQuery': 0,
            'IsTrigger': 1 }
        dArgs.update(dParam)
        ComPhyCollider.__init__(self, oGame.m_ID, nid, 'DyncEvent', dArgs['Shape'], dArgs)
        self.rigidbody.E_SetKinematic(1)
        self.m_TriggerCallback = None

    
    def SetTriggerCallback(self, fCallback):
        self.m_TriggerCallback = fCallback

    
    def C_OnTrigger(self, iTriType, oTarget):
        iLeave = 1 if iTriType == SCENE_EVT_LEAVE else 0
        self.m_TriggerCallback(self.m_ID, oTarget, iLeave)



class CAttachEventObject(ComPhyCollider):
    
    def __init__(self, oGame, oOwner, iLayer, dShape, cb):
        self.m_Game = oGame
        dArgs = {
            'layer': iLayer,
            'EnableSimulation': 0,
            'EnableSceneQuery': 0,
            'IsTrigger': 1 }
        dArgs.update(dShape)
        ComPhyCollider.__init__(self, oGame.m_ID, oOwner.m_ID, 'AttachEvent', dArgs['Shape'], dArgs)
        self.m_TriggerCallback = cb

    
    def C_OnTrigger(self, iTriType, obj):
        iLeave = 1 if iTriType == SCENE_EVT_LEAVE else 0
        self.m_TriggerCallback(obj, iLeave)

    
    def Unstall(self):
        self.m_TriggerCallback = None
        super().E_Unstall()

    
    def Disable(self):
        self.E_SetTrigger(0)

    
    def Enable(self):
        self.E_SetTrigger(1)



class CBulletInterface(object):
    
    def Key(self):
        return (0, '')

    
    def Rigidbody(self):
        return self.rigidbody

    
    def SetBulletSpeed(self, fSpeed):
        self.rigidbody.E_SetLinearVelocity(fSpeed)

    
    def GetBulletSpeed(self):
        return self.rigidbody.E_GetLinearVelocity()

    
    def SetBulletAccSpeed(self, fAccSpeed):
        self.rigidbody.E_SetAccSpeed(fAccSpeed)

    
    def SetBulletPosition(self, vPos):
        self.rigidbody.E_SetPosition(vPos)

    
    def GetBulletPosition(self):
        return self.rigidbody.E_GetPosition()

    
    def OnContact(self, oGame, collider, iTarget, dArgs):
        tRet = oGame.m_SkillMgr.GetSkillCartoonByBullet(self.Key())
        if not tRet:
            return None
        if dArgs is not None:
            dArgs['speed'] = self.GetBulletSpeed()
        (oSkill, dCartoon) = tRet
        clsCartoon = dCartoon['cls']
        clsCartoon.AddHitTarget(oSkill, dCartoon, iTarget, dArgs)
        oSkill.Update([
            dCartoon['ID']])



class CTraceEventBullet(CBulletInterface, ComPhyCollider):
    
    def __init__(self, oGame, oOwner, dBulletParam, iLayer, dShape):
        self.m_Game = oGame
        self.m_OwnerID = oOwner.m_ID
        dArgs = {
            'layer': iLayer,
            'EnableSimulation': 0,
            'EnableSceneQuery': 0,
            'IsTrigger': 1 }
        dArgs.update(dShape)
        self.m_ComName = 'TraceEventBullet.%s' % dBulletParam['TraceIdx']
        ComPhyCollider.__init__(self, oGame.m_ID, oOwner.m_ID, self.m_ComName, dArgs['Shape'], dArgs)
        if 'LocalPos' in dBulletParam:
            self.E_SetLocalPosition(dBulletParam['LocalPos'])
        if 'PassID' in dBulletParam:
            self.SetPassID(dBulletParam['PassID'])
        if 'LockDirection' in dBulletParam:
            self.rigidbody.E_LockDirection(dBulletParam['LockDirection'])
        self.rigidbody.E_SetKinematic(1)
        oOwner.m_BulletDict['Bullet.%s' % self.m_ComName] = self

    
    def SetPassID(self, iObjID):
        self.E_SetFilterData(1, iObjID)

    
    def Key(self):
        return (self.m_OwnerID, 'Bullet.%s' % self.m_ComName)

    
    def C_OnTrigger(self, iTriType, obj):
        if iTriType == SCENE_EVT_ENTER:
            self.OnContact(self.m_Game, self, obj.m_ID, { })

    
    def C_OnTriggerStatic(self, iTriType):
        if iTriType == SCENE_EVT_ENTER:
            self.OnContact(self.m_Game, self, 0, { })

    
    def Unstall(self):
        oOwner = self.m_Game.GetObject(self.m_OwnerID)
        if oOwner:
            sKey = 'Bullet.%s' % self.m_ComName
            if sKey in oOwner.m_BulletDict:
                del oOwner.m_BulletDict[sKey]
        super().E_Unstall()

    
    def Disable(self):
        self.E_SetTrigger(0)

    
    def Enable(self):
        self.E_SetTrigger(1)



class CTraceEvent(CTraceEventBullet):
    
    def __init__(self, oGame, oOwner, dBulletParam, iLayer, dShape, tFunc):
        self.m_Game = oGame
        self.m_OwnerID = oOwner.m_ID
        dArgs = {
            'layer': iLayer,
            'EnableSimulation': 0,
            'EnableSceneQuery': 0,
            'IsTrigger': 1 }
        dArgs.update(dShape)
        self.m_ComName = 'TraceEventBullet.%s' % dBulletParam['TraceIdx']
        ComPhyCollider.__init__(self, oGame.m_ID, oOwner.m_ID, self.m_ComName, dArgs['Shape'], dArgs)
        if 'PassID' in dBulletParam:
            self.SetPassID(dBulletParam['PassID'])
        self.rigidbody.E_SetKinematic(1)
        self.m_Func = tFunc
        self.m_ReleaseFlag = 0

    
    def C_OnTrigger(self, iTriType, obj):
        (enterfunc, leavefunc) = self.m_Func
        oOwner = self.m_Game.GetObject(self.m_OwnerID)
        if iTriType == SCENE_EVT_ENTER:
            func = enterfunc
        else:
            func = leavefunc
        if not func:
            return None
        func(oOwner, {
            'VID': obj.m_ID })

    
    def Unstall(self):
        if self.m_ReleaseFlag:
            return None
        self.m_ReleaseFlag = 1
        self.m_Func = None
        super().E_Unstall()



class CPhyAttachRigidBullet(ComPhyCollider):
    
    def __init__(self, oGame, oOwner, oBulletOwner, sDesc, iLayer, dShape):
        self.m_Game = oGame
        self.m_OwnerID = oOwner.m_ID
        self.m_BulletOwner = oBulletOwner
        dArgs = {
            'layer': iLayer,
            'EnableSimulation': 1,
            'EnableSceneQuery': 0,
            'IsTrigger': 0 }
        dArgs.update(dShape)
        super().__init__(oGame.m_ID, oOwner.m_ID, sDesc, dArgs['Shape'], dArgs)

    
    def SetPassID(self, iObjID):
        self.E_SetFilterData(1, iObjID)

    
    def C_OnContact(self, iTarget, dArgs):
        self.m_BulletOwner.OnContact(self.m_Game, self, iTarget, dArgs)

    
    def Unstall(self):
        super().E_Unstall()
        self.m_BulletOwner = None



class CAttachRigidBullet(CBulletInterface):
    
    def __init__(self, oGame, oOwner, dBulletParam, iLayer, dShape):
        self.m_Game = oGame
        self.m_OwnerID = oOwner.m_ID
        self.m_ComName = 'AttachRigidBullet.%s' % dBulletParam['TraceIdx']
        self.m_Outer = CPhyAttachRigidBullet(oGame, oOwner, self, self.m_ComName + 'Outer', iLayer, dShape)
        sharedrigidbody = self.m_Outer.rigidbody
        sharedrigidbody.E_SetEnableCCD(1)
        sharedrigidbody.E_SetEnableGravity(1)
        sharedrigidbody.E_SetEnableSimulation(1)
        self.rigidbody = sharedrigidbody
        if 'PassID' in dBulletParam:
            self.m_Outer.SetPassID(dBulletParam['PassID'])
        if 'Speed' in dBulletParam:
            self.SetBulletSpeed(dBulletParam['Speed'])
        if 'AccSpeed' in dBulletParam:
            self.SetBulletAccSpeed(dBulletParam['AccSpeed'])
        oOwner.m_BulletDict['Bullet.%s' % self.m_ComName] = self

    
    def Key(self):
        return (self.m_OwnerID, 'Bullet.%s' % self.m_ComName)

    
    def Unstall(self):
        oOwner = self.m_Game.GetObject(self.m_OwnerID)
        if oOwner:
            sKey = 'Bullet.%s' % self.m_ComName
            if sKey in oOwner.m_BulletDict:
                del oOwner.m_BulletDict[sKey]
        self.m_Outer.Unstall()
        self.m_Outer = None
        self.m_Game = None



class CDoubleAttachRigidBullet(CBulletInterface):
    
    def __init__(self, oGame, oOwner, dBulletParam, iInnerLayer, dInnerShape, iOuterLayer, dOuterShape):
        self.m_Game = oGame
        self.m_OwnerID = oOwner.m_ID
        self.m_ComName = 'AttachRigidBullet.%s' % dBulletParam['TraceIdx']
        self.m_Outer = CPhyAttachRigidBullet(oGame, oOwner, self, self.m_ComName + 'Inner', iInnerLayer, dInnerShape)
        self.m_Inner = CPhyAttachRigidBullet(oGame, oOwner, self, self.m_ComName + 'Outer', iOuterLayer, dOuterShape)
        sharedrigidbody = self.m_Outer.rigidbody
        sharedrigidbody.E_SetEnableCCD(1)
        sharedrigidbody.E_SetEnableGravity(1)
        sharedrigidbody.E_SetEnableSimulation(1)
        self.rigidbody = sharedrigidbody
        if 'PassID' in dBulletParam:
            self.m_Outer.SetPassID(dBulletParam['PassID'])
            self.m_Inner.SetPassID(dBulletParam['PassID'])
        if 'Speed' in dBulletParam:
            self.SetBulletSpeed(dBulletParam['Speed'])
        if 'AccSpeed' in dBulletParam:
            self.SetBulletAccSpeed(dBulletParam['AccSpeed'])
        oOwner.m_BulletDict['Bullet.%s' % self.m_ComName] = self

    
    def Key(self):
        return (self.m_OwnerID, 'Bullet.%s' % self.m_ComName)

    
    def Unstall(self):
        oOwner = self.m_Game.GetObject(self.m_OwnerID)
        if oOwner:
            sKey = 'Bullet.%s' % self.m_ComName
            if sKey in oOwner.m_BulletDict:
                del oOwner.m_BulletDict[sKey]
        self.m_Outer.Unstall()
        self.m_Outer = None
        self.m_Inner.Unstall()
        self.m_Inner = None
        self.m_Game = None



class CRigidBulletCollider(ComPhyCollider):
    
    def __init__(self, oGame, oOwner, sDesc, iLayer, dShape):
        self.m_Game = oGame
        self.m_Owner = oOwner
        dArgs = {
            'layer': iLayer,
            'EnableSimulation': 1,
            'EnableSceneQuery': 0,
            'IsTrigger': 0 }
        dArgs.update(dShape)
        super().__init__(oGame.m_ID, oOwner.m_ID, sDesc, dArgs['Shape'], dArgs)

    
    def SetPassID(self, iObjID):
        self.E_SetFilterData(1, iObjID)

    
    def C_OnContact(self, iTarget, dArgs):
        self.m_Owner.OnContact(self.m_Game, self, iTarget, dArgs)

    
    def C_OnTrigger(self, iTriType, obj):
        if iTriType == SCENE_EVT_ENTER:
            self.m_Owner.OnContact(self.m_Game, self, obj.m_ID, { })

    
    def C_OnTriggerStatic(self, iTriType):
        if iTriType == SCENE_EVT_ENTER:
            self.m_Owner.OnContact(self.m_Game, self, 0, { })



class CRigidBullet(CSceneObject, CBulletInterface):
    m_Type = 'RealBullet'
    m_FightType = NWARRIOR_VIRTUAL_REALBULLET
    
    def __init__(self, oGame, nid, dBulletParam, iLayer, dShape):
        CSceneObject.__init__(self, oGame, nid)
        self.m_Outer = CRigidBulletCollider(oGame, self, 'RealBullet', iLayer, dShape)
        if 'PassID' in dBulletParam:
            self.m_Outer.SetPassID(dBulletParam['PassID'])
        sharedrigidbody = self.m_Outer.rigidbody
        sharedrigidbody.E_SetEnableCCD(1)
        sharedrigidbody.E_SetEnableGravity(1)
        sharedrigidbody.E_SetEnableSimulation(1)
        self.rigidbody = sharedrigidbody

    
    def OnInitToScene(self, tPos):
        pass

    
    def Key(self):
        return (self.m_ID, '')

    
    def Remove(self, sReason):
        self.m_Outer = None
        self.rigidbody = None
        CSceneObject.Remove(self, sReason)



class CDoubleRigidBullet(CSceneObject, CBulletInterface):
    m_Type = 'RealBullet'
    m_FightType = NWARRIOR_VIRTUAL_REALBULLET
    
    def __init__(self, oGame, nid, dBulletParam, iInnerLayer, dInnerShape, iOuterLayer, dOuterShape):
        CSceneObject.__init__(self, oGame, nid)
        self.m_Inner = CRigidBulletCollider(oGame, self, 'RealBulletInner', iInnerLayer, dInnerShape)
        self.m_Outer = CRigidBulletCollider(oGame, self, 'RealBulletOuter', iOuterLayer, dOuterShape)
        if 'PassID' in dBulletParam:
            self.m_Inner.SetPassID(dBulletParam['PassID'])
            self.m_Outer.SetPassID(dBulletParam['PassID'])
        sharedrigidbody = self.m_Outer.rigidbody
        sharedrigidbody.E_SetEnableCCD(1)
        sharedrigidbody.E_SetEnableGravity(1)
        sharedrigidbody.E_SetEnableSimulation(1)
        sharedrigidbody.E_SetLinearVelocity(dBulletParam['Speed'])
        sharedrigidbody.E_SetAccSpeed(dBulletParam['AccSpeed'])
        self.rigidbody = sharedrigidbody

    
    def OnInitToScene(self, tPos):
        pass

    
    def Key(self):
        return (self.m_ID, '')

    
    def Remove(self, sReason):
        self.m_Inner = None
        self.m_Outer = None
        self.rigidbody = None
        CSceneObject.Remove(self, sReason)



def CreateDynamicEventObject(oGame, dShape):
    nid = oGame.NewNPCID()
    obj = CDynamicEventObject(oGame, nid, dShape)
    return obj


def CreateAttachEventObject(oGame, oOwner, iLayer, dShape, cb):
    obj = CAttachEventObject(oGame, oOwner, iLayer, dShape, cb)
    return obj


def CreateTraceBullet(oGame, oOwner, dBulletParam, iLayer, dShape):
    obj = CTraceEventBullet(oGame, oOwner, dBulletParam, iLayer, dShape)
    return obj


def CreateTraceEvent(oGame, oOwner, dBulletParam, iLayer, dShape, tFunc):
    obj = CTraceEvent(oGame, oOwner, dBulletParam, iLayer, dShape, tFunc)
    return obj


def CreateAttachBullet(oGame, oOwner, dBulletParam, iLayer, dShape):
    obj = CAttachRigidBullet(oGame, oOwner, dBulletParam, iLayer, dShape)
    return obj


def CreateDoubleAttachBullet(oGame, oOwner, dBulletParam, iInnerLayer, dInnerShape, iOuterLayer, dOuterShape):
    obj = CDoubleAttachRigidBullet(oGame, oOwner, dBulletParam, iInnerLayer, dInnerShape, iOuterLayer, dOuterShape)
    return obj


def CreateRigidBullet(oGame, dBulletParam, iLayer, dShape):
    nid = oGame.NewNPCID()
    obj = CRigidBullet(oGame, nid, dBulletParam, iLayer, dShape)
    return obj


def CreateDoubleRigidBullet(oGame, dBulletParam, iInnerLayer, dInnerShape, iOuterLayer, dOuterShape):
    nid = oGame.NewNPCID()
    obj = CDoubleRigidBullet(oGame, nid, dBulletParam, iInnerLayer, dInnerShape, iOuterLayer, dOuterShape)
    return obj

