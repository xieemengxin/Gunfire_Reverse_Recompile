# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_device/__init__.pyc
# RelativePath: clientlogic/cl_device/__init__.pyc
# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.6)

from . import mobject
from cl_commondefines import WARRIOR_DEVICE, WARRIOR_DEVICE_POISON, WARRIOR_DEVICE_TURRET, WARRIOR_DEVICE_BARRIER
g_DeviceClass = {
    WARRIOR_DEVICE_BARRIER: mobject.CBarrierDevice,
    WARRIOR_DEVICE_TURRET: mobject.CTurretDevice,
    WARRIOR_DEVICE_POISON: mobject.CPoisonDevice,
    WARRIOR_DEVICE: mobject.CDevice }

def CreateDevice(oGame, oHero, clsData, dAddData):
    nid = oGame.NewNPCID()
    iFightType = clsData.m_FightType
    if iFightType in g_DeviceClass:
        clsDevice = g_DeviceClass[iFightType]
    else:
        clsDevice = g_DeviceClass[WARRIOR_DEVICE]
    oDevice = clsDevice(oGame, nid)
    clsData.InitDeviceData(oHero, oDevice, dAddData)
    oDevice.InitDevice(dAddData)
    return oDevice

