# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_shop/goodsdata.pyc
# RelativePath: clientlogic/cl_shop/goodsdata.pyc
# Source Generated with Decompyle++
# File: goodsdata.pyc (Python 3.6)


class CGoodsData(object):
    m_SID = 0
    m_Name = ''
    m_GoodsType = None
    m_Items = ()

g_GoodsData = { }

def GetGoodsData(iSID):
    if iSID in g_GoodsData:
        return g_GoodsData[iSID]

from cl_commondefines import SHOPITEM_BULLET, SHOPITEM_CURSERELIC, SHOPITEM_RECOVER, SHOPITEM_RELIC, SHOPITEM_SUPER, SHOPITEM_THROW, VIRTUAL_ITEM_AUTOPERFORM, VIRTUAL_ITEM_BULLET, VIRTUAL_ITEM_GOLDENCUP, VIRTUAL_ITEM_RANDOM, VIRTUAL_ITEM_SHOPREFRESH

class CGoodsData1001(CGoodsData):
    m_SID = 1001
    m_Name = '弹药补给'
    m_GoodsType = VIRTUAL_ITEM_BULLET
    m_Items = ({
        'item': VIRTUAL_ITEM_BULLET,
        'info': {
            'bullet': {
                4502: 5000,
                4503: 1000,
                4504: 1000 } } },)


class CGoodsData1002(CGoodsData):
    m_SID = 1002
    m_Name = '商品刷新'
    m_GoodsType = VIRTUAL_ITEM_SHOPREFRESH
    m_Items = ({
        'item': VIRTUAL_ITEM_SHOPREFRESH,
        'info': { } },)


class CGoodsData1007(CGoodsData):
    m_SID = 1007
    m_Name = '神奇包子'
    m_GoodsType = VIRTUAL_ITEM_AUTOPERFORM
    m_Items = ({
        'item': VIRTUAL_ITEM_AUTOPERFORM,
        'info': {
            'sid': 1604,
            'data': { } } },)


class CGoodsData1008(CGoodsData):
    m_SID = 1008
    m_Name = '手雷补给'
    m_GoodsType = VIRTUAL_ITEM_BULLET
    m_Items = ({
        'item': VIRTUAL_ITEM_BULLET,
        'info': {
            'bullet': {
                4508: 50 } } },)


class CGoodsData1009(CGoodsData):
    m_SID = 1009
    m_Name = '灵羽补给'
    m_GoodsType = VIRTUAL_ITEM_BULLET
    m_Items = ({
        'item': VIRTUAL_ITEM_BULLET,
        'info': {
            'bullet': {
                4508: 50 } } },)


class CGoodsData1010(CGoodsData):
    m_SID = 1010
    m_Name = '神奇包子'
    m_GoodsType = VIRTUAL_ITEM_AUTOPERFORM
    m_Items = ({
        'item': VIRTUAL_ITEM_AUTOPERFORM,
        'info': {
            'sid': 1657,
            'data': { } } },)


class CGoodsData1011(CGoodsData):
    m_SID = 1011
    m_Name = '雷珠补给'
    m_GoodsType = VIRTUAL_ITEM_BULLET
    m_Items = ({
        'item': VIRTUAL_ITEM_BULLET,
        'info': {
            'bullet': {
                4508: 50 } } },)


class CGoodsData1012(CGoodsData):
    m_SID = 1012
    m_Name = '桃花补给'
    m_GoodsType = VIRTUAL_ITEM_BULLET
    m_Items = ({
        'item': VIRTUAL_ITEM_BULLET,
        'info': {
            'bullet': {
                4508: 50 } } },)


class CGoodsData1013(CGoodsData):
    m_SID = 1013
    m_Name = '贝壳补给'
    m_GoodsType = VIRTUAL_ITEM_BULLET
    m_Items = ({
        'item': VIRTUAL_ITEM_BULLET,
        'info': {
            'bullet': {
                4508: 50 } } },)


class CGoodsData1014(CGoodsData):
    m_SID = 1014
    m_Name = '铃铛补给'
    m_GoodsType = VIRTUAL_ITEM_BULLET
    m_Items = ({
        'item': VIRTUAL_ITEM_BULLET,
        'info': {
            'bullet': {
                4508: 50 } } },)


class CGoodsData1015(CGoodsData):
    m_SID = 1015
    m_Name = '灵镯补给'
    m_GoodsType = VIRTUAL_ITEM_BULLET
    m_Items = ({
        'item': VIRTUAL_ITEM_BULLET,
        'info': {
            'bullet': {
                4508: 50 } } },)


class CGoodsData1016(CGoodsData):
    m_SID = 1016
    m_Name = '卡包补给'
    m_GoodsType = VIRTUAL_ITEM_BULLET
    m_Items = ({
        'item': VIRTUAL_ITEM_BULLET,
        'info': {
            'bullet': {
                4508: 50 } } },)


class CGoodsData1017(CGoodsData):
    m_SID = 1017
    m_Name = '镜片补给'
    m_GoodsType = VIRTUAL_ITEM_BULLET
    m_Items = ({
        'item': VIRTUAL_ITEM_BULLET,
        'info': {
            'bullet': {
                4508: 50 } } },)


class CGoodsData1018(CGoodsData):
    m_SID = 1018
    m_Name = '补充状态'
    m_GoodsType = VIRTUAL_ITEM_AUTOPERFORM
    m_Items = ({
        'item': VIRTUAL_ITEM_AUTOPERFORM,
        'info': {
            'sid': 1720,
            'data': { } } },)


class CGoodsData1019(CGoodsData):
    m_SID = 1019
    m_Name = '金爵'
    m_GoodsType = VIRTUAL_ITEM_GOLDENCUP
    m_Items = ({
        'item': VIRTUAL_ITEM_GOLDENCUP,
        'info': {
            'sid': 1027 } },)


class CGoodsData1020(CGoodsData):
    m_SID = 1020
    m_Name = '手雷补给'
    m_GoodsType = VIRTUAL_ITEM_BULLET
    m_Items = ({
        'item': VIRTUAL_ITEM_BULLET,
        'info': {
            'bullet': {
                4508: 50 } } },)


class CGoodsData1021(CGoodsData):
    m_SID = 1021
    m_Name = '卷轴补给'
    m_GoodsType = VIRTUAL_ITEM_BULLET
    m_Items = ({
        'item': VIRTUAL_ITEM_BULLET,
        'info': {
            'bullet': {
                4508: 50 } } },)


class CGoodsData1022(CGoodsData):
    m_SID = 1022
    m_Name = '随机物品'
    m_GoodsType = VIRTUAL_ITEM_RANDOM
    m_Items = ({
        'item': VIRTUAL_ITEM_RANDOM,
        'info': {
            'ChooseWeight': {
                SHOPITEM_RELIC: 60,
                SHOPITEM_CURSERELIC: 25,
                SHOPITEM_THROW: 5,
                SHOPITEM_RECOVER: 5,
                SHOPITEM_BULLET: 5 },
            'ExtraInfo': { },
            'WeaponChooseMG': {
                1: 1001,
                2: 1001,
                3: 1001 },
            'RelicChooseMG': {
                1: 2401,
                2: 2401,
                3: 2401 } } },)


class CGoodsData1023(CGoodsData):
    m_SID = 1023
    m_Name = '随机物品'
    m_GoodsType = VIRTUAL_ITEM_RANDOM
    m_Items = ({
        'item': VIRTUAL_ITEM_RANDOM,
        'info': {
            'ChooseWeight': {
                SHOPITEM_SUPER: 5,
                SHOPITEM_RELIC: 55,
                SHOPITEM_CURSERELIC: 25,
                SHOPITEM_THROW: 5,
                SHOPITEM_RECOVER: 5,
                SHOPITEM_BULLET: 5 },
            'ExtraInfo': {
                'SuperWeaponWeight': 70,
                'SuperRelicWeight': 30,
                'SuperRelicLevel': 2,
                'SuperWeaponEnhance': 1 },
            'WeaponChooseMG': {
                1: 1001,
                2: 1001,
                3: 1001 },
            'RelicChooseMG': {
                1: 2401,
                2: 2401,
                3: 2401 } } },)


class CGoodsData1024(CGoodsData):
    m_SID = 1024
    m_Name = '自然元素球补给'
    m_GoodsType = VIRTUAL_ITEM_BULLET
    m_Items = ({
        'item': VIRTUAL_ITEM_BULLET,
        'info': {
            'bullet': {
                4508: 50 } } },)


class CGoodsData1025(CGoodsData):
    m_SID = 1025
    m_Name = '云纹补给'
    m_GoodsType = VIRTUAL_ITEM_BULLET
    m_Items = ({
        'item': VIRTUAL_ITEM_BULLET,
        'info': {
            'bullet': {
                4508: 50 } } },)

g_GoodsData[1001] = CGoodsData1001
g_GoodsData[1002] = CGoodsData1002
g_GoodsData[1007] = CGoodsData1007
g_GoodsData[1008] = CGoodsData1008
g_GoodsData[1009] = CGoodsData1009
g_GoodsData[1010] = CGoodsData1010
g_GoodsData[1011] = CGoodsData1011
g_GoodsData[1012] = CGoodsData1012
g_GoodsData[1013] = CGoodsData1013
g_GoodsData[1014] = CGoodsData1014
g_GoodsData[1015] = CGoodsData1015
g_GoodsData[1016] = CGoodsData1016
g_GoodsData[1017] = CGoodsData1017
g_GoodsData[1018] = CGoodsData1018
g_GoodsData[1019] = CGoodsData1019
g_GoodsData[1020] = CGoodsData1020
g_GoodsData[1021] = CGoodsData1021
g_GoodsData[1022] = CGoodsData1022
g_GoodsData[1023] = CGoodsData1023
g_GoodsData[1024] = CGoodsData1024
g_GoodsData[1025] = CGoodsData1025
