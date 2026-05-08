# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/keyitem/i6001.pyc
# RelativePath: clientlogic/cl_platformdata/pc/keyitem/i6001.pyc
# Source Generated with Decompyle++
# File: i6001.pyc (Python 3.6)

import cl_msgcenter
import cl_evact
import cl_evcon
import cl_action
import cl_condition
from . import keyitemdata
from cl_item.defines import KEYITEM_CANNONBALL

def AddAction(oOwner, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oOwner, oLifeCycle, cl_msgcenter.MSG_WAR_PLAYERLEAVEGAME, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oOwner, oLifeCycle, cl_msgcenter.MSG_WAR_DYING, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oOwner, oLifeCycle, cl_msgcenter.MSG_WAR_DIE, -1, 0, 0, 0)
    cl_action.ItemAddState(oOwner, oLifeCycle, 1171, 0, { }, 1)
    cl_action.CommonListenMsgCallBack(oOwner, oLifeCycle, cl_msgcenter.MSG_WAR_LEAVESCENE, -1, 0, 0, 0)


def CallBack0(oEventCB, oOwner):
    cl_evact.ItemCBDropSelf(oOwner, oEventCB)


class CItem(keyitemdata.CKeyItemData):
    m_SID = 6001
    m_Shape = 5509
    m_Type = KEYITEM_CANNONBALL
    m_Name = '炮弹'
    m_MaxAmount = 1
    m_MaxGroup = 1
    m_Action = (AddAction, None)
    m_CBFuncAction = {
        0: CallBack0 }

