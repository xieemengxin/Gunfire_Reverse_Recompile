# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_wardata/w3011/build.pyc
# RelativePath: clientlogic/cl_wardata/w3011/build.pyc
# Source Generated with Decompyle++
# File: build.pyc (Python 3.6)

from cl_resmgr.resdata import CBuildData as CCustom
import cl_resmgr.resdata as baseconfig
import cl_wardata.buildaction as buildaction

def BuildSmashAction1002(oBuild, who):
    buildaction.SmashObstacleRewardItemList(oBuild, who, {
        201: {
            'Prop': 5000,
            'Times': 1 },
        401: {
            'Prop': 5000,
            'Times': 1 } }, 0, 1)


def BuildSmashAction1003(oBuild, who):
    buildaction.SmashObstacleRewardItemList(oBuild, who, {
        201: {
            'Prop': 5000,
            'Times': 1 },
        401: {
            'Prop': 5000,
            'Times': 1 } }, 0, 1)


def BuildSmashAction1004(oBuild, who):
    buildaction.SmashObstacleRewardItemList(oBuild, who, {
        201: {
            'Prop': 5000,
            'Times': 1 },
        401: {
            'Prop': 5000,
            'Times': 1 } }, 0, 1)


def BuildSmashAction1005(oBuild, who):
    buildaction.SmashObstacleRewardItemList(oBuild, who, {
        201: {
            'Prop': 5000,
            'Times': 1 },
        401: {
            'Prop': 5000,
            'Times': 1 } }, 0, 1)


class CBuildData1001(baseconfig.CBuildData):
    m_SID = 1001
    m_DataSID = 1008
    m_Name = '#NT#爆炸木桶'
    m_SmashFunc = None
    m_InteractFunc = None


class CBuildData1002(baseconfig.CBuildData):
    m_SID = 1002
    m_DataSID = 1003
    m_Name = '#NT#木箱'
    m_SmashFunc = BuildSmashAction1002
    m_InteractFunc = None


class CBuildData1003(baseconfig.CBuildData):
    m_SID = 1003
    m_DataSID = 1005
    m_Name = '#NT#瓶子'
    m_SmashFunc = BuildSmashAction1003
    m_InteractFunc = None


class CBuildData1004(baseconfig.CBuildData):
    m_SID = 1004
    m_DataSID = 1006
    m_Name = '#NT#瓶子'
    m_SmashFunc = BuildSmashAction1004
    m_InteractFunc = None


class CBuildData1005(baseconfig.CBuildData):
    m_SID = 1005
    m_DataSID = 1007
    m_Name = '#NT#瓶子'
    m_SmashFunc = BuildSmashAction1005
    m_InteractFunc = None


class CBuildData1114(baseconfig.CBuildData):
    m_SID = 1114
    m_DataSID = 1034
    m_Name = '#NT#能量障壁'
    m_SmashFunc = None
    m_InteractFunc = None

