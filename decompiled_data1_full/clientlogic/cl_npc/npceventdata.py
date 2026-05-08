# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_npc/npceventdata.pyc
# RelativePath: clientlogic/cl_npc/npceventdata.pyc
# Source Generated with Decompyle++
# File: npceventdata.pyc (Python 3.6)

from cl_npc.eventnpc import NPCEventData as CCustom
from cl_commondefines import *
import cl_npc.eventnpcaction as eventnpcaction
from cl_newformula import Func16, Func201, Func202, Func206, Func207, Func210, Func441, Func678
from cl_commondefines import CAL_BY_CURSE_RELIC, INSCRIPTION_TYPE_EXCLUSIVE, RELIC_TYPE_CURSE, RELIC_TYPE_NORMAL
from cl_item.defines import QUALITY_TYPE_CURSE, QUALITY_TYPE_HIGH, QUALITY_TYPE_LOW, QUALITY_TYPE_NORMAL, WEAPON_ACTION_ENHANCE, WEAPON_ACTION_RECAST, WEAPON_ACTION_UPGRADE, WEAPON_ACTION_UPGRADEINSCRIPTION
from math import ceil

def OptionInitCostAction100100(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (10 + Func201(*a) * 3 + Func202(*a) * 5) * Func16(*a, **{
'a': 10,
'b': 20 })))


def OptionInitRewardAction100100(oOption, oHero):
    eventnpcaction.InitWarCashReward(oOption, oHero, (lambda *a: (10 + Func201(*a) * 3 + Func202(*a) * 5) * Func16(*a, **{
'a': 100,
'b': 200 })), None, None)


def OptionInitCostAction100200(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (10 + Func201(*a) * 3 + Func202(*a) * 5) * Func16(*a, **{
'a': 10,
'b': 20 })))


def OptionInitRewardAction100200(oOption, oHero):
    eventnpcaction.InitWarCashReward(oOption, oHero, (lambda *a: (10 + Func201(*a) * 3 + Func202(*a) * 5) * Func16(*a, **{
'a': 100,
'b': 200 })), None, None)


def OptionInitCostAction100300(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (10 + Func201(*a) * 3 + Func202(*a) * 5) * Func16(*a, **{
'a': 10,
'b': 20 })))


def OptionInitRewardAction100300(oOption, oHero):
    eventnpcaction.InitAttrReward(oOption, oHero, 'HPMax', 0, 10000)


def OptionInitCostAction100400(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (10 + Func201(*a) * 3 + Func202(*a) * 5) * Func16(*a, **{
'a': 10,
'b': 20 })))


def OptionInitRewardAction100400(oOption, oHero):
    eventnpcaction.InitAttrReward(oOption, oHero, 'ShieldMax', 0, 10000)


def OptionInitCostAction100500(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (10 + Func201(*a) * 3 + Func202(*a) * 5) * Func16(*a, **{
'a': 10,
'b': 20 })))


def OptionInitRewardAction100500(oOption, oHero):
    eventnpcaction.InitRelicReward(oOption, oHero, 0, {
        5701: 10,
        5702: 10,
        5703: 10 }, None, { }, None)


def OptionInitCostAction100600(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (10 + Func201(*a) * 3 + Func202(*a) * 5) * Func16(*a, **{
'a': 10,
'b': 20 })))


def OptionInitRewardAction100600(oOption, oHero):
    eventnpcaction.InitRelicReward(oOption, oHero, 1, {
        5706: 10,
        5704: 10,
        5705: 10 }, None, { }, None)


def OptionInitCostAction100700(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (10 + Func201(*a) * 3 + Func202(*a) * 5) * Func16(*a, **{
'a': 10,
'b': 20 })))


def OptionInitRewardAction100700(oOption, oHero):
    eventnpcaction.InitGoldenCupReward(oOption, oHero, {
        3001: 30011027 })


def OptionInitCostAction100800(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (10 + Func201(*a) * 3 + Func202(*a) * 5) * Func16(*a, **{
'a': 10,
'b': 20 })))


def OptionInitRewardAction100800(oOption, oHero):
    eventnpcaction.InitWeaponReward(oOption, oHero, 0, {
        3001: 30011001 }, None, None, { }, None)


def OptionInitCostAction100900(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (10 + Func201(*a) * 3 + Func202(*a) * 5) * Func16(*a, **{
'a': 10,
'b': 20 })))


def OptionInitRewardAction100900(oOption, oHero):
    eventnpcaction.InitWeaponReward(oOption, oHero, 1, {
        3001: 30011001 }, None, None, { }, None)


def OptionInitCostAction101000(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (10 + Func201(*a) * 3 + Func202(*a) * 5) * Func16(*a, **{
'a': 10,
'b': 20 })))


def OptionInitRewardAction101000(oOption, oHero):
    eventnpcaction.InitHPReward(oOption, oHero, 100, 0)


def OptionInitCostAction101100(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (10 + Func201(*a) * 3 + Func202(*a) * 5) * Func16(*a, **{
'a': 10,
'b': 20 })))


def OptionInitRewardAction101100(oOption, oHero):
    eventnpcaction.InitWarCashReward(oOption, oHero, (lambda *a: (10 + Func201(*a) * 3 + Func202(*a) * 5) * Func16(*a, **{
'a': 100,
'b': 200 })), None, None)


def OptionInitCostAction101200(oOption, oHero):
    eventnpcaction.InitHPCost(oOption, oHero, 50, 0)


def OptionInitRewardAction101200(oOption, oHero):
    eventnpcaction.InitWarCashReward(oOption, oHero, (lambda *a: (10 + Func201(*a) * 3 + Func202(*a) * 5) * Func16(*a, **{
'a': 100,
'b': 200 })), None, None)


def OptionInitCostAction101300(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (10 + Func201(*a) * 3 + Func202(*a) * 5) * Func16(*a, **{
'a': 10,
'b': 20 })))


def OptionInitRewardAction101300(oOption, oHero):
    eventnpcaction.InitWarCashReward(oOption, oHero, (lambda *a: (10 + Func201(*a) * 3 + Func202(*a) * 5) * Func16(*a, **{
'a': 100,
'b': 200 })), 1, None)


def OptionInitCostAction101301(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (10 + Func201(*a) * 3 + Func202(*a) * 5) * Func16(*a, **{
'a': 10,
'b': 20 })))


def OptionInitRewardAction101301(oOption, oHero):
    eventnpcaction.InitWarCashReward(oOption, oHero, (lambda *a: (10 + Func201(*a) * 3 + Func202(*a) * 5) * Func16(*a, **{
'a': 100,
'b': 200 })), 0, None)


def OptionInitCostAction101302(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (10 + Func201(*a) * 3 + Func202(*a) * 5) * Func16(*a, **{
'a': 10,
'b': 20 })))


def OptionInitRewardAction101302(oOption, oHero):
    eventnpcaction.InitWeaponReward(oOption, oHero, 0, {
        3001: 30011001,
        3008: 30081001 }, 1, None, { }, None)


def OptionInitCostAction101400(oOption, oHero):
    eventnpcaction.InitAttrCost(oOption, oHero, 'ShieldMax', 0, 5000)


def OptionInitRewardAction101400(oOption, oHero):
    eventnpcaction.InitWarCashReward(oOption, oHero, (lambda *a: (10 + Func201(*a) * 3 + Func202(*a) * 5) * Func16(*a, **{
'a': 100,
'b': 200 })), None, None)


def OptionInitCostAction101500(oOption, oHero):
    eventnpcaction.InitRelicCost(oOption, oHero, 1, None)


def OptionInitRewardAction101500(oOption, oHero):
    eventnpcaction.InitWarCashReward(oOption, oHero, (lambda *a: (10 + Func201(*a) * 3 + Func202(*a) * 5) * Func16(*a, **{
'a': 100,
'b': 200 })), None, None)


def OptionInitCostAction101600(oOption, oHero):
    eventnpcaction.InitRelicCost(oOption, oHero, 0, None)


def OptionInitRewardAction101600(oOption, oHero):
    eventnpcaction.InitWarCashReward(oOption, oHero, (lambda *a: (10 + Func201(*a) * 3 + Func202(*a) * 5) * Func16(*a, **{
'a': 100,
'b': 200 })), None, None)


def OptionInitCostAction101700(oOption, oHero):
    eventnpcaction.InitCurseRelicCost(oOption, oHero, 1)


def OptionInitRewardAction101700(oOption, oHero):
    eventnpcaction.InitWarCashReward(oOption, oHero, (lambda *a: (10 + Func201(*a) * 3 + Func202(*a) * 5) * Func16(*a, **{
'a': 100,
'b': 200 })), None, None)


def OptionInitCostAction101800(oOption, oHero):
    eventnpcaction.InitCurseRelicCost(oOption, oHero, 0)


def OptionInitRewardAction101800(oOption, oHero):
    eventnpcaction.InitWarCashReward(oOption, oHero, (lambda *a: (10 + Func201(*a) * 3 + Func202(*a) * 5) * Func16(*a, **{
'a': 100,
'b': 200 })), None, None)


def OptionInitCostAction101900(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (10 + Func201(*a) * 3 + Func202(*a) * 5) * Func16(*a, **{
'a': 10,
'b': 20 })))


def OptionInitRewardAction101900(oOption, oHero):
    eventnpcaction.InitWarCashReward(oOption, oHero, (lambda *a: (10 + Func201(*a) * 3 + Func202(*a) * 5) * Func16(*a, **{
'a': 100,
'b': 200 })), 1, None)


def OptionInitCostAction101901(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (10 + Func201(*a) * 3 + Func202(*a) * 5) * Func16(*a, **{
'a': 10,
'b': 20 })))


def OptionInitRewardAction101901(oOption, oHero):
    eventnpcaction.InitWarCashReward(oOption, oHero, (lambda *a: (10 + Func201(*a) * 3 + Func202(*a) * 5) * Func16(*a, **{
'a': 100,
'b': 200 })), 0, None)


def OptionInitCostAction101902(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (10 + Func201(*a) * 3 + Func202(*a) * 5) * Func16(*a, **{
'a': 10,
'b': 20 })))


def OptionInitRewardAction101902(oOption, oHero):
    eventnpcaction.InitWeaponReward(oOption, oHero, 0, {
        3001: 30011001,
        3008: 30081001 }, 1, None, { }, None)


def OptionInitCostAction102000(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (10 + Func201(*a) * 3 + Func202(*a) * 5) * Func16(*a, **{
'a': 10,
'b': 20 })))


def OptionInitRewardAction102000(oOption, oHero):
    eventnpcaction.InitWarCashReward(oOption, oHero, (lambda *a: (10 + Func201(*a) * 3 + Func202(*a) * 5) * Func16(*a, **{
'a': 100,
'b': 200 })), None, None)


def OptionInitCostAction102001(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (10 + Func201(*a) * 3 + Func202(*a) * 5) * Func16(*a, **{
'a': 10,
'b': 20 })))


def OptionInitRewardAction102001(oOption, oHero):
    eventnpcaction.InitWarCashReward(oOption, oHero, (lambda *a: (10 + Func201(*a) * 3 + Func202(*a) * 5) * Func16(*a, **{
'a': 100,
'b': 200 })), None, None)


def OptionInitCostAction102002(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (10 + Func201(*a) * 3 + Func202(*a) * 5) * Func16(*a, **{
'a': 10,
'b': 20 })))


def OptionInitRewardAction102002(oOption, oHero):
    eventnpcaction.InitWarCashReward(oOption, oHero, (lambda *a: (10 + Func201(*a) * 3 + Func202(*a) * 5) * Func16(*a, **{
'a': 100,
'b': 200 })), None, None)


def OptionInitCostAction102100(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (10 + Func201(*a) * 3 + Func202(*a) * 5) * Func16(*a, **{
'a': 10,
'b': 20 })))


def OptionInitRewardAction102100(oOption, oHero):
    eventnpcaction.InitWarCashReward(oOption, oHero, (lambda *a: (10 + Func201(*a) * 3 + Func202(*a) * 5) * Func16(*a, **{
'a': 100,
'b': 200 })), None, None)


def OptionInitCostAction102101(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (10 + Func201(*a) * 3 + Func202(*a) * 5) * Func16(*a, **{
'a': 10,
'b': 20 })))


def OptionInitRewardAction102101(oOption, oHero):
    eventnpcaction.InitWarCashReward(oOption, oHero, (lambda *a: (10 + Func201(*a) * 3 + Func202(*a) * 5) * Func16(*a, **{
'a': 100,
'b': 200 })), None, None)


def OptionInitCostAction102102(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (10 + Func201(*a) * 3 + Func202(*a) * 5) * Func16(*a, **{
'a': 10,
'b': 20 })))


def OptionInitRewardAction102102(oOption, oHero):
    eventnpcaction.InitWarCashReward(oOption, oHero, (lambda *a: (10 + Func201(*a) * 3 + Func202(*a) * 5) * Func16(*a, **{
'a': 100,
'b': 200 })), None, None)


def OptionInitCostAction102103(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (10 + Func201(*a) * 3 + Func202(*a) * 5) * Func16(*a, **{
'a': 10,
'b': 20 })))


def OptionInitRewardAction102103(oOption, oHero):
    eventnpcaction.InitWarCashReward(oOption, oHero, (lambda *a: (10 + Func201(*a) * 3 + Func202(*a) * 5) * Func16(*a, **{
'a': 100,
'b': 200 })), None, None)


def OptionInitCostAction102200(oOption, oHero):
    eventnpcaction.InitSelectedRelicCost(oOption, oHero, RELIC_TYPE_NORMAL | RELIC_TYPE_CURSE, QUALITY_TYPE_LOW | QUALITY_TYPE_NORMAL | QUALITY_TYPE_HIGH | QUALITY_TYPE_CURSE, 1, None)


def OptionInitRewardAction102200(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 1, WEAPON_ACTION_UPGRADE, { })


def OptionInitCostAction102201(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (10 + Func201(*a) * 3 + Func202(*a) * 5) * Func16(*a, **{
'a': 10,
'b': 20 })))


def OptionInitRewardAction102201(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 1, WEAPON_ACTION_RECAST, { })


def OptionInitCostAction102202(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (10 + Func201(*a) * 3 + Func202(*a) * 5) * Func16(*a, **{
'a': 10,
'b': 20 })))


def OptionInitRewardAction102202(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 1, WEAPON_ACTION_UPGRADEINSCRIPTION, {
        'InscriptionCnt': 1 })


def OptionInitCostAction102203(oOption, oHero):
    eventnpcaction.InitSelectedRelicCost(oOption, oHero, RELIC_TYPE_NORMAL | RELIC_TYPE_CURSE, QUALITY_TYPE_LOW | QUALITY_TYPE_NORMAL | QUALITY_TYPE_HIGH | QUALITY_TYPE_CURSE, 1, None)


def OptionInitRewardAction102203(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 2, WEAPON_ACTION_UPGRADE, { })


def OptionInitRewardAction102300(oOption, oHero):
    eventnpcaction.InitWeaponReward(oOption, oHero, 1, {
        3001: 30011004 }, 1, None, { }, None)


def OptionInitRewardAction102400(oOption, oHero):
    eventnpcaction.InitWeaponReward(oOption, oHero, 1, {
        3001: 30011005 }, 1, None, { }, None)


def OptionInitCostAction110100(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: min(int(Func16(*a, **{
'a': 60,
'b': 70 }) * 10.3), int((0.1 + Func201(*a) * 1.5 + Func202(*a) * 0.3) * Func16(*a, **{
'a': 60,
'b': 70 })))))


def OptionInitRewardAction110100(oOption, oHero):
    eventnpcaction.InitRelicReward(oOption, oHero, 0, {
        5701: 15,
        5705: 10,
        5706: 15,
        5707: 10,
        5708: 15,
        5709: 15,
        5712: 15,
        5713: 10,
        5714: 15,
        5715: 10,
        5718: 15,
        5720: 5,
        5728: 15,
        5729: 15,
        5730: 10,
        5732: 10,
        5735: 10,
        5736: 10,
        5739: 5,
        5741: 10,
        5742: 5,
        5745: 10,
        5746: 10,
        5754: 15,
        5755: 10,
        5758: 5,
        5759: 10,
        5760: 15,
        5762: 15,
        5763: 10,
        5764: 15,
        5769: 15,
        5771: 10,
        5774: 10 }, 1, { }, None)


def OptionInitCostAction110101(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: min(int(Func16(*a, **{
'a': 90,
'b': 100 }) * 10.3), int((0.1 + Func201(*a) * 1.5 + Func202(*a) * 0.3) * Func16(*a, **{
'a': 90,
'b': 100 })))))


def OptionInitRewardAction110101(oOption, oHero):
    eventnpcaction.InitRelicReward(oOption, oHero, 1, {
        5701: 15,
        5705: 10,
        5706: 15,
        5707: 10,
        5708: 15,
        5709: 15,
        5712: 15,
        5713: 10,
        5714: 15,
        5715: 10,
        5718: 15,
        5720: 5,
        5728: 15,
        5729: 15,
        5730: 10,
        5732: 10,
        5735: 10,
        5736: 10,
        5739: 5,
        5741: 10,
        5742: 5,
        5745: 10,
        5746: 10,
        5754: 15,
        5755: 10,
        5758: 5,
        5759: 10,
        5760: 15,
        5762: 15,
        5763: 10,
        5764: 15,
        5769: 15,
        5771: 10,
        5774: 10 }, 1, { }, None)


def OptionInitCostAction110102(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: min(int(Func16(*a, **{
'a': 90,
'b': 100 }) * 10.3), int((0.1 + Func201(*a) * 1.5 + Func202(*a) * 0.3) * Func16(*a, **{
'a': 90,
'b': 100 })))))


def OptionInitRewardAction110102(oOption, oHero):
    eventnpcaction.InitWeaponReward(oOption, oHero, 1, {
        3001: 30011001,
        3008: 30081001,
        3007: 30071001,
        3009: 30091001,
        3012: 30121001 }, 1, None, { }, None)


def OptionInitCostAction110200(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (0.1 + Func201(*a) * 1.5 + Func202(*a) * 0.3) * Func16(*a, **{
'a': 90,
'b': 100 })))


def OptionInitRewardAction110200(oOption, oHero):
    eventnpcaction.InitAttrReward(oOption, oHero, 'HPMax', 0, 1800)


def OptionInitCostAction110201(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (0.1 + Func201(*a) * 1.5 + Func202(*a) * 0.3) * Func16(*a, **{
'a': 90,
'b': 100 })))


def OptionInitRewardAction110201(oOption, oHero):
    eventnpcaction.InitAttrReward(oOption, oHero, 'ShieldMax', 0, 1200)


def OptionInitCostAction110300(oOption, oHero):
    eventnpcaction.InitCurseRelicCost(oOption, oHero, 1)


def OptionInitRewardAction110300(oOption, oHero):
    eventnpcaction.InitRelicReward(oOption, oHero, 0, { }, 1, {
        1: {
            3001: {
                30012401: 100 },
            3008: {
                30082401: 100 },
            3007: {
                30072401: 100 },
            3009: {
                30092401: 100 },
            3010: {
                30102401: 100 },
            3012: {
                30122401: 100 } },
        2: {
            3001: {
                30012401: 100 },
            3008: {
                30082401: 100 },
            3007: {
                30072401: 100 },
            3009: {
                30092401: 100 },
            3012: {
                30122401: 100 } },
        3: {
            3001: {
                30012401: 100 },
            3008: {
                30082401: 100 },
            3007: {
                30072401: 100 },
            3009: {
                30092401: 100 },
            3012: {
                30122401: 100 } } }, None)


def OptionInitCostAction110301(oOption, oHero):
    eventnpcaction.InitCurseRelicCost(oOption, oHero, 1)


def OptionInitRewardAction110301(oOption, oHero):
    eventnpcaction.InitWeaponReward(oOption, oHero, 1, {
        3001: 30011001,
        3008: 30081001,
        3007: 30071001,
        3009: 30091001,
        3012: 30121001 }, 1, None, { }, None)


def OptionInitCostAction110302(oOption, oHero):
    eventnpcaction.InitCurseRelicCost(oOption, oHero, 1)


def OptionInitRewardAction110302(oOption, oHero):
    eventnpcaction.InitWarCashReward(oOption, oHero, (lambda *a: (0.1 + Func201(*a) * 1.5 + Func202(*a) * 0.3) * Func16(*a, **{
'a': 90,
'b': 100 })), 1, None)


def OptionInitCostAction110400(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (0.1 + Func201(*a) * 1.5 + Func202(*a) * 0.3) * Func16(*a, **{
'a': 90,
'b': 100 })))


def OptionInitRewardAction110400(oOption, oHero):
    eventnpcaction.InitGoldenCupReward(oOption, oHero, {
        3001: 30011027,
        3007: 30071027,
        3012: 30121027 })


def OptionInitCostAction110401(oOption, oHero):
    eventnpcaction.InitCurseRelicCost(oOption, oHero, 0)


def OptionInitRewardAction110401(oOption, oHero):
    eventnpcaction.InitGoldenCupReward(oOption, oHero, {
        3001: 30011027,
        3007: 30071027,
        3012: 30121027 })


def OptionInitCostAction110402(oOption, oHero):
    eventnpcaction.InitRelicCost(oOption, oHero, 0, None)


def OptionInitRewardAction110402(oOption, oHero):
    eventnpcaction.InitGoldenCupReward(oOption, oHero, {
        3001: 30011027,
        3007: 30071027,
        3012: 30121027 })


def OptionInitCostAction110500(oOption, oHero):
    eventnpcaction.InitHPCost(oOption, oHero, 25, 0)


def OptionInitRewardAction110500(oOption, oHero):
    eventnpcaction.InitWarCashReward(oOption, oHero, (lambda *a: (0.1 + Func201(*a) * 0.5 + Func202(*a) * 0.1) * Func16(*a, **{
'a': 90,
'b': 100 })), 1, None)


def OptionInitCostAction110501(oOption, oHero):
    eventnpcaction.InitHPCost(oOption, oHero, 50, 0)


def OptionInitRewardAction110501(oOption, oHero):
    eventnpcaction.InitWarCashReward(oOption, oHero, (lambda *a: (0.1 + Func201(*a) * 1 + Func202(*a) * 0.2) * Func16(*a, **{
'a': 95,
'b': 110 })), 1, None)


def OptionInitCostAction110502(oOption, oHero):
    eventnpcaction.InitHPCost(oOption, oHero, 75, 0)


def OptionInitRewardAction110502(oOption, oHero):
    eventnpcaction.InitWarCashReward(oOption, oHero, (lambda *a: (0.1 + Func201(*a) * 1.5 + Func202(*a) * 0.3) * Func16(*a, **{
'a': 115,
'b': 125 })), 1, None)


def OptionInitCostAction110600(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (0.1 + Func201(*a) * 1.5 + Func202(*a) * 0.3) * Func16(*a, **{
'a': 60,
'b': 70 })))


def OptionInitRewardAction110600(oOption, oHero):
    eventnpcaction.InitRelicReward(oOption, oHero, 0, { }, 1, {
        1: {
            3001: {
                30012401: 100 },
            3008: {
                30082401: 100 },
            3007: {
                30072401: 100 },
            3009: {
                30092401: 100 },
            3010: {
                30102401: 100 },
            3012: {
                30122401: 100 } },
        2: {
            3001: {
                30012401: 100 },
            3008: {
                30082401: 100 },
            3007: {
                30072401: 100 },
            3009: {
                30092401: 100 },
            3012: {
                30122401: 100 } },
        3: {
            3001: {
                30012401: 100 },
            3008: {
                30082401: 100 },
            3007: {
                30072401: 100 },
            3009: {
                30092401: 100 },
            3012: {
                30122401: 100 } } }, None)


def OptionInitCostAction110601(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (0.1 + Func201(*a) * 1.5 + Func202(*a) * 0.3) * Func16(*a, **{
'a': 57,
'b': 67 })))


def OptionInitRewardAction110601(oOption, oHero):
    eventnpcaction.InitWeaponReward(oOption, oHero, 0, {
        3001: 30011001,
        3005: 30051001,
        3008: 30081001,
        3007: 30071001,
        3009: 30091001,
        3010: 30101001,
        3012: 30121001 }, 1, None, { }, None)


def OptionInitCostAction110700(oOption, oHero):
    eventnpcaction.InitHPCost(oOption, oHero, 30, 0)


def OptionInitRewardAction110700(oOption, oHero):
    eventnpcaction.InitWarCashReward(oOption, oHero, (lambda *a: (0.1 + Func201(*a) * 1.5 + Func202(*a) * 0.1) * Func16(*a, **{
'a': 60,
'b': 70 })), 1, None)


def OptionInitCostAction110701(oOption, oHero):
    eventnpcaction.InitHPCost(oOption, oHero, 40, 0)


def OptionInitRewardAction110701(oOption, oHero):
    eventnpcaction.InitRelicReward(oOption, oHero, 0, { }, 1, {
        1: {
            3001: {
                30012401: 100 },
            3008: {
                30082401: 100 },
            3007: {
                30072401: 100 },
            3009: {
                30092401: 100 },
            3010: {
                30102401: 100 },
            3012: {
                30122401: 100 } },
        2: {
            3001: {
                30012401: 100 },
            3008: {
                30082401: 100 },
            3007: {
                30072401: 100 },
            3009: {
                30092401: 100 },
            3012: {
                30122401: 100 } },
        3: {
            3001: {
                30012401: 100 },
            3008: {
                30082401: 100 },
            3007: {
                30072401: 100 },
            3009: {
                30092401: 100 },
            3012: {
                30122401: 100 } } }, None)


def OptionInitCostAction110702(oOption, oHero):
    eventnpcaction.InitHPCost(oOption, oHero, 35, 0)


def OptionInitRewardAction110702(oOption, oHero):
    eventnpcaction.InitWeaponReward(oOption, oHero, 0, {
        3001: 30011001,
        3005: 30051001,
        3008: 30081001,
        3007: 30071001,
        3009: 30091001,
        3010: 30101001,
        3012: 30121001 }, 1, None, { }, None)


def OptionInitCostAction110800(oOption, oHero):
    eventnpcaction.InitHPCost(oOption, oHero, 40, 0)


def OptionInitRewardAction110800(oOption, oHero):
    eventnpcaction.InitWarCashReward(oOption, oHero, (lambda *a: (0.1 + Func201(*a) * 1.5 + Func202(*a) * 0.3) * Func16(*a, **{
'a': 60,
'b': 70 })), 1, None)


def OptionInitCostAction110801(oOption, oHero):
    eventnpcaction.InitCurseRelicCost(oOption, oHero, 0)


def OptionInitRewardAction110801(oOption, oHero):
    eventnpcaction.InitRelicReward(oOption, oHero, 0, {
        5701: 15,
        5705: 10,
        5706: 15,
        5707: 10,
        5708: 15,
        5709: 15,
        5712: 15,
        5713: 10,
        5714: 15,
        5715: 10,
        5718: 15,
        5720: 5,
        5728: 15,
        5729: 15,
        5730: 10,
        5732: 10,
        5735: 10,
        5736: 10,
        5739: 5,
        5741: 10,
        5742: 5,
        5745: 10,
        5746: 10,
        5754: 15,
        5755: 10,
        5758: 5,
        5759: 10,
        5760: 15,
        5762: 15,
        5763: 10,
        5764: 15,
        5769: 15,
        5771: 10,
        5774: 10 }, 1, { }, None)


def OptionInitCostAction110802(oOption, oHero):
    eventnpcaction.InitCurseRelicCost(oOption, oHero, 0)


def OptionInitRewardAction110802(oOption, oHero):
    eventnpcaction.InitWeaponReward(oOption, oHero, 0, {
        3001: 30011001,
        3008: 30081001,
        3007: 30071001,
        3009: 30091001,
        3012: 30121001 }, 1, None, { }, None)


def OptionInitCostAction110900(oOption, oHero):
    eventnpcaction.InitHPCost(oOption, oHero, 45, 0)


def OptionInitRewardAction110900(oOption, oHero):
    eventnpcaction.InitAttrReward(oOption, oHero, 'HPMax', 0, 2400)


def OptionInitCostAction110901(oOption, oHero):
    eventnpcaction.InitHPCost(oOption, oHero, 45, 0)


def OptionInitRewardAction110901(oOption, oHero):
    eventnpcaction.InitAttrReward(oOption, oHero, 'ShieldMax', 0, 1600)


def OptionInitCostAction111000(oOption, oHero):
    eventnpcaction.InitRelicCost(oOption, oHero, 1, None)


def OptionInitRewardAction111000(oOption, oHero):
    eventnpcaction.InitWeaponReward(oOption, oHero, 1, {
        3001: 30011001,
        3008: 30081001,
        3007: 30071001,
        3009: 30091001,
        3012: 30121001 }, 1, None, { }, None)


def OptionInitCostAction111001(oOption, oHero):
    eventnpcaction.InitCurseRelicCost(oOption, oHero, 0)


def OptionInitRewardAction111001(oOption, oHero):
    eventnpcaction.InitWeaponReward(oOption, oHero, 1, {
        3001: 30011001,
        3008: 30081001,
        3007: 30071001,
        3009: 30091001,
        3012: 30121001 }, 1, None, { }, None)


def OptionInitCostAction111002(oOption, oHero):
    eventnpcaction.InitHPCost(oOption, oHero, 50, 0)


def OptionInitRewardAction111002(oOption, oHero):
    eventnpcaction.InitWeaponReward(oOption, oHero, 1, {
        3001: 30011001,
        3008: 30081001,
        3007: 30071001,
        3009: 30091001,
        3012: 30121001 }, 1, None, { }, None)


def OptionInitCostAction111100(oOption, oHero):
    eventnpcaction.InitRelicCost(oOption, oHero, 1, None)


def OptionInitRewardAction111100(oOption, oHero):
    eventnpcaction.InitGoldenCupReward(oOption, oHero, {
        3001: 30011027,
        3007: 30071027,
        3012: 30121027 })


def OptionInitCostAction111101(oOption, oHero):
    eventnpcaction.InitCurseRelicCost(oOption, oHero, 0)


def OptionInitRewardAction111101(oOption, oHero):
    eventnpcaction.InitGoldenCupReward(oOption, oHero, {
        3001: 30011027,
        3007: 30071027,
        3012: 30121027 })


def OptionInitCostAction111102(oOption, oHero):
    eventnpcaction.InitHPCost(oOption, oHero, 75, 0)


def OptionInitRewardAction111102(oOption, oHero):
    eventnpcaction.InitGoldenCupReward(oOption, oHero, {
        3001: 30011027,
        3007: 30071027,
        3012: 30121027 })


def OptionInitCostAction111200(oOption, oHero):
    eventnpcaction.InitCurseRelicCost(oOption, oHero, 0)


def OptionInitRewardAction111200(oOption, oHero):
    eventnpcaction.InitRelicReward(oOption, oHero, 1, {
        5701: 15,
        5705: 10,
        5706: 15,
        5707: 10,
        5708: 15,
        5709: 15,
        5712: 15,
        5713: 10,
        5714: 15,
        5715: 10,
        5718: 15,
        5720: 5,
        5728: 15,
        5729: 15,
        5730: 10,
        5732: 10,
        5735: 10,
        5736: 10,
        5739: 5,
        5741: 10,
        5742: 5,
        5745: 10,
        5746: 10,
        5754: 15,
        5755: 10,
        5758: 5,
        5759: 10,
        5760: 15,
        5762: 15,
        5763: 10,
        5764: 15,
        5769: 15,
        5771: 10,
        5774: 10 }, 1, { }, None)


def OptionInitCostAction111201(oOption, oHero):
    eventnpcaction.InitRelicCost(oOption, oHero, 1, None)


def OptionInitRewardAction111201(oOption, oHero):
    eventnpcaction.InitRelicReward(oOption, oHero, 1, {
        5701: 15,
        5705: 10,
        5706: 15,
        5707: 10,
        5708: 15,
        5709: 15,
        5712: 15,
        5713: 10,
        5714: 15,
        5715: 10,
        5718: 15,
        5720: 5,
        5728: 15,
        5729: 15,
        5730: 10,
        5732: 10,
        5735: 10,
        5736: 10,
        5739: 5,
        5741: 10,
        5742: 5,
        5745: 10,
        5746: 10,
        5754: 15,
        5755: 10,
        5758: 5,
        5759: 10,
        5760: 15,
        5762: 15,
        5763: 10,
        5764: 15,
        5769: 15,
        5771: 10,
        5774: 10 }, 1, { }, None)


def OptionInitCostAction111202(oOption, oHero):
    eventnpcaction.InitHPCost(oOption, oHero, 75, 0)


def OptionInitRewardAction111202(oOption, oHero):
    eventnpcaction.InitRelicReward(oOption, oHero, 1, {
        5701: 15,
        5705: 10,
        5706: 15,
        5707: 10,
        5708: 15,
        5709: 15,
        5712: 15,
        5713: 10,
        5714: 15,
        5715: 10,
        5718: 15,
        5720: 5,
        5728: 15,
        5729: 15,
        5730: 10,
        5732: 10,
        5735: 10,
        5736: 10,
        5739: 5,
        5741: 10,
        5742: 5,
        5745: 10,
        5746: 10,
        5754: 15,
        5755: 10,
        5758: 5,
        5759: 10,
        5760: 15,
        5762: 15,
        5763: 10,
        5764: 15,
        5769: 15,
        5771: 10,
        5774: 10 }, 1, { }, None)


def OptionInitCostAction111300(oOption, oHero):
    eventnpcaction.InitHPCost(oOption, oHero, 45, 0)


def OptionInitRewardAction111300(oOption, oHero):
    eventnpcaction.InitRelicReward(oOption, oHero, 0, { }, 1, {
        1: {
            3001: {
                30012401: 100 },
            3008: {
                30082401: 100 },
            3007: {
                30072401: 100 },
            3009: {
                30092401: 100 },
            3010: {
                30102401: 100 },
            3012: {
                30122401: 100 } },
        2: {
            3001: {
                30012401: 100 },
            3008: {
                30082401: 100 },
            3007: {
                30072401: 100 },
            3009: {
                30092401: 100 },
            3012: {
                30122401: 100 } },
        3: {
            3001: {
                30012401: 100 },
            3008: {
                30082401: 100 },
            3007: {
                30072401: 100 },
            3009: {
                30092401: 100 },
            3012: {
                30122401: 100 } } }, None)


def OptionInitCostAction111301(oOption, oHero):
    eventnpcaction.InitRelicCost(oOption, oHero, 1, None)


def OptionInitRewardAction111301(oOption, oHero):
    eventnpcaction.InitRelicReward(oOption, oHero, 0, { }, 1, {
        1: {
            3001: {
                30012401: 100 },
            3008: {
                30082401: 100 },
            3007: {
                30072401: 100 },
            3009: {
                30092401: 100 },
            3010: {
                30102401: 100 },
            3012: {
                30122401: 100 } },
        2: {
            3001: {
                30012401: 100 },
            3008: {
                30082401: 100 },
            3007: {
                30072401: 100 },
            3009: {
                30092401: 100 },
            3012: {
                30122401: 100 } },
        3: {
            3001: {
                30012401: 100 },
            3008: {
                30082401: 100 },
            3007: {
                30072401: 100 },
            3009: {
                30092401: 100 },
            3012: {
                30122401: 100 } } }, None)


def OptionInitCostAction111302(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (0.1 + Func201(*a) * 1.5 + Func202(*a) * 0.3) * Func16(*a, **{
'a': 65,
'b': 72 })))


def OptionInitRewardAction111302(oOption, oHero):
    eventnpcaction.InitRelicReward(oOption, oHero, 0, { }, 1, {
        1: {
            3001: {
                30012401: 100 },
            3008: {
                30082401: 100 },
            3007: {
                30072401: 100 },
            3009: {
                30092401: 100 },
            3010: {
                30102401: 100 },
            3012: {
                30122401: 100 } },
        2: {
            3001: {
                30012401: 100 },
            3008: {
                30082401: 100 },
            3007: {
                30072401: 100 },
            3009: {
                30092401: 100 },
            3012: {
                30122401: 100 } },
        3: {
            3001: {
                30012401: 100 },
            3008: {
                30082401: 100 },
            3007: {
                30072401: 100 },
            3009: {
                30092401: 100 },
            3012: {
                30122401: 100 } } }, None)


def OptionInitCostAction200100(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (0.1 + Func201(*a) * 1.5 + Func202(*a) * 0.3) * Func16(*a, **{
'a': 40,
'b': 50 })))


def OptionInitRewardAction200100(oOption, oHero):
    eventnpcaction.InitRelicReward(oOption, oHero, 0, { }, 1, {
        1: {
            3001: {
                30012104: 50,
                30012108: 35,
                30012117: 15 },
            3005: {
                30052104: 50,
                30052108: 35,
                30052117: 15 },
            3008: {
                30082104: 50,
                30082108: 35,
                30082117: 15 },
            3007: {
                30072104: 50,
                30072108: 35,
                30072117: 15 },
            3009: {
                30092104: 50,
                30092108: 35,
                30092117: 15 },
            3010: {
                30102104: 50,
                30102108: 35,
                30102117: 15 },
            3012: {
                30122104: 50,
                30122108: 35,
                30122117: 15 } },
        2: {
            3001: {
                30012104: 40,
                30012108: 48,
                30012117: 12 },
            3005: {
                30052104: 40,
                30052108: 48,
                30052117: 12 },
            3008: {
                30082104: 40,
                30082108: 48,
                30082117: 12 },
            3007: {
                30072104: 40,
                30072108: 48,
                30072117: 12 },
            3009: {
                30092104: 40,
                30092108: 48,
                30092117: 12 },
            3012: {
                30122104: 40,
                30122108: 48,
                30122117: 12 } },
        3: {
            3001: {
                30012104: 40,
                30012108: 48,
                30012117: 12 },
            3005: {
                30052104: 40,
                30052108: 48,
                30052117: 12 },
            3008: {
                30082104: 40,
                30082108: 48,
                30082117: 12 },
            3007: {
                30072104: 40,
                30072108: 48,
                30072117: 12 },
            3009: {
                30092104: 40,
                30092108: 48,
                30092117: 12 },
            3012: {
                30122104: 40,
                30122108: 48,
                30122117: 12 } } }, None)


def OptionInitCostAction200101(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (0.1 + Func201(*a) * 1.5 + Func202(*a) * 0.3) * Func16(*a, **{
'a': 65,
'b': 75 })))


def OptionInitRewardAction200101(oOption, oHero):
    eventnpcaction.InitRelicReward(oOption, oHero, 0, { }, 1, {
        1: {
            3001: {
                30012104: 40,
                30012108: 47,
                30012112: 8,
                30012117: 5 },
            3005: {
                30052104: 40,
                30052108: 47,
                30052112: 8,
                30052117: 5 },
            3008: {
                30082104: 40,
                30082108: 47,
                30082112: 8,
                30082117: 5 },
            3007: {
                30072104: 40,
                30072108: 47,
                30072112: 8,
                30072117: 5 },
            3009: {
                30092104: 40,
                30092108: 47,
                30092112: 8,
                30092117: 5 },
            3010: {
                30102104: 40,
                30102108: 47,
                30102112: 8,
                30102117: 5 },
            3012: {
                30122104: 40,
                30122108: 47,
                30122112: 8,
                30122117: 5 } },
        2: {
            3001: {
                30012104: 25,
                30012108: 55,
                30012112: 17,
                30012117: 3 },
            3005: {
                30052104: 25,
                30052108: 55,
                30052112: 17,
                30052117: 3 },
            3008: {
                30082104: 25,
                30082108: 55,
                30082112: 17,
                30082117: 3 },
            3007: {
                30072104: 25,
                30072108: 55,
                30072112: 17,
                30072117: 3 },
            3009: {
                30092104: 25,
                30092108: 55,
                30092112: 17,
                30092117: 3 },
            3012: {
                30122104: 25,
                30122108: 55,
                30122112: 17,
                30122117: 3 } },
        3: {
            3001: {
                30012104: 25,
                30012108: 55,
                30012112: 17,
                30012117: 3 },
            3005: {
                30052104: 25,
                30052108: 55,
                30052112: 17,
                30052117: 3 },
            3008: {
                30082104: 25,
                30082108: 55,
                30082112: 17,
                30082117: 3 },
            3007: {
                30072104: 25,
                30072108: 55,
                30072112: 17,
                30072117: 3 },
            3009: {
                30092104: 25,
                30092108: 55,
                30092112: 17,
                30092117: 3 },
            3012: {
                30122104: 25,
                30122108: 55,
                30122112: 17,
                30122117: 3 } } }, None)


def OptionInitCostAction200102(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (0.1 + Func201(*a) * 1.5 + Func202(*a) * 0.3) * Func16(*a, **{
'a': 95,
'b': 110 })))


def OptionInitRewardAction200102(oOption, oHero):
    eventnpcaction.InitRelicReward(oOption, oHero, 0, { }, 1, {
        1: {
            3001: {
                30012104: 40,
                30012108: 48,
                30012112: 12 },
            3005: {
                30052104: 40,
                30052108: 48,
                30052112: 12 },
            3008: {
                30082104: 40,
                30082108: 48,
                30082112: 12 },
            3007: {
                30072104: 40,
                30072108: 48,
                30072112: 12 },
            3009: {
                30092104: 40,
                30092108: 48,
                30092112: 12 },
            3010: {
                30102104: 40,
                30102108: 48,
                30102112: 12 },
            3012: {
                30122104: 40,
                30122108: 48,
                30122112: 12 } },
        2: {
            3001: {
                30012104: 20,
                30012108: 60,
                30012112: 20 },
            3005: {
                30052104: 20,
                30052108: 60,
                30052112: 20 },
            3008: {
                30082104: 20,
                30082108: 60,
                30082112: 20 },
            3007: {
                30072104: 20,
                30072108: 60,
                30072112: 20 },
            3009: {
                30092104: 20,
                30092108: 60,
                30092112: 20 },
            3012: {
                30122104: 20,
                30122108: 60,
                30122112: 20 } },
        3: {
            3001: {
                30012104: 20,
                30012108: 60,
                30012112: 20 },
            3005: {
                30052104: 20,
                30052108: 60,
                30052012: 20 },
            3008: {
                30082104: 20,
                30082108: 60,
                30082112: 20 },
            3007: {
                30072104: 20,
                30072108: 60,
                30072112: 20 },
            3009: {
                30092104: 20,
                30092108: 60,
                30092112: 20 },
            3012: {
                30122104: 20,
                30122108: 60,
                30122112: 20 } } }, None)


def OptionInitCostAction200200(oOption, oHero):
    eventnpcaction.InitHPCost(oOption, oHero, 35, 0)


def OptionInitRewardAction200200(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 1, WEAPON_ACTION_RECAST, { })


def OptionInitCostAction200201(oOption, oHero):
    eventnpcaction.InitHPCost(oOption, oHero, 35, 0)


def OptionInitRewardAction200201(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 2, WEAPON_ACTION_RECAST, { })


def OptionInitCostAction200202(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (0.1 + Func201(*a) * 1.5 + Func202(*a) * 0.3) * Func16(*a, **{
'a': 40,
'b': 50 })))


def OptionInitRewardAction200202(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 1, WEAPON_ACTION_UPGRADEINSCRIPTION, {
        'InscriptionCnt': 1 })


def OptionInitCostAction200203(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (0.1 + Func201(*a) * 1.5 + Func202(*a) * 0.3) * Func16(*a, **{
'a': 40,
'b': 50 })))


def OptionInitRewardAction200203(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 2, WEAPON_ACTION_UPGRADEINSCRIPTION, {
        'InscriptionCnt': 1 })


def OptionInitCostAction200300(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (0.1 + Func201(*a) * 1.5 + Func202(*a) * 0.3) * Func16(*a, **{
'a': 30,
'b': 40 })))


def OptionInitRewardAction200300(oOption, oHero):
    eventnpcaction.InitHPReward(oOption, oHero, 0, 3500)


def OptionInitCostAction200301(oOption, oHero):
    eventnpcaction.InitHPCost(oOption, oHero, 35, 0)


def OptionInitRewardAction200301(oOption, oHero):
    eventnpcaction.InitWarCashReward(oOption, oHero, (lambda *a: (0.1 + Func201(*a) * 1.5 + Func202(*a) * 0.3) * Func16(*a, **{
'a': 40,
'b': 50 })), 1, None)


def OptionInitCostAction200302(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (0.1 + Func201(*a) * 1.5 + Func202(*a) * 0.3) * Func16(*a, **{
'a': 60,
'b': 70 })))


def OptionInitRewardAction200302(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 1, WEAPON_ACTION_UPGRADEINSCRIPTION, {
        'InscriptionCnt': 1 })


def OptionInitCostAction200303(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (0.1 + Func201(*a) * 1.5 + Func202(*a) * 0.3) * Func16(*a, **{
'a': 60,
'b': 70 })))


def OptionInitRewardAction200303(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 2, WEAPON_ACTION_UPGRADEINSCRIPTION, {
        'InscriptionCnt': 1 })


def OptionInitCostAction200400(oOption, oHero):
    eventnpcaction.InitSelectedRelicCost(oOption, oHero, RELIC_TYPE_NORMAL, QUALITY_TYPE_LOW | QUALITY_TYPE_NORMAL | QUALITY_TYPE_HIGH, 1, None)


def OptionInitRewardAction200400(oOption, oHero):
    eventnpcaction.InitRelicReward(oOption, oHero, 0, { }, 1, {
        1: {
            3001: {
                30012104: 40,
                30012108: 42,
                30012112: 18 },
            3005: {
                30052104: 40,
                30052108: 42,
                30052112: 18 },
            3008: {
                30082104: 40,
                30082108: 42,
                30082112: 18 },
            3007: {
                30072104: 40,
                30072108: 42,
                30072112: 18 },
            3009: {
                30092104: 40,
                30092108: 42,
                30092112: 18 },
            3010: {
                30102104: 40,
                30102108: 42,
                30102112: 18 },
            3012: {
                30122104: 40,
                30122108: 42,
                30122112: 18 } },
        2: {
            3001: {
                30012104: 20,
                30012108: 55,
                30012112: 25 },
            3005: {
                30052104: 20,
                30052108: 55,
                30052112: 25 },
            3008: {
                30082104: 20,
                30082108: 55,
                30082112: 25 },
            3007: {
                30072104: 20,
                30072108: 55,
                30072112: 25 },
            3009: {
                30092104: 20,
                30092108: 55,
                30092112: 25 },
            3012: {
                30122104: 20,
                30122108: 55,
                30122112: 25 } },
        3: {
            3001: {
                30012104: 20,
                30012108: 55,
                30012112: 25 },
            3005: {
                30052104: 20,
                30052108: 55,
                30052112: 25 },
            3008: {
                30082104: 20,
                30082108: 55,
                30082112: 25 },
            3007: {
                30072104: 20,
                30072108: 55,
                30072112: 25 },
            3009: {
                30092104: 20,
                30092108: 55,
                30092112: 25 },
            3012: {
                30122104: 20,
                30122108: 55,
                30122112: 25 } } }, None)


def OptionInitCostAction200401(oOption, oHero):
    eventnpcaction.InitHPCost(oOption, oHero, 35, 0)


def OptionInitRewardAction200401(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 1, WEAPON_ACTION_RECAST, { })


def OptionInitCostAction200402(oOption, oHero):
    eventnpcaction.InitHPCost(oOption, oHero, 35, 0)


def OptionInitRewardAction200402(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 2, WEAPON_ACTION_RECAST, { })


def OptionInitCostAction200500(oOption, oHero):
    eventnpcaction.InitCurseRelicCost(oOption, oHero, 0)


def OptionInitRewardAction200500(oOption, oHero):
    eventnpcaction.InitRelicReward(oOption, oHero, 0, { }, 1, {
        1: {
            3001: {
                30012108: 80,
                30012112: 20 },
            3005: {
                30052108: 80,
                30052112: 20 },
            3008: {
                30082108: 80,
                30082112: 20 },
            3007: {
                30072108: 80,
                30072112: 20 },
            3009: {
                30092108: 80,
                30092112: 20 },
            3010: {
                30102108: 80,
                30102112: 20 },
            3012: {
                30122108: 80,
                30122112: 20 } },
        2: {
            3001: {
                30012108: 70,
                30012112: 30 },
            3005: {
                30052108: 70,
                30052112: 30 },
            3008: {
                30082108: 70,
                30082112: 30 },
            3007: {
                30072108: 70,
                30072112: 30 },
            3009: {
                30092108: 70,
                30092112: 30 },
            3012: {
                30122108: 70,
                30122112: 30 } },
        3: {
            3001: {
                30012108: 70,
                30012112: 30 },
            3005: {
                30052108: 70,
                30052112: 30 },
            3008: {
                30082108: 70,
                30082112: 30 },
            3007: {
                30072108: 70,
                30072112: 30 },
            3009: {
                30092108: 70,
                30092112: 30 },
            3012: {
                30122108: 70,
                30122112: 30 } } }, None)


def OptionInitCostAction200501(oOption, oHero):
    eventnpcaction.InitSelectedRelicCost(oOption, oHero, RELIC_TYPE_NORMAL, QUALITY_TYPE_LOW | QUALITY_TYPE_NORMAL | QUALITY_TYPE_HIGH, 1, None)


def OptionInitRewardAction200501(oOption, oHero):
    eventnpcaction.InitRelicReward(oOption, oHero, 0, { }, 1, {
        1: {
            3001: {
                30012104: 40,
                30012108: 42,
                30012112: 18 },
            3005: {
                30052104: 40,
                30052108: 42,
                30052112: 18 },
            3008: {
                30082104: 40,
                30082108: 42,
                30082112: 18 },
            3007: {
                30072104: 40,
                30072108: 42,
                30072112: 18 },
            3009: {
                30092104: 40,
                30092108: 42,
                30092112: 18 },
            3010: {
                30102104: 40,
                30102108: 42,
                30102112: 18 },
            3012: {
                30122104: 40,
                30122108: 42,
                30122112: 18 } },
        2: {
            3001: {
                30012104: 20,
                30012108: 55,
                30012112: 25 },
            3005: {
                30052104: 20,
                30052108: 55,
                30052112: 25 },
            3008: {
                30082104: 20,
                30082108: 55,
                30082112: 25 },
            3007: {
                30072104: 20,
                30072108: 55,
                30072112: 25 },
            3009: {
                30092104: 20,
                30092108: 55,
                30092112: 25 },
            3012: {
                30122104: 20,
                30122108: 55,
                30122112: 25 } },
        3: {
            3001: {
                30012104: 20,
                30012108: 55,
                30012112: 25 },
            3005: {
                30052104: 20,
                30052108: 55,
                30052112: 25 },
            3008: {
                30082104: 20,
                30082108: 55,
                30082112: 25 },
            3007: {
                30072104: 20,
                30072108: 55,
                30072112: 25 },
            3009: {
                30092104: 20,
                30092108: 55,
                30092112: 25 },
            3012: {
                30122104: 20,
                30122108: 55,
                30122112: 25 } } }, None)


def OptionInitCostAction200600(oOption, oHero):
    eventnpcaction.InitSelectedRelicCost(oOption, oHero, RELIC_TYPE_NORMAL, QUALITY_TYPE_LOW | QUALITY_TYPE_NORMAL | QUALITY_TYPE_HIGH, 1, None)


def OptionInitRewardAction200600(oOption, oHero):
    eventnpcaction.InitRelicReward(oOption, oHero, 0, { }, 1, {
        1: {
            3001: {
                30012104: 40,
                30012108: 42,
                30012112: 18 },
            3005: {
                30052104: 40,
                30052108: 42,
                30052112: 18 },
            3008: {
                30082104: 40,
                30082108: 42,
                30082112: 18 },
            3007: {
                30072104: 40,
                30072108: 42,
                30072112: 18 },
            3009: {
                30092104: 40,
                30092108: 42,
                30092112: 18 },
            3010: {
                30102104: 40,
                30102108: 42,
                30102112: 18 },
            3012: {
                30122104: 40,
                30122108: 42,
                30122112: 18 } },
        2: {
            3001: {
                30012104: 20,
                30012108: 55,
                30012112: 25 },
            3005: {
                30052104: 20,
                30052108: 55,
                30052112: 25 },
            3008: {
                30082104: 20,
                30082108: 55,
                30082112: 25 },
            3007: {
                30072104: 20,
                30072108: 55,
                30072112: 25 },
            3009: {
                30092104: 20,
                30092108: 55,
                30092112: 25 },
            3012: {
                30122104: 20,
                30122108: 55,
                30122112: 25 } },
        3: {
            3001: {
                30012104: 20,
                30012108: 55,
                30012112: 25 },
            3005: {
                30052104: 20,
                30052108: 55,
                30052112: 25 },
            3008: {
                30082104: 20,
                30082108: 55,
                30082112: 25 },
            3007: {
                30072104: 20,
                30072108: 55,
                30072112: 25 },
            3009: {
                30092104: 20,
                30092108: 55,
                30092112: 25 },
            3012: {
                30122104: 20,
                30122108: 55,
                30122112: 25 } } }, None)


def OptionInitCostAction200601(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (0.1 + Func201(*a) * 1.5 + Func202(*a) * 0.3) * Func16(*a, **{
'a': 50,
'b': 60 })))


def OptionInitRewardAction200601(oOption, oHero):
    eventnpcaction.InitRelicReward(oOption, oHero, 0, { }, 1, {
        1: {
            3001: {
                30012401: 100 },
            3008: {
                30082401: 100 },
            3007: {
                30072401: 100 },
            3009: {
                30092401: 100 },
            3010: {
                30102401: 100 },
            3012: {
                30122401: 100 } },
        2: {
            3001: {
                30012401: 100 },
            3008: {
                30082401: 100 },
            3007: {
                30072401: 100 },
            3009: {
                30092401: 100 },
            3012: {
                30122401: 100 } },
        3: {
            3001: {
                30012401: 100 },
            3008: {
                30082401: 100 },
            3007: {
                30072401: 100 },
            3009: {
                30092401: 100 },
            3012: {
                30122401: 100 } } }, None)


def OptionInitRewardAction200602(oOption, oHero):
    eventnpcaction.InitRelicReward(oOption, oHero, 0, { }, 1, {
        1: {
            3001: {
                30012104: 40,
                30012108: 27,
                30012112: 3,
                30012117: 30 },
            3005: {
                30052104: 40,
                30052108: 27,
                30052112: 3,
                30052117: 30 },
            3008: {
                30082104: 40,
                30082108: 27,
                30082112: 3,
                30082117: 30 },
            3007: {
                30072104: 40,
                30072108: 27,
                30072112: 3,
                30072117: 30 },
            3009: {
                30092104: 40,
                30092108: 27,
                30092112: 3,
                30092117: 30 },
            3010: {
                30102104: 40,
                30102108: 27,
                30102112: 3,
                30102117: 30 },
            3012: {
                30122104: 40,
                30122108: 27,
                30122112: 3,
                30122117: 30 } },
        2: {
            3001: {
                30012104: 30,
                30012108: 32,
                30012112: 8,
                30012117: 30 },
            3005: {
                30052104: 30,
                30052108: 32,
                30052112: 8,
                30052117: 30 },
            3008: {
                30082104: 30,
                30082108: 32,
                30082112: 8,
                30082117: 30 },
            3007: {
                30072104: 30,
                30072108: 32,
                30072112: 8,
                30072117: 30 },
            3009: {
                30092104: 30,
                30092108: 32,
                30092112: 8,
                30092117: 30 },
            3012: {
                30122104: 30,
                30122108: 32,
                30122112: 8,
                30122117: 30 } },
        3: {
            3001: {
                30012104: 30,
                30012108: 32,
                30012112: 8,
                30012117: 30 },
            3005: {
                30052104: 30,
                30052108: 32,
                30052112: 8,
                30052117: 30 },
            3008: {
                30082104: 30,
                30082108: 32,
                30082112: 8,
                30082117: 30 },
            3007: {
                30072104: 30,
                30072108: 32,
                30072112: 8,
                30072117: 30 },
            3009: {
                30092104: 30,
                30092108: 32,
                30092112: 8,
                30092117: 30 },
            3012: {
                30122104: 30,
                30122108: 32,
                30122112: 8,
                30122117: 30 } } }, None)


def OptionInitCostAction200700(oOption, oHero):
    eventnpcaction.InitSelectedRelicCost(oOption, oHero, RELIC_TYPE_NORMAL | RELIC_TYPE_CURSE, QUALITY_TYPE_LOW | QUALITY_TYPE_NORMAL | QUALITY_TYPE_HIGH | QUALITY_TYPE_CURSE, 1, None)


def OptionInitRewardAction200700(oOption, oHero):
    eventnpcaction.InitWarCashReward(oOption, oHero, (lambda *a: (0.1 + Func201(*a) * 1.5 + Func202(*a) * 0.3) * Func16(*a, **{
'a': 65,
'b': 70 })), 1, None)


def OptionInitCostAction200800(oOption, oHero):
    eventnpcaction.InitCurseRelicCost(oOption, oHero, 0)


def OptionInitRewardAction200800(oOption, oHero):
    eventnpcaction.InitRelicReward(oOption, oHero, 0, { }, 1, {
        1: {
            3001: {
                30012108: 80,
                30012112: 20 },
            3005: {
                30052108: 80,
                30052112: 20 },
            3008: {
                30082108: 80,
                30082112: 20 },
            3007: {
                30072108: 80,
                30072112: 20 },
            3009: {
                30092108: 80,
                30092112: 20 },
            3010: {
                30102108: 80,
                30102112: 20 },
            3012: {
                30122108: 80,
                30122112: 20 } },
        2: {
            3001: {
                30012108: 70,
                30012112: 30 },
            3005: {
                30052108: 70,
                30052112: 30 },
            3008: {
                30082108: 70,
                30082112: 30 },
            3007: {
                30072108: 70,
                30072112: 30 },
            3009: {
                30092108: 70,
                30092112: 30 },
            3012: {
                30122108: 70,
                30122112: 30 } },
        3: {
            3001: {
                30012108: 70,
                30012112: 30 },
            3005: {
                30052108: 70,
                30052112: 30 },
            3008: {
                30082108: 70,
                30082112: 30 },
            3007: {
                30072108: 70,
                30072112: 30 },
            3009: {
                30092108: 70,
                30092112: 30 },
            3012: {
                30122108: 70,
                30122112: 30 } } }, None)


def OptionInitCostAction200801(oOption, oHero):
    eventnpcaction.InitHPCost(oOption, oHero, 45, 0)


def OptionInitRewardAction200801(oOption, oHero):
    eventnpcaction.InitRelicReward(oOption, oHero, 0, { }, 1, {
        1: {
            3001: {
                30012401: 100 },
            3008: {
                30082401: 100 },
            3007: {
                30072401: 100 },
            3009: {
                30092401: 100 },
            3010: {
                30102401: 100 },
            3012: {
                30122401: 100 } },
        2: {
            3001: {
                30012401: 100 },
            3008: {
                30082401: 100 },
            3007: {
                30072401: 100 },
            3009: {
                30092401: 100 },
            3012: {
                30122401: 100 } },
        3: {
            3001: {
                30012401: 100 },
            3008: {
                30082401: 100 },
            3007: {
                30072401: 100 },
            3009: {
                30092401: 100 },
            3012: {
                30122401: 100 } } }, None)


def OptionInitRewardAction200802(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 1, WEAPON_ACTION_RECAST, { })


def OptionInitRewardAction200803(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 2, WEAPON_ACTION_RECAST, { })


def OptionInitCostAction200900(oOption, oHero):
    eventnpcaction.InitCurseRelicCost(oOption, oHero, 0)


def OptionInitRewardAction200900(oOption, oHero):
    eventnpcaction.InitRelicReward(oOption, oHero, 0, { }, 1, {
        1: {
            3001: {
                30012108: 80,
                30012112: 20 },
            3005: {
                30052108: 80,
                30052112: 20 },
            3008: {
                30082108: 80,
                30082112: 20 },
            3007: {
                30072108: 80,
                30072112: 20 },
            3009: {
                30092108: 80,
                30092112: 20 },
            3010: {
                30102108: 80,
                30102112: 20 },
            3012: {
                30122108: 80,
                30122112: 20 } },
        2: {
            3001: {
                30012108: 70,
                30012112: 30 },
            3005: {
                30052108: 70,
                30052112: 30 },
            3008: {
                30082108: 70,
                30082112: 30 },
            3007: {
                30072108: 70,
                30072112: 30 },
            3009: {
                30092108: 70,
                30092112: 30 },
            3012: {
                30122108: 70,
                30122112: 30 } },
        3: {
            3001: {
                30012108: 70,
                30012112: 30 },
            3005: {
                30052108: 70,
                30052112: 30 },
            3008: {
                30082108: 70,
                30082112: 30 },
            3007: {
                30072108: 70,
                30072112: 30 },
            3009: {
                30092108: 70,
                30092112: 30 },
            3012: {
                30122108: 70,
                30122112: 30 } } }, None)


def OptionInitCostAction200901(oOption, oHero):
    eventnpcaction.InitHPCost(oOption, oHero, 45, 0)


def OptionInitRewardAction200901(oOption, oHero):
    eventnpcaction.InitRelicReward(oOption, oHero, 0, { }, 1, {
        1: {
            3001: {
                30012401: 100 },
            3008: {
                30082401: 100 },
            3007: {
                30072401: 100 },
            3009: {
                30092401: 100 },
            3010: {
                30102401: 100 },
            3012: {
                30122401: 100 } },
        2: {
            3001: {
                30012401: 100 },
            3008: {
                30082401: 100 },
            3007: {
                30072401: 100 },
            3009: {
                30092401: 100 },
            3012: {
                30122401: 100 } },
        3: {
            3001: {
                30012401: 100 },
            3008: {
                30082401: 100 },
            3007: {
                30072401: 100 },
            3009: {
                30092401: 100 },
            3012: {
                30122401: 100 } } }, None)


def OptionInitRewardAction200902(oOption, oHero):
    eventnpcaction.InitRelicReward(oOption, oHero, 0, { }, 1, {
        1: {
            3001: {
                30012104: 40,
                30012108: 27,
                30012112: 3,
                30012117: 30 },
            3005: {
                30052104: 40,
                30052108: 27,
                30052112: 3,
                30052117: 30 },
            3008: {
                30082104: 40,
                30082108: 27,
                30082112: 3,
                30082117: 30 },
            3007: {
                30072104: 40,
                30072108: 27,
                30072112: 3,
                30072117: 30 },
            3009: {
                30092104: 40,
                30092108: 27,
                30092112: 3,
                30092117: 30 },
            3010: {
                30102104: 40,
                30102108: 27,
                30102112: 3,
                30102117: 30 },
            3012: {
                30122104: 40,
                30122108: 27,
                30122112: 3,
                30122117: 30 } },
        2: {
            3001: {
                30012104: 30,
                30012108: 32,
                30012112: 8,
                30012117: 30 },
            3005: {
                30052104: 30,
                30052108: 32,
                30052112: 8,
                30052117: 30 },
            3008: {
                30082104: 30,
                30082108: 32,
                30082112: 8,
                30082117: 30 },
            3007: {
                30072104: 30,
                30072108: 32,
                30072112: 8,
                30072117: 30 },
            3009: {
                30092104: 30,
                30092108: 32,
                30092112: 8,
                30092117: 30 },
            3012: {
                30122104: 30,
                30122108: 32,
                30122112: 8,
                30122117: 30 } },
        3: {
            3001: {
                30012104: 30,
                30012108: 32,
                30012112: 8,
                30012117: 30 },
            3005: {
                30052104: 30,
                30052108: 32,
                30052112: 8,
                30052117: 30 },
            3008: {
                30082104: 30,
                30082108: 32,
                30082112: 8,
                30082117: 30 },
            3007: {
                30072104: 30,
                30072108: 32,
                30072112: 8,
                30072117: 30 },
            3009: {
                30092104: 30,
                30092108: 32,
                30092112: 8,
                30092117: 30 },
            3012: {
                30122104: 30,
                30122108: 32,
                30122112: 8,
                30122117: 30 } } }, None)


def OptionInitCostAction201000(oOption, oHero):
    eventnpcaction.InitCurseRelicCost(oOption, oHero, 0)


def OptionInitRewardAction201000(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 1, WEAPON_ACTION_UPGRADEINSCRIPTION, {
        'InscriptionCnt': 0 })


def OptionInitCostAction201001(oOption, oHero):
    eventnpcaction.InitCurseRelicCost(oOption, oHero, 0)


def OptionInitRewardAction201001(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 2, WEAPON_ACTION_UPGRADEINSCRIPTION, {
        'InscriptionCnt': 0 })


def OptionInitCostAction201002(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (0.1 + Func201(*a) * 1.5 + Func202(*a) * 0.3) * Func16(*a, **{
'a': 37,
'b': 45 })))


def OptionInitRewardAction201002(oOption, oHero):
    eventnpcaction.InitHPReward(oOption, oHero, 35, 0)


def OptionInitRewardAction201003(oOption, oHero):
    eventnpcaction.InitRelicReward(oOption, oHero, 0, { }, 1, {
        1: {
            3001: {
                30012104: 40,
                30012108: 27,
                30012112: 3,
                30012117: 30 },
            3005: {
                30052104: 40,
                30052108: 27,
                30052112: 3,
                30052117: 30 },
            3008: {
                30082104: 40,
                30082108: 27,
                30082112: 3,
                30082117: 30 },
            3007: {
                30072104: 40,
                30072108: 27,
                30072112: 3,
                30072117: 30 },
            3009: {
                30092104: 40,
                30092108: 27,
                30092112: 3,
                30092117: 30 },
            3010: {
                30102104: 40,
                30102108: 27,
                30102112: 3,
                30102117: 30 },
            3012: {
                30122104: 40,
                30122108: 27,
                30122112: 3,
                30122117: 30 } },
        2: {
            3001: {
                30012104: 30,
                30012108: 32,
                30012112: 8,
                30012117: 30 },
            3005: {
                30052104: 30,
                30052108: 32,
                30052112: 8,
                30052117: 30 },
            3008: {
                30082104: 30,
                30082108: 32,
                30082112: 8,
                30082117: 30 },
            3007: {
                30072104: 30,
                30072108: 32,
                30072112: 8,
                30072117: 30 },
            3009: {
                30092104: 30,
                30092108: 32,
                30092112: 8,
                30092117: 30 },
            3012: {
                30122104: 30,
                30122108: 32,
                30122112: 8,
                30122117: 30 } },
        3: {
            3001: {
                30012104: 30,
                30012108: 32,
                30012112: 8,
                30012117: 30 },
            3005: {
                30052104: 30,
                30052108: 32,
                30052112: 8,
                30052117: 30 },
            3008: {
                30082104: 30,
                30082108: 32,
                30082112: 8,
                30082117: 30 },
            3007: {
                30072104: 30,
                30072108: 32,
                30072112: 8,
                30072117: 30 },
            3009: {
                30092104: 30,
                30092108: 32,
                30092112: 8,
                30092117: 30 },
            3012: {
                30122104: 30,
                30122108: 32,
                30122112: 8,
                30122117: 30 } } }, None)


def OptionInitCostAction201100(oOption, oHero):
    eventnpcaction.InitCurseRelicCost(oOption, oHero, 0)


def OptionInitRewardAction201100(oOption, oHero):
    eventnpcaction.InitRelicReward(oOption, oHero, 0, { }, 1, {
        1: {
            3001: {
                30012108: 80,
                30012112: 20 },
            3005: {
                30052108: 80,
                30052112: 20 },
            3008: {
                30082108: 80,
                30082112: 20 },
            3007: {
                30072108: 80,
                30072112: 20 },
            3009: {
                30092108: 80,
                30092112: 20 },
            3010: {
                30102108: 80,
                30102112: 20 },
            3012: {
                30122108: 80,
                30122112: 20 } },
        2: {
            3001: {
                30012108: 70,
                30012112: 30 },
            3005: {
                30052108: 70,
                30052112: 30 },
            3008: {
                30082108: 70,
                30082112: 30 },
            3007: {
                30072108: 70,
                30072112: 30 },
            3009: {
                30092108: 70,
                30092112: 30 },
            3012: {
                30122108: 70,
                30122112: 30 } },
        3: {
            3001: {
                30012108: 70,
                30012112: 30 },
            3005: {
                30052108: 70,
                30052112: 30 },
            3008: {
                30082108: 70,
                30082112: 30 },
            3007: {
                30072108: 70,
                30072112: 30 },
            3009: {
                30092108: 70,
                30092112: 30 },
            3012: {
                30122108: 70,
                30122112: 30 } } }, None)


def OptionInitCostAction201101(oOption, oHero):
    eventnpcaction.InitCurseRelicCost(oOption, oHero, 0)


def OptionInitRewardAction201101(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 1, WEAPON_ACTION_UPGRADEINSCRIPTION, {
        'InscriptionCnt': 0 })


def OptionInitCostAction201102(oOption, oHero):
    eventnpcaction.InitCurseRelicCost(oOption, oHero, 0)


def OptionInitRewardAction201102(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 2, WEAPON_ACTION_UPGRADEINSCRIPTION, {
        'InscriptionCnt': 0 })


def OptionInitCostAction201200(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (0.1 + Func201(*a) * 1.5 + Func202(*a) * 0.3) * Func16(*a, **{
'a': 57,
'b': 67 })))


def OptionInitRewardAction201200(oOption, oHero):
    eventnpcaction.InitWeaponReward(oOption, oHero, 0, {
        3001: 30011001,
        3005: 30051001,
        3008: 30081001,
        3007: 30071001,
        3009: 30091001,
        3010: 30101001,
        3012: 30121001 }, 1, None, { }, None)


def OptionInitCostAction201201(oOption, oHero):
    eventnpcaction.InitHPCost(oOption, oHero, 35, 0)


def OptionInitRewardAction201201(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 1, WEAPON_ACTION_RECAST, { })


def OptionInitCostAction201202(oOption, oHero):
    eventnpcaction.InitHPCost(oOption, oHero, 35, 0)


def OptionInitRewardAction201202(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 2, WEAPON_ACTION_RECAST, { })


def OptionInitCostAction201300(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (0.1 + Func201(*a) * 1.5 + Func202(*a) * 0.3) * Func16(*a, **{
'a': 57,
'b': 67 })))


def OptionInitRewardAction201300(oOption, oHero):
    eventnpcaction.InitWeaponReward(oOption, oHero, 0, {
        3001: 30011001,
        3005: 30051001,
        3008: 30081001,
        3007: 30071001,
        3009: 30091001,
        3010: 30101001,
        3012: 30121001 }, 1, None, { }, None)


def OptionInitCostAction201301(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (0.1 + Func201(*a) * 1.5 + Func202(*a) * 0.3) * Func16(*a, **{
'a': 60,
'b': 70 })))


def OptionInitRewardAction201301(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 1, WEAPON_ACTION_UPGRADEINSCRIPTION, {
        'InscriptionCnt': 1 })


def OptionInitCostAction201302(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (0.1 + Func201(*a) * 1.5 + Func202(*a) * 0.3) * Func16(*a, **{
'a': 60,
'b': 70 })))


def OptionInitRewardAction201302(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 2, WEAPON_ACTION_UPGRADEINSCRIPTION, {
        'InscriptionCnt': 1 })


def OptionInitCostAction201400(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (0.1 + Func201(*a) * 1.5 + Func202(*a) * 0.3) * Func16(*a, **{
'a': 40,
'b': 50 })))


def OptionInitRewardAction201400(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 1, WEAPON_ACTION_UPGRADEINSCRIPTION, {
        'InscriptionCnt': 1 })


def OptionInitCostAction201401(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (0.1 + Func201(*a) * 1.5 + Func202(*a) * 0.3) * Func16(*a, **{
'a': 40,
'b': 50 })))


def OptionInitRewardAction201401(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 2, WEAPON_ACTION_UPGRADEINSCRIPTION, {
        'InscriptionCnt': 1 })


def OptionInitCostAction201402(oOption, oHero):
    eventnpcaction.InitCurseRelicCost(oOption, oHero, 0)


def OptionInitRewardAction201402(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 1, WEAPON_ACTION_UPGRADE, { })


def OptionInitCostAction201403(oOption, oHero):
    eventnpcaction.InitCurseRelicCost(oOption, oHero, 0)


def OptionInitRewardAction201403(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 2, WEAPON_ACTION_UPGRADE, { })


def OptionInitRewardAction201500(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 1, WEAPON_ACTION_RECAST, { })


def OptionInitRewardAction201501(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 2, WEAPON_ACTION_RECAST, { })


def OptionInitCostAction201502(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (0.1 + Func201(*a) * 1.5 + Func202(*a) * 0.3) * Func16(*a, **{
'a': 50,
'b': 60 })))


def OptionInitRewardAction201502(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 1, WEAPON_ACTION_UPGRADEINSCRIPTION, {
        'InscriptionCnt': 1 })


def OptionInitCostAction201503(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (0.1 + Func201(*a) * 1.5 + Func202(*a) * 0.3) * Func16(*a, **{
'a': 50,
'b': 60 })))


def OptionInitRewardAction201503(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 2, WEAPON_ACTION_UPGRADEINSCRIPTION, {
        'InscriptionCnt': 1 })


def OptionInitCostAction210100(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (0.1 + Func201(*a) * 1.5 + Func202(*a) * 0.3) * Func16(*a, **{
'a': 48,
'b': 60 })))


def OptionInitRewardAction210100(oOption, oHero):
    eventnpcaction.InitWeaponReward(oOption, oHero, 0, {
        3001: 30011001,
        3005: 30051001,
        3008: 30081001,
        3007: 30071001,
        3009: 30091001,
        3010: 30101001,
        3012: 30121001 }, 1, None, { }, None)


def OptionInitCostAction210101(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (0.1 + Func201(*a) * 1.5 + Func202(*a) * 0.3) * Func16(*a, **{
'a': 72,
'b': 84 })))


def OptionInitRewardAction210101(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 1, WEAPON_ACTION_UPGRADEINSCRIPTION, {
        'InscriptionCnt': 1 })


def OptionInitCostAction210102(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (0.1 + Func201(*a) * 1.5 + Func202(*a) * 0.3) * Func16(*a, **{
'a': 68,
'b': 80 })))


def OptionInitRewardAction210102(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 2, WEAPON_ACTION_RECAST, { })


def OptionInitCostAction210200(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (0.1 + Func201(*a) * 1.5 + Func202(*a) * 0.3) * Func16(*a, **{
'a': 90,
'b': 110 })))


def OptionInitRewardAction210200(oOption, oHero):
    eventnpcaction.InitAttrReward(oOption, oHero, 'HPMax', 0, 1800)


def OptionInitCostAction210201(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (0.1 + Func201(*a) * 1.5 + Func202(*a) * 0.3) * Func16(*a, **{
'a': 90,
'b': 110 })))


def OptionInitRewardAction210201(oOption, oHero):
    eventnpcaction.InitAttrReward(oOption, oHero, 'ShieldMax', 0, 1200)


def OptionInitCostAction210300(oOption, oHero):
    eventnpcaction.InitHPCost(oOption, oHero, 45, 0)


def OptionInitRewardAction210300(oOption, oHero):
    eventnpcaction.InitAttrReward(oOption, oHero, 'HPMax', 0, 2400)


def OptionInitCostAction210301(oOption, oHero):
    eventnpcaction.InitHPCost(oOption, oHero, 45, 0)


def OptionInitRewardAction210301(oOption, oHero):
    eventnpcaction.InitAttrReward(oOption, oHero, 'ShieldMax', 0, 1600)


def OptionInitCostAction210400(oOption, oHero):
    eventnpcaction.InitHPCost(oOption, oHero, 25, 0)


def OptionInitRewardAction210400(oOption, oHero):
    eventnpcaction.InitWarCashReward(oOption, oHero, (lambda *a: (0.1 + Func201(*a) * 0.5 + Func202(*a) * 0.1) * Func16(*a, **{
'a': 90,
'b': 100 })), 1, None)


def OptionInitCostAction210401(oOption, oHero):
    eventnpcaction.InitHPCost(oOption, oHero, 50, 0)


def OptionInitRewardAction210401(oOption, oHero):
    eventnpcaction.InitWarCashReward(oOption, oHero, (lambda *a: (0.1 + Func201(*a) * 1 + Func202(*a) * 0.2) * Func16(*a, **{
'a': 95,
'b': 110 })), 1, None)


def OptionInitCostAction210402(oOption, oHero):
    eventnpcaction.InitHPCost(oOption, oHero, 75, 0)


def OptionInitRewardAction210402(oOption, oHero):
    eventnpcaction.InitWarCashReward(oOption, oHero, (lambda *a: (0.1 + Func201(*a) * 1.5 + Func202(*a) * 0.3) * Func16(*a, **{
'a': 115,
'b': 125 })), 1, None)


def OptionInitCostAction210500(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (0.1 + Func201(*a) * 1.5 + Func202(*a) * 0.3) * Func16(*a, **{
'a': 78,
'b': 90 })))


def OptionInitRewardAction210500(oOption, oHero):
    eventnpcaction.InitRelicReward(oOption, oHero, 0, { }, 1, {
        1: {
            3001: {
                30012104: 43,
                30012108: 49,
                30012112: 8 },
            3005: {
                30052104: 43,
                30052108: 49,
                30052112: 8 },
            3008: {
                30082104: 43,
                30082108: 49,
                30082112: 8 },
            3007: {
                30072104: 43,
                30072108: 49,
                30072112: 8 },
            3009: {
                30092104: 43,
                30092108: 49,
                30092112: 8 },
            3010: {
                30102104: 43,
                30102108: 49,
                30102112: 8 },
            3012: {
                30122104: 43,
                30122108: 49,
                30122112: 8 } },
        2: {
            3001: {
                30012104: 28,
                30012108: 55,
                30012112: 17 },
            3005: {
                30052104: 28,
                30052108: 55,
                30052112: 17 },
            3008: {
                30082104: 28,
                30082108: 55,
                30082112: 17 },
            3007: {
                30072104: 28,
                30072108: 55,
                30072112: 17 },
            3009: {
                30092104: 28,
                30092108: 55,
                30092112: 17 },
            3012: {
                30122104: 28,
                30122108: 55,
                30122112: 17 } },
        3: {
            3001: {
                30012104: 28,
                30012108: 55,
                30012112: 17 },
            3005: {
                30052104: 28,
                30052108: 55,
                30052112: 17 },
            3008: {
                30082104: 28,
                30082108: 55,
                30082112: 17 },
            3007: {
                30072104: 28,
                30072108: 55,
                30072112: 17 },
            3009: {
                30092104: 28,
                30092108: 55,
                30092112: 17 },
            3012: {
                30122104: 28,
                30122108: 55,
                30122112: 17 } } }, None)


def OptionInitCostAction210501(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (0.1 + Func201(*a) * 1.5 + Func202(*a) * 0.3) * Func16(*a, **{
'a': 78,
'b': 90 })))


def OptionInitRewardAction210501(oOption, oHero):
    eventnpcaction.InitRelicReward(oOption, oHero, 0, { }, 1, {
        1: {
            3001: {
                30012108: 47 },
            3005: {
                30052108: 47 },
            3008: {
                30082108: 47 },
            3007: {
                30072108: 47 },
            3009: {
                30092108: 47 },
            3010: {
                30102108: 47 },
            3012: {
                30122108: 47 } },
        2: {
            3001: {
                30012108: 55 },
            3005: {
                30052108: 55 },
            3008: {
                30082108: 55 },
            3007: {
                30072108: 55 },
            3009: {
                30092108: 55 },
            3012: {
                30122108: 55 } },
        3: {
            3001: {
                30012108: 55 },
            3005: {
                30052108: 55 },
            3008: {
                30082108: 55 },
            3007: {
                30072108: 55 },
            3009: {
                30092108: 55 },
            3012: {
                30122108: 55 } } }, None)


def OptionInitCostAction210502(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (0.1 + Func201(*a) * 1.5 + Func202(*a) * 0.3) * Func16(*a, **{
'a': 48,
'b': 60 })))


def OptionInitRewardAction210502(oOption, oHero):
    eventnpcaction.InitRelicReward(oOption, oHero, 0, { }, 1, {
        1: {
            3001: {
                30012104: 40 },
            3005: {
                30052104: 40 },
            3008: {
                30082104: 40 },
            3007: {
                30072104: 40 },
            3009: {
                30092104: 40 },
            3010: {
                30102104: 40 },
            3012: {
                30122104: 40 } },
        2: {
            3001: {
                30012104: 20 },
            3005: {
                30052104: 20 },
            3008: {
                30082104: 20 },
            3007: {
                30072104: 20 },
            3009: {
                30092104: 20 },
            3012: {
                30122104: 20 } },
        3: {
            3001: {
                30012104: 20 },
            3005: {
                30052104: 20 },
            3008: {
                30082104: 20 },
            3007: {
                30072104: 20 },
            3009: {
                30092104: 20 },
            3012: {
                30122104: 20 } } }, None)


def OptionInitCostAction210600(oOption, oHero):
    eventnpcaction.InitSelectedRelicCost(oOption, oHero, RELIC_TYPE_NORMAL | RELIC_TYPE_CURSE, QUALITY_TYPE_LOW | QUALITY_TYPE_NORMAL | QUALITY_TYPE_HIGH | QUALITY_TYPE_CURSE, 1, None)


def OptionInitRewardAction210600(oOption, oHero):
    eventnpcaction.InitWarCashReward(oOption, oHero, (lambda *a: (0.1 + Func201(*a) * 1.5 + Func202(*a) * 0.3) * Func16(*a, **{
'a': 65,
'b': 70 })), 1, None)


def OptionInitCostAction210700(oOption, oHero):
    eventnpcaction.InitSelectedRelicCost(oOption, oHero, RELIC_TYPE_NORMAL | RELIC_TYPE_CURSE, QUALITY_TYPE_LOW | QUALITY_TYPE_NORMAL | QUALITY_TYPE_HIGH | QUALITY_TYPE_CURSE, 1, None)


def OptionInitRewardAction210700(oOption, oHero):
    eventnpcaction.InitRelicReward(oOption, oHero, 0, { }, 1, {
        1: {
            3001: {
                30012104: 40,
                30012108: 42,
                30012112: 18 },
            3005: {
                30052104: 40,
                30052108: 42,
                30052112: 18 },
            3008: {
                30082104: 40,
                30082108: 42,
                30082112: 18 },
            3007: {
                30072104: 40,
                30072108: 42,
                30072112: 18 },
            3009: {
                30092104: 40,
                30092108: 42,
                30092112: 18 },
            3010: {
                30102104: 40,
                30102108: 42,
                30102112: 18 },
            3012: {
                30122104: 40,
                30122108: 42,
                30122112: 18 } },
        2: {
            3001: {
                30012104: 20,
                30012108: 55,
                30012112: 25 },
            3005: {
                30052104: 20,
                30052108: 55,
                30052112: 25 },
            3008: {
                30082104: 20,
                30082108: 55,
                30082112: 25 },
            3007: {
                30072104: 20,
                30072108: 55,
                30072112: 25 },
            3009: {
                30092104: 20,
                30092108: 55,
                30092112: 25 },
            3012: {
                30122104: 20,
                30122108: 55,
                30122112: 25 } },
        3: {
            3001: {
                30012104: 20,
                30012108: 55,
                30012112: 25 },
            3005: {
                30052104: 20,
                30052108: 55,
                30052112: 25 },
            3008: {
                30082104: 20,
                30082108: 55,
                30082112: 25 },
            3007: {
                30072104: 20,
                30072108: 55,
                30072112: 25 },
            3009: {
                30092104: 20,
                30092108: 55,
                30092112: 25 },
            3012: {
                30122104: 20,
                30122108: 55,
                30122112: 25 } } }, None)


def OptionInitCostAction210701(oOption, oHero):
    eventnpcaction.InitSelectedRelicCost(oOption, oHero, RELIC_TYPE_NORMAL | RELIC_TYPE_CURSE, QUALITY_TYPE_LOW | QUALITY_TYPE_NORMAL | QUALITY_TYPE_HIGH | QUALITY_TYPE_CURSE, 1, None)


def OptionInitRewardAction210701(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 1, WEAPON_ACTION_UPGRADEINSCRIPTION, {
        'UpAllInsToRare': 1 })


def OptionInitCostAction210702(oOption, oHero):
    eventnpcaction.InitSelectedRelicCost(oOption, oHero, RELIC_TYPE_NORMAL | RELIC_TYPE_CURSE, QUALITY_TYPE_LOW | QUALITY_TYPE_NORMAL | QUALITY_TYPE_HIGH | QUALITY_TYPE_CURSE, 1, None)


def OptionInitRewardAction210702(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 1, WEAPON_ACTION_UPGRADE, {
        'WeaponUpgradeLevel': 2 })


def OptionInitRewardAction210800(oOption, oHero):
    eventnpcaction.InitSelectedRelicReward(oOption, oHero, RELIC_TYPE_CURSE, QUALITY_TYPE_CURSE, 1)


def OptionInitRewardAction210801(oOption, oHero):
    eventnpcaction.InitWarCashReward(oOption, oHero, (lambda *a: (0.1 + Func201(*a) * 1 + Func202(*a) * 0.2) * 125 * min(int(Func210(*a)), 3)), 1, CAL_BY_CURSE_RELIC)


def OptionInitCostAction210802(oOption, oHero):
    eventnpcaction.InitHPCost(oOption, oHero, 45, 0)


def OptionInitRewardAction210802(oOption, oHero):
    eventnpcaction.InitWarCashReward(oOption, oHero, (lambda *a: (0.1 + Func201(*a) * 1 + Func202(*a) * 0.2) * Func16(*a, **{
'a': 95,
'b': 110 })), -1, None)


def OptionInitCostAction211000(oOption, oHero):
    eventnpcaction.InitHPCost(oOption, oHero, 75, 0)


def OptionInitRewardAction211000(oOption, oHero):
    eventnpcaction.InitRelicReward(oOption, oHero, 0, { }, 1, {
        1: {
            3001: {
                30012104: 50 },
            3005: {
                30052104: 50 },
            3008: {
                30082104: 50 },
            3007: {
                30072104: 50 },
            3009: {
                30092104: 50 },
            3010: {
                30102104: 50 },
            3012: {
                30122104: 50 } },
        2: {
            3001: {
                30012104: 40 },
            3005: {
                30052104: 40 },
            3008: {
                30082104: 40 },
            3007: {
                30072104: 40 },
            3009: {
                30092104: 40 },
            3012: {
                30122104: 40 } },
        3: {
            3001: {
                30012104: 40 },
            3005: {
                30052104: 40 },
            3008: {
                30082104: 40 },
            3007: {
                30072104: 40 },
            3009: {
                30092104: 40 },
            3012: {
                30122104: 40 } } }, None)


def OptionInitCostAction211001(oOption, oHero):
    eventnpcaction.InitHPCost(oOption, oHero, 75, 0)


def OptionInitRewardAction211001(oOption, oHero):
    eventnpcaction.InitWarCashReward(oOption, oHero, (lambda *a: (0.1 + Func201(*a) * 1.5 + Func202(*a) * 0.3) * Func16(*a, **{
'a': 145,
'b': 155 })), 1, None)


def OptionInitCostAction211002(oOption, oHero):
    eventnpcaction.InitHPCost(oOption, oHero, 75, 0)


def OptionInitRewardAction211002(oOption, oHero):
    eventnpcaction.InitSelectedRelicReward(oOption, oHero, RELIC_TYPE_CURSE, QUALITY_TYPE_CURSE, 1)


def OptionInitCostAction211200(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (0.1 + Func201(*a) * 1.5 + Func202(*a) * 0.3) * Func16(*a, **{
'a': 180,
'b': 200 })))


def OptionInitRewardAction211200(oOption, oHero):
    eventnpcaction.InitRelicReward(oOption, oHero, 0, { }, 1, {
        1: {
            3001: {
                30012112: 20 },
            3005: {
                30052112: 20 },
            3008: {
                30082112: 20 },
            3007: {
                30072112: 20 },
            3009: {
                30092112: 20 },
            3010: {
                30102112: 20 },
            3012: {
                30122112: 20 } },
        2: {
            3001: {
                30012112: 30 },
            3005: {
                30052112: 30 },
            3008: {
                30082112: 30 },
            3007: {
                30072112: 30 },
            3009: {
                30092112: 30 },
            3012: {
                30122112: 30 } },
        3: {
            3001: {
                30012112: 30 },
            3005: {
                30052112: 30 },
            3008: {
                30082112: 30 },
            3007: {
                30072112: 30 },
            3009: {
                30092112: 30 },
            3012: {
                30122112: 30 } } }, None)


def OptionInitCostAction211201(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (0.1 + Func201(*a) * 1.5 + Func202(*a) * 0.3) * Func16(*a, **{
'a': 78,
'b': 90 })))


def OptionInitRewardAction211201(oOption, oHero):
    eventnpcaction.InitRelicReward(oOption, oHero, 0, { }, 1, {
        1: {
            3001: {
                30012104: 43,
                30012108: 49,
                30012112: 8 },
            3005: {
                30052104: 43,
                30052108: 49,
                30052112: 8 },
            3008: {
                30082104: 43,
                30082108: 49,
                30082112: 8 },
            3007: {
                30072104: 43,
                30072108: 49,
                30072112: 8 },
            3009: {
                30092104: 43,
                30092108: 49,
                30092112: 8 },
            3010: {
                30102104: 43,
                30102108: 49,
                30102112: 8 },
            3012: {
                30122104: 43,
                30122108: 49,
                30122112: 8 } },
        2: {
            3001: {
                30012104: 28,
                30012108: 55,
                30012112: 17 },
            3005: {
                30052104: 28,
                30052108: 55,
                30052112: 17 },
            3008: {
                30082104: 28,
                30082108: 55,
                30082112: 17 },
            3007: {
                30072104: 28,
                30072108: 55,
                30072112: 17 },
            3009: {
                30092104: 28,
                30092108: 55,
                30092112: 17 },
            3012: {
                30122104: 28,
                30122108: 55,
                30122112: 17 } },
        3: {
            3001: {
                30012104: 28,
                30012108: 55,
                30012112: 17 },
            3005: {
                30052104: 28,
                30052108: 55,
                30052112: 17 },
            3008: {
                30082104: 28,
                30082108: 55,
                30082112: 17 },
            3007: {
                30072104: 28,
                30072108: 55,
                30072112: 17 },
            3009: {
                30092104: 28,
                30092108: 55,
                30092112: 17 },
            3012: {
                30122104: 28,
                30122108: 55,
                30122112: 17 } } }, None)


def OptionInitCostAction211300(oOption, oHero):
    eventnpcaction.InitCurseRelicCost(oOption, oHero, 0)


def OptionInitRewardAction211300(oOption, oHero):
    eventnpcaction.InitGoldenCupReward(oOption, oHero, {
        3001: 30011027,
        3007: 30071027,
        3012: 30121027,
        3008: 30081027,
        3009: 30091027 })


def OptionInitCostAction211400(oOption, oHero):
    eventnpcaction.InitCurseRelicCost(oOption, oHero, 0)


def OptionInitRewardAction211400(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 1, WEAPON_ACTION_UPGRADEINSCRIPTION, {
        'UpInsToExclusive': 1 })


def OptionInitCostAction211401(oOption, oHero):
    eventnpcaction.InitCurseRelicCost(oOption, oHero, 0)


def OptionInitRewardAction211401(oOption, oHero):
    eventnpcaction.InitWeaponReward(oOption, oHero, 0, {
        3001: 30011001,
        3005: 30051001,
        3008: 30081001,
        3007: 30071001,
        3009: 30091001,
        3010: 30101001,
        3012: 30121001 }, 1, 0, {
        INSCRIPTION_TYPE_EXCLUSIVE: 1 }, None)


def OptionInitCostAction211402(oOption, oHero):
    eventnpcaction.InitCurseRelicCost(oOption, oHero, 0)


def OptionInitRewardAction211402(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 0, WEAPON_ACTION_UPGRADE, {
        'WeaponUpgradeLevel': 3 })


def OptionInitCostAction211500(oOption, oHero):
    eventnpcaction.InitCurseRelicCost(oOption, oHero, 0)


def OptionInitRewardAction211500(oOption, oHero):
    eventnpcaction.InitAttrReward(oOption, oHero, 'HPMax', 0, 3000)


def OptionInitCostAction211501(oOption, oHero):
    eventnpcaction.InitCurseRelicCost(oOption, oHero, 0)


def OptionInitRewardAction211501(oOption, oHero):
    eventnpcaction.InitAttrReward(oOption, oHero, 'ShieldMax', 0, 2000)


def OptionInitCostAction211502(oOption, oHero):
    eventnpcaction.InitCurseRelicCost(oOption, oHero, 0)


def OptionInitRewardAction211502(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 0, WEAPON_ACTION_UPGRADE, {
        'WeaponUpgradeLevel': 3 })


def OptionInitCostAction211600(oOption, oHero):
    eventnpcaction.InitCurseRelicCost(oOption, oHero, 0)


def OptionInitRewardAction211600(oOption, oHero):
    eventnpcaction.InitRelicReward(oOption, oHero, 0, { }, 1, {
        1: {
            3001: {
                30012112: 20 },
            3005: {
                30052112: 20 },
            3008: {
                30082112: 20 },
            3007: {
                30072112: 20 },
            3009: {
                30092112: 20 },
            3010: {
                30102112: 20 },
            3012: {
                30122112: 20 } },
        2: {
            3001: {
                30012112: 30 },
            3005: {
                30052112: 30 },
            3008: {
                30082112: 30 },
            3007: {
                30072112: 30 },
            3009: {
                30092112: 30 },
            3012: {
                30122112: 30 } },
        3: {
            3001: {
                30012112: 30 },
            3005: {
                30052112: 30 },
            3008: {
                30082112: 30 },
            3007: {
                30072112: 30 },
            3009: {
                30092112: 30 },
            3012: {
                30122112: 30 } } }, None)


def OptionInitCostAction211601(oOption, oHero):
    eventnpcaction.InitCurseRelicCost(oOption, oHero, 0)


def OptionInitRewardAction211601(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 0, WEAPON_ACTION_UPGRADE, {
        'WeaponUpgradeLevel': 3 })


def OptionInitCostAction211602(oOption, oHero):
    eventnpcaction.InitCurseRelicCost(oOption, oHero, 0)


def OptionInitRewardAction211602(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 1, WEAPON_ACTION_UPGRADEINSCRIPTION, {
        'UpInsToExclusive': 1 })


def OptionInitCostAction211700(oOption, oHero):
    eventnpcaction.InitCurseRelicCost(oOption, oHero, 0)


def OptionInitRewardAction211700(oOption, oHero):
    eventnpcaction.InitWeaponReward(oOption, oHero, 0, {
        3001: 30011001,
        3005: 30051001,
        3008: 30081001,
        3007: 30071001,
        3009: 30091001,
        3010: 30101001,
        3012: 30121001 }, 1, 0, {
        INSCRIPTION_TYPE_EXCLUSIVE: 1 }, None)


def OptionInitCostAction211701(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (0.1 + Func201(*a) * 1.5 + Func202(*a) * 0.3) * Func16(*a, **{
'a': 78,
'b': 90 })))


def OptionInitRewardAction211701(oOption, oHero):
    eventnpcaction.InitRelicReward(oOption, oHero, 0, { }, 1, {
        1: {
            3001: {
                30012104: 45,
                30012108: 55 },
            3005: {
                30052104: 45,
                30052108: 55 },
            3008: {
                30082104: 45,
                30082108: 55 },
            3007: {
                30072104: 45,
                30072108: 55 },
            3009: {
                30092104: 45,
                30092108: 55 },
            3010: {
                30102104: 45,
                30102108: 55 },
            3012: {
                30122104: 45,
                30122108: 55 } },
        2: {
            3001: {
                30012104: 37,
                30012108: 63 },
            3005: {
                30052104: 37,
                30052108: 63 },
            3008: {
                30082104: 37,
                30082108: 63 },
            3007: {
                30072104: 37,
                30072108: 63 },
            3009: {
                30092104: 37,
                30092108: 63 },
            3012: {
                30122104: 37,
                30122108: 63 } },
        3: {
            3001: {
                30012104: 37,
                30012108: 63 },
            3005: {
                30052104: 37,
                30052108: 63 },
            3008: {
                30082104: 37,
                30082108: 63 },
            3007: {
                30072104: 37,
                30072108: 63 },
            3009: {
                30092104: 37,
                30092108: 63 },
            3012: {
                30122104: 37,
                30122108: 63 } } }, None)


def OptionInitCostAction211702(oOption, oHero):
    eventnpcaction.InitHPCost(oOption, oHero, 75, 0)


def OptionInitRewardAction211702(oOption, oHero):
    eventnpcaction.InitSelectedRelicReward(oOption, oHero, RELIC_TYPE_CURSE, QUALITY_TYPE_CURSE, 1)


def OptionInitCostAction211800(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (0.1 + Func201(*a) * 1.5 + Func202(*a) * 0.3) * Func16(*a, **{
'a': 78,
'b': 90 })))


def OptionInitRewardAction211800(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 1, WEAPON_ACTION_UPGRADE, {
        'WeaponUpgradeLevel': 1 })


def OptionInitCostAction211801(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (0.1 + Func201(*a) * 1.5 + Func202(*a) * 0.3) * Func16(*a, **{
'a': 144,
'b': 168 })))


def OptionInitRewardAction211801(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 1, WEAPON_ACTION_UPGRADEINSCRIPTION, {
        'UpAllInsToRare': 1 })


def OptionInitCostAction211802(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (0.1 + Func201(*a) * 1.5 + Func202(*a) * 0.3) * Func16(*a, **{
'a': 68,
'b': 80 })))


def OptionInitRewardAction211802(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 2, WEAPON_ACTION_RECAST, { })


def OptionInitCostAction211900(oOption, oHero):
    eventnpcaction.InitHPCost(oOption, oHero, 50, 0)


def OptionInitRewardAction211900(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 1, WEAPON_ACTION_UPGRADE, {
        'WeaponUpgradeLevel': 1 })


def OptionInitCostAction211901(oOption, oHero):
    eventnpcaction.InitHPCost(oOption, oHero, 50, 0)


def OptionInitRewardAction211901(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 1, WEAPON_ACTION_UPGRADEINSCRIPTION, {
        'InscriptionCnt': 1 })


def OptionInitCostAction211902(oOption, oHero):
    eventnpcaction.InitHPCost(oOption, oHero, 50, 0)


def OptionInitRewardAction211902(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 2, WEAPON_ACTION_RECAST, { })


def OptionInitCostAction212000(oOption, oHero):
    eventnpcaction.InitSelectedRelicCost(oOption, oHero, RELIC_TYPE_NORMAL | RELIC_TYPE_CURSE, QUALITY_TYPE_LOW | QUALITY_TYPE_NORMAL | QUALITY_TYPE_HIGH | QUALITY_TYPE_CURSE, 3, None)


def OptionInitRewardAction212000(oOption, oHero):
    eventnpcaction.InitGoldenCupReward(oOption, oHero, {
        3001: 30011027,
        3007: 30071027,
        3012: 30121027,
        3008: 30011027 })


def OptionInitCostAction212100(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (0.1 + Func201(*a) * 1.5 + Func202(*a) * 0.3) * Func16(*a, **{
'a': 78,
'b': 90 })))


def OptionInitRewardAction212100(oOption, oHero):
    eventnpcaction.InitRelicReward(oOption, oHero, 0, { }, 1, {
        1: {
            3001: {
                30012104: 43,
                30012108: 49,
                30012112: 8 },
            3005: {
                30052104: 43,
                30052108: 49,
                30052112: 8 },
            3008: {
                30082104: 43,
                30082108: 49,
                30082112: 8 },
            3007: {
                30072104: 43,
                30072108: 49,
                30072112: 8 },
            3009: {
                30092104: 43,
                30092108: 49,
                30092112: 8 },
            3010: {
                30102104: 43,
                30102108: 49,
                30102112: 8 },
            3012: {
                30122104: 43,
                30122108: 49,
                30122112: 8 } },
        2: {
            3001: {
                30012104: 28,
                30012108: 55,
                30012112: 17 },
            3005: {
                30052104: 28,
                30052108: 55,
                30052112: 17 },
            3008: {
                30082104: 28,
                30082108: 55,
                30082112: 17 },
            3007: {
                30072104: 28,
                30072108: 55,
                30072112: 17 },
            3009: {
                30092104: 28,
                30092108: 55,
                30092112: 17 },
            3012: {
                30122104: 28,
                30122108: 55,
                30122112: 17 } },
        3: {
            3001: {
                30012104: 28,
                30012108: 55,
                30012112: 17 },
            3005: {
                30052104: 28,
                30052108: 55,
                30052112: 17 },
            3008: {
                30082104: 28,
                30082108: 55,
                30082112: 17 },
            3007: {
                30072104: 28,
                30072108: 55,
                30072112: 17 },
            3009: {
                30092104: 28,
                30092108: 55,
                30092112: 17 },
            3012: {
                30122104: 28,
                30122108: 55,
                30122112: 17 } } }, None)


def OptionInitCostAction212101(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (0.1 + Func201(*a) * 1.5 + Func202(*a) * 0.3) * Func16(*a, **{
'a': 78,
'b': 90 })))


def OptionInitRewardAction212101(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 1, WEAPON_ACTION_UPGRADEINSCRIPTION, {
        'UpAllInsToRare': 1 })


def OptionInitRewardAction212102(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 2, WEAPON_ACTION_RECAST, { })


def OptionInitCostAction212200(oOption, oHero):
    eventnpcaction.InitCurseRelicCost(oOption, oHero, 0)


def OptionInitRewardAction212200(oOption, oHero):
    eventnpcaction.InitWeaponReward(oOption, oHero, 0, {
        3001: 30011001,
        3005: 30051001,
        3008: 30081001,
        3007: 30071001,
        3009: 30091001,
        3010: 30101001,
        3012: 30121001 }, 1, 0, {
        INSCRIPTION_TYPE_EXCLUSIVE: 1 }, None)


def OptionInitCostAction212201(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (0.1 + Func201(*a) * 1.5 + Func202(*a) * 0.3) * Func16(*a, **{
'a': 48,
'b': 60 })))


def OptionInitRewardAction212201(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 1, WEAPON_ACTION_UPGRADE, {
        'WeaponUpgradeLevel': 1 })


def OptionInitCostAction212202(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (0.1 + Func201(*a) * 1.5 + Func202(*a) * 0.3) * Func16(*a, **{
'a': 48,
'b': 60 })))


def OptionInitRewardAction212202(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 1, WEAPON_ACTION_UPGRADEINSCRIPTION, {
        'InscriptionCnt': 1 })


def OptionInitCostAction212300(oOption, oHero):
    eventnpcaction.InitHPCost(oOption, oHero, 75, 0)


def OptionInitRewardAction212300(oOption, oHero):
    eventnpcaction.InitRelicReward(oOption, oHero, 0, { }, 1, {
        1: {
            3001: {
                30012104: 50 },
            3005: {
                30052104: 50 },
            3008: {
                30082104: 50 },
            3007: {
                30072104: 50 },
            3009: {
                30092104: 50 },
            3010: {
                30102104: 50 },
            3012: {
                30122104: 50 } },
        2: {
            3001: {
                30012104: 40 },
            3005: {
                30052104: 40 },
            3008: {
                30082104: 40 },
            3007: {
                30072104: 40 },
            3009: {
                30092104: 40 },
            3012: {
                30122104: 40 } },
        3: {
            3001: {
                30012104: 40 },
            3005: {
                30052104: 40 },
            3008: {
                30082104: 40 },
            3007: {
                30072104: 40 },
            3009: {
                30092104: 40 },
            3012: {
                30122104: 40 } } }, None)


def OptionInitCostAction212301(oOption, oHero):
    eventnpcaction.InitHPCost(oOption, oHero, 75, 0)


def OptionInitRewardAction212301(oOption, oHero):
    eventnpcaction.InitWarCashReward(oOption, oHero, (lambda *a: (0.1 + Func201(*a) * 1.5 + Func202(*a) * 0.3) * Func16(*a, **{
'a': 145,
'b': 155 })), 1, None)


def OptionInitCostAction220100(oOption, oHero):
    eventnpcaction.InitCurseRelicCost(oOption, oHero, 0)


def OptionInitRewardAction220100(oOption, oHero):
    eventnpcaction.InitRelicReward(oOption, oHero, 0, { }, 1, {
        1: {
            3001: {
                30012407: 100 },
            3008: {
                30082401: 100 },
            3007: {
                30072407: 100 },
            3009: {
                30092401: 100 },
            3010: {
                30102407: 100 },
            3012: {
                30122407: 100 } },
        2: {
            3001: {
                30012407: 100 },
            3008: {
                30082401: 100 },
            3007: {
                30072407: 100 },
            3009: {
                30092401: 100 },
            3012: {
                30122407: 100 } },
        3: {
            3001: {
                30012407: 100 },
            3008: {
                30082401: 100 },
            3007: {
                30072407: 100 },
            3009: {
                30092401: 100 },
            3012: {
                30122407: 100 } } }, 2)


def OptionInitCostAction220101(oOption, oHero):
    eventnpcaction.InitGSCashCost(oOption, oHero, (lambda *a: ceil(Func16(*a, **{
'a': 100,
'b': 120 }) * Func678(*a) / 100)))


def OptionInitRewardAction220101(oOption, oHero):
    eventnpcaction.InitUpgradeRelicReward(oOption, oHero, QUALITY_TYPE_LOW | QUALITY_TYPE_NORMAL | QUALITY_TYPE_HIGH, 1, 0)


def OptionInitCostAction220200(oOption, oHero):
    eventnpcaction.InitGSCashCost(oOption, oHero, (lambda *a: ceil((Func201(*a) * 20 + Func202(*a) * 5) * Func16(*a, **{
'a': 0.3,
'b': 0.5 }) * Func678(*a) / 100)))


def OptionInitRewardAction220200(oOption, oHero):
    eventnpcaction.InitWeaponReward(oOption, oHero, 0, {
        3001: 30011006,
        3005: 30051006,
        3008: 30081001,
        3007: 30071006,
        3009: 30091001,
        3010: 30101006,
        3012: 30121006 }, 1, 0, { }, 1)


def OptionInitCostAction220201(oOption, oHero):
    eventnpcaction.InitGSCashCost(oOption, oHero, (lambda *a: ceil((Func201(*a) * 20 + Func202(*a) * 5) * Func16(*a, **{
'a': 1.2,
'b': 1.5 }) * Func678(*a) / 100)))


def OptionInitRewardAction220201(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 0, WEAPON_ACTION_ENHANCE, { })


def OptionInitCostAction220202(oOption, oHero):
    eventnpcaction.InitGSCashCost(oOption, oHero, (lambda *a: ceil((Func201(*a) * 20 + Func202(*a) * 5) * Func16(*a, **{
'a': 0.8,
'b': 1.1 }) * Func678(*a) / 100)))


def OptionInitRewardAction220202(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 0, WEAPON_ACTION_UPGRADE, {
        'WeaponUpgradeLevel': 3 })


def OptionInitCostAction220400(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: 300 * (Func207(*a) + 1) // (Func207(*a) + 3000) + (0.1 + Func201(*a) * 1.5 + Func202(*a) * 0.3) * Func16(*a, **{
'a': 117,
'b': 135 })))


def OptionInitRewardAction220400(oOption, oHero):
    eventnpcaction.InitRelicReward(oOption, oHero, 0, { }, 1, {
        1: {
            3001: {
                30012407: 100 },
            3008: {
                30082401: 100 },
            3007: {
                30072407: 100 },
            3009: {
                30092401: 100 },
            3010: {
                30102407: 100 },
            3012: {
                30122407: 100 } },
        2: {
            3001: {
                30012407: 100 },
            3008: {
                30082401: 100 },
            3007: {
                30072407: 100 },
            3009: {
                30092401: 100 },
            3012: {
                30122407: 100 } },
        3: {
            3001: {
                30012407: 100 },
            3008: {
                30082401: 100 },
            3007: {
                30072407: 100 },
            3009: {
                30092401: 100 },
            3012: {
                30122407: 100 } } }, 2)


def OptionInitCostAction220401(oOption, oHero):
    eventnpcaction.InitGSCashCost(oOption, oHero, (lambda *a: ceil((Func678(*a) / 100) * (40 * (Func206(*a) + 1) // (Func206(*a) + 4000) + Func16(*a, **{
'a': 50,
'b': 60 })))))


def OptionInitRewardAction220401(oOption, oHero):
    eventnpcaction.InitRelicReward(oOption, oHero, 0, { }, 1, {
        1: {
            3001: {
                30012407: 100 },
            3008: {
                30082401: 100 },
            3007: {
                30072407: 100 },
            3009: {
                30092401: 100 },
            3010: {
                30102407: 100 },
            3012: {
                30122407: 100 } },
        2: {
            3001: {
                30012407: 100 },
            3008: {
                30082401: 100 },
            3007: {
                30072407: 100 },
            3009: {
                30092401: 100 },
            3012: {
                30122407: 100 } },
        3: {
            3001: {
                30012407: 100 },
            3008: {
                30082401: 100 },
            3007: {
                30072407: 100 },
            3009: {
                30092401: 100 },
            3012: {
                30122407: 100 } } }, 2)


def OptionInitCostAction220500(oOption, oHero):
    eventnpcaction.InitGSCashCost(oOption, oHero, (lambda *a: ceil(Func16(*a, **{
'a': 45,
'b': 65 }) * Func678(*a) / 100)))


def OptionInitRewardAction220500(oOption, oHero):
    eventnpcaction.InitRelicReward(oOption, oHero, 0, { }, 1, {
        1: {
            3001: {
                30012407: 100 },
            3008: {
                30082401: 100 },
            3007: {
                30072407: 100 },
            3009: {
                30092401: 100 },
            3010: {
                30102407: 100 },
            3012: {
                30122407: 100 } },
        2: {
            3001: {
                30012407: 100 },
            3008: {
                30082401: 100 },
            3007: {
                30072407: 100 },
            3009: {
                30092401: 100 },
            3012: {
                30122407: 100 } },
        3: {
            3001: {
                30012407: 100 },
            3008: {
                30082401: 100 },
            3007: {
                30072407: 100 },
            3009: {
                30092401: 100 },
            3012: {
                30122407: 100 } } }, 2)


def OptionInitCostAction220501(oOption, oHero):
    eventnpcaction.InitGSCashCost(oOption, oHero, (lambda *a: ceil(Func16(*a, **{
'a': 100,
'b': 120 }) * Func678(*a) / 100)))


def OptionInitRewardAction220501(oOption, oHero):
    eventnpcaction.InitUpgradeRelicReward(oOption, oHero, QUALITY_TYPE_LOW | QUALITY_TYPE_NORMAL | QUALITY_TYPE_HIGH, 1, 0)


def OptionInitCostAction220600(oOption, oHero):
    eventnpcaction.InitSelectedRelicCost(oOption, oHero, RELIC_TYPE_NORMAL | RELIC_TYPE_CURSE, QUALITY_TYPE_LOW | QUALITY_TYPE_NORMAL | QUALITY_TYPE_HIGH | QUALITY_TYPE_CURSE, 3, 0)


def OptionInitRewardAction220600(oOption, oHero):
    eventnpcaction.InitRelicReward(oOption, oHero, 0, { }, 1, {
        1: {
            3001: {
                30012407: 100 },
            3008: {
                30082401: 100 },
            3007: {
                30072407: 100 },
            3009: {
                30092401: 100 },
            3010: {
                30102407: 100 },
            3012: {
                30122407: 100 } },
        2: {
            3001: {
                30012407: 100 },
            3008: {
                30082401: 100 },
            3007: {
                30072407: 100 },
            3009: {
                30092401: 100 },
            3012: {
                30122407: 100 } },
        3: {
            3001: {
                30012407: 100 },
            3008: {
                30082401: 100 },
            3007: {
                30072407: 100 },
            3009: {
                30092401: 100 },
            3012: {
                30122407: 100 } } }, 2)


def OptionInitCostAction220601(oOption, oHero):
    eventnpcaction.InitSelectedRelicCost(oOption, oHero, RELIC_TYPE_NORMAL, QUALITY_TYPE_LOW | QUALITY_TYPE_NORMAL | QUALITY_TYPE_HIGH, 1, 2)


def OptionInitRewardAction220601(oOption, oHero):
    eventnpcaction.InitRelicReward(oOption, oHero, 0, { }, 1, {
        1: {
            3001: {
                30012407: 100 },
            3008: {
                30082401: 100 },
            3007: {
                30072407: 100 },
            3009: {
                30092401: 100 },
            3010: {
                30102407: 100 },
            3012: {
                30122407: 100 } },
        2: {
            3001: {
                30012407: 100 },
            3008: {
                30082401: 100 },
            3007: {
                30072407: 100 },
            3009: {
                30092401: 100 },
            3012: {
                30122407: 100 } },
        3: {
            3001: {
                30012407: 100 },
            3008: {
                30082401: 100 },
            3007: {
                30072407: 100 },
            3009: {
                30092401: 100 },
            3012: {
                30122407: 100 } } }, 2)


def OptionInitCostAction230100(oOption, oHero):
    eventnpcaction.InitCurseRelicCost(oOption, oHero, -1)


def OptionInitRewardAction230100(oOption, oHero):
    eventnpcaction.InitMagicPowerReward(oOption, oHero, 2, 3)


def OptionInitCostAction230101(oOption, oHero):
    eventnpcaction.InitSelectedRelicCost(oOption, oHero, RELIC_TYPE_NORMAL | RELIC_TYPE_CURSE, QUALITY_TYPE_LOW | QUALITY_TYPE_NORMAL | QUALITY_TYPE_HIGH | QUALITY_TYPE_CURSE, 1, 0)


def OptionInitRewardAction230101(oOption, oHero):
    eventnpcaction.InitMagicPowerReward(oOption, oHero, 2, 3)


def OptionInitCostAction230200(oOption, oHero):
    eventnpcaction.InitSelectedRelicCost(oOption, oHero, RELIC_TYPE_NORMAL | RELIC_TYPE_CURSE, QUALITY_TYPE_LOW | QUALITY_TYPE_NORMAL | QUALITY_TYPE_HIGH | QUALITY_TYPE_CURSE, 1, 0)


def OptionInitRewardAction230200(oOption, oHero):
    eventnpcaction.InitMagicPowerReward(oOption, oHero, 1, 3)


def OptionInitCostAction230201(oOption, oHero):
    eventnpcaction.InitSelectedRelicCost(oOption, oHero, RELIC_TYPE_NORMAL, QUALITY_TYPE_NORMAL, 1, 0)


def OptionInitRewardAction230201(oOption, oHero):
    eventnpcaction.InitMagicPowerReward(oOption, oHero, 2, 3)


def OptionInitCostAction230202(oOption, oHero):
    eventnpcaction.InitSelectedRelicCost(oOption, oHero, RELIC_TYPE_NORMAL, QUALITY_TYPE_HIGH, 1, 0)


def OptionInitRewardAction230202(oOption, oHero):
    eventnpcaction.InitMagicPowerReward(oOption, oHero, 3, 3)


def OptionInitCostAction310100(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (1.7 + Func441(*a) * 0.2) * Func16(*a, **{
'a': 48,
'b': 60 })))


def OptionInitRewardAction310100(oOption, oHero):
    eventnpcaction.InitWeaponReward(oOption, oHero, 0, {
        3001: 30011001,
        3005: 30051001,
        3008: 30081001,
        3007: 30071001,
        3009: 30091001,
        3010: 30101001,
        3012: 30121001,
        3020: 30201001,
        3030: 30301001 }, 1, None, { }, -1)


def OptionInitCostAction310101(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (1.7 + Func441(*a) * 0.2) * Func16(*a, **{
'a': 72,
'b': 84 })))


def OptionInitRewardAction310101(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 1, WEAPON_ACTION_UPGRADEINSCRIPTION, {
        'InscriptionCnt': 1 })


def OptionInitCostAction310102(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (1.7 + Func441(*a) * 0.2) * Func16(*a, **{
'a': 68,
'b': 80 })))


def OptionInitRewardAction310102(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 2, WEAPON_ACTION_RECAST, { })


def OptionInitCostAction310200(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (1.7 + Func441(*a) * 0.2) * Func16(*a, **{
'a': 90,
'b': 110 })))


def OptionInitRewardAction310200(oOption, oHero):
    eventnpcaction.InitAttrReward(oOption, oHero, 'HPMax', 0, 1800)


def OptionInitCostAction310201(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (1.7 + Func441(*a) * 0.2) * Func16(*a, **{
'a': 90,
'b': 110 })))


def OptionInitRewardAction310201(oOption, oHero):
    eventnpcaction.InitAttrReward(oOption, oHero, 'ShieldMax', 0, 1200)


def OptionInitCostAction310300(oOption, oHero):
    eventnpcaction.InitHPCost(oOption, oHero, 45, 0)


def OptionInitRewardAction310300(oOption, oHero):
    eventnpcaction.InitAttrReward(oOption, oHero, 'HPMax', 0, 2400)


def OptionInitCostAction310301(oOption, oHero):
    eventnpcaction.InitHPCost(oOption, oHero, 45, 0)


def OptionInitRewardAction310301(oOption, oHero):
    eventnpcaction.InitAttrReward(oOption, oHero, 'ShieldMax', 0, 1600)


def OptionInitCostAction310500(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (1.5 + Func441(*a) * 0.2) * Func16(*a, **{
'a': 45,
'b': 55 })))


def OptionInitRewardAction310500(oOption, oHero):
    eventnpcaction.InitRelicReward(oOption, oHero, 0, { }, 1, {
        1: {
            3001: {
                30012104: 43,
                30012108: 49,
                30012112: 8 },
            3005: {
                30052104: 43,
                30052108: 49,
                30052112: 8 },
            3008: {
                30082104: 43,
                30082108: 49,
                30082112: 8 },
            3007: {
                30072104: 43,
                30072108: 49,
                30072112: 8 },
            3009: {
                30092104: 43,
                30092108: 49,
                30092112: 8 },
            3010: {
                30102104: 43,
                30102108: 49,
                30102112: 8 },
            3012: {
                30122104: 43,
                30122108: 49,
                30122112: 8 },
            3020: {
                30202104: 43,
                30202108: 49,
                30202112: 8 },
            3030: {
                30302104: 43,
                30202108: 49,
                30302112: 8 } },
        2: {
            3001: {
                30012104: 28,
                30012108: 55,
                30012112: 17 },
            3005: {
                30052104: 28,
                30052108: 55,
                30052112: 17 },
            3008: {
                30082104: 28,
                30082108: 55,
                30082112: 17 },
            3007: {
                30072104: 28,
                30072108: 55,
                30072112: 17 },
            3009: {
                30092104: 28,
                30092108: 55,
                30092112: 17 },
            3012: {
                30122104: 28,
                30122108: 55,
                30122112: 17 },
            3020: {
                30202104: 28,
                30202108: 55,
                30202112: 17 },
            3030: {
                30302104: 28,
                30302108: 55,
                30302112: 17 } },
        3: {
            3001: {
                30012104: 28,
                30012108: 55,
                30012112: 17 },
            3005: {
                30052104: 28,
                30052108: 55,
                30052112: 17 },
            3008: {
                30082104: 28,
                30082108: 55,
                30082112: 17 },
            3007: {
                30072104: 28,
                30072108: 55,
                30072112: 17 },
            3009: {
                30092104: 28,
                30092108: 55,
                30092112: 17 },
            3012: {
                30122104: 28,
                30122108: 55,
                30122112: 17 },
            3020: {
                30202104: 28,
                30202108: 55,
                30202112: 17 },
            3030: {
                30302104: 28,
                30302108: 55,
                30302112: 17 } } }, 1)


def OptionInitCostAction310501(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (1.5 + Func441(*a) * 0.2) * Func16(*a, **{
'a': 45,
'b': 55 })))


def OptionInitRewardAction310501(oOption, oHero):
    eventnpcaction.InitRelicReward(oOption, oHero, 0, { }, 1, {
        1: {
            3001: {
                30012108: 47 },
            3005: {
                30052108: 47 },
            3008: {
                30082108: 47 },
            3007: {
                30072108: 47 },
            3009: {
                30092108: 47 },
            3010: {
                30102108: 47 },
            3012: {
                30122108: 47 },
            3020: {
                30202108: 47 },
            3030: {
                30302108: 47 } },
        2: {
            3001: {
                30012108: 55 },
            3005: {
                30052108: 55 },
            3008: {
                30082108: 55 },
            3007: {
                30072108: 55 },
            3009: {
                30092108: 55 },
            3012: {
                30122108: 55 },
            3020: {
                30202108: 55 },
            3030: {
                30302108: 55 } },
        3: {
            3001: {
                30012108: 55 },
            3005: {
                30052108: 55 },
            3008: {
                30082108: 55 },
            3007: {
                30072108: 55 },
            3009: {
                30092108: 55 },
            3012: {
                30122108: 55 },
            3020: {
                30202108: 55 },
            3030: {
                30302108: 55 } } }, 1)


def OptionInitCostAction310502(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (1.5 + Func441(*a) * 0.2) * Func16(*a, **{
'a': 25,
'b': 35 })))


def OptionInitRewardAction310502(oOption, oHero):
    eventnpcaction.InitRelicReward(oOption, oHero, 0, { }, 1, {
        1: {
            3001: {
                30012104: 40 },
            3005: {
                30052104: 40 },
            3008: {
                30082104: 40 },
            3007: {
                30072104: 40 },
            3009: {
                30092104: 40 },
            3010: {
                30102104: 40 },
            3012: {
                30122104: 40 },
            3020: {
                30202104: 40 },
            3030: {
                30302104: 40 } },
        2: {
            3001: {
                30012104: 20 },
            3005: {
                30052104: 20 },
            3008: {
                30082104: 20 },
            3007: {
                30072104: 20 },
            3009: {
                30092104: 20 },
            3012: {
                30122104: 20 },
            3020: {
                30202104: 20 },
            3030: {
                30302104: 20 } },
        3: {
            3001: {
                30012104: 20 },
            3005: {
                30052104: 20 },
            3008: {
                30082104: 20 },
            3007: {
                30072104: 20 },
            3009: {
                30092104: 20 },
            3012: {
                30122104: 20 },
            3020: {
                30202104: 20 },
            3030: {
                30302104: 20 } } }, 1)


def OptionInitCostAction311200(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (1.5 + Func441(*a) * 0.2) * Func16(*a, **{
'a': 120,
'b': 140 })))


def OptionInitRewardAction311200(oOption, oHero):
    eventnpcaction.InitRelicReward(oOption, oHero, 0, { }, 1, {
        1: {
            3001: {
                30012112: 20 },
            3005: {
                30052112: 20 },
            3008: {
                30082112: 20 },
            3007: {
                30072112: 20 },
            3009: {
                30092112: 20 },
            3010: {
                30102112: 20 },
            3012: {
                30122112: 20 },
            3020: {
                30202112: 20 },
            3030: {
                30302112: 20 } },
        2: {
            3001: {
                30012112: 30 },
            3005: {
                30052112: 30 },
            3008: {
                30082112: 30 },
            3007: {
                30072112: 30 },
            3009: {
                30092112: 30 },
            3012: {
                30122112: 30 },
            3020: {
                30202112: 30 },
            3030: {
                30302112: 30 } },
        3: {
            3001: {
                30012112: 30 },
            3005: {
                30052112: 30 },
            3008: {
                30082112: 30 },
            3007: {
                30072112: 30 },
            3009: {
                30092112: 30 },
            3012: {
                30122112: 30 },
            3020: {
                30202112: 30 },
            3030: {
                30302112: 30 } } }, 1)


def OptionInitCostAction311201(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (1.5 + Func441(*a) * 0.2) * Func16(*a, **{
'a': 45,
'b': 55 })))


def OptionInitRewardAction311201(oOption, oHero):
    eventnpcaction.InitRelicReward(oOption, oHero, 0, { }, 1, {
        1: {
            3001: {
                30012104: 43,
                30012108: 49,
                30012112: 8 },
            3005: {
                30052104: 43,
                30052108: 49,
                30052112: 8 },
            3008: {
                30082104: 43,
                30082108: 49,
                30082112: 8 },
            3007: {
                30072104: 43,
                30072108: 49,
                30072112: 8 },
            3009: {
                30092104: 43,
                30092108: 49,
                30092112: 8 },
            3010: {
                30102104: 43,
                30102108: 49,
                30102112: 8 },
            3012: {
                30122104: 43,
                30122108: 49,
                30122112: 8 },
            3020: {
                30202104: 43,
                30202108: 49,
                30202112: 8 },
            3030: {
                30302104: 43,
                30302108: 49,
                30302112: 8 } },
        2: {
            3001: {
                30012104: 28,
                30012108: 55,
                30012112: 17 },
            3005: {
                30052104: 28,
                30052108: 55,
                30052112: 17 },
            3008: {
                30082104: 28,
                30082108: 55,
                30082112: 17 },
            3007: {
                30072104: 28,
                30072108: 55,
                30072112: 17 },
            3009: {
                30092104: 28,
                30092108: 55,
                30092112: 17 },
            3012: {
                30122104: 28,
                30122108: 55,
                30122112: 17 },
            3020: {
                30202104: 28,
                30202108: 55,
                30202112: 17 },
            3030: {
                30302104: 28,
                30302108: 55,
                30302112: 17 } },
        3: {
            3001: {
                30012104: 28,
                30012108: 55,
                30012112: 17 },
            3005: {
                30052104: 28,
                30052108: 55,
                30052112: 17 },
            3008: {
                30082104: 28,
                30082108: 55,
                30082112: 17 },
            3007: {
                30072104: 28,
                30072108: 55,
                30072112: 17 },
            3009: {
                30092104: 28,
                30092108: 55,
                30092112: 17 },
            3012: {
                30122104: 28,
                30122108: 55,
                30122112: 17 },
            3020: {
                30202104: 28,
                30202108: 55,
                30202112: 17 },
            3030: {
                30302104: 28,
                30302108: 55,
                30302112: 17 } } }, 1)


def OptionInitCostAction311202(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (1.5 + Func441(*a) * 0.2) * Func16(*a, **{
'a': 25,
'b': 35 })))


def OptionInitRewardAction311202(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 1, WEAPON_ACTION_UPGRADEINSCRIPTION, {
        'InscriptionCnt': 1 })


def OptionInitCostAction311300(oOption, oHero):
    eventnpcaction.InitCurseRelicCost(oOption, oHero, 0)


def OptionInitRewardAction311300(oOption, oHero):
    eventnpcaction.InitGoldenCupReward(oOption, oHero, {
        3001: 30011027,
        3007: 30071027,
        3012: 30121027,
        3008: 30011027,
        3020: 30201027,
        3030: 30301027 })


def OptionInitCostAction311500(oOption, oHero):
    eventnpcaction.InitCurseRelicCost(oOption, oHero, 0)


def OptionInitRewardAction311500(oOption, oHero):
    eventnpcaction.InitAttrReward(oOption, oHero, 'HPMax', 0, 3000)


def OptionInitCostAction311501(oOption, oHero):
    eventnpcaction.InitCurseRelicCost(oOption, oHero, 0)


def OptionInitRewardAction311501(oOption, oHero):
    eventnpcaction.InitAttrReward(oOption, oHero, 'ShieldMax', 0, 2000)


def OptionInitCostAction311502(oOption, oHero):
    eventnpcaction.InitCurseRelicCost(oOption, oHero, 0)


def OptionInitRewardAction311502(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 0, WEAPON_ACTION_UPGRADE, {
        'WeaponUpgradeLevel': 3 })


def OptionInitCostAction311600(oOption, oHero):
    eventnpcaction.InitCurseRelicCost(oOption, oHero, 0)


def OptionInitRewardAction311600(oOption, oHero):
    eventnpcaction.InitRelicReward(oOption, oHero, 0, { }, 1, {
        1: {
            3001: {
                30012112: 20 },
            3005: {
                30052112: 20 },
            3008: {
                30082112: 20 },
            3007: {
                30072112: 20 },
            3009: {
                30092112: 20 },
            3010: {
                30102112: 20 },
            3012: {
                30122112: 20 },
            3020: {
                30202112: 20 },
            3030: {
                30302112: 20 } },
        2: {
            3001: {
                30012112: 30 },
            3005: {
                30052112: 30 },
            3008: {
                30082112: 30 },
            3007: {
                30072112: 30 },
            3009: {
                30092112: 30 },
            3012: {
                30122112: 30 },
            3020: {
                30202112: 30 },
            3030: {
                30302112: 30 } },
        3: {
            3001: {
                30012112: 30 },
            3005: {
                30052112: 30 },
            3008: {
                30082112: 30 },
            3007: {
                30072112: 30 },
            3009: {
                30092112: 30 },
            3012: {
                30122112: 30 },
            3020: {
                30202112: 30 },
            3030: {
                30302112: 30 } } }, 1)


def OptionInitCostAction311601(oOption, oHero):
    eventnpcaction.InitCurseRelicCost(oOption, oHero, 0)


def OptionInitRewardAction311601(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 0, WEAPON_ACTION_UPGRADE, {
        'WeaponUpgradeLevel': 3 })


def OptionInitCostAction311602(oOption, oHero):
    eventnpcaction.InitCurseRelicCost(oOption, oHero, 0)


def OptionInitRewardAction311602(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 1, WEAPON_ACTION_UPGRADEINSCRIPTION, {
        'UpInsToExclusive': 1 })


def OptionInitCostAction311700(oOption, oHero):
    eventnpcaction.InitCurseRelicCost(oOption, oHero, 0)


def OptionInitRewardAction311700(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 1, WEAPON_ACTION_UPGRADEINSCRIPTION, {
        'UpInsToExclusive': 1 })


def OptionInitCostAction311701(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (1.5 + Func441(*a) * 0.2) * Func16(*a, **{
'a': 45,
'b': 55 })))


def OptionInitRewardAction311701(oOption, oHero):
    eventnpcaction.InitRelicReward(oOption, oHero, 0, { }, 1, {
        1: {
            3001: {
                30012104: 43,
                30012108: 49,
                30012112: 8 },
            3005: {
                30052104: 43,
                30052108: 49,
                30052112: 8 },
            3008: {
                30082104: 43,
                30082108: 49,
                30082112: 8 },
            3007: {
                30072104: 43,
                30072108: 49,
                30072112: 8 },
            3009: {
                30092104: 43,
                30092108: 49,
                30092112: 8 },
            3010: {
                30102104: 43,
                30102108: 49,
                30102112: 8 },
            3012: {
                30122104: 43,
                30122108: 49,
                30122112: 8 },
            3020: {
                30202104: 43,
                30202108: 49,
                30202112: 8 },
            3030: {
                30302104: 43,
                30302108: 49,
                30302112: 8 } },
        2: {
            3001: {
                30012104: 28,
                30012108: 55,
                30012112: 17 },
            3005: {
                30052104: 28,
                30052108: 55,
                30052112: 17 },
            3008: {
                30082104: 28,
                30082108: 55,
                30082112: 17 },
            3007: {
                30072104: 28,
                30072108: 55,
                30072112: 17 },
            3009: {
                30092104: 28,
                30092108: 55,
                30092112: 17 },
            3012: {
                30122104: 28,
                30122108: 55,
                30122112: 17 },
            3020: {
                30202104: 28,
                30202108: 55,
                30202112: 17 },
            3030: {
                30302104: 28,
                30302108: 55,
                30302112: 17 } },
        3: {
            3001: {
                30012104: 28,
                30012108: 55,
                30012112: 17 },
            3005: {
                30052104: 28,
                30052108: 55,
                30052112: 17 },
            3008: {
                30082104: 28,
                30082108: 55,
                30082112: 17 },
            3007: {
                30072104: 28,
                30072108: 55,
                30072112: 17 },
            3009: {
                30092104: 28,
                30092108: 55,
                30092112: 17 },
            3012: {
                30122104: 28,
                30122108: 55,
                30122112: 17 },
            3020: {
                30202104: 28,
                30202108: 55,
                30202112: 17 },
            3030: {
                30302104: 28,
                30302108: 55,
                30302112: 17 } } }, 1)


def OptionInitCostAction311702(oOption, oHero):
    eventnpcaction.InitHPCost(oOption, oHero, 75, 0)


def OptionInitRewardAction311702(oOption, oHero):
    eventnpcaction.InitSelectedRelicReward(oOption, oHero, RELIC_TYPE_CURSE, QUALITY_TYPE_CURSE, 1)


def OptionInitCostAction311800(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (1.5 + Func441(*a) * 0.2) * Func16(*a, **{
'a': 45,
'b': 55 })))


def OptionInitRewardAction311800(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 0, WEAPON_ACTION_UPGRADE, {
        'WeaponUpgradeLevel': 3 })


def OptionInitCostAction311801(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (1.5 + Func441(*a) * 0.2) * Func16(*a, **{
'a': 75,
'b': 85 })))


def OptionInitRewardAction311801(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 1, WEAPON_ACTION_UPGRADEINSCRIPTION, {
        'UpAllInsToRare': 1 })


def OptionInitCostAction311802(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (1.5 + Func441(*a) * 0.2) * Func16(*a, **{
'a': 45,
'b': 55 })))


def OptionInitRewardAction311802(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 2, WEAPON_ACTION_RECAST, { })


def OptionInitCostAction311900(oOption, oHero):
    eventnpcaction.InitSelectedRelicCost(oOption, oHero, RELIC_TYPE_NORMAL | RELIC_TYPE_CURSE, QUALITY_TYPE_LOW | QUALITY_TYPE_NORMAL | QUALITY_TYPE_HIGH | QUALITY_TYPE_CURSE, 1, 0)


def OptionInitRewardAction311900(oOption, oHero):
    eventnpcaction.InitRelicReward(oOption, oHero, 0, { }, 1, {
        1: {
            3001: {
                30012104: 43,
                30012108: 49,
                30012112: 8 },
            3005: {
                30052104: 43,
                30052108: 49,
                30052112: 8 },
            3008: {
                30082104: 43,
                30082108: 49,
                30082112: 8 },
            3007: {
                30072104: 43,
                30072108: 49,
                30072112: 8 },
            3009: {
                30092104: 43,
                30092108: 49,
                30092112: 8 },
            3010: {
                30102104: 43,
                30102108: 49,
                30102112: 8 },
            3012: {
                30122104: 43,
                30122108: 49,
                30122112: 8 },
            3020: {
                30202104: 43,
                30202108: 49,
                30202112: 8 },
            3030: {
                30302104: 43,
                30202108: 49,
                30302112: 8 } },
        2: {
            3001: {
                30012104: 28,
                30012108: 55,
                30012112: 17 },
            3005: {
                30052104: 28,
                30052108: 55,
                30052112: 17 },
            3008: {
                30082104: 28,
                30082108: 55,
                30082112: 17 },
            3007: {
                30072104: 28,
                30072108: 55,
                30072112: 17 },
            3009: {
                30092104: 28,
                30092108: 55,
                30092112: 17 },
            3012: {
                30122104: 28,
                30122108: 55,
                30122112: 17 },
            3020: {
                30202104: 28,
                30202108: 55,
                30202112: 17 },
            3030: {
                30302104: 28,
                30302108: 55,
                30302112: 17 } },
        3: {
            3001: {
                30012104: 28,
                30012108: 55,
                30012112: 17 },
            3005: {
                30052104: 28,
                30052108: 55,
                30052112: 17 },
            3008: {
                30082104: 28,
                30082108: 55,
                30082112: 17 },
            3007: {
                30072104: 28,
                30072108: 55,
                30072112: 17 },
            3009: {
                30092104: 28,
                30092108: 55,
                30092112: 17 },
            3012: {
                30122104: 28,
                30122108: 55,
                30122112: 17 },
            3020: {
                30202104: 28,
                30202108: 55,
                30202112: 17 },
            3030: {
                30302104: 28,
                30302108: 55,
                30302112: 17 } } }, 1)


def OptionInitCostAction311901(oOption, oHero):
    eventnpcaction.InitSelectedRelicCost(oOption, oHero, RELIC_TYPE_NORMAL | RELIC_TYPE_CURSE, QUALITY_TYPE_LOW | QUALITY_TYPE_NORMAL | QUALITY_TYPE_HIGH | QUALITY_TYPE_CURSE, 1, 0)


def OptionInitRewardAction311901(oOption, oHero):
    eventnpcaction.InitAttrReward(oOption, oHero, 'HPMax', 0, 2400)


def OptionInitCostAction311902(oOption, oHero):
    eventnpcaction.InitSelectedRelicCost(oOption, oHero, RELIC_TYPE_NORMAL | RELIC_TYPE_CURSE, QUALITY_TYPE_LOW | QUALITY_TYPE_NORMAL | QUALITY_TYPE_HIGH | QUALITY_TYPE_CURSE, 1, 0)


def OptionInitRewardAction311902(oOption, oHero):
    eventnpcaction.InitAttrReward(oOption, oHero, 'ShieldMax', 0, 1600)


def OptionInitCostAction312100(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (1.7 + Func441(*a) * 0.2) * Func16(*a, **{
'a': 78,
'b': 90 })))


def OptionInitRewardAction312100(oOption, oHero):
    eventnpcaction.InitRelicReward(oOption, oHero, 0, { }, 1, {
        1: {
            3001: {
                30012104: 43,
                30012108: 49,
                30012112: 8 },
            3005: {
                30052104: 43,
                30052108: 49,
                30052112: 8 },
            3008: {
                30082104: 43,
                30082108: 49,
                30082112: 8 },
            3007: {
                30072104: 43,
                30072108: 49,
                30072112: 8 },
            3009: {
                30092104: 43,
                30092108: 49,
                30092112: 8 },
            3010: {
                30102104: 43,
                30102108: 49,
                30102112: 8 },
            3012: {
                30122104: 43,
                30122108: 49,
                30122112: 8 },
            3020: {
                30202104: 43,
                30202108: 49,
                30202112: 8 },
            3030: {
                30302104: 43,
                30302108: 49,
                30302112: 8 } },
        2: {
            3001: {
                30012104: 28,
                30012108: 55,
                30012112: 17 },
            3005: {
                30052104: 28,
                30052108: 55,
                30052112: 17 },
            3008: {
                30082104: 28,
                30082108: 55,
                30082112: 17 },
            3007: {
                30072104: 28,
                30072108: 55,
                30072112: 17 },
            3009: {
                30092104: 28,
                30092108: 55,
                30092112: 17 },
            3012: {
                30122104: 28,
                30122108: 55,
                30122112: 17 },
            3020: {
                30202104: 28,
                30202108: 55,
                30202112: 17 },
            3030: {
                30302104: 28,
                30302108: 55,
                30302112: 17 } },
        3: {
            3001: {
                30012104: 28,
                30012108: 55,
                30012112: 17 },
            3005: {
                30052104: 28,
                30052108: 55,
                30052112: 17 },
            3008: {
                30082104: 28,
                30082108: 55,
                30082112: 17 },
            3007: {
                30072104: 28,
                30072108: 55,
                30072112: 17 },
            3009: {
                30092104: 28,
                30092108: 55,
                30092112: 17 },
            3012: {
                30122104: 28,
                30122108: 55,
                30122112: 17 },
            3020: {
                30202104: 28,
                30202108: 55,
                30202112: 17 },
            3030: {
                30302104: 28,
                30302108: 55,
                30302112: 17 } } }, 1)


def OptionInitCostAction312101(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (1.7 + Func441(*a) * 0.2) * Func16(*a, **{
'a': 78,
'b': 90 })))


def OptionInitRewardAction312101(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 1, WEAPON_ACTION_UPGRADEINSCRIPTION, {
        'UpAllInsToRare': 1 })


def OptionInitRewardAction312102(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 2, WEAPON_ACTION_RECAST, { })


def OptionInitCostAction312200(oOption, oHero):
    eventnpcaction.InitCurseRelicCost(oOption, oHero, 0)


def OptionInitRewardAction312200(oOption, oHero):
    eventnpcaction.InitWeaponReward(oOption, oHero, 0, {
        3001: 30011001,
        3005: 30051001,
        3008: 30081001,
        3007: 30071001,
        3009: 30091001,
        3010: 30101001,
        3012: 30121001,
        3020: 30201001,
        3030: 30301001 }, 1, 0, {
        INSCRIPTION_TYPE_EXCLUSIVE: 1 }, -1)


def OptionInitCostAction312201(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (1.7 + Func441(*a) * 0.2) * Func16(*a, **{
'a': 48,
'b': 60 })))


def OptionInitRewardAction312201(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 1, WEAPON_ACTION_UPGRADE, {
        'WeaponUpgradeLevel': 1 })


def OptionInitCostAction312202(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (1.7 + Func441(*a) * 0.2) * Func16(*a, **{
'a': 48,
'b': 60 })))


def OptionInitRewardAction312202(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 1, WEAPON_ACTION_UPGRADEINSCRIPTION, {
        'InscriptionCnt': 1 })


def OptionInitCostAction320100(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (1.7 + Func441(*a) * 0.6) * Func16(*a, **{
'a': 48,
'b': 60 })))


def OptionInitRewardAction320100(oOption, oHero):
    eventnpcaction.InitWeaponReward(oOption, oHero, 0, {
        3001: 30011001,
        3005: 30051001,
        3008: 30081001,
        3007: 30071001,
        3009: 30091001,
        3010: 30101001,
        3012: 30121001,
        3020: 30201001,
        3030: 30301001 }, 1, None, { }, -1)


def OptionInitCostAction320101(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (1.7 + Func441(*a) * 0.6) * Func16(*a, **{
'a': 72,
'b': 84 })))


def OptionInitRewardAction320101(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 1, WEAPON_ACTION_UPGRADEINSCRIPTION, {
        'InscriptionCnt': 1 })


def OptionInitCostAction320102(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (1.7 + Func441(*a) * 0.6) * Func16(*a, **{
'a': 68,
'b': 80 })))


def OptionInitRewardAction320102(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 2, WEAPON_ACTION_RECAST, { })


def OptionInitCostAction320200(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (1.7 + Func441(*a) * 0.6) * Func16(*a, **{
'a': 90,
'b': 110 })))


def OptionInitRewardAction320200(oOption, oHero):
    eventnpcaction.InitAttrReward(oOption, oHero, 'HPMax', 0, 1800)


def OptionInitCostAction320201(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (1.7 + Func441(*a) * 0.6) * Func16(*a, **{
'a': 90,
'b': 110 })))


def OptionInitRewardAction320201(oOption, oHero):
    eventnpcaction.InitAttrReward(oOption, oHero, 'ShieldMax', 0, 1200)


def OptionInitCostAction320300(oOption, oHero):
    eventnpcaction.InitHPCost(oOption, oHero, 45, 0)


def OptionInitRewardAction320300(oOption, oHero):
    eventnpcaction.InitAttrReward(oOption, oHero, 'HPMax', 0, 2400)


def OptionInitCostAction320301(oOption, oHero):
    eventnpcaction.InitHPCost(oOption, oHero, 45, 0)


def OptionInitRewardAction320301(oOption, oHero):
    eventnpcaction.InitAttrReward(oOption, oHero, 'ShieldMax', 0, 1600)


def OptionInitCostAction320500(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (1.5 + Func441(*a) * 0.6) * Func16(*a, **{
'a': 45,
'b': 55 })))


def OptionInitRewardAction320500(oOption, oHero):
    eventnpcaction.InitRelicReward(oOption, oHero, 0, { }, 1, {
        1: {
            3001: {
                30012104: 43,
                30012108: 49,
                30012112: 8 },
            3005: {
                30052104: 43,
                30052108: 49,
                30052112: 8 },
            3008: {
                30082104: 43,
                30082108: 49,
                30082112: 8 },
            3007: {
                30072104: 43,
                30072108: 49,
                30072112: 8 },
            3009: {
                30092104: 43,
                30092108: 49,
                30092112: 8 },
            3010: {
                30102104: 43,
                30102108: 49,
                30102112: 8 },
            3012: {
                30122104: 43,
                30122108: 49,
                30122112: 8 },
            3020: {
                30202104: 43,
                30202108: 49,
                30202112: 8 },
            3030: {
                30302104: 43,
                30202108: 49,
                30302112: 8 } },
        2: {
            3001: {
                30012104: 28,
                30012108: 55,
                30012112: 17 },
            3005: {
                30052104: 28,
                30052108: 55,
                30052112: 17 },
            3008: {
                30082104: 28,
                30082108: 55,
                30082112: 17 },
            3007: {
                30072104: 28,
                30072108: 55,
                30072112: 17 },
            3009: {
                30092104: 28,
                30092108: 55,
                30092112: 17 },
            3012: {
                30122104: 28,
                30122108: 55,
                30122112: 17 },
            3020: {
                30202104: 28,
                30202108: 55,
                30202112: 17 },
            3030: {
                30302104: 28,
                30302108: 55,
                30302112: 17 } },
        3: {
            3001: {
                30012104: 28,
                30012108: 55,
                30012112: 17 },
            3005: {
                30052104: 28,
                30052108: 55,
                30052112: 17 },
            3008: {
                30082104: 28,
                30082108: 55,
                30082112: 17 },
            3007: {
                30072104: 28,
                30072108: 55,
                30072112: 17 },
            3009: {
                30092104: 28,
                30092108: 55,
                30092112: 17 },
            3012: {
                30122104: 28,
                30122108: 55,
                30122112: 17 },
            3020: {
                30202104: 28,
                30202108: 55,
                30202112: 17 },
            3030: {
                30302104: 28,
                30302108: 55,
                30302112: 17 } } }, 1)


def OptionInitCostAction320501(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (1.5 + Func441(*a) * 0.6) * Func16(*a, **{
'a': 45,
'b': 55 })))


def OptionInitRewardAction320501(oOption, oHero):
    eventnpcaction.InitRelicReward(oOption, oHero, 0, { }, 1, {
        1: {
            3001: {
                30012108: 47 },
            3005: {
                30052108: 47 },
            3008: {
                30082108: 47 },
            3007: {
                30072108: 47 },
            3009: {
                30092108: 47 },
            3010: {
                30102108: 47 },
            3012: {
                30122108: 47 },
            3020: {
                30202108: 47 },
            3030: {
                30302108: 47 } },
        2: {
            3001: {
                30012108: 55 },
            3005: {
                30052108: 55 },
            3008: {
                30082108: 55 },
            3007: {
                30072108: 55 },
            3009: {
                30092108: 55 },
            3012: {
                30122108: 55 },
            3020: {
                30202108: 55 },
            3030: {
                30302108: 55 } },
        3: {
            3001: {
                30012108: 55 },
            3005: {
                30052108: 55 },
            3008: {
                30082108: 55 },
            3007: {
                30072108: 55 },
            3009: {
                30092108: 55 },
            3012: {
                30122108: 55 },
            3020: {
                30202108: 55 },
            3030: {
                30302108: 55 } } }, 1)


def OptionInitCostAction320502(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (1.5 + Func441(*a) * 0.6) * Func16(*a, **{
'a': 25,
'b': 35 })))


def OptionInitRewardAction320502(oOption, oHero):
    eventnpcaction.InitRelicReward(oOption, oHero, 0, { }, 1, {
        1: {
            3001: {
                30012104: 40 },
            3005: {
                30052104: 40 },
            3008: {
                30082104: 40 },
            3007: {
                30072104: 40 },
            3009: {
                30092104: 40 },
            3010: {
                30102104: 40 },
            3012: {
                30122104: 40 },
            3020: {
                30202104: 40 },
            3030: {
                30302104: 40 } },
        2: {
            3001: {
                30012104: 20 },
            3005: {
                30052104: 20 },
            3008: {
                30082104: 20 },
            3007: {
                30072104: 20 },
            3009: {
                30092104: 20 },
            3012: {
                30122104: 20 },
            3020: {
                30202104: 20 },
            3030: {
                30302104: 20 } },
        3: {
            3001: {
                30012104: 20 },
            3005: {
                30052104: 20 },
            3008: {
                30082104: 20 },
            3007: {
                30072104: 20 },
            3009: {
                30092104: 20 },
            3012: {
                30122104: 20 },
            3020: {
                30202104: 20 },
            3030: {
                30302104: 20 } } }, 1)


def OptionInitCostAction321200(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (1.5 + Func441(*a) * 0.6) * Func16(*a, **{
'a': 120,
'b': 140 })))


def OptionInitRewardAction321200(oOption, oHero):
    eventnpcaction.InitRelicReward(oOption, oHero, 0, { }, 1, {
        1: {
            3001: {
                30012112: 20 },
            3005: {
                30052112: 20 },
            3008: {
                30082112: 20 },
            3007: {
                30072112: 20 },
            3009: {
                30092112: 20 },
            3010: {
                30102112: 20 },
            3012: {
                30122112: 20 },
            3020: {
                30202112: 20 },
            3030: {
                30302112: 20 } },
        2: {
            3001: {
                30012112: 30 },
            3005: {
                30052112: 30 },
            3008: {
                30082112: 30 },
            3007: {
                30072112: 30 },
            3009: {
                30092112: 30 },
            3012: {
                30122112: 30 },
            3020: {
                30202112: 30 },
            3030: {
                30302112: 30 } },
        3: {
            3001: {
                30012112: 30 },
            3005: {
                30052112: 30 },
            3008: {
                30082112: 30 },
            3007: {
                30072112: 30 },
            3009: {
                30092112: 30 },
            3012: {
                30122112: 30 },
            3020: {
                30202112: 30 },
            3030: {
                30302112: 30 } } }, 1)


def OptionInitCostAction321201(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (1.5 + Func441(*a) * 0.6) * Func16(*a, **{
'a': 45,
'b': 55 })))


def OptionInitRewardAction321201(oOption, oHero):
    eventnpcaction.InitRelicReward(oOption, oHero, 0, { }, 1, {
        1: {
            3001: {
                30012104: 43,
                30012108: 49,
                30012112: 8 },
            3005: {
                30052104: 43,
                30052108: 49,
                30052112: 8 },
            3008: {
                30082104: 43,
                30082108: 49,
                30082112: 8 },
            3007: {
                30072104: 43,
                30072108: 49,
                30072112: 8 },
            3009: {
                30092104: 43,
                30092108: 49,
                30092112: 8 },
            3010: {
                30102104: 43,
                30102108: 49,
                30102112: 8 },
            3012: {
                30122104: 43,
                30122108: 49,
                30122112: 8 },
            3020: {
                30202104: 43,
                30202108: 49,
                30202112: 8 },
            3030: {
                30302104: 43,
                30302108: 49,
                30302112: 8 } },
        2: {
            3001: {
                30012104: 28,
                30012108: 55,
                30012112: 17 },
            3005: {
                30052104: 28,
                30052108: 55,
                30052112: 17 },
            3008: {
                30082104: 28,
                30082108: 55,
                30082112: 17 },
            3007: {
                30072104: 28,
                30072108: 55,
                30072112: 17 },
            3009: {
                30092104: 28,
                30092108: 55,
                30092112: 17 },
            3012: {
                30122104: 28,
                30122108: 55,
                30122112: 17 },
            3020: {
                30202104: 28,
                30202108: 55,
                30202112: 17 },
            3030: {
                30302104: 28,
                30302108: 55,
                30302112: 17 } },
        3: {
            3001: {
                30012104: 28,
                30012108: 55,
                30012112: 17 },
            3005: {
                30052104: 28,
                30052108: 55,
                30052112: 17 },
            3008: {
                30082104: 28,
                30082108: 55,
                30082112: 17 },
            3007: {
                30072104: 28,
                30072108: 55,
                30072112: 17 },
            3009: {
                30092104: 28,
                30092108: 55,
                30092112: 17 },
            3012: {
                30122104: 28,
                30122108: 55,
                30122112: 17 },
            3020: {
                30202104: 28,
                30202108: 55,
                30202112: 17 },
            3030: {
                30302104: 28,
                30302108: 55,
                30302112: 17 } } }, 1)


def OptionInitCostAction321202(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (1.5 + Func441(*a) * 0.6) * Func16(*a, **{
'a': 25,
'b': 35 })))


def OptionInitRewardAction321202(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 1, WEAPON_ACTION_UPGRADEINSCRIPTION, {
        'InscriptionCnt': 1 })


def OptionInitCostAction321300(oOption, oHero):
    eventnpcaction.InitCurseRelicCost(oOption, oHero, 0)


def OptionInitRewardAction321300(oOption, oHero):
    eventnpcaction.InitGoldenCupReward(oOption, oHero, {
        3001: 30011027,
        3007: 30071027,
        3012: 30121027,
        3008: 30011027,
        3020: 30201027,
        3030: 30301027 })


def OptionInitCostAction321500(oOption, oHero):
    eventnpcaction.InitCurseRelicCost(oOption, oHero, 0)


def OptionInitRewardAction321500(oOption, oHero):
    eventnpcaction.InitAttrReward(oOption, oHero, 'HPMax', 0, 3000)


def OptionInitCostAction321501(oOption, oHero):
    eventnpcaction.InitCurseRelicCost(oOption, oHero, 0)


def OptionInitRewardAction321501(oOption, oHero):
    eventnpcaction.InitAttrReward(oOption, oHero, 'ShieldMax', 0, 2000)


def OptionInitCostAction321502(oOption, oHero):
    eventnpcaction.InitCurseRelicCost(oOption, oHero, 0)


def OptionInitRewardAction321502(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 0, WEAPON_ACTION_UPGRADE, {
        'WeaponUpgradeLevel': 3 })


def OptionInitCostAction321600(oOption, oHero):
    eventnpcaction.InitCurseRelicCost(oOption, oHero, 0)


def OptionInitRewardAction321600(oOption, oHero):
    eventnpcaction.InitRelicReward(oOption, oHero, 0, { }, 1, {
        1: {
            3001: {
                30012112: 20 },
            3005: {
                30052112: 20 },
            3008: {
                30082112: 20 },
            3007: {
                30072112: 20 },
            3009: {
                30092112: 20 },
            3010: {
                30102112: 20 },
            3012: {
                30122112: 20 },
            3020: {
                30202112: 20 },
            3030: {
                30302112: 20 } },
        2: {
            3001: {
                30012112: 30 },
            3005: {
                30052112: 30 },
            3008: {
                30082112: 30 },
            3007: {
                30072112: 30 },
            3009: {
                30092112: 30 },
            3012: {
                30122112: 30 },
            3020: {
                30202112: 30 },
            3030: {
                30302112: 30 } },
        3: {
            3001: {
                30012112: 30 },
            3005: {
                30052112: 30 },
            3008: {
                30082112: 30 },
            3007: {
                30072112: 30 },
            3009: {
                30092112: 30 },
            3012: {
                30122112: 30 },
            3020: {
                30202112: 30 },
            3030: {
                30302112: 30 } } }, 1)


def OptionInitCostAction321601(oOption, oHero):
    eventnpcaction.InitCurseRelicCost(oOption, oHero, 0)


def OptionInitRewardAction321601(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 0, WEAPON_ACTION_UPGRADE, {
        'WeaponUpgradeLevel': 3 })


def OptionInitCostAction321602(oOption, oHero):
    eventnpcaction.InitCurseRelicCost(oOption, oHero, 0)


def OptionInitRewardAction321602(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 1, WEAPON_ACTION_UPGRADEINSCRIPTION, {
        'UpInsToExclusive': 1 })


def OptionInitCostAction321700(oOption, oHero):
    eventnpcaction.InitCurseRelicCost(oOption, oHero, 0)


def OptionInitRewardAction321700(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 1, WEAPON_ACTION_UPGRADEINSCRIPTION, {
        'UpInsToExclusive': 1 })


def OptionInitCostAction321701(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (1.5 + Func441(*a) * 0.6) * Func16(*a, **{
'a': 45,
'b': 55 })))


def OptionInitRewardAction321701(oOption, oHero):
    eventnpcaction.InitRelicReward(oOption, oHero, 0, { }, 1, {
        1: {
            3001: {
                30012104: 43,
                30012108: 49,
                30012112: 8 },
            3005: {
                30052104: 43,
                30052108: 49,
                30052112: 8 },
            3008: {
                30082104: 43,
                30082108: 49,
                30082112: 8 },
            3007: {
                30072104: 43,
                30072108: 49,
                30072112: 8 },
            3009: {
                30092104: 43,
                30092108: 49,
                30092112: 8 },
            3010: {
                30102104: 43,
                30102108: 49,
                30102112: 8 },
            3012: {
                30122104: 43,
                30122108: 49,
                30122112: 8 },
            3020: {
                30202104: 43,
                30202108: 49,
                30202112: 8 },
            3030: {
                30302104: 43,
                30302108: 49,
                30302112: 8 } },
        2: {
            3001: {
                30012104: 28,
                30012108: 55,
                30012112: 17 },
            3005: {
                30052104: 28,
                30052108: 55,
                30052112: 17 },
            3008: {
                30082104: 28,
                30082108: 55,
                30082112: 17 },
            3007: {
                30072104: 28,
                30072108: 55,
                30072112: 17 },
            3009: {
                30092104: 28,
                30092108: 55,
                30092112: 17 },
            3012: {
                30122104: 28,
                30122108: 55,
                30122112: 17 },
            3020: {
                30202104: 28,
                30202108: 55,
                30202112: 17 },
            3030: {
                30302104: 28,
                30302108: 55,
                30302112: 17 } },
        3: {
            3001: {
                30012104: 28,
                30012108: 55,
                30012112: 17 },
            3005: {
                30052104: 28,
                30052108: 55,
                30052112: 17 },
            3008: {
                30082104: 28,
                30082108: 55,
                30082112: 17 },
            3007: {
                30072104: 28,
                30072108: 55,
                30072112: 17 },
            3009: {
                30092104: 28,
                30092108: 55,
                30092112: 17 },
            3012: {
                30122104: 28,
                30122108: 55,
                30122112: 17 },
            3020: {
                30202104: 28,
                30202108: 55,
                30202112: 17 },
            3030: {
                30302104: 28,
                30302108: 55,
                30302112: 17 } } }, 1)


def OptionInitCostAction321702(oOption, oHero):
    eventnpcaction.InitHPCost(oOption, oHero, 75, 0)


def OptionInitRewardAction321702(oOption, oHero):
    eventnpcaction.InitSelectedRelicReward(oOption, oHero, RELIC_TYPE_CURSE, QUALITY_TYPE_CURSE, 1)


def OptionInitCostAction321800(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (1.5 + Func441(*a) * 0.6) * Func16(*a, **{
'a': 45,
'b': 55 })))


def OptionInitRewardAction321800(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 0, WEAPON_ACTION_UPGRADE, {
        'WeaponUpgradeLevel': 3 })


def OptionInitCostAction321801(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (1.5 + Func441(*a) * 0.6) * Func16(*a, **{
'a': 75,
'b': 85 })))


def OptionInitRewardAction321801(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 1, WEAPON_ACTION_UPGRADEINSCRIPTION, {
        'UpAllInsToRare': 1 })


def OptionInitCostAction321802(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (1.5 + Func441(*a) * 0.6) * Func16(*a, **{
'a': 45,
'b': 55 })))


def OptionInitRewardAction321802(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 2, WEAPON_ACTION_RECAST, { })


def OptionInitCostAction322100(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (1.7 + Func441(*a) * 0.6) * Func16(*a, **{
'a': 78,
'b': 90 })))


def OptionInitRewardAction322100(oOption, oHero):
    eventnpcaction.InitRelicReward(oOption, oHero, 0, { }, 1, {
        1: {
            3001: {
                30012104: 43,
                30012108: 49,
                30012112: 8 },
            3005: {
                30052104: 43,
                30052108: 49,
                30052112: 8 },
            3008: {
                30082104: 43,
                30082108: 49,
                30082112: 8 },
            3007: {
                30072104: 43,
                30072108: 49,
                30072112: 8 },
            3009: {
                30092104: 43,
                30092108: 49,
                30092112: 8 },
            3010: {
                30102104: 43,
                30102108: 49,
                30102112: 8 },
            3012: {
                30122104: 43,
                30122108: 49,
                30122112: 8 },
            3020: {
                30202104: 43,
                30202108: 49,
                30202112: 8 },
            3030: {
                30302104: 43,
                30302108: 49,
                30302112: 8 } },
        2: {
            3001: {
                30012104: 28,
                30012108: 55,
                30012112: 17 },
            3005: {
                30052104: 28,
                30052108: 55,
                30052112: 17 },
            3008: {
                30082104: 28,
                30082108: 55,
                30082112: 17 },
            3007: {
                30072104: 28,
                30072108: 55,
                30072112: 17 },
            3009: {
                30092104: 28,
                30092108: 55,
                30092112: 17 },
            3012: {
                30122104: 28,
                30122108: 55,
                30122112: 17 },
            3020: {
                30202104: 28,
                30202108: 55,
                30202112: 17 },
            3030: {
                30302104: 28,
                30302108: 55,
                30302112: 17 } },
        3: {
            3001: {
                30012104: 28,
                30012108: 55,
                30012112: 17 },
            3005: {
                30052104: 28,
                30052108: 55,
                30052112: 17 },
            3008: {
                30082104: 28,
                30082108: 55,
                30082112: 17 },
            3007: {
                30072104: 28,
                30072108: 55,
                30072112: 17 },
            3009: {
                30092104: 28,
                30092108: 55,
                30092112: 17 },
            3012: {
                30122104: 28,
                30122108: 55,
                30122112: 17 },
            3020: {
                30202104: 28,
                30202108: 55,
                30202112: 17 },
            3030: {
                30302104: 28,
                30302108: 55,
                30302112: 17 } } }, 1)


def OptionInitCostAction322101(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (1.7 + Func441(*a) * 0.6) * Func16(*a, **{
'a': 78,
'b': 90 })))


def OptionInitRewardAction322101(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 1, WEAPON_ACTION_UPGRADEINSCRIPTION, {
        'UpAllInsToRare': 1 })


def OptionInitRewardAction322102(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 2, WEAPON_ACTION_RECAST, { })


def OptionInitCostAction322200(oOption, oHero):
    eventnpcaction.InitCurseRelicCost(oOption, oHero, 0)


def OptionInitRewardAction322200(oOption, oHero):
    eventnpcaction.InitWeaponReward(oOption, oHero, 0, {
        3001: 30011001,
        3005: 30051001,
        3008: 30081001,
        3007: 30071001,
        3009: 30091001,
        3010: 30101001,
        3012: 30121001,
        3020: 30201001,
        3030: 30301001 }, 1, 0, {
        INSCRIPTION_TYPE_EXCLUSIVE: 1 }, -1)


def OptionInitCostAction322201(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (1.7 + Func441(*a) * 0.6) * Func16(*a, **{
'a': 48,
'b': 60 })))


def OptionInitRewardAction322201(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 1, WEAPON_ACTION_UPGRADE, {
        'WeaponUpgradeLevel': 1 })


def OptionInitCostAction322202(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (1.7 + Func441(*a) * 0.6) * Func16(*a, **{
'a': 48,
'b': 60 })))


def OptionInitRewardAction322202(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 1, WEAPON_ACTION_UPGRADEINSCRIPTION, {
        'InscriptionCnt': 1 })


def OptionInitCostAction322300(oOption, oHero):
    eventnpcaction.InitCurseRelicCost(oOption, oHero, 0)


def OptionInitRewardAction322300(oOption, oHero):
    eventnpcaction.InitRelicReward(oOption, oHero, 0, { }, 1, {
        1: {
            3001: {
                30012407: 100 },
            3008: {
                30082401: 100 },
            3007: {
                30072407: 100 },
            3009: {
                30092401: 100 },
            3010: {
                30102407: 100 },
            3012: {
                30122407: 100 },
            3030: {
                30302401: 100 } },
        2: {
            3001: {
                30012407: 100 },
            3008: {
                30082401: 100 },
            3007: {
                30072407: 100 },
            3009: {
                30092401: 100 },
            3012: {
                30122407: 100 },
            3030: {
                30302401: 100 } },
        3: {
            3001: {
                30012407: 100 },
            3008: {
                30082401: 100 },
            3007: {
                30072407: 100 },
            3009: {
                30092401: 100 },
            3012: {
                30122407: 100 },
            3030: {
                30302401: 100 } } }, 2)


def OptionInitCostAction322301(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (1.5 + Func441(*a) * 0.6) * Func16(*a, **{
'a': 120,
'b': 140 })))


def OptionInitRewardAction322301(oOption, oHero):
    eventnpcaction.InitUpgradeRelicReward(oOption, oHero, QUALITY_TYPE_LOW | QUALITY_TYPE_NORMAL | QUALITY_TYPE_HIGH, 1, 0)


def OptionInitCostAction322400(oOption, oHero):
    eventnpcaction.InitSelectedRelicCost(oOption, oHero, RELIC_TYPE_NORMAL | RELIC_TYPE_CURSE, QUALITY_TYPE_LOW | QUALITY_TYPE_NORMAL | QUALITY_TYPE_HIGH | QUALITY_TYPE_CURSE, 3, 0)


def OptionInitRewardAction322400(oOption, oHero):
    eventnpcaction.InitRelicReward(oOption, oHero, 0, { }, 1, {
        1: {
            3001: {
                30012407: 100 },
            3008: {
                30082401: 100 },
            3007: {
                30072407: 100 },
            3009: {
                30092401: 100 },
            3010: {
                30102407: 100 },
            3012: {
                30122407: 100 },
            3030: {
                30302401: 100 } },
        2: {
            3001: {
                30012407: 100 },
            3008: {
                30082401: 100 },
            3007: {
                30072407: 100 },
            3009: {
                30092401: 100 },
            3012: {
                30122407: 100 },
            3030: {
                30302401: 100 } },
        3: {
            3001: {
                30012407: 100 },
            3008: {
                30082401: 100 },
            3007: {
                30072407: 100 },
            3009: {
                30092401: 100 },
            3012: {
                30122407: 100 },
            3030: {
                30302401: 100 } } }, 2)


def OptionInitCostAction322401(oOption, oHero):
    eventnpcaction.InitSelectedRelicCost(oOption, oHero, RELIC_TYPE_NORMAL, QUALITY_TYPE_LOW | QUALITY_TYPE_NORMAL | QUALITY_TYPE_HIGH, 1, 2)


def OptionInitRewardAction322401(oOption, oHero):
    eventnpcaction.InitRelicReward(oOption, oHero, 0, { }, 1, {
        1: {
            3001: {
                30012407: 100 },
            3008: {
                30082401: 100 },
            3007: {
                30072407: 100 },
            3009: {
                30092401: 100 },
            3010: {
                30102407: 100 },
            3012: {
                30122407: 100 },
            3030: {
                30302401: 100 } },
        2: {
            3001: {
                30012407: 100 },
            3008: {
                30082401: 100 },
            3007: {
                30072407: 100 },
            3009: {
                30092401: 100 },
            3012: {
                30122407: 100 },
            3030: {
                30302401: 100 } },
        3: {
            3001: {
                30012407: 100 },
            3008: {
                30082401: 100 },
            3007: {
                30072407: 100 },
            3009: {
                30092401: 100 },
            3012: {
                30122407: 100 },
            3030: {
                30302401: 100 } } }, 2)


def OptionInitCostAction400100(oOption, oHero):
    eventnpcaction.InitRelicCost(oOption, oHero, 0, 1)


def OptionInitRewardAction400100(oOption, oHero):
    eventnpcaction.InitWarCashReward(oOption, oHero, (lambda *a: (0.1 + Func201(*a) * 1.5 + Func202(*a) * 0.3) * Func16(*a, **{
'a': 60,
'b': 70 })), None, None)


def OptionInitCostAction400200(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (0.1 + Func201(*a) * 1.5 + Func202(*a) * 0.3) * Func16(*a, **{
'a': 60,
'b': 70 })))


def OptionInitRewardAction400200(oOption, oHero):
    eventnpcaction.InitSelectedRelicReward(oOption, oHero, RELIC_TYPE_NORMAL | RELIC_TYPE_CURSE, QUALITY_TYPE_LOW | QUALITY_TYPE_NORMAL | QUALITY_TYPE_HIGH | QUALITY_TYPE_CURSE, 1)


def OptionInitRewardAction400300(oOption, oHero):
    eventnpcaction.InitRelicReward(oOption, oHero, 0, { }, 1, {
        2: {
            3008: {
                30082112: 50,
                30082117: 50 },
            3009: {
                30092112: 50,
                30092117: 50 } } }, None)


def OptionInitCostAction400400(oOption, oHero):
    eventnpcaction.InitHPCost(oOption, oHero, 25, 0)


def OptionInitRewardAction400400(oOption, oHero):
    eventnpcaction.InitWarCashReward(oOption, oHero, (lambda *a: (0.1 + Func201(*a) * 0.5 + Func202(*a) * 0.1) * Func16(*a, **{
'a': 90,
'b': 100 })), 1, None)


def OptionInitCostAction400401(oOption, oHero):
    eventnpcaction.InitHPCost(oOption, oHero, 50, 0)


def OptionInitRewardAction400401(oOption, oHero):
    eventnpcaction.InitWarCashReward(oOption, oHero, (lambda *a: (0.1 + Func201(*a) * 1 + Func202(*a) * 0.2) * Func16(*a, **{
'a': 95,
'b': 110 })), 1, None)


def OptionInitCostAction400402(oOption, oHero):
    eventnpcaction.InitHPCost(oOption, oHero, 75, 0)


def OptionInitRewardAction400402(oOption, oHero):
    eventnpcaction.InitWarCashReward(oOption, oHero, (lambda *a: (0.1 + Func201(*a) * 1.5 + Func202(*a) * 0.3) * Func16(*a, **{
'a': 115,
'b': 125 })), 1, None)


def OptionInitCostAction400500(oOption, oHero):
    eventnpcaction.InitHPCost(oOption, oHero, 45, 0)


def OptionInitRewardAction400500(oOption, oHero):
    eventnpcaction.InitAttrReward(oOption, oHero, 'HPMax', 0, 1600)


def OptionInitCostAction400501(oOption, oHero):
    eventnpcaction.InitHPCost(oOption, oHero, 80, 0)


def OptionInitRewardAction400501(oOption, oHero):
    eventnpcaction.InitAttrReward(oOption, oHero, 'HPMax', 0, 3000)


def OptionInitCostAction400600(oOption, oHero):
    eventnpcaction.InitHPCost(oOption, oHero, 50, 0)


def OptionInitRewardAction400600(oOption, oHero):
    eventnpcaction.InitWarCashReward(oOption, oHero, (lambda *a: (0.1 + Func201(*a) * 1.5 + Func202(*a) * 0.1) * Func16(*a, **{
'a': 90,
'b': 110 })), 1, None)


def OptionInitCostAction400601(oOption, oHero):
    eventnpcaction.InitHPCost(oOption, oHero, 60, 0)


def OptionInitRewardAction400601(oOption, oHero):
    eventnpcaction.InitRelicReward(oOption, oHero, 0, { }, 1, {
        1: {
            3001: {
                30012401: 100 },
            3008: {
                30082401: 100 },
            3007: {
                30072401: 100 },
            3009: {
                30092401: 100 },
            3010: {
                30102401: 100 },
            3012: {
                30122401: 100 } },
        2: {
            3001: {
                30012401: 100 },
            3008: {
                30082401: 100 },
            3007: {
                30072401: 100 },
            3009: {
                30092401: 100 },
            3012: {
                30122401: 100 } },
        3: {
            3001: {
                30012401: 100 },
            3008: {
                30082401: 100 },
            3007: {
                30072401: 100 },
            3009: {
                30092401: 100 },
            3012: {
                30122401: 100 } } }, None)


def OptionInitCostAction400602(oOption, oHero):
    eventnpcaction.InitHPCost(oOption, oHero, 45, 0)


def OptionInitRewardAction400602(oOption, oHero):
    eventnpcaction.InitWeaponReward(oOption, oHero, 0, {
        3001: 30011001,
        3005: 30051001,
        3008: 30081001,
        3007: 30071001,
        3009: 30091001,
        3010: 30101001,
        3012: 30121001 }, 1, None, { }, None)


def OptionInitCostAction400700(oOption, oHero):
    eventnpcaction.InitHPCost(oOption, oHero, 35, 0)


def OptionInitRewardAction400700(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 1, WEAPON_ACTION_RECAST, { })


def OptionInitCostAction400701(oOption, oHero):
    eventnpcaction.InitHPCost(oOption, oHero, 35, 0)


def OptionInitRewardAction400701(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 2, WEAPON_ACTION_RECAST, { })


def OptionInitCostAction400702(oOption, oHero):
    eventnpcaction.InitHPCost(oOption, oHero, 40, 0)


def OptionInitRewardAction400702(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 1, WEAPON_ACTION_UPGRADE, { })


def OptionInitCostAction400703(oOption, oHero):
    eventnpcaction.InitHPCost(oOption, oHero, 40, 0)


def OptionInitRewardAction400703(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 2, WEAPON_ACTION_UPGRADE, { })


def OptionInitCostAction400800(oOption, oHero):
    eventnpcaction.InitHPCost(oOption, oHero, 50, 0)


def OptionInitRewardAction400800(oOption, oHero):
    eventnpcaction.InitRelicReward(oOption, oHero, 0, { }, 1, {
        1: {
            3001: {
                30012108: 80,
                30012112: 20 },
            3005: {
                30052108: 80,
                30052112: 20 },
            3008: {
                30082108: 80,
                30082112: 20 },
            3007: {
                30072108: 80,
                30072112: 20 },
            3009: {
                30092108: 80,
                30092112: 20 },
            3010: {
                30102108: 80,
                30102112: 20 },
            3012: {
                30122108: 80,
                30122112: 20 } },
        2: {
            3001: {
                30012108: 70,
                30012112: 30 },
            3005: {
                30052108: 70,
                30052112: 30 },
            3008: {
                30082108: 70,
                30082112: 30 },
            3007: {
                30072108: 70,
                30072112: 30 },
            3009: {
                30092108: 70,
                30092112: 30 },
            3012: {
                30122108: 70,
                30122112: 30 } },
        3: {
            3001: {
                30012108: 70,
                30012112: 30 },
            3005: {
                30052108: 70,
                30052112: 30 },
            3008: {
                30082108: 70,
                30082112: 30 },
            3007: {
                30072108: 70,
                30072112: 30 },
            3009: {
                30092108: 70,
                30092112: 30 },
            3012: {
                30122108: 70,
                30122112: 30 } } }, None)


def OptionInitCostAction400801(oOption, oHero):
    eventnpcaction.InitHPCost(oOption, oHero, 45, 0)


def OptionInitRewardAction400801(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 1, WEAPON_ACTION_UPGRADEINSCRIPTION, {
        'InscriptionCnt': 0 })


def OptionInitCostAction400802(oOption, oHero):
    eventnpcaction.InitHPCost(oOption, oHero, 45, 0)


def OptionInitRewardAction400802(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 2, WEAPON_ACTION_UPGRADEINSCRIPTION, {
        'InscriptionCnt': 0 })


def OptionInitCostAction401000(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (50 + 65 * Func201(*a) + 15 * Func202(*a)) * 0.8 * -1))


def OptionInitRewardAction401000(oOption, oHero):
    eventnpcaction.InitRelicReward(oOption, oHero, 0, { }, 0, {
        1: {
            3001: {
                30012104: 50,
                30012108: 35,
                30012117: 15 },
            3005: {
                30052104: 50,
                30052108: 35,
                30052117: 15 },
            3008: {
                30082104: 50,
                30082108: 35,
                30082117: 15 },
            3007: {
                30072104: 50,
                30072108: 35,
                30072117: 15 },
            3009: {
                30092104: 50,
                30092108: 35,
                30092117: 15 },
            3010: {
                30102104: 50,
                30102108: 35,
                30102117: 15 },
            3012: {
                30122104: 50,
                30122108: 35,
                30122117: 15 } },
        2: {
            3001: {
                30012104: 40,
                30012108: 48,
                30012117: 12 },
            3005: {
                30052104: 40,
                30052108: 48,
                30052117: 12 },
            3008: {
                30082104: 40,
                30082108: 48,
                30082117: 12 },
            3007: {
                30072104: 40,
                30072108: 48,
                30072117: 12 },
            3009: {
                30092104: 40,
                30092108: 48,
                30092117: 12 },
            3012: {
                30122104: 40,
                30122108: 48,
                30122117: 12 } },
        3: {
            3001: {
                30012104: 40,
                30012108: 48,
                30012117: 12 },
            3005: {
                30052104: 40,
                30052108: 48,
                30052117: 12 },
            3008: {
                30082104: 40,
                30082108: 48,
                30082117: 12 },
            3007: {
                30072104: 40,
                30072108: 48,
                30072117: 12 },
            3009: {
                30092104: 40,
                30092108: 48,
                30092117: 12 },
            3012: {
                30122104: 40,
                30122108: 48,
                30122117: 12 } } }, None)


def OptionInitCostAction401001(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (50 + 65 * Func201(*a) + 15 * Func202(*a)) * 1 * -1))


def OptionInitRewardAction401001(oOption, oHero):
    eventnpcaction.InitRelicReward(oOption, oHero, 0, { }, 0, {
        1: {
            3001: {
                30012104: 40,
                30012108: 47,
                30012112: 8,
                30012117: 5 },
            3005: {
                30052104: 40,
                30052108: 47,
                30052112: 8,
                30052117: 5 },
            3008: {
                30082104: 40,
                30082108: 47,
                30082112: 8,
                30082117: 5 },
            3007: {
                30072104: 40,
                30072108: 47,
                30072112: 8,
                30072117: 5 },
            3009: {
                30092104: 40,
                30092108: 47,
                30092112: 8,
                30092117: 5 },
            3010: {
                30102104: 40,
                30102108: 47,
                30102112: 8,
                30102117: 5 },
            3012: {
                30122104: 40,
                30122401: 47,
                30122112: 8,
                30122117: 5 } },
        2: {
            3001: {
                30012104: 25,
                30012108: 55,
                30012112: 17,
                30012117: 3 },
            3005: {
                30052104: 25,
                30052108: 55,
                30052112: 17,
                30052117: 3 },
            3008: {
                30082104: 25,
                30082108: 55,
                30082112: 17,
                30082117: 3 },
            3007: {
                30072104: 25,
                30072108: 55,
                30072112: 17,
                30072117: 3 },
            3009: {
                30092104: 25,
                30092108: 55,
                30092112: 17,
                30092117: 3 },
            3012: {
                30122104: 25,
                30122108: 55,
                30122112: 17,
                30122117: 3 } },
        3: {
            3001: {
                30012104: 25,
                30012108: 55,
                30012112: 17,
                30012117: 3 },
            3005: {
                30052104: 25,
                30052108: 55,
                30052112: 17,
                30052117: 3 },
            3008: {
                30082104: 25,
                30082108: 55,
                30082112: 17,
                30082117: 3 },
            3007: {
                30072104: 25,
                30072108: 55,
                30072112: 17,
                30072117: 3 },
            3009: {
                30092104: 25,
                30092108: 55,
                30092112: 17,
                30092117: 3 },
            3012: {
                30122104: 25,
                30122108: 55,
                30122112: 17,
                30122117: 3 } } }, None)


def OptionInitCostAction401002(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (50 + 65 * Func201(*a) + 15 * Func202(*a)) * 1.2 * -1))


def OptionInitRewardAction401002(oOption, oHero):
    eventnpcaction.InitRelicReward(oOption, oHero, 0, { }, 0, {
        1: {
            3001: {
                30012104: 40,
                30012108: 48,
                30012112: 12 },
            3005: {
                30052104: 40,
                30052108: 48,
                30052112: 12 },
            3008: {
                30082104: 40,
                30082108: 48,
                30082112: 12 },
            3007: {
                30072104: 40,
                30072108: 48,
                30072112: 12 },
            3009: {
                30092104: 40,
                30092108: 48,
                30092112: 12 },
            3010: {
                30102104: 40,
                30102108: 48,
                30102112: 12 },
            3012: {
                30122104: 40,
                30122108: 48,
                30122112: 12 } },
        2: {
            3001: {
                30012104: 20,
                30012108: 60,
                30012112: 20 },
            3005: {
                30052104: 20,
                30052108: 60,
                30052112: 20 },
            3008: {
                30082104: 20,
                30082108: 60,
                30082112: 20 },
            3007: {
                30072104: 20,
                30072108: 60,
                30072112: 20 },
            3009: {
                30092104: 20,
                30092108: 60,
                30092112: 20 },
            3012: {
                30122104: 20,
                30122108: 60,
                30122112: 20 } },
        3: {
            3001: {
                30012104: 20,
                30012108: 60,
                30012112: 20 },
            3005: {
                30052104: 20,
                30052108: 60,
                30052012: 20 },
            3008: {
                30082104: 20,
                30082108: 60,
                30082112: 20 },
            3007: {
                30072104: 20,
                30072108: 60,
                30072112: 20 },
            3009: {
                30092104: 20,
                30092108: 60,
                30092112: 20 },
            3012: {
                30122104: 20,
                30122108: 60,
                30122112: 20 } } }, None)


def OptionInitCostAction401100(oOption, oHero):
    eventnpcaction.InitRelicCost(oOption, oHero, 0, None)


def OptionInitRewardAction401100(oOption, oHero):
    eventnpcaction.InitWarCashReward(oOption, oHero, (lambda *a: (50 + 65 * Func201(*a) + 15 * Func202(*a)) * Func16(*a, **{
'a': 1.5,
'b': 1.8 }) * -1), 0, None)


def OptionInitRewardAction401200(oOption, oHero):
    eventnpcaction.InitRelicReward(oOption, oHero, 0, { }, 1, {
        1: {
            3001: {
                30012104: 40,
                30012108: 42,
                30012112: 18 },
            3005: {
                30052104: 40,
                30052108: 42,
                30052112: 18 },
            3008: {
                30082104: 40,
                30082108: 42,
                30082112: 18 },
            3007: {
                30072104: 40,
                30072108: 42,
                30072112: 18 },
            3009: {
                30092104: 40,
                30092108: 42,
                30092112: 18 },
            3010: {
                30102104: 40,
                30102108: 42,
                30102112: 18 },
            3012: {
                30122104: 40,
                30122108: 42,
                30122112: 18 } },
        2: {
            3001: {
                30012104: 20,
                30012108: 55,
                30012112: 25 },
            3005: {
                30052104: 20,
                30052108: 55,
                30052112: 25 },
            3008: {
                30082104: 20,
                30082108: 55,
                30082112: 25 },
            3007: {
                30072104: 20,
                30072108: 55,
                30072112: 25 },
            3009: {
                30092104: 20,
                30092108: 55,
                30092112: 25 },
            3012: {
                30122104: 20,
                30122108: 55,
                30122112: 25 } },
        3: {
            3001: {
                30012104: 20,
                30012108: 55,
                30012112: 25 },
            3005: {
                30052104: 20,
                30052108: 55,
                30052112: 25 },
            3008: {
                30082104: 20,
                30082108: 55,
                30082112: 25 },
            3007: {
                30072104: 20,
                30072108: 55,
                30072112: 25 },
            3009: {
                30092104: 20,
                30092108: 55,
                30092112: 25 },
            3012: {
                30122104: 20,
                30122108: 55,
                30122112: 25 } } }, None)


def OptionInitCostAction401300(oOption, oHero):
    eventnpcaction.InitHPCost(oOption, oHero, 25, 0)


def OptionInitRewardAction401300(oOption, oHero):
    eventnpcaction.InitWarCashReward(oOption, oHero, (lambda *a: (50 + 65 * Func201(*a) + 15 * Func202(*a)) * Func16(*a, **{
'a': 0.5,
'b': 0.6 }) * -1), 0, None)


def OptionInitCostAction401301(oOption, oHero):
    eventnpcaction.InitHPCost(oOption, oHero, 50, 0)


def OptionInitRewardAction401301(oOption, oHero):
    eventnpcaction.InitWarCashReward(oOption, oHero, (lambda *a: (50 + 65 * Func201(*a) + 15 * Func202(*a)) * -1), 0, None)


def OptionInitCostAction401302(oOption, oHero):
    eventnpcaction.InitHPCost(oOption, oHero, 75, 0)


def OptionInitRewardAction401302(oOption, oHero):
    eventnpcaction.InitWarCashReward(oOption, oHero, (lambda *a: (50 + 65 * Func201(*a) + 15 * Func202(*a)) * Func16(*a, **{
'a': 1.4,
'b': 1.5 }) * -1), 0, None)


def OptionInitCostAction401400(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (50 + 65 * Func201(*a) + 15 * Func202(*a)) * Func16(*a, **{
'a': 0.9,
'b': 1 }) * -1))


def OptionInitRewardAction401400(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 1, WEAPON_ACTION_UPGRADEINSCRIPTION, {
        'InscriptionCnt': 0 })


def OptionInitCostAction401401(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (50 + 65 * Func201(*a) + 15 * Func202(*a)) * Func16(*a, **{
'a': 0.9,
'b': 1 }) * -1))


def OptionInitRewardAction401401(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 2, WEAPON_ACTION_UPGRADEINSCRIPTION, {
        'InscriptionCnt': 0 })


def OptionInitCostAction401500(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (50 + 65 * Func201(*a) + 15 * Func202(*a)) * Func16(*a, **{
'a': 0.9,
'b': 1 }) * -1))


def OptionInitRewardAction401500(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 1, WEAPON_ACTION_UPGRADEINSCRIPTION, {
        'InscriptionCnt': 1 })


def OptionInitCostAction401501(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (50 + 65 * Func201(*a) + 15 * Func202(*a)) * Func16(*a, **{
'a': 0.9,
'b': 1 }) * -1))


def OptionInitRewardAction401501(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 2, WEAPON_ACTION_UPGRADEINSCRIPTION, {
        'InscriptionCnt': 1 })


def OptionInitCostAction401502(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (50 + 65 * Func201(*a) + 15 * Func202(*a)) * Func16(*a, **{
'a': 1,
'b': 1.1 }) * -1))


def OptionInitRewardAction401502(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 1, WEAPON_ACTION_RECAST, { })


def OptionInitCostAction401503(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (50 + 65 * Func201(*a) + 15 * Func202(*a)) * Func16(*a, **{
'a': 1,
'b': 1.1 }) * -1))


def OptionInitRewardAction401503(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 2, WEAPON_ACTION_RECAST, { })


def OptionInitCostAction410100(oOption, oHero):
    eventnpcaction.InitHPCost(oOption, oHero, 40, 0)


def OptionInitRewardAction410100(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 1, WEAPON_ACTION_UPGRADE, {
        'WeaponUpgradeLevel': 1 })


def OptionInitCostAction410101(oOption, oHero):
    eventnpcaction.InitHPCost(oOption, oHero, 40, 0)


def OptionInitRewardAction410101(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 1, WEAPON_ACTION_UPGRADEINSCRIPTION, {
        'InscriptionCnt': 1 })


def OptionInitCostAction410102(oOption, oHero):
    eventnpcaction.InitHPCost(oOption, oHero, 35, 0)


def OptionInitRewardAction410102(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 2, WEAPON_ACTION_RECAST, { })


def OptionInitCostAction410200(oOption, oHero):
    eventnpcaction.InitHPCost(oOption, oHero, 50, 0)


def OptionInitRewardAction410200(oOption, oHero):
    eventnpcaction.InitRelicReward(oOption, oHero, 0, { }, 1, {
        1: {
            3001: {
                30012104: 43,
                30012108: 49,
                30012112: 8 },
            3005: {
                30052104: 43,
                30052108: 49,
                30052112: 8 },
            3008: {
                30082104: 43,
                30082108: 49,
                30082112: 8 },
            3007: {
                30072104: 43,
                30072108: 49,
                30072112: 8 },
            3009: {
                30092104: 43,
                30092108: 49,
                30092112: 8 },
            3010: {
                30102104: 43,
                30102108: 49,
                30102112: 8 },
            3012: {
                30122104: 43,
                30122108: 49,
                30122112: 8 } },
        2: {
            3001: {
                30012104: 28,
                30012108: 55,
                30012112: 17 },
            3005: {
                30052104: 28,
                30052108: 55,
                30052112: 17 },
            3008: {
                30082104: 28,
                30082108: 55,
                30082112: 17 },
            3007: {
                30072104: 28,
                30072108: 55,
                30072112: 17 },
            3009: {
                30092104: 28,
                30092108: 55,
                30092112: 17 },
            3012: {
                30122104: 28,
                30122108: 55,
                30122112: 17 } },
        3: {
            3001: {
                30012104: 28,
                30012108: 55,
                30012112: 17 },
            3005: {
                30052104: 28,
                30052108: 55,
                30052112: 17 },
            3008: {
                30082104: 28,
                30082108: 55,
                30082112: 17 },
            3007: {
                30072104: 28,
                30072108: 55,
                30072112: 17 },
            3009: {
                30092104: 28,
                30092108: 55,
                30092112: 17 },
            3012: {
                30122104: 28,
                30122108: 55,
                30122112: 17 } } }, None)


def OptionInitCostAction410201(oOption, oHero):
    eventnpcaction.InitHPCost(oOption, oHero, 35, 0)


def OptionInitRewardAction410201(oOption, oHero):
    eventnpcaction.InitRelicReward(oOption, oHero, 0, { }, 1, {
        1: {
            3001: {
                30012104: 45,
                30012108: 55 },
            3005: {
                30052104: 45,
                30052108: 55 },
            3008: {
                30082104: 45,
                30082108: 55 },
            3007: {
                30072104: 45,
                30072108: 55 },
            3009: {
                30092104: 45,
                30092108: 55 },
            3010: {
                30102104: 45,
                30102108: 55 },
            3012: {
                30122104: 45,
                30122108: 55 } },
        2: {
            3001: {
                30012104: 37,
                30012108: 63 },
            3005: {
                30052104: 37,
                30052108: 63 },
            3008: {
                30082104: 37,
                30082108: 63 },
            3007: {
                30072104: 37,
                30072108: 63 },
            3009: {
                30092104: 37,
                30092108: 63 },
            3012: {
                30122104: 37,
                30122108: 63 } },
        3: {
            3001: {
                30012104: 37,
                30012108: 63 },
            3005: {
                30052104: 37,
                30052108: 63 },
            3008: {
                30082104: 37,
                30082108: 63 },
            3007: {
                30072104: 37,
                30072108: 63 },
            3009: {
                30092104: 37,
                30092108: 63 },
            3012: {
                30122104: 37,
                30122108: 63 } } }, None)


def OptionInitCostAction410202(oOption, oHero):
    eventnpcaction.InitHPCost(oOption, oHero, 45, 0)


def OptionInitRewardAction410202(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 1, WEAPON_ACTION_UPGRADEINSCRIPTION, {
        'UpAllInsToRare': 1 })


def OptionInitCostAction410300(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (50 + 65 * Func201(*a) + 15 * Func202(*a)) * 1.2 * -1))


def OptionInitRewardAction410300(oOption, oHero):
    eventnpcaction.InitRelicReward(oOption, oHero, 0, { }, 1, {
        1: {
            3001: {
                30012104: 43,
                30012108: 49,
                30012112: 8 },
            3005: {
                30052104: 43,
                30052108: 49,
                30052112: 8 },
            3008: {
                30082104: 43,
                30082108: 49,
                30082112: 8 },
            3007: {
                30072104: 43,
                30072108: 49,
                30072112: 8 },
            3009: {
                30092104: 43,
                30092108: 49,
                30092112: 8 },
            3010: {
                30102104: 43,
                30102108: 49,
                30102112: 8 },
            3012: {
                30122104: 43,
                30122108: 49,
                30122112: 8 } },
        2: {
            3001: {
                30012104: 28,
                30012108: 55,
                30012112: 17 },
            3005: {
                30052104: 28,
                30052108: 55,
                30052112: 17 },
            3008: {
                30082104: 28,
                30082108: 55,
                30082112: 17 },
            3007: {
                30072104: 28,
                30072108: 55,
                30072112: 17 },
            3009: {
                30092104: 28,
                30092108: 55,
                30092112: 17 },
            3012: {
                30122104: 28,
                30122108: 55,
                30122112: 17 } },
        3: {
            3001: {
                30012104: 28,
                30012108: 55,
                30012112: 17 },
            3005: {
                30052104: 28,
                30052108: 55,
                30052112: 17 },
            3008: {
                30082104: 28,
                30082108: 55,
                30082112: 17 },
            3007: {
                30072104: 28,
                30072108: 55,
                30072112: 17 },
            3009: {
                30092104: 28,
                30092108: 55,
                30092112: 17 },
            3012: {
                30122104: 28,
                30122108: 55,
                30122112: 17 } } }, None)


def OptionInitCostAction410301(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (50 + 65 * Func201(*a) + 15 * Func202(*a)) * 1.2 * -1))


def OptionInitRewardAction410301(oOption, oHero):
    eventnpcaction.InitRelicReward(oOption, oHero, 0, { }, 1, {
        1: {
            3001: {
                30012108: 47 },
            3005: {
                30052108: 47 },
            3008: {
                30082108: 47 },
            3007: {
                30072108: 47 },
            3009: {
                30092108: 47 },
            3010: {
                30102108: 47 },
            3012: {
                30122108: 47 } },
        2: {
            3001: {
                30012108: 55 },
            3005: {
                30052108: 55 },
            3008: {
                30082108: 55 },
            3007: {
                30072108: 55 },
            3009: {
                30092108: 55 },
            3012: {
                30122108: 55 } },
        3: {
            3001: {
                30012108: 55 },
            3005: {
                30052108: 55 },
            3008: {
                30082108: 55 },
            3007: {
                30072108: 55 },
            3009: {
                30092108: 55 },
            3012: {
                30122108: 55 } } }, None)


def OptionInitCostAction410302(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (50 + 65 * Func201(*a) + 15 * Func202(*a)) * 1 * -1))


def OptionInitRewardAction410302(oOption, oHero):
    eventnpcaction.InitRelicReward(oOption, oHero, 0, { }, 1, {
        1: {
            3001: {
                30012104: 40 },
            3005: {
                30052104: 40 },
            3008: {
                30082104: 40 },
            3007: {
                30072104: 40 },
            3009: {
                30092104: 40 },
            3010: {
                30102104: 40 },
            3012: {
                30122104: 40 } },
        2: {
            3001: {
                30012104: 20 },
            3005: {
                30052104: 20 },
            3008: {
                30082104: 20 },
            3007: {
                30072104: 20 },
            3009: {
                30092104: 20 },
            3012: {
                30122104: 20 } },
        3: {
            3001: {
                30012104: 20 },
            3005: {
                30052104: 20 },
            3008: {
                30082104: 20 },
            3007: {
                30072104: 20 },
            3009: {
                30092104: 20 },
            3012: {
                30122104: 20 } } }, None)


def OptionInitCostAction410400(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (50 + 65 * Func201(*a) + 15 * Func202(*a)) * Func16(*a, **{
'a': 0.9,
'b': 1 }) * -1))


def OptionInitRewardAction410400(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 1, WEAPON_ACTION_UPGRADE, {
        'WeaponUpgradeLevel': 1 })


def OptionInitCostAction410401(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (50 + 65 * Func201(*a) + 15 * Func202(*a)) * Func16(*a, **{
'a': 1.1,
'b': 1.2 }) * -1))


def OptionInitRewardAction410401(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 1, WEAPON_ACTION_UPGRADEINSCRIPTION, {
        'UpAllInsToRare': 1 })


def OptionInitCostAction410402(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (50 + 65 * Func201(*a) + 15 * Func202(*a)) * Func16(*a, **{
'a': 0.9,
'b': 1 }) * -1))


def OptionInitRewardAction410402(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 2, WEAPON_ACTION_RECAST, { })


def OptionInitCostAction410500(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (50 + 65 * Func201(*a) + 15 * Func202(*a)) * Func16(*a, **{
'a': 0.9,
'b': 1 }) * -1))


def OptionInitRewardAction410500(oOption, oHero):
    eventnpcaction.InitWeaponReward(oOption, oHero, 0, {
        3001: 30011001,
        3005: 30051001,
        3008: 30081001,
        3007: 30071001,
        3009: 30091001,
        3010: 30101001,
        3012: 30121001 }, 1, None, { }, None)


def OptionInitCostAction410501(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (50 + 65 * Func201(*a) + 15 * Func202(*a)) * Func16(*a, **{
'a': 0.9,
'b': 1 }) * -1))


def OptionInitRewardAction410501(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 1, WEAPON_ACTION_UPGRADEINSCRIPTION, {
        'InscriptionCnt': 1 })


def OptionInitCostAction410502(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (50 + 65 * Func201(*a) + 15 * Func202(*a)) * Func16(*a, **{
'a': 0.9,
'b': 1 }) * -1))


def OptionInitRewardAction410502(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 2, WEAPON_ACTION_RECAST, { })


def OptionInitCostAction900100(oOption, oHero):
    eventnpcaction.InitHPCost(oOption, oHero, 30, 0)


def OptionInitRewardAction900100(oOption, oHero):
    eventnpcaction.InitWarCashReward(oOption, oHero, (lambda *a: (0.1 + Func201(*a) * 1.5 + Func202(*a) * 0.1) * Func16(*a, **{
'a': 60,
'b': 70 })), 1, None)


def OptionInitCostAction900101(oOption, oHero):
    eventnpcaction.InitHPCost(oOption, oHero, 50, 0)


def OptionInitRewardAction900101(oOption, oHero):
    eventnpcaction.InitWarCashReward(oOption, oHero, (lambda *a: (0.1 + Func201(*a) * 1.5 + Func202(*a) * 0.1) * Func16(*a, **{
'a': 80,
'b': 90 })), 1, None)


def OptionInitCostAction900200(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (0.1 + Func201(*a) * 1.5 + Func202(*a) * 0.3) * Func16(*a, **{
'a': 40,
'b': 50 })))


def OptionInitRewardAction900200(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 1, WEAPON_ACTION_RECAST, { })


def OptionInitCostAction900201(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (0.1 + Func201(*a) * 1.5 + Func202(*a) * 0.3) * Func16(*a, **{
'a': 40,
'b': 50 })))


def OptionInitRewardAction900201(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 2, WEAPON_ACTION_RECAST, { })


def OptionInitCostAction900300(oOption, oHero):
    eventnpcaction.InitAttrCost(oOption, oHero, 'ShieldMax', 0, 20)


def OptionInitRewardAction900300(oOption, oHero):
    eventnpcaction.InitWarCashReward(oOption, oHero, (lambda *a: (0.1 + Func201(*a) * 1.5 + Func202(*a) * 0.1) * Func16(*a, **{
'a': 60,
'b': 70 })), 1, None)


def OptionInitCostAction900301(oOption, oHero):
    eventnpcaction.InitRelicCost(oOption, oHero, 1, None)


def OptionInitRewardAction900301(oOption, oHero):
    eventnpcaction.InitWarCashReward(oOption, oHero, (lambda *a: (0.1 + Func201(*a) * 1.5 + Func202(*a) * 0.1) * Func16(*a, **{
'a': 60,
'b': 70 })), 1, None)


def OptionInitCostAction900302(oOption, oHero):
    eventnpcaction.InitAttrCost(oOption, oHero, 'HPMax', 0, 20)


def OptionInitRewardAction900302(oOption, oHero):
    eventnpcaction.InitWarCashReward(oOption, oHero, (lambda *a: (0.1 + Func201(*a) * 1.5 + Func202(*a) * 0.1) * Func16(*a, **{
'a': 60,
'b': 70 })), 1, None)


def OptionInitCostAction900400(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (0.1 + Func201(*a) * 1.5 + Func202(*a) * 0.3) * Func16(*a, **{
'a': 40,
'b': 50 })))


def OptionInitRewardAction900400(oOption, oHero):
    eventnpcaction.InitRelicReward(oOption, oHero, 0, { }, 1, {
        1: {
            3001: {
                30012104: 50,
                30012108: 35,
                30012117: 15 },
            3008: {
                30082104: 50,
                30082108: 35,
                30082117: 15 },
            3007: {
                30072104: 50,
                30072108: 35,
                30072117: 15 },
            3009: {
                30092104: 50,
                30092108: 35,
                30092117: 15 },
            3012: {
                30122104: 50,
                30122108: 35,
                30122117: 15 } },
        2: {
            3001: {
                30012104: 40,
                30012108: 48,
                30012117: 12 },
            3008: {
                30082104: 40,
                30082108: 48,
                30082117: 12 },
            3007: {
                30072104: 40,
                30072108: 48,
                30072117: 12 },
            3009: {
                30092104: 40,
                30092108: 48,
                30092117: 12 },
            3012: {
                30122104: 40,
                30122108: 48,
                30122117: 12 } },
        3: {
            3001: {
                30012104: 40,
                30012108: 48,
                30012117: 12 },
            3008: {
                30082104: 40,
                30082108: 48,
                30082117: 12 },
            3007: {
                30072104: 40,
                30072108: 48,
                30072117: 12 },
            3009: {
                30092104: 40,
                30092108: 48,
                30092117: 12 },
            3012: {
                30122104: 40,
                30122108: 48,
                30122117: 12 } } }, None)


def OptionInitCostAction900401(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (0.1 + Func201(*a) * 1.5 + Func202(*a) * 0.3) * Func16(*a, **{
'a': 65,
'b': 75 })))


def OptionInitRewardAction900401(oOption, oHero):
    eventnpcaction.InitRelicReward(oOption, oHero, 0, { }, 1, {
        1: {
            3001: {
                30012104: 40,
                30012108: 47,
                30012112: 8 },
            3008: {
                30082104: 40,
                30082108: 47,
                30082112: 8 },
            3007: {
                30072104: 40,
                30072108: 47,
                30072112: 8 },
            3009: {
                30092104: 40,
                30092108: 47,
                30092112: 8 },
            3012: {
                30122104: 40,
                30122108: 47,
                30122112: 8 } },
        2: {
            3001: {
                30012104: 25,
                30012108: 55,
                30012112: 17,
                30012117: 3 },
            3008: {
                30082104: 25,
                30082108: 55,
                30082112: 17,
                30082117: 3 },
            3007: {
                30072104: 25,
                30072108: 55,
                30072112: 17,
                30072117: 3 },
            3009: {
                30092104: 25,
                30092108: 55,
                30092112: 17,
                30092117: 3 },
            3012: {
                30122104: 25,
                30122108: 55,
                30122112: 17,
                30122117: 3 } },
        3: {
            3001: {
                30012104: 25,
                30012108: 55,
                30012112: 17,
                30012117: 3 },
            3008: {
                30082104: 25,
                30082108: 55,
                30082112: 17,
                30082117: 3 },
            3007: {
                30072104: 25,
                30072108: 55,
                30072112: 17,
                30072117: 3 },
            3009: {
                30092104: 25,
                30092108: 55,
                30092112: 17,
                30092117: 3 },
            3012: {
                30122104: 25,
                30122108: 55,
                30122112: 17,
                30122117: 3 } } }, None)


def OptionInitCostAction900402(oOption, oHero):
    eventnpcaction.InitWarCashCost(oOption, oHero, (lambda *a: (0.1 + Func201(*a) * 1.5 + Func202(*a) * 0.3) * Func16(*a, **{
'a': 95,
'b': 110 })))


def OptionInitRewardAction900402(oOption, oHero):
    eventnpcaction.InitRelicReward(oOption, oHero, 0, { }, 1, {
        1: {
            3001: {
                30012104: 40,
                30012108: 48,
                30012112: 12 },
            3008: {
                30082104: 40,
                30082108: 48,
                30082112: 12 },
            3007: {
                30072104: 40,
                30072108: 48,
                30072112: 12 },
            3009: {
                30092104: 40,
                30092108: 48,
                30092112: 12 },
            3012: {
                30122104: 40,
                30122108: 48,
                30122112: 12 } },
        2: {
            3001: {
                30012104: 20,
                30012108: 60,
                30012112: 20 },
            3008: {
                30082104: 20,
                30082108: 60,
                30082112: 20 },
            3007: {
                30072104: 20,
                30072108: 60,
                30072112: 20 },
            3009: {
                30092104: 20,
                30092108: 60,
                30092112: 20 },
            3012: {
                30122104: 20,
                30122108: 60,
                30122112: 20 } },
        3: {
            3001: {
                30012104: 20,
                30012108: 60,
                30012112: 20 },
            3008: {
                30082104: 20,
                30082108: 60,
                30082112: 20 },
            3007: {
                30072104: 20,
                30072108: 60,
                30072112: 20 },
            3009: {
                30092104: 20,
                30092108: 60,
                30092112: 20 },
            3012: {
                30122104: 20,
                30122108: 60,
                30122112: 20 } } }, None)


def OptionInitCostAction900500(oOption, oHero):
    eventnpcaction.InitRelicCost(oOption, oHero, 1, None)


def OptionInitRewardAction900500(oOption, oHero):
    eventnpcaction.InitHPReward(oOption, oHero, 35, 0)


def OptionInitCostAction900501(oOption, oHero):
    eventnpcaction.InitCurseRelicCost(oOption, oHero, 1)


def OptionInitRewardAction900501(oOption, oHero):
    eventnpcaction.InitHPReward(oOption, oHero, 35, 0)


def OptionInitRewardAction900600(oOption, oHero):
    eventnpcaction.InitHPReward(oOption, oHero, 35, 0)


def OptionInitRewardAction900601(oOption, oHero):
    eventnpcaction.InitAttrReward(oOption, oHero, 'HPMax', 0, 25)


def OptionInitRewardAction900602(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 1, WEAPON_ACTION_UPGRADEINSCRIPTION, {
        'InscriptionCnt': 0 })


def OptionInitRewardAction900603(oOption, oHero):
    eventnpcaction.InitWeaponAction(oOption, oHero, 2, WEAPON_ACTION_UPGRADEINSCRIPTION, {
        'InscriptionCnt': 0 })


class CNpcEventData1001(CCustom):
    m_SID = 1001
    m_Titles = {
        1: 3001,
        2: 3002 }
    m_Event = {
        1: {
            0: {
                'Title': 3101,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction100100,
                'RewardTips': 3701,
                'RewardType': NPC_OPTION_REWARD_WARCASH,
                'InitRewardFunc': OptionInitRewardAction100100,
                'GainRewardTips': 3103,
                'RewardDelay': 0 } },
        2: { } }


class CNpcEventData1002(CCustom):
    m_SID = 1002
    m_Titles = {
        1: 3001,
        2: 3002 }
    m_Event = {
        1: {
            0: {
                'Title': 3101,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction100200,
                'RewardTips': 3701,
                'RewardType': NPC_OPTION_REWARD_WARCASH,
                'InitRewardFunc': OptionInitRewardAction100200,
                'GainRewardTips': 3103,
                'RewardDelay': 0 } },
        2: { } }


class CNpcEventData1003(CCustom):
    m_SID = 1003
    m_Titles = {
        1: 3001,
        2: 3002 }
    m_Event = {
        1: {
            0: {
                'Title': 3101,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction100300,
                'RewardTips': 3702,
                'RewardType': NPC_OPTION_REWARD_ATTR,
                'InitRewardFunc': OptionInitRewardAction100300,
                'GainRewardTips': 3103,
                'RewardDelay': 0 } },
        2: { } }


class CNpcEventData1004(CCustom):
    m_SID = 1004
    m_Titles = {
        1: 3001,
        2: 3002 }
    m_Event = {
        1: {
            0: {
                'Title': 3101,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction100400,
                'RewardTips': 3703,
                'RewardType': NPC_OPTION_REWARD_ATTR,
                'InitRewardFunc': OptionInitRewardAction100400,
                'GainRewardTips': 3103,
                'RewardDelay': 0 } },
        2: { } }


class CNpcEventData1005(CCustom):
    m_SID = 1005
    m_Titles = {
        1: 3001,
        2: 3002 }
    m_Event = {
        1: {
            0: {
                'Title': 3101,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction100500,
                'RewardTips': 3704,
                'RewardType': NPC_OPTION_REWARD_RELIC,
                'InitRewardFunc': OptionInitRewardAction100500,
                'GainRewardTips': 3103,
                'RewardDelay': 0 } },
        2: { } }


class CNpcEventData1006(CCustom):
    m_SID = 1006
    m_Titles = {
        1: 3001,
        2: 3002 }
    m_Event = {
        1: {
            0: {
                'Title': 3101,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction100600,
                'RewardTips': 3705,
                'RewardType': NPC_OPTION_REWARD_RELIC,
                'InitRewardFunc': OptionInitRewardAction100600,
                'GainRewardTips': 3103,
                'RewardDelay': 0 } },
        2: { } }


class CNpcEventData1007(CCustom):
    m_SID = 1007
    m_Titles = {
        1: 3001,
        2: 3002 }
    m_Event = {
        1: {
            0: {
                'Title': 3101,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction100700,
                'RewardTips': 3706,
                'RewardType': NPC_OPTION_REWARD_GOLDENCUP,
                'InitRewardFunc': OptionInitRewardAction100700,
                'GainRewardTips': 3107,
                'RewardDelay': 0 } },
        2: { } }


class CNpcEventData1008(CCustom):
    m_SID = 1008
    m_Titles = {
        1: 3001,
        2: 3002 }
    m_Event = {
        1: {
            0: {
                'Title': 3101,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction100800,
                'RewardTips': 3707,
                'RewardType': NPC_OPTION_REWARD_WEAPON,
                'InitRewardFunc': OptionInitRewardAction100800,
                'GainRewardTips': 3103,
                'RewardDelay': 0 } },
        2: { } }


class CNpcEventData1009(CCustom):
    m_SID = 1009
    m_Titles = {
        1: 3001,
        2: 3002 }
    m_Event = {
        1: {
            0: {
                'Title': 3101,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction100900,
                'RewardTips': 3705,
                'RewardType': NPC_OPTION_REWARD_WEAPON,
                'InitRewardFunc': OptionInitRewardAction100900,
                'GainRewardTips': 3103,
                'RewardDelay': 0 } },
        2: { } }


class CNpcEventData1010(CCustom):
    m_SID = 1010
    m_Titles = {
        1: 3001,
        2: 3002 }
    m_Event = {
        1: {
            0: {
                'Title': 3101,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction101000,
                'RewardTips': 3708,
                'RewardType': NPC_OPTION_REWARD_HP,
                'InitRewardFunc': OptionInitRewardAction101000,
                'GainRewardTips': 3117,
                'RewardDelay': 0 } },
        2: { } }


class CNpcEventData1011(CCustom):
    m_SID = 1011
    m_Titles = {
        1: 3001,
        2: 3002 }
    m_Event = {
        1: {
            0: {
                'Title': 3101,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction101100,
                'RewardTips': 3701,
                'RewardType': NPC_OPTION_REWARD_WARCASH,
                'InitRewardFunc': OptionInitRewardAction101100,
                'GainRewardTips': 3116,
                'RewardDelay': 0 } },
        2: { } }


class CNpcEventData1012(CCustom):
    m_SID = 1012
    m_Titles = {
        1: 3001,
        2: 3002 }
    m_Event = {
        1: {
            0: {
                'Title': 3101,
                'CostTips': 3409,
                'CostType': NPC_OPTION_COST_HP,
                'InitCostFunc': OptionInitCostAction101200,
                'RewardTips': 3701,
                'RewardType': NPC_OPTION_REWARD_WARCASH,
                'InitRewardFunc': OptionInitRewardAction101200,
                'GainRewardTips': 3116,
                'RewardDelay': 0 } },
        2: { } }


class CNpcEventData1013(CCustom):
    m_SID = 1013
    m_Titles = {
        1: 3001 }
    m_Event = {
        1: {
            0: {
                'Title': 3101,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction101300,
                'RewardTips': 3701,
                'RewardType': NPC_OPTION_REWARD_WARCASH,
                'InitRewardFunc': OptionInitRewardAction101300,
                'GainRewardTips': 3116,
                'RewardDelay': 12 },
            1: {
                'Title': 3101,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction101301,
                'RewardTips': 3701,
                'RewardType': NPC_OPTION_REWARD_WARCASH,
                'InitRewardFunc': OptionInitRewardAction101301,
                'GainRewardTips': 3116,
                'RewardDelay': 12 },
            2: {
                'Title': 3101,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction101302,
                'RewardTips': 3707,
                'RewardType': NPC_OPTION_REWARD_WEAPON,
                'InitRewardFunc': OptionInitRewardAction101302,
                'GainRewardTips': 3103,
                'RewardDelay': 12 } } }


class CNpcEventData1014(CCustom):
    m_SID = 1014
    m_Titles = {
        1: 3001,
        2: 3002 }
    m_Event = {
        1: {
            0: {
                'Title': 3101,
                'CostTips': 3404,
                'CostType': NPC_OPTION_COST_ATTR,
                'InitCostFunc': OptionInitCostAction101400,
                'RewardTips': 3701,
                'RewardType': NPC_OPTION_REWARD_WARCASH,
                'InitRewardFunc': OptionInitRewardAction101400,
                'GainRewardTips': 3116,
                'RewardDelay': 0 } },
        2: { } }


class CNpcEventData1015(CCustom):
    m_SID = 1015
    m_Titles = {
        1: 3001,
        2: 3002 }
    m_Event = {
        1: {
            0: {
                'Title': 3101,
                'CostTips': 3405,
                'CostType': NPC_OPTION_COST_RELIC,
                'InitCostFunc': OptionInitCostAction101500,
                'RewardTips': 3701,
                'RewardType': NPC_OPTION_REWARD_WARCASH,
                'InitRewardFunc': OptionInitRewardAction101500,
                'GainRewardTips': 3116,
                'RewardDelay': 0 } },
        2: { } }


class CNpcEventData1016(CCustom):
    m_SID = 1016
    m_Titles = {
        1: 3001,
        2: 3002 }
    m_Event = {
        1: {
            0: {
                'Title': 3101,
                'CostTips': 3406,
                'CostType': NPC_OPTION_COST_RELIC,
                'InitCostFunc': OptionInitCostAction101600,
                'RewardTips': 3701,
                'RewardType': NPC_OPTION_REWARD_WARCASH,
                'InitRewardFunc': OptionInitRewardAction101600,
                'GainRewardTips': 3116,
                'RewardDelay': 0 } },
        2: { } }


class CNpcEventData1017(CCustom):
    m_SID = 1017
    m_Titles = {
        1: 3001,
        2: 3002 }
    m_Event = {
        1: {
            0: {
                'Title': 3101,
                'CostTips': 3407,
                'CostType': NPC_OPTION_COST_CURSERELIC,
                'InitCostFunc': OptionInitCostAction101700,
                'RewardTips': 3701,
                'RewardType': NPC_OPTION_REWARD_WARCASH,
                'InitRewardFunc': OptionInitRewardAction101700,
                'GainRewardTips': 3116,
                'RewardDelay': 0 } },
        2: { } }


class CNpcEventData1018(CCustom):
    m_SID = 1018
    m_Titles = {
        1: 3001,
        2: 3002 }
    m_Event = {
        1: {
            0: {
                'Title': 3101,
                'CostTips': 3408,
                'CostType': NPC_OPTION_COST_CURSERELIC,
                'InitCostFunc': OptionInitCostAction101800,
                'RewardTips': 3701,
                'RewardType': NPC_OPTION_REWARD_WARCASH,
                'InitRewardFunc': OptionInitRewardAction101800,
                'GainRewardTips': 3116,
                'RewardDelay': 0 } },
        2: { } }


class CNpcEventData1019(CCustom):
    m_SID = 1019
    m_Titles = {
        1: 3001 }
    m_Event = {
        1: {
            0: {
                'Title': 3101,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction101900,
                'RewardTips': 3701,
                'RewardType': NPC_OPTION_REWARD_WARCASH,
                'InitRewardFunc': OptionInitRewardAction101900,
                'GainRewardTips': 3116,
                'RewardDelay': 12 },
            1: {
                'Title': 3101,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction101901,
                'RewardTips': 3701,
                'RewardType': NPC_OPTION_REWARD_WARCASH,
                'InitRewardFunc': OptionInitRewardAction101901,
                'GainRewardTips': 3116,
                'RewardDelay': 12 },
            2: {
                'Title': 3101,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction101902,
                'RewardTips': 3707,
                'RewardType': NPC_OPTION_REWARD_WEAPON,
                'InitRewardFunc': OptionInitRewardAction101902,
                'GainRewardTips': 3103,
                'RewardDelay': 12 } } }


class CNpcEventData1020(CCustom):
    m_SID = 1020
    m_Titles = {
        1: 3001,
        2: 3002 }
    m_Event = {
        1: {
            0: {
                'Title': 3101,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction102000,
                'RewardTips': 3701,
                'RewardType': NPC_OPTION_REWARD_WARCASH,
                'InitRewardFunc': OptionInitRewardAction102000,
                'GainRewardTips': 3116,
                'RewardDelay': 0 },
            1: {
                'Title': 3101,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction102001,
                'RewardTips': 3701,
                'RewardType': NPC_OPTION_REWARD_WARCASH,
                'InitRewardFunc': OptionInitRewardAction102001,
                'GainRewardTips': 3116,
                'RewardDelay': 0 },
            2: {
                'Title': 3101,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction102002,
                'RewardTips': 3701,
                'RewardType': NPC_OPTION_REWARD_WARCASH,
                'InitRewardFunc': OptionInitRewardAction102002,
                'GainRewardTips': 3116,
                'RewardDelay': 0 } },
        2: { } }


class CNpcEventData1021(CCustom):
    m_SID = 1021
    m_Titles = {
        1: 3001,
        2: 3002 }
    m_Event = {
        1: {
            0: {
                'Title': 3101,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction102100,
                'RewardTips': 3701,
                'RewardType': NPC_OPTION_REWARD_WARCASH,
                'InitRewardFunc': OptionInitRewardAction102100,
                'GainRewardTips': 3116,
                'RewardDelay': 0 },
            1: {
                'Title': 3101,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction102101,
                'RewardTips': 3701,
                'RewardType': NPC_OPTION_REWARD_WARCASH,
                'InitRewardFunc': OptionInitRewardAction102101,
                'GainRewardTips': 3116,
                'RewardDelay': 0 },
            2: {
                'Title': 3101,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction102102,
                'RewardTips': 3701,
                'RewardType': NPC_OPTION_REWARD_WARCASH,
                'InitRewardFunc': OptionInitRewardAction102102,
                'GainRewardTips': 3116,
                'RewardDelay': 0 },
            3: {
                'Title': 3101,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction102103,
                'RewardTips': 3701,
                'RewardType': NPC_OPTION_REWARD_WARCASH,
                'InitRewardFunc': OptionInitRewardAction102103,
                'GainRewardTips': 3116,
                'RewardDelay': 0 } },
        2: { } }


class CNpcEventData1022(CCustom):
    m_SID = 1022
    m_Titles = {
        1: 3001,
        2: 3002 }
    m_Event = {
        1: {
            0: {
                'Title': 3101,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_SELECTRELIC,
                'InitCostFunc': OptionInitCostAction102200,
                'RewardTips': 3701,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction102200,
                'GainRewardTips': 3116,
                'RewardDelay': 0 },
            1: {
                'Title': 3101,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction102201,
                'RewardTips': 3701,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction102201,
                'GainRewardTips': 3116,
                'RewardDelay': 0 },
            2: {
                'Title': 3101,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction102202,
                'RewardTips': 3701,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction102202,
                'GainRewardTips': 3116,
                'RewardDelay': 0 },
            3: {
                'Title': 3101,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_SELECTRELIC,
                'InitCostFunc': OptionInitCostAction102203,
                'RewardTips': 3701,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction102203,
                'GainRewardTips': 3116,
                'RewardDelay': 0 } },
        2: { } }


class CNpcEventData1023(CCustom):
    m_SID = 1023
    m_Titles = {
        1: 7228 }
    m_Event = {
        1: {
            0: {
                'Title': 7229,
                'CostTips': 0,
                'CostType': NPC_OPTION_COST_NONE,
                'InitCostFunc': None,
                'RewardTips': 0,
                'RewardType': NPC_OPTION_REWARD_WEAPON,
                'InitRewardFunc': OptionInitRewardAction102300,
                'GainRewardTips': 0,
                'RewardDelay': 0 } } }


class CNpcEventData1024(CCustom):
    m_SID = 1024
    m_Titles = {
        1: 7228 }
    m_Event = {
        1: {
            0: {
                'Title': 7229,
                'CostTips': 0,
                'CostType': NPC_OPTION_COST_NONE,
                'InitCostFunc': None,
                'RewardTips': 0,
                'RewardType': NPC_OPTION_REWARD_WEAPON,
                'InitRewardFunc': OptionInitRewardAction102400,
                'GainRewardTips': 0,
                'RewardDelay': 0 } } }


class CNpcEventData1101(CCustom):
    m_SID = 1101
    m_Titles = {
        1: 3004 }
    m_Event = {
        1: {
            0: {
                'Title': 3101,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction110100,
                'RewardTips': 3704,
                'RewardType': NPC_OPTION_REWARD_RELIC,
                'InitRewardFunc': OptionInitRewardAction110100,
                'GainRewardTips': 3103,
                'RewardDelay': 32 },
            1: {
                'Title': 3101,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction110101,
                'RewardTips': 3705,
                'RewardType': NPC_OPTION_REWARD_RELIC,
                'InitRewardFunc': OptionInitRewardAction110101,
                'GainRewardTips': 3103,
                'RewardDelay': 32 },
            2: {
                'Title': 3101,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction110102,
                'RewardTips': 3705,
                'RewardType': NPC_OPTION_REWARD_WEAPON,
                'InitRewardFunc': OptionInitRewardAction110102,
                'GainRewardTips': 3103,
                'RewardDelay': 32 } } }


class CNpcEventData1102(CCustom):
    m_SID = 1102
    m_Titles = {
        1: 3003 }
    m_Event = {
        1: {
            0: {
                'Title': 3105,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction110200,
                'RewardTips': 3702,
                'RewardType': NPC_OPTION_REWARD_ATTR,
                'InitRewardFunc': OptionInitRewardAction110200,
                'GainRewardTips': 3104,
                'RewardDelay': 37 },
            1: {
                'Title': 3106,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction110201,
                'RewardTips': 3703,
                'RewardType': NPC_OPTION_REWARD_ATTR,
                'InitRewardFunc': OptionInitRewardAction110201,
                'GainRewardTips': 3104,
                'RewardDelay': 37 } } }


class CNpcEventData1103(CCustom):
    m_SID = 1103
    m_Titles = {
        1: 3005 }
    m_Event = {
        1: {
            0: {
                'Title': 3101,
                'CostTips': 3408,
                'CostType': NPC_OPTION_COST_CURSERELIC,
                'InitCostFunc': OptionInitCostAction110300,
                'RewardTips': 3705,
                'RewardType': NPC_OPTION_REWARD_RELIC,
                'InitRewardFunc': OptionInitRewardAction110300,
                'GainRewardTips': 3108,
                'RewardDelay': 37 },
            1: {
                'Title': 3101,
                'CostTips': 3408,
                'CostType': NPC_OPTION_COST_CURSERELIC,
                'InitCostFunc': OptionInitCostAction110301,
                'RewardTips': 3705,
                'RewardType': NPC_OPTION_REWARD_WEAPON,
                'InitRewardFunc': OptionInitRewardAction110301,
                'GainRewardTips': 3108,
                'RewardDelay': 37 },
            2: {
                'Title': 3101,
                'CostTips': 3408,
                'CostType': NPC_OPTION_COST_CURSERELIC,
                'InitCostFunc': OptionInitCostAction110302,
                'RewardTips': 3701,
                'RewardType': NPC_OPTION_REWARD_WARCASH,
                'InitRewardFunc': OptionInitRewardAction110302,
                'GainRewardTips': 3109,
                'RewardDelay': 37 } } }


class CNpcEventData1104(CCustom):
    m_SID = 1104
    m_Titles = {
        1: 3001 }
    m_Event = {
        1: {
            0: {
                'Title': 3101,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction110400,
                'RewardTips': 3706,
                'RewardType': NPC_OPTION_REWARD_GOLDENCUP,
                'InitRewardFunc': OptionInitRewardAction110400,
                'GainRewardTips': 3107,
                'RewardDelay': 32 },
            1: {
                'Title': 3101,
                'CostTips': 3408,
                'CostType': NPC_OPTION_COST_CURSERELIC,
                'InitCostFunc': OptionInitCostAction110401,
                'RewardTips': 3706,
                'RewardType': NPC_OPTION_REWARD_GOLDENCUP,
                'InitRewardFunc': OptionInitRewardAction110401,
                'GainRewardTips': 3115,
                'RewardDelay': 32 },
            2: {
                'Title': 3101,
                'CostTips': 3406,
                'CostType': NPC_OPTION_COST_RELIC,
                'InitCostFunc': OptionInitCostAction110402,
                'RewardTips': 3706,
                'RewardType': NPC_OPTION_REWARD_GOLDENCUP,
                'InitRewardFunc': OptionInitRewardAction110402,
                'GainRewardTips': 3114,
                'RewardDelay': 32 } } }


class CNpcEventData1105(CCustom):
    m_SID = 1105
    m_Titles = {
        1: 3006 }
    m_Event = {
        1: {
            0: {
                'Title': 3113,
                'CostTips': 3409,
                'CostType': NPC_OPTION_COST_HP,
                'InitCostFunc': OptionInitCostAction110500,
                'RewardTips': 3701,
                'RewardType': NPC_OPTION_REWARD_WARCASH,
                'InitRewardFunc': OptionInitRewardAction110500,
                'GainRewardTips': 3110,
                'RewardDelay': 37 },
            1: {
                'Title': 3113,
                'CostTips': 3409,
                'CostType': NPC_OPTION_COST_HP,
                'InitCostFunc': OptionInitCostAction110501,
                'RewardTips': 3701,
                'RewardType': NPC_OPTION_REWARD_WARCASH,
                'InitRewardFunc': OptionInitRewardAction110501,
                'GainRewardTips': 3111,
                'RewardDelay': 37 },
            2: {
                'Title': 3113,
                'CostTips': 3409,
                'CostType': NPC_OPTION_COST_HP,
                'InitCostFunc': OptionInitCostAction110502,
                'RewardTips': 3701,
                'RewardType': NPC_OPTION_REWARD_WARCASH,
                'InitRewardFunc': OptionInitRewardAction110502,
                'GainRewardTips': 3112,
                'RewardDelay': 37 } } }


class CNpcEventData1106(CCustom):
    m_SID = 1106
    m_Titles = {
        1: 3007,
        2: 7181 }
    m_Event = {
        1: {
            0: {
                'Title': 3101,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction110600,
                'RewardTips': 3704,
                'RewardType': NPC_OPTION_REWARD_RELIC,
                'InitRewardFunc': OptionInitRewardAction110600,
                'GainRewardTips': 3131,
                'RewardDelay': 37 },
            1: {
                'Title': 3101,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction110601,
                'RewardTips': 3707,
                'RewardType': NPC_OPTION_REWARD_WEAPON,
                'InitRewardFunc': OptionInitRewardAction110601,
                'GainRewardTips': 3131,
                'RewardDelay': 37 } },
        2: { } }


class CNpcEventData1107(CCustom):
    m_SID = 1107
    m_Titles = {
        1: 3008,
        2: 7182 }
    m_Event = {
        1: {
            0: {
                'Title': 3113,
                'CostTips': 3409,
                'CostType': NPC_OPTION_COST_HP,
                'InitCostFunc': OptionInitCostAction110700,
                'RewardTips': 3701,
                'RewardType': NPC_OPTION_REWARD_WARCASH,
                'InitRewardFunc': OptionInitRewardAction110700,
                'GainRewardTips': 3134,
                'RewardDelay': 37 },
            1: {
                'Title': 3113,
                'CostTips': 3409,
                'CostType': NPC_OPTION_COST_HP,
                'InitCostFunc': OptionInitCostAction110701,
                'RewardTips': 3704,
                'RewardType': NPC_OPTION_REWARD_RELIC,
                'InitRewardFunc': OptionInitRewardAction110701,
                'GainRewardTips': 3129,
                'RewardDelay': 37 },
            2: {
                'Title': 3113,
                'CostTips': 3409,
                'CostType': NPC_OPTION_COST_HP,
                'InitCostFunc': OptionInitCostAction110702,
                'RewardTips': 3707,
                'RewardType': NPC_OPTION_REWARD_WEAPON,
                'InitRewardFunc': OptionInitRewardAction110702,
                'GainRewardTips': 3129,
                'RewardDelay': 37 } },
        2: { } }


class CNpcEventData1108(CCustom):
    m_SID = 1108
    m_Titles = {
        1: 3011 }
    m_Event = {
        1: {
            0: {
                'Title': 3119,
                'CostTips': 3409,
                'CostType': NPC_OPTION_COST_HP,
                'InitCostFunc': OptionInitCostAction110800,
                'RewardTips': 3701,
                'RewardType': NPC_OPTION_REWARD_WARCASH,
                'InitRewardFunc': OptionInitRewardAction110800,
                'GainRewardTips': 3132,
                'RewardDelay': 32 },
            1: {
                'Title': 3120,
                'CostTips': 3408,
                'CostType': NPC_OPTION_COST_CURSERELIC,
                'InitCostFunc': OptionInitCostAction110801,
                'RewardTips': 3704,
                'RewardType': NPC_OPTION_REWARD_RELIC,
                'InitRewardFunc': OptionInitRewardAction110801,
                'GainRewardTips': 3133,
                'RewardDelay': 32 },
            2: {
                'Title': 3121,
                'CostTips': 3408,
                'CostType': NPC_OPTION_COST_CURSERELIC,
                'InitCostFunc': OptionInitCostAction110802,
                'RewardTips': 3707,
                'RewardType': NPC_OPTION_REWARD_WEAPON,
                'InitRewardFunc': OptionInitRewardAction110802,
                'GainRewardTips': 3133,
                'RewardDelay': 32 } } }


class CNpcEventData1109(CCustom):
    m_SID = 1109
    m_Titles = {
        1: 3008,
        2: 7182 }
    m_Event = {
        1: {
            0: {
                'Title': 3113,
                'CostTips': 3409,
                'CostType': NPC_OPTION_COST_HP,
                'InitCostFunc': OptionInitCostAction110900,
                'RewardTips': 3702,
                'RewardType': NPC_OPTION_REWARD_ATTR,
                'InitRewardFunc': OptionInitRewardAction110900,
                'GainRewardTips': 3130,
                'RewardDelay': 37 },
            1: {
                'Title': 3113,
                'CostTips': 3409,
                'CostType': NPC_OPTION_COST_HP,
                'InitCostFunc': OptionInitCostAction110901,
                'RewardTips': 3703,
                'RewardType': NPC_OPTION_REWARD_ATTR,
                'InitRewardFunc': OptionInitRewardAction110901,
                'GainRewardTips': 3130,
                'RewardDelay': 37 } },
        2: { } }


class CNpcEventData1110(CCustom):
    m_SID = 1110
    m_Titles = {
        1: 3012 }
    m_Event = {
        1: {
            0: {
                'Title': 3123,
                'CostTips': 3405,
                'CostType': NPC_OPTION_COST_RELIC,
                'InitCostFunc': OptionInitCostAction111000,
                'RewardTips': 3705,
                'RewardType': NPC_OPTION_REWARD_WEAPON,
                'InitRewardFunc': OptionInitRewardAction111000,
                'GainRewardTips': 3103,
                'RewardDelay': 32 },
            1: {
                'Title': 3123,
                'CostTips': 3408,
                'CostType': NPC_OPTION_COST_CURSERELIC,
                'InitCostFunc': OptionInitCostAction111001,
                'RewardTips': 3705,
                'RewardType': NPC_OPTION_REWARD_WEAPON,
                'InitRewardFunc': OptionInitRewardAction111001,
                'GainRewardTips': 3103,
                'RewardDelay': 32 },
            2: {
                'Title': 3123,
                'CostTips': 3409,
                'CostType': NPC_OPTION_COST_HP,
                'InitCostFunc': OptionInitCostAction111002,
                'RewardTips': 3705,
                'RewardType': NPC_OPTION_REWARD_WEAPON,
                'InitRewardFunc': OptionInitRewardAction111002,
                'GainRewardTips': 3103,
                'RewardDelay': 32 } } }


class CNpcEventData1111(CCustom):
    m_SID = 1111
    m_Titles = {
        1: 3009 }
    m_Event = {
        1: {
            0: {
                'Title': 3127,
                'CostTips': 3405,
                'CostType': NPC_OPTION_COST_RELIC,
                'InitCostFunc': OptionInitCostAction111100,
                'RewardTips': 3706,
                'RewardType': NPC_OPTION_REWARD_GOLDENCUP,
                'InitRewardFunc': OptionInitRewardAction111100,
                'GainRewardTips': 3107,
                'RewardDelay': 32 },
            1: {
                'Title': 3128,
                'CostTips': 3408,
                'CostType': NPC_OPTION_COST_CURSERELIC,
                'InitCostFunc': OptionInitCostAction111101,
                'RewardTips': 3706,
                'RewardType': NPC_OPTION_REWARD_GOLDENCUP,
                'InitRewardFunc': OptionInitRewardAction111101,
                'GainRewardTips': 3107,
                'RewardDelay': 32 },
            2: {
                'Title': 3119,
                'CostTips': 3409,
                'CostType': NPC_OPTION_COST_HP,
                'InitCostFunc': OptionInitCostAction111102,
                'RewardTips': 3706,
                'RewardType': NPC_OPTION_REWARD_GOLDENCUP,
                'InitRewardFunc': OptionInitRewardAction111102,
                'GainRewardTips': 3107,
                'RewardDelay': 32 } } }


class CNpcEventData1112(CCustom):
    m_SID = 1112
    m_Titles = {
        1: 3010 }
    m_Event = {
        1: {
            0: {
                'Title': 3120,
                'CostTips': 3408,
                'CostType': NPC_OPTION_COST_CURSERELIC,
                'InitCostFunc': OptionInitCostAction111200,
                'RewardTips': 3705,
                'RewardType': NPC_OPTION_REWARD_RELIC,
                'InitRewardFunc': OptionInitRewardAction111200,
                'GainRewardTips': 3103,
                'RewardDelay': 32 },
            1: {
                'Title': 3118,
                'CostTips': 3405,
                'CostType': NPC_OPTION_COST_RELIC,
                'InitCostFunc': OptionInitCostAction111201,
                'RewardTips': 3705,
                'RewardType': NPC_OPTION_REWARD_RELIC,
                'InitRewardFunc': OptionInitRewardAction111201,
                'GainRewardTips': 3103,
                'RewardDelay': 32 },
            2: {
                'Title': 3113,
                'CostTips': 3409,
                'CostType': NPC_OPTION_COST_HP,
                'InitCostFunc': OptionInitCostAction111202,
                'RewardTips': 3705,
                'RewardType': NPC_OPTION_REWARD_RELIC,
                'InitRewardFunc': OptionInitRewardAction111202,
                'GainRewardTips': 3103,
                'RewardDelay': 32 } } }


class CNpcEventData1113(CCustom):
    m_SID = 1113
    m_Titles = {
        1: 3010 }
    m_Event = {
        1: {
            0: {
                'Title': 3119,
                'CostTips': 3409,
                'CostType': NPC_OPTION_COST_HP,
                'InitCostFunc': OptionInitCostAction111300,
                'RewardTips': 3704,
                'RewardType': NPC_OPTION_REWARD_RELIC,
                'InitRewardFunc': OptionInitRewardAction111300,
                'GainRewardTips': 3103,
                'RewardDelay': 37 },
            1: {
                'Title': 3125,
                'CostTips': 3405,
                'CostType': NPC_OPTION_COST_RELIC,
                'InitCostFunc': OptionInitCostAction111301,
                'RewardTips': 3704,
                'RewardType': NPC_OPTION_REWARD_RELIC,
                'InitRewardFunc': OptionInitRewardAction111301,
                'GainRewardTips': 3103,
                'RewardDelay': 37 },
            2: {
                'Title': 3122,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction111302,
                'RewardTips': 3704,
                'RewardType': NPC_OPTION_REWARD_RELIC,
                'InitRewardFunc': OptionInitRewardAction111302,
                'GainRewardTips': 3103,
                'RewardDelay': 37 } } }


class CNpcEventData2001(CCustom):
    m_SID = 2001
    m_Titles = {
        1: 7127,
        2: 7153 }
    m_Event = {
        1: {
            0: {
                'Title': 7140,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction200100,
                'RewardTips': 7161,
                'RewardType': NPC_OPTION_REWARD_RELIC,
                'InitRewardFunc': OptionInitRewardAction200100,
                'GainRewardTips': 3103,
                'RewardDelay': 37 },
            1: {
                'Title': 7141,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction200101,
                'RewardTips': 7162,
                'RewardType': NPC_OPTION_REWARD_RELIC,
                'InitRewardFunc': OptionInitRewardAction200101,
                'GainRewardTips': 3103,
                'RewardDelay': 37 },
            2: {
                'Title': 7142,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction200102,
                'RewardTips': 7163,
                'RewardType': NPC_OPTION_REWARD_RELIC,
                'InitRewardFunc': OptionInitRewardAction200102,
                'GainRewardTips': 3103,
                'RewardDelay': 37 } },
        2: { } }


class CNpcEventData2002(CCustom):
    m_SID = 2002
    m_Titles = {
        1: 7128,
        2: 7154 }
    m_Event = {
        1: {
            0: {
                'Title': 7144,
                'CostTips': 3409,
                'CostType': NPC_OPTION_COST_HP,
                'InitCostFunc': OptionInitCostAction200200,
                'RewardTips': 7158,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction200200,
                'GainRewardTips': 7180,
                'RewardDelay': 37 },
            1: {
                'Title': 7144,
                'CostTips': 3409,
                'CostType': NPC_OPTION_COST_HP,
                'InitCostFunc': OptionInitCostAction200201,
                'RewardTips': 7158,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction200201,
                'GainRewardTips': 7180,
                'RewardDelay': 37 },
            2: {
                'Title': 7133,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction200202,
                'RewardTips': 7150,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction200202,
                'GainRewardTips': 7175,
                'RewardDelay': 37 },
            3: {
                'Title': 7133,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction200203,
                'RewardTips': 7150,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction200203,
                'GainRewardTips': 7175,
                'RewardDelay': 37 } },
        2: { } }


class CNpcEventData2003(CCustom):
    m_SID = 2003
    m_Titles = {
        1: 7128,
        2: 7154 }
    m_Event = {
        1: {
            0: {
                'Title': 7143,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction200300,
                'RewardTips': 7167,
                'RewardType': NPC_OPTION_REWARD_HP,
                'InitRewardFunc': OptionInitRewardAction200300,
                'GainRewardTips': 7178,
                'RewardDelay': 37 },
            1: {
                'Title': 7164,
                'CostTips': 3409,
                'CostType': NPC_OPTION_COST_HP,
                'InitCostFunc': OptionInitCostAction200301,
                'RewardTips': 3701,
                'RewardType': NPC_OPTION_REWARD_WARCASH,
                'InitRewardFunc': OptionInitRewardAction200301,
                'GainRewardTips': 7177,
                'RewardDelay': 37 },
            2: {
                'Title': 7133,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction200302,
                'RewardTips': 7150,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction200302,
                'GainRewardTips': 7175,
                'RewardDelay': 37 },
            3: {
                'Title': 7133,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction200303,
                'RewardTips': 7150,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction200303,
                'GainRewardTips': 7175,
                'RewardDelay': 37 } },
        2: { } }


class CNpcEventData2004(CCustom):
    m_SID = 2004
    m_Titles = {
        1: 7128,
        2: 7154 }
    m_Event = {
        1: {
            0: {
                'Title': 7145,
                'CostTips': 7147,
                'CostType': NPC_OPTION_COST_SELECTRELIC,
                'InitCostFunc': OptionInitCostAction200400,
                'RewardTips': 7165,
                'RewardType': NPC_OPTION_REWARD_RELIC,
                'InitRewardFunc': OptionInitRewardAction200400,
                'GainRewardTips': 3103,
                'RewardDelay': 37 },
            1: {
                'Title': 7144,
                'CostTips': 3409,
                'CostType': NPC_OPTION_COST_HP,
                'InitCostFunc': OptionInitCostAction200401,
                'RewardTips': 7158,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction200401,
                'GainRewardTips': 7180,
                'RewardDelay': 37 },
            2: {
                'Title': 7144,
                'CostTips': 3409,
                'CostType': NPC_OPTION_COST_HP,
                'InitCostFunc': OptionInitCostAction200402,
                'RewardTips': 7158,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction200402,
                'GainRewardTips': 7180,
                'RewardDelay': 37 } },
        2: { } }


class CNpcEventData2005(CCustom):
    m_SID = 2005
    m_Titles = {
        1: 7129,
        2: 7155 }
    m_Event = {
        1: {
            0: {
                'Title': 7132,
                'CostTips': 3408,
                'CostType': NPC_OPTION_COST_CURSERELIC,
                'InitCostFunc': OptionInitCostAction200500,
                'RewardTips': 7159,
                'RewardType': NPC_OPTION_REWARD_RELIC,
                'InitRewardFunc': OptionInitRewardAction200500,
                'GainRewardTips': 7202,
                'RewardDelay': 37 },
            1: {
                'Title': 7145,
                'CostTips': 7147,
                'CostType': NPC_OPTION_COST_SELECTRELIC,
                'InitCostFunc': OptionInitCostAction200501,
                'RewardTips': 7165,
                'RewardType': NPC_OPTION_REWARD_RELIC,
                'InitRewardFunc': OptionInitRewardAction200501,
                'GainRewardTips': 3103,
                'RewardDelay': 37 } },
        2: { } }


class CNpcEventData2006(CCustom):
    m_SID = 2006
    m_Titles = {
        1: 7129,
        2: 7155 }
    m_Event = {
        1: {
            0: {
                'Title': 7132,
                'CostTips': 7147,
                'CostType': NPC_OPTION_COST_SELECTRELIC,
                'InitCostFunc': OptionInitCostAction200600,
                'RewardTips': 7165,
                'RewardType': NPC_OPTION_REWARD_RELIC,
                'InitRewardFunc': OptionInitRewardAction200600,
                'GainRewardTips': 3103,
                'RewardDelay': 37 },
            1: {
                'Title': 7168,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction200601,
                'RewardTips': 7162,
                'RewardType': NPC_OPTION_REWARD_RELIC,
                'InitRewardFunc': OptionInitRewardAction200601,
                'GainRewardTips': 3103,
                'RewardDelay': 37 },
            2: {
                'Title': 7169,
                'CostTips': 7179,
                'CostType': NPC_OPTION_COST_NONE,
                'InitCostFunc': None,
                'RewardTips': 7160,
                'RewardType': NPC_OPTION_REWARD_RELIC,
                'InitRewardFunc': OptionInitRewardAction200602,
                'GainRewardTips': 3103,
                'RewardDelay': 37 } },
        2: { } }


class CNpcEventData2007(CCustom):
    m_SID = 2007
    m_Titles = {
        1: 7131,
        2: 7156 }
    m_Event = {
        1: {
            0: {
                'Title': 7168,
                'CostTips': 7147,
                'CostType': NPC_OPTION_COST_SELECTRELIC,
                'InitCostFunc': OptionInitCostAction200700,
                'RewardTips': 3701,
                'RewardType': NPC_OPTION_REWARD_WARCASH,
                'InitRewardFunc': OptionInitRewardAction200700,
                'GainRewardTips': 7177,
                'RewardDelay': 37 } },
        2: { } }


class CNpcEventData2008(CCustom):
    m_SID = 2008
    m_Titles = {
        1: 7126,
        2: 7152 }
    m_Event = {
        1: {
            0: {
                'Title': 7138,
                'CostTips': 3408,
                'CostType': NPC_OPTION_COST_CURSERELIC,
                'InitCostFunc': OptionInitCostAction200800,
                'RewardTips': 7159,
                'RewardType': NPC_OPTION_REWARD_RELIC,
                'InitRewardFunc': OptionInitRewardAction200800,
                'GainRewardTips': 7202,
                'RewardDelay': 37 },
            1: {
                'Title': 7136,
                'CostTips': 3409,
                'CostType': NPC_OPTION_COST_HP,
                'InitCostFunc': OptionInitCostAction200801,
                'RewardTips': 3704,
                'RewardType': NPC_OPTION_REWARD_RELIC,
                'InitRewardFunc': OptionInitRewardAction200801,
                'GainRewardTips': 3103,
                'RewardDelay': 37 },
            2: {
                'Title': 7139,
                'CostTips': 7179,
                'CostType': NPC_OPTION_COST_NONE,
                'InitCostFunc': None,
                'RewardTips': 7158,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction200802,
                'GainRewardTips': 7180,
                'RewardDelay': 37 },
            3: {
                'Title': 7139,
                'CostTips': 7179,
                'CostType': NPC_OPTION_COST_NONE,
                'InitCostFunc': None,
                'RewardTips': 7158,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction200803,
                'GainRewardTips': 7180,
                'RewardDelay': 37 } },
        2: { } }


class CNpcEventData2009(CCustom):
    m_SID = 2009
    m_Titles = {
        1: 7126,
        2: 7152 }
    m_Event = {
        1: {
            0: {
                'Title': 7138,
                'CostTips': 3408,
                'CostType': NPC_OPTION_COST_CURSERELIC,
                'InitCostFunc': OptionInitCostAction200900,
                'RewardTips': 7159,
                'RewardType': NPC_OPTION_REWARD_RELIC,
                'InitRewardFunc': OptionInitRewardAction200900,
                'GainRewardTips': 7202,
                'RewardDelay': 37 },
            1: {
                'Title': 7136,
                'CostTips': 3409,
                'CostType': NPC_OPTION_COST_HP,
                'InitCostFunc': OptionInitCostAction200901,
                'RewardTips': 3704,
                'RewardType': NPC_OPTION_REWARD_RELIC,
                'InitRewardFunc': OptionInitRewardAction200901,
                'GainRewardTips': 3103,
                'RewardDelay': 37 },
            2: {
                'Title': 7139,
                'CostTips': 7179,
                'CostType': NPC_OPTION_COST_NONE,
                'InitCostFunc': None,
                'RewardTips': 7166,
                'RewardType': NPC_OPTION_REWARD_RELIC,
                'InitRewardFunc': OptionInitRewardAction200902,
                'GainRewardTips': 3103,
                'RewardDelay': 37 } },
        2: { } }


class CNpcEventData2010(CCustom):
    m_SID = 2010
    m_Titles = {
        1: 7126,
        2: 7152 }
    m_Event = {
        1: {
            0: {
                'Title': 7138,
                'CostTips': 3408,
                'CostType': NPC_OPTION_COST_CURSERELIC,
                'InitCostFunc': OptionInitCostAction201000,
                'RewardTips': 7148,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction201000,
                'GainRewardTips': 7201,
                'RewardDelay': 37 },
            1: {
                'Title': 7138,
                'CostTips': 3408,
                'CostType': NPC_OPTION_COST_CURSERELIC,
                'InitCostFunc': OptionInitCostAction201001,
                'RewardTips': 7148,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction201001,
                'GainRewardTips': 7201,
                'RewardDelay': 37 },
            2: {
                'Title': 7136,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction201002,
                'RewardTips': 7167,
                'RewardType': NPC_OPTION_REWARD_HP,
                'InitRewardFunc': OptionInitRewardAction201002,
                'GainRewardTips': 7178,
                'RewardDelay': 37 },
            3: {
                'Title': 7139,
                'CostTips': 7179,
                'CostType': NPC_OPTION_COST_NONE,
                'InitCostFunc': None,
                'RewardTips': 7166,
                'RewardType': NPC_OPTION_REWARD_RELIC,
                'InitRewardFunc': OptionInitRewardAction201003,
                'GainRewardTips': 3103,
                'RewardDelay': 37 } },
        2: { } }


class CNpcEventData2011(CCustom):
    m_SID = 2011
    m_Titles = {
        1: 7125,
        2: 7151 }
    m_Event = {
        1: {
            0: {
                'Title': 7132,
                'CostTips': 3408,
                'CostType': NPC_OPTION_COST_CURSERELIC,
                'InitCostFunc': OptionInitCostAction201100,
                'RewardTips': 7159,
                'RewardType': NPC_OPTION_REWARD_RELIC,
                'InitRewardFunc': OptionInitRewardAction201100,
                'GainRewardTips': 7202,
                'RewardDelay': 37 },
            1: {
                'Title': 7133,
                'CostTips': 3408,
                'CostType': NPC_OPTION_COST_CURSERELIC,
                'InitCostFunc': OptionInitCostAction201101,
                'RewardTips': 7148,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction201101,
                'GainRewardTips': 7201,
                'RewardDelay': 37 },
            2: {
                'Title': 7133,
                'CostTips': 3408,
                'CostType': NPC_OPTION_COST_CURSERELIC,
                'InitCostFunc': OptionInitCostAction201102,
                'RewardTips': 7148,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction201102,
                'GainRewardTips': 7201,
                'RewardDelay': 37 } },
        2: { } }


class CNpcEventData2012(CCustom):
    m_SID = 2012
    m_Titles = {
        1: 3007,
        2: 7181 }
    m_Event = {
        1: {
            0: {
                'Title': 3101,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction201200,
                'RewardTips': 3707,
                'RewardType': NPC_OPTION_REWARD_WEAPON,
                'InitRewardFunc': OptionInitRewardAction201200,
                'GainRewardTips': 3131,
                'RewardDelay': 37 },
            1: {
                'Title': 3101,
                'CostTips': 3409,
                'CostType': NPC_OPTION_COST_HP,
                'InitCostFunc': OptionInitCostAction201201,
                'RewardTips': 7158,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction201201,
                'GainRewardTips': 7180,
                'RewardDelay': 37 },
            2: {
                'Title': 3101,
                'CostTips': 3409,
                'CostType': NPC_OPTION_COST_HP,
                'InitCostFunc': OptionInitCostAction201202,
                'RewardTips': 7158,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction201202,
                'GainRewardTips': 7180,
                'RewardDelay': 37 } },
        2: { } }


class CNpcEventData2013(CCustom):
    m_SID = 2013
    m_Titles = {
        1: 3007,
        2: 7181 }
    m_Event = {
        1: {
            0: {
                'Title': 3101,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction201300,
                'RewardTips': 3707,
                'RewardType': NPC_OPTION_REWARD_WEAPON,
                'InitRewardFunc': OptionInitRewardAction201300,
                'GainRewardTips': 3131,
                'RewardDelay': 37 },
            1: {
                'Title': 7133,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction201301,
                'RewardTips': 7150,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction201301,
                'GainRewardTips': 7175,
                'RewardDelay': 37 },
            2: {
                'Title': 7133,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction201302,
                'RewardTips': 7150,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction201302,
                'GainRewardTips': 7175,
                'RewardDelay': 37 } },
        2: { } }


class CNpcEventData2014(CCustom):
    m_SID = 2014
    m_Titles = {
        1: 7128,
        2: 7154 }
    m_Event = {
        1: {
            0: {
                'Title': 7133,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction201400,
                'RewardTips': 7150,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction201400,
                'GainRewardTips': 7175,
                'RewardDelay': 37 },
            1: {
                'Title': 7133,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction201401,
                'RewardTips': 7150,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction201401,
                'GainRewardTips': 7175,
                'RewardDelay': 37 },
            2: {
                'Title': 7134,
                'CostTips': 3408,
                'CostType': NPC_OPTION_COST_CURSERELIC,
                'InitCostFunc': OptionInitCostAction201402,
                'RewardTips': 7149,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction201402,
                'GainRewardTips': 7203,
                'RewardDelay': 37 },
            3: {
                'Title': 7134,
                'CostTips': 3408,
                'CostType': NPC_OPTION_COST_CURSERELIC,
                'InitCostFunc': OptionInitCostAction201403,
                'RewardTips': 7149,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction201403,
                'GainRewardTips': 7203,
                'RewardDelay': 37 } },
        2: { } }


class CNpcEventData2015(CCustom):
    m_SID = 2015
    m_Titles = {
        1: 7126,
        2: 7152 }
    m_Event = {
        1: {
            0: {
                'Title': 7144,
                'CostTips': 7179,
                'CostType': NPC_OPTION_COST_NONE,
                'InitCostFunc': None,
                'RewardTips': 7158,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction201500,
                'GainRewardTips': 7180,
                'RewardDelay': 37 },
            1: {
                'Title': 7144,
                'CostTips': 7179,
                'CostType': NPC_OPTION_COST_NONE,
                'InitCostFunc': None,
                'RewardTips': 7158,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction201501,
                'GainRewardTips': 7180,
                'RewardDelay': 37 },
            2: {
                'Title': 7133,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction201502,
                'RewardTips': 7150,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction201502,
                'GainRewardTips': 7175,
                'RewardDelay': 37 },
            3: {
                'Title': 7133,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction201503,
                'RewardTips': 7150,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction201503,
                'GainRewardTips': 7175,
                'RewardDelay': 37 } },
        2: { } }


class CNpcEventData2101(CCustom):
    m_SID = 2101
    m_Titles = {
        1: 3019,
        2: 3020 }
    m_Event = {
        1: {
            0: {
                'Title': 3163,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction210100,
                'RewardTips': 3707,
                'RewardType': NPC_OPTION_REWARD_WEAPON,
                'InitRewardFunc': OptionInitRewardAction210100,
                'GainRewardTips': 3131,
                'RewardDelay': 37 },
            1: {
                'Title': 3164,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction210101,
                'RewardTips': 3711,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction210101,
                'GainRewardTips': 7175,
                'RewardDelay': 37 },
            2: {
                'Title': 3165,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction210102,
                'RewardTips': 3712,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction210102,
                'GainRewardTips': 7180,
                'RewardDelay': 37 } },
        2: { } }


class CNpcEventData2102(CCustom):
    m_SID = 2102
    m_Titles = {
        1: 3015,
        2: 7156 }
    m_Event = {
        1: {
            0: {
                'Title': 3147,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction210200,
                'RewardTips': 3702,
                'RewardType': NPC_OPTION_REWARD_ATTR,
                'InitRewardFunc': OptionInitRewardAction210200,
                'GainRewardTips': 3184,
                'RewardDelay': 37 },
            1: {
                'Title': 3148,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction210201,
                'RewardTips': 3703,
                'RewardType': NPC_OPTION_REWARD_ATTR,
                'InitRewardFunc': OptionInitRewardAction210201,
                'GainRewardTips': 3184,
                'RewardDelay': 37 } },
        2: { } }


class CNpcEventData2103(CCustom):
    m_SID = 2103
    m_Titles = {
        1: 3008,
        2: 7182 }
    m_Event = {
        1: {
            0: {
                'Title': 3168,
                'CostTips': 3409,
                'CostType': NPC_OPTION_COST_HP,
                'InitCostFunc': OptionInitCostAction210300,
                'RewardTips': 3702,
                'RewardType': NPC_OPTION_REWARD_ATTR,
                'InitRewardFunc': OptionInitRewardAction210300,
                'GainRewardTips': 3130,
                'RewardDelay': 37 },
            1: {
                'Title': 3173,
                'CostTips': 3409,
                'CostType': NPC_OPTION_COST_HP,
                'InitCostFunc': OptionInitCostAction210301,
                'RewardTips': 3703,
                'RewardType': NPC_OPTION_REWARD_ATTR,
                'InitRewardFunc': OptionInitRewardAction210301,
                'GainRewardTips': 3130,
                'RewardDelay': 37 } },
        2: { } }


class CNpcEventData2104(CCustom):
    m_SID = 2104
    m_Titles = {
        1: 3008,
        2: 7182 }
    m_Event = {
        1: {
            0: {
                'Title': 3172,
                'CostTips': 3409,
                'CostType': NPC_OPTION_COST_HP,
                'InitCostFunc': OptionInitCostAction210400,
                'RewardTips': 3701,
                'RewardType': NPC_OPTION_REWARD_WARCASH,
                'InitRewardFunc': OptionInitRewardAction210400,
                'GainRewardTips': 3110,
                'RewardDelay': 37 },
            1: {
                'Title': 3171,
                'CostTips': 3409,
                'CostType': NPC_OPTION_COST_HP,
                'InitCostFunc': OptionInitCostAction210401,
                'RewardTips': 3701,
                'RewardType': NPC_OPTION_REWARD_WARCASH,
                'InitRewardFunc': OptionInitRewardAction210401,
                'GainRewardTips': 3111,
                'RewardDelay': 37 },
            2: {
                'Title': 3176,
                'CostTips': 3409,
                'CostType': NPC_OPTION_COST_HP,
                'InitCostFunc': OptionInitCostAction210402,
                'RewardTips': 3701,
                'RewardType': NPC_OPTION_REWARD_WARCASH,
                'InitRewardFunc': OptionInitRewardAction210402,
                'GainRewardTips': 3112,
                'RewardDelay': 37 } },
        2: { } }


class CNpcEventData2105(CCustom):
    m_SID = 2105
    m_Titles = {
        1: 3016,
        2: 7156 }
    m_Event = {
        1: {
            0: {
                'Title': 3149,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction210500,
                'RewardTips': 3713,
                'RewardType': NPC_OPTION_REWARD_RELIC,
                'InitRewardFunc': OptionInitRewardAction210500,
                'GainRewardTips': 3103,
                'RewardDelay': 37 },
            1: {
                'Title': 3150,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction210501,
                'RewardTips': 3714,
                'RewardType': NPC_OPTION_REWARD_RELIC,
                'InitRewardFunc': OptionInitRewardAction210501,
                'GainRewardTips': 3103,
                'RewardDelay': 37 },
            2: {
                'Title': 3151,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction210502,
                'RewardTips': 3715,
                'RewardType': NPC_OPTION_REWARD_RELIC,
                'InitRewardFunc': OptionInitRewardAction210502,
                'GainRewardTips': 3103,
                'RewardDelay': 37 } },
        2: { } }


class CNpcEventData2106(CCustom):
    m_SID = 2106
    m_Titles = {
        1: 7131,
        2: 7156 }
    m_Event = {
        1: {
            0: {
                'Title': 7168,
                'CostTips': 3727,
                'CostType': NPC_OPTION_COST_SELECTRELIC,
                'InitCostFunc': OptionInitCostAction210600,
                'RewardTips': 3701,
                'RewardType': NPC_OPTION_REWARD_WARCASH,
                'InitRewardFunc': OptionInitRewardAction210600,
                'GainRewardTips': 7177,
                'RewardDelay': 37 } },
        2: { } }


class CNpcEventData2107(CCustom):
    m_SID = 2107
    m_Titles = {
        1: 3019,
        2: 3020 }
    m_Event = {
        1: {
            0: {
                'Title': 3166,
                'CostTips': 3727,
                'CostType': NPC_OPTION_COST_SELECTRELIC,
                'InitCostFunc': OptionInitCostAction210700,
                'RewardTips': 3713,
                'RewardType': NPC_OPTION_REWARD_RELIC,
                'InitRewardFunc': OptionInitRewardAction210700,
                'GainRewardTips': 3103,
                'RewardDelay': 37 },
            1: {
                'Title': 3164,
                'CostTips': 3727,
                'CostType': NPC_OPTION_COST_SELECTRELIC,
                'InitCostFunc': OptionInitCostAction210701,
                'RewardTips': 3716,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction210701,
                'GainRewardTips': 3141,
                'RewardDelay': 37 },
            2: {
                'Title': 3167,
                'CostTips': 3727,
                'CostType': NPC_OPTION_COST_SELECTRELIC,
                'InitCostFunc': OptionInitCostAction210702,
                'RewardTips': 3717,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction210702,
                'GainRewardTips': 7176,
                'RewardDelay': 37 } },
        2: { } }


class CNpcEventData2108(CCustom):
    m_SID = 2108
    m_Titles = {
        1: 3013,
        2: 3021 }
    m_Event = {
        1: {
            0: {
                'Title': 3136,
                'CostTips': 7179,
                'CostType': NPC_OPTION_COST_NONE,
                'InitCostFunc': None,
                'RewardTips': 3718,
                'RewardType': NPC_OPTION_REWARD_COSTRELIC,
                'InitRewardFunc': OptionInitRewardAction210800,
                'GainRewardTips': 3142,
                'RewardDelay': 37 },
            1: {
                'Title': 3137,
                'CostTips': 7179,
                'CostType': NPC_OPTION_COST_NONE,
                'InitCostFunc': None,
                'RewardTips': 3719,
                'RewardType': NPC_OPTION_REWARD_WARCASH,
                'InitRewardFunc': OptionInitRewardAction210801,
                'GainRewardTips': 3143,
                'RewardDelay': 37 },
            2: {
                'Title': 3138,
                'CostTips': 3409,
                'CostType': NPC_OPTION_COST_HP,
                'InitCostFunc': OptionInitCostAction210802,
                'RewardTips': 3701,
                'RewardType': NPC_OPTION_REWARD_WARCASH,
                'InitRewardFunc': OptionInitRewardAction210802,
                'GainRewardTips': 3111,
                'RewardDelay': 37 } },
        2: { } }


class CNpcEventData2110(CCustom):
    m_SID = 2110
    m_Titles = {
        1: 3008,
        2: 7182 }
    m_Event = {
        1: {
            0: {
                'Title': 3177,
                'CostTips': 3409,
                'CostType': NPC_OPTION_COST_HP,
                'InitCostFunc': OptionInitCostAction211000,
                'RewardTips': 3715,
                'RewardType': NPC_OPTION_REWARD_RELIC,
                'InitRewardFunc': OptionInitRewardAction211000,
                'GainRewardTips': 3103,
                'RewardDelay': 37 },
            1: {
                'Title': 3175,
                'CostTips': 3409,
                'CostType': NPC_OPTION_COST_HP,
                'InitCostFunc': OptionInitCostAction211001,
                'RewardTips': 3701,
                'RewardType': NPC_OPTION_REWARD_WARCASH,
                'InitRewardFunc': OptionInitRewardAction211001,
                'GainRewardTips': 3112,
                'RewardDelay': 37 },
            2: {
                'Title': 3179,
                'CostTips': 3409,
                'CostType': NPC_OPTION_COST_HP,
                'InitCostFunc': OptionInitCostAction211002,
                'RewardTips': 3718,
                'RewardType': NPC_OPTION_REWARD_COSTRELIC,
                'InitRewardFunc': OptionInitRewardAction211002,
                'GainRewardTips': 3142,
                'RewardDelay': 37 } },
        2: { } }


class CNpcEventData2112(CCustom):
    m_SID = 2112
    m_Titles = {
        1: 3017,
        2: 7156 }
    m_Event = {
        1: {
            0: {
                'Title': 3155,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction211200,
                'RewardTips': 3722,
                'RewardType': NPC_OPTION_REWARD_RELIC,
                'InitRewardFunc': OptionInitRewardAction211200,
                'GainRewardTips': 3103,
                'RewardDelay': 37 },
            1: {
                'Title': 3156,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction211201,
                'RewardTips': 3713,
                'RewardType': NPC_OPTION_REWARD_RELIC,
                'InitRewardFunc': OptionInitRewardAction211201,
                'GainRewardTips': 3103,
                'RewardDelay': 37 } },
        2: { } }


class CNpcEventData2113(CCustom):
    m_SID = 2113
    m_Titles = {
        1: 3018,
        2: 3021 }
    m_Event = {
        1: {
            0: {
                'Title': 3101,
                'CostTips': 3729,
                'CostType': NPC_OPTION_COST_CURSERELIC,
                'InitCostFunc': OptionInitCostAction211300,
                'RewardTips': 3726,
                'RewardType': NPC_OPTION_REWARD_GOLDENCUP,
                'InitRewardFunc': OptionInitRewardAction211300,
                'GainRewardTips': 3115,
                'RewardDelay': 37 } },
        2: { } }


class CNpcEventData2114(CCustom):
    m_SID = 2114
    m_Titles = {
        1: 3013,
        2: 3021 }
    m_Event = {
        1: {
            0: {
                'Title': 3157,
                'CostTips': 3408,
                'CostType': NPC_OPTION_COST_CURSERELIC,
                'InitCostFunc': OptionInitCostAction211400,
                'RewardTips': 3723,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction211400,
                'GainRewardTips': 3144,
                'RewardDelay': 37 },
            1: {
                'Title': 3158,
                'CostTips': 3408,
                'CostType': NPC_OPTION_COST_CURSERELIC,
                'InitCostFunc': OptionInitCostAction211401,
                'RewardTips': 3728,
                'RewardType': NPC_OPTION_REWARD_WEAPON,
                'InitRewardFunc': OptionInitRewardAction211401,
                'GainRewardTips': 7202,
                'RewardDelay': 37 },
            2: {
                'Title': 3159,
                'CostTips': 3408,
                'CostType': NPC_OPTION_COST_CURSERELIC,
                'InitCostFunc': OptionInitCostAction211402,
                'RewardTips': 3717,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction211402,
                'GainRewardTips': 7203,
                'RewardDelay': 37 } },
        2: { } }


class CNpcEventData2115(CCustom):
    m_SID = 2115
    m_Titles = {
        1: 3013,
        2: 3021 }
    m_Event = {
        1: {
            0: {
                'Title': 3160,
                'CostTips': 3408,
                'CostType': NPC_OPTION_COST_CURSERELIC,
                'InitCostFunc': OptionInitCostAction211500,
                'RewardTips': 3702,
                'RewardType': NPC_OPTION_REWARD_ATTR,
                'InitRewardFunc': OptionInitRewardAction211500,
                'GainRewardTips': 3145,
                'RewardDelay': 37 },
            1: {
                'Title': 3161,
                'CostTips': 3408,
                'CostType': NPC_OPTION_COST_CURSERELIC,
                'InitCostFunc': OptionInitCostAction211501,
                'RewardTips': 3703,
                'RewardType': NPC_OPTION_REWARD_ATTR,
                'InitRewardFunc': OptionInitRewardAction211501,
                'GainRewardTips': 3145,
                'RewardDelay': 37 },
            2: {
                'Title': 3159,
                'CostTips': 3408,
                'CostType': NPC_OPTION_COST_CURSERELIC,
                'InitCostFunc': OptionInitCostAction211502,
                'RewardTips': 3717,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction211502,
                'GainRewardTips': 7203,
                'RewardDelay': 37 } },
        2: { } }


class CNpcEventData2116(CCustom):
    m_SID = 2116
    m_Titles = {
        1: 3013,
        2: 3021 }
    m_Event = {
        1: {
            0: {
                'Title': 3162,
                'CostTips': 3408,
                'CostType': NPC_OPTION_COST_CURSERELIC,
                'InitCostFunc': OptionInitCostAction211600,
                'RewardTips': 3722,
                'RewardType': NPC_OPTION_REWARD_RELIC,
                'InitRewardFunc': OptionInitRewardAction211600,
                'GainRewardTips': 7202,
                'RewardDelay': 37 },
            1: {
                'Title': 3159,
                'CostTips': 3408,
                'CostType': NPC_OPTION_COST_CURSERELIC,
                'InitCostFunc': OptionInitCostAction211601,
                'RewardTips': 3717,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction211601,
                'GainRewardTips': 7203,
                'RewardDelay': 37 },
            2: {
                'Title': 3157,
                'CostTips': 3408,
                'CostType': NPC_OPTION_COST_CURSERELIC,
                'InitCostFunc': OptionInitCostAction211602,
                'RewardTips': 3723,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction211602,
                'GainRewardTips': 3144,
                'RewardDelay': 37 } },
        2: { } }


class CNpcEventData2117(CCustom):
    m_SID = 2117
    m_Titles = {
        1: 3008,
        2: 7182 }
    m_Event = {
        1: {
            0: {
                'Title': 3178,
                'CostTips': 3408,
                'CostType': NPC_OPTION_COST_CURSERELIC,
                'InitCostFunc': OptionInitCostAction211700,
                'RewardTips': 3728,
                'RewardType': NPC_OPTION_REWARD_WEAPON,
                'InitRewardFunc': OptionInitRewardAction211700,
                'GainRewardTips': 3145,
                'RewardDelay': 37 },
            1: {
                'Title': 3174,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction211701,
                'RewardTips': 3725,
                'RewardType': NPC_OPTION_REWARD_RELIC,
                'InitRewardFunc': OptionInitRewardAction211701,
                'GainRewardTips': 3103,
                'RewardDelay': 37 },
            2: {
                'Title': 3179,
                'CostTips': 3409,
                'CostType': NPC_OPTION_COST_HP,
                'InitCostFunc': OptionInitCostAction211702,
                'RewardTips': 3718,
                'RewardType': NPC_OPTION_REWARD_COSTRELIC,
                'InitRewardFunc': OptionInitRewardAction211702,
                'GainRewardTips': 3142,
                'RewardDelay': 37 } },
        2: { } }


class CNpcEventData2118(CCustom):
    m_SID = 2118
    m_Titles = {
        1: 3019,
        2: 3020 }
    m_Event = {
        1: {
            0: {
                'Title': 3167,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction211800,
                'RewardTips': 3717,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction211800,
                'GainRewardTips': 7176,
                'RewardDelay': 37 },
            1: {
                'Title': 3164,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction211801,
                'RewardTips': 3716,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction211801,
                'GainRewardTips': 3141,
                'RewardDelay': 37 },
            2: {
                'Title': 3165,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction211802,
                'RewardTips': 3712,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction211802,
                'GainRewardTips': 7180,
                'RewardDelay': 37 } },
        2: { } }


class CNpcEventData2119(CCustom):
    m_SID = 2119
    m_Titles = {
        1: 3008,
        2: 7182 }
    m_Event = {
        1: {
            0: {
                'Title': 3180,
                'CostTips': 3409,
                'CostType': NPC_OPTION_COST_HP,
                'InitCostFunc': OptionInitCostAction211900,
                'RewardTips': 3717,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction211900,
                'GainRewardTips': 7176,
                'RewardDelay': 37 },
            1: {
                'Title': 3181,
                'CostTips': 3409,
                'CostType': NPC_OPTION_COST_HP,
                'InitCostFunc': OptionInitCostAction211901,
                'RewardTips': 3711,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction211901,
                'GainRewardTips': 7175,
                'RewardDelay': 37 },
            2: {
                'Title': 3182,
                'CostTips': 3409,
                'CostType': NPC_OPTION_COST_HP,
                'InitCostFunc': OptionInitCostAction211902,
                'RewardTips': 3712,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction211902,
                'GainRewardTips': 7180,
                'RewardDelay': 37 } },
        2: { } }


class CNpcEventData2120(CCustom):
    m_SID = 2120
    m_Titles = {
        1: 3014,
        2: 3022 }
    m_Event = {
        1: {
            0: {
                'Title': 3140,
                'CostTips': 3411,
                'CostType': NPC_OPTION_COST_SELECTRELIC,
                'InitCostFunc': OptionInitCostAction212000,
                'RewardTips': 3726,
                'RewardType': NPC_OPTION_REWARD_GOLDENCUP,
                'InitRewardFunc': OptionInitRewardAction212000,
                'GainRewardTips': 3107,
                'RewardDelay': 37 } },
        2: { } }


class CNpcEventData2121(CCustom):
    m_SID = 2121
    m_Titles = {
        1: 3019,
        2: 3020 }
    m_Event = {
        1: {
            0: {
                'Title': 3170,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction212100,
                'RewardTips': 3713,
                'RewardType': NPC_OPTION_REWARD_RELIC,
                'InitRewardFunc': OptionInitRewardAction212100,
                'GainRewardTips': 3103,
                'RewardDelay': 37 },
            1: {
                'Title': 3164,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction212101,
                'RewardTips': 3716,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction212101,
                'GainRewardTips': 3141,
                'RewardDelay': 37 },
            2: {
                'Title': 3165,
                'CostTips': 7179,
                'CostType': NPC_OPTION_COST_NONE,
                'InitCostFunc': None,
                'RewardTips': 3712,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction212102,
                'GainRewardTips': 7180,
                'RewardDelay': 37 } },
        2: { } }


class CNpcEventData2122(CCustom):
    m_SID = 2122
    m_Titles = {
        1: 3019,
        2: 3020 }
    m_Event = {
        1: {
            0: {
                'Title': 3169,
                'CostTips': 3408,
                'CostType': NPC_OPTION_COST_CURSERELIC,
                'InitCostFunc': OptionInitCostAction212200,
                'RewardTips': 3728,
                'RewardType': NPC_OPTION_REWARD_WEAPON,
                'InitRewardFunc': OptionInitRewardAction212200,
                'GainRewardTips': 3145,
                'RewardDelay': 37 },
            1: {
                'Title': 3167,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction212201,
                'RewardTips': 3717,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction212201,
                'GainRewardTips': 7176,
                'RewardDelay': 37 },
            2: {
                'Title': 3164,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction212202,
                'RewardTips': 3711,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction212202,
                'GainRewardTips': 7175,
                'RewardDelay': 37 } },
        2: { } }


class CNpcEventData2123(CCustom):
    m_SID = 2123
    m_Titles = {
        1: 3008,
        2: 7182 }
    m_Event = {
        1: {
            0: {
                'Title': 3177,
                'CostTips': 3409,
                'CostType': NPC_OPTION_COST_HP,
                'InitCostFunc': OptionInitCostAction212300,
                'RewardTips': 3715,
                'RewardType': NPC_OPTION_REWARD_RELIC,
                'InitRewardFunc': OptionInitRewardAction212300,
                'GainRewardTips': 3103,
                'RewardDelay': 37 },
            1: {
                'Title': 3175,
                'CostTips': 3409,
                'CostType': NPC_OPTION_COST_HP,
                'InitCostFunc': OptionInitCostAction212301,
                'RewardTips': 3701,
                'RewardType': NPC_OPTION_REWARD_WARCASH,
                'InitRewardFunc': OptionInitRewardAction212301,
                'GainRewardTips': 3112,
                'RewardDelay': 37 } },
        2: { } }


class CNpcEventData2201(CCustom):
    m_SID = 2201
    m_Titles = {
        1: 7125,
        2: 7151 }
    m_Event = {
        1: {
            0: {
                'Title': 3101,
                'CostTips': 3729,
                'CostType': NPC_OPTION_COST_CURSERELIC,
                'InitCostFunc': OptionInitCostAction220100,
                'RewardTips': 3730,
                'RewardType': NPC_OPTION_REWARD_RELIC,
                'InitRewardFunc': OptionInitRewardAction220100,
                'GainRewardTips': 9594,
                'RewardDelay': 37 },
            1: {
                'Title': 3101,
                'CostTips': 3413,
                'CostType': NPC_OPTION_COST_GSCASH,
                'InitCostFunc': OptionInitCostAction220101,
                'RewardTips': 3731,
                'RewardType': NPC_OPTION_REWARD_UPGRADERELIC,
                'InitRewardFunc': OptionInitRewardAction220101,
                'GainRewardTips': 3191,
                'RewardDelay': 37 } },
        2: { } }


class CNpcEventData2202(CCustom):
    m_SID = 2202
    m_Titles = {
        1: 3019,
        2: 7152 }
    m_Event = {
        1: {
            0: {
                'Title': 3163,
                'CostTips': 3413,
                'CostType': NPC_OPTION_COST_GSCASH,
                'InitCostFunc': OptionInitCostAction220200,
                'RewardTips': 3732,
                'RewardType': NPC_OPTION_REWARD_WEAPON,
                'InitRewardFunc': OptionInitRewardAction220200,
                'GainRewardTips': 3131,
                'RewardDelay': 37 },
            1: {
                'Title': 3165,
                'CostTips': 3413,
                'CostType': NPC_OPTION_COST_GSCASH,
                'InitCostFunc': OptionInitCostAction220201,
                'RewardTips': 3733,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction220201,
                'GainRewardTips': 3192,
                'RewardDelay': 37 },
            2: {
                'Title': 3167,
                'CostTips': 3413,
                'CostType': NPC_OPTION_COST_GSCASH,
                'InitCostFunc': OptionInitCostAction220202,
                'RewardTips': 3717,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction220202,
                'GainRewardTips': 7176,
                'RewardDelay': 37 } },
        2: { } }


class CNpcEventData2204(CCustom):
    m_SID = 2204
    m_Titles = {
        1: 3007,
        2: 7156 }
    m_Event = {
        1: {
            0: {
                'Title': 3101,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction220400,
                'RewardTips': 3730,
                'RewardType': NPC_OPTION_REWARD_RELIC,
                'InitRewardFunc': OptionInitRewardAction220400,
                'GainRewardTips': 9594,
                'RewardDelay': 37 },
            1: {
                'Title': 3101,
                'CostTips': 3413,
                'CostType': NPC_OPTION_COST_GSCASH,
                'InitCostFunc': OptionInitCostAction220401,
                'RewardTips': 3730,
                'RewardType': NPC_OPTION_REWARD_RELIC,
                'InitRewardFunc': OptionInitRewardAction220401,
                'GainRewardTips': 9594,
                'RewardDelay': 37 } },
        2: { } }


class CNpcEventData2205(CCustom):
    m_SID = 2205
    m_Titles = {
        1: 3007,
        2: 7156 }
    m_Event = {
        1: {
            0: {
                'Title': 3101,
                'CostTips': 3413,
                'CostType': NPC_OPTION_COST_GSCASH,
                'InitCostFunc': OptionInitCostAction220500,
                'RewardTips': 3730,
                'RewardType': NPC_OPTION_REWARD_RELIC,
                'InitRewardFunc': OptionInitRewardAction220500,
                'GainRewardTips': 9594,
                'RewardDelay': 37 },
            1: {
                'Title': 3101,
                'CostTips': 3413,
                'CostType': NPC_OPTION_COST_GSCASH,
                'InitCostFunc': OptionInitCostAction220501,
                'RewardTips': 3731,
                'RewardType': NPC_OPTION_REWARD_UPGRADERELIC,
                'InitRewardFunc': OptionInitRewardAction220501,
                'GainRewardTips': 3191,
                'RewardDelay': 37 } },
        2: { } }


class CNpcEventData2206(CCustom):
    m_SID = 2206
    m_Titles = {
        1: 7128,
        2: 7154 }
    m_Event = {
        1: {
            0: {
                'Title': 3140,
                'CostTips': 3411,
                'CostType': NPC_OPTION_COST_SELECTRELIC,
                'InitCostFunc': OptionInitCostAction220600,
                'RewardTips': 3730,
                'RewardType': NPC_OPTION_REWARD_RELIC,
                'InitRewardFunc': OptionInitRewardAction220600,
                'GainRewardTips': 9594,
                'RewardDelay': 37 },
            1: {
                'Title': 3190,
                'CostTips': 3414,
                'CostType': NPC_OPTION_COST_SELECTRELIC,
                'InitCostFunc': OptionInitCostAction220601,
                'RewardTips': 3730,
                'RewardType': NPC_OPTION_REWARD_RELIC,
                'InitRewardFunc': OptionInitRewardAction220601,
                'GainRewardTips': 9594,
                'RewardDelay': 37 } },
        2: { } }


class CNpcEventData2301(CCustom):
    m_SID = 2301
    m_Titles = {
        1: 7128,
        2: 7154 }
    m_Event = {
        1: {
            0: {
                'Title': 3101,
                'CostTips': 3408,
                'CostType': NPC_OPTION_COST_CURSERELIC,
                'InitCostFunc': OptionInitCostAction230100,
                'RewardTips': 3735,
                'RewardType': NPC_OPTION_REWARD_MAGICPOWER,
                'InitRewardFunc': OptionInitRewardAction230100,
                'GainRewardTips': 3183,
                'RewardDelay': 37 },
            1: {
                'Title': 3140,
                'CostTips': 3727,
                'CostType': NPC_OPTION_COST_SELECTRELIC,
                'InitCostFunc': OptionInitCostAction230101,
                'RewardTips': 3735,
                'RewardType': NPC_OPTION_REWARD_MAGICPOWER,
                'InitRewardFunc': OptionInitRewardAction230101,
                'GainRewardTips': 3183,
                'RewardDelay': 37 } },
        2: { } }


class CNpcEventData2302(CCustom):
    m_SID = 2302
    m_Titles = {
        1: 7128,
        2: 7154 }
    m_Event = {
        1: {
            0: {
                'Title': 3140,
                'CostTips': 3740,
                'CostType': NPC_OPTION_COST_SELECTRELIC,
                'InitCostFunc': OptionInitCostAction230200,
                'RewardTips': 3736,
                'RewardType': NPC_OPTION_REWARD_MAGICPOWER,
                'InitRewardFunc': OptionInitRewardAction230200,
                'GainRewardTips': 3146,
                'RewardDelay': 37 },
            1: {
                'Title': 3140,
                'CostTips': 3738,
                'CostType': NPC_OPTION_COST_SELECTRELIC,
                'InitCostFunc': OptionInitCostAction230201,
                'RewardTips': 3735,
                'RewardType': NPC_OPTION_REWARD_MAGICPOWER,
                'InitRewardFunc': OptionInitRewardAction230201,
                'GainRewardTips': 3183,
                'RewardDelay': 37 },
            2: {
                'Title': 3140,
                'CostTips': 3739,
                'CostType': NPC_OPTION_COST_SELECTRELIC,
                'InitCostFunc': OptionInitCostAction230202,
                'RewardTips': 3737,
                'RewardType': NPC_OPTION_REWARD_MAGICPOWER,
                'InitRewardFunc': OptionInitRewardAction230202,
                'GainRewardTips': 3193,
                'RewardDelay': 37 } },
        2: { } }


class CNpcEventData3101(CCustom):
    m_SID = 3101
    m_Titles = {
        1: 3019,
        2: 3020 }
    m_Event = {
        1: {
            0: {
                'Title': 3163,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction310100,
                'RewardTips': 3707,
                'RewardType': NPC_OPTION_REWARD_WEAPON,
                'InitRewardFunc': OptionInitRewardAction310100,
                'GainRewardTips': 3131,
                'RewardDelay': 37 },
            1: {
                'Title': 3164,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction310101,
                'RewardTips': 3711,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction310101,
                'GainRewardTips': 7175,
                'RewardDelay': 37 },
            2: {
                'Title': 3165,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction310102,
                'RewardTips': 3712,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction310102,
                'GainRewardTips': 7180,
                'RewardDelay': 37 } },
        2: { } }


class CNpcEventData3102(CCustom):
    m_SID = 3102
    m_Titles = {
        1: 3015,
        2: 7156 }
    m_Event = {
        1: {
            0: {
                'Title': 3147,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction310200,
                'RewardTips': 3702,
                'RewardType': NPC_OPTION_REWARD_ATTR,
                'InitRewardFunc': OptionInitRewardAction310200,
                'GainRewardTips': 3184,
                'RewardDelay': 37 },
            1: {
                'Title': 3148,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction310201,
                'RewardTips': 3703,
                'RewardType': NPC_OPTION_REWARD_ATTR,
                'InitRewardFunc': OptionInitRewardAction310201,
                'GainRewardTips': 3184,
                'RewardDelay': 37 } },
        2: { } }


class CNpcEventData3103(CCustom):
    m_SID = 3103
    m_Titles = {
        1: 3008,
        2: 7182 }
    m_Event = {
        1: {
            0: {
                'Title': 3168,
                'CostTips': 3409,
                'CostType': NPC_OPTION_COST_HP,
                'InitCostFunc': OptionInitCostAction310300,
                'RewardTips': 3702,
                'RewardType': NPC_OPTION_REWARD_ATTR,
                'InitRewardFunc': OptionInitRewardAction310300,
                'GainRewardTips': 3130,
                'RewardDelay': 37 },
            1: {
                'Title': 3173,
                'CostTips': 3409,
                'CostType': NPC_OPTION_COST_HP,
                'InitCostFunc': OptionInitCostAction310301,
                'RewardTips': 3703,
                'RewardType': NPC_OPTION_REWARD_ATTR,
                'InitRewardFunc': OptionInitRewardAction310301,
                'GainRewardTips': 3130,
                'RewardDelay': 37 } },
        2: { } }


class CNpcEventData3105(CCustom):
    m_SID = 3105
    m_Titles = {
        1: 3016,
        2: 7156 }
    m_Event = {
        1: {
            0: {
                'Title': 3149,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction310500,
                'RewardTips': 3713,
                'RewardType': NPC_OPTION_REWARD_RELIC,
                'InitRewardFunc': OptionInitRewardAction310500,
                'GainRewardTips': 3103,
                'RewardDelay': 37 },
            1: {
                'Title': 3150,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction310501,
                'RewardTips': 3714,
                'RewardType': NPC_OPTION_REWARD_RELIC,
                'InitRewardFunc': OptionInitRewardAction310501,
                'GainRewardTips': 3103,
                'RewardDelay': 37 },
            2: {
                'Title': 3151,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction310502,
                'RewardTips': 3715,
                'RewardType': NPC_OPTION_REWARD_RELIC,
                'InitRewardFunc': OptionInitRewardAction310502,
                'GainRewardTips': 3103,
                'RewardDelay': 37 } },
        2: { } }


class CNpcEventData3112(CCustom):
    m_SID = 3112
    m_Titles = {
        1: 3017,
        2: 7156 }
    m_Event = {
        1: {
            0: {
                'Title': 3155,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction311200,
                'RewardTips': 3722,
                'RewardType': NPC_OPTION_REWARD_RELIC,
                'InitRewardFunc': OptionInitRewardAction311200,
                'GainRewardTips': 3103,
                'RewardDelay': 37 },
            1: {
                'Title': 3156,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction311201,
                'RewardTips': 3713,
                'RewardType': NPC_OPTION_REWARD_RELIC,
                'InitRewardFunc': OptionInitRewardAction311201,
                'GainRewardTips': 3103,
                'RewardDelay': 37 },
            2: {
                'Title': 3164,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction311202,
                'RewardTips': 3711,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction311202,
                'GainRewardTips': 7175,
                'RewardDelay': 37 } },
        2: { } }


class CNpcEventData3113(CCustom):
    m_SID = 3113
    m_Titles = {
        1: 3018,
        2: 3021 }
    m_Event = {
        1: {
            0: {
                'Title': 3101,
                'CostTips': 3729,
                'CostType': NPC_OPTION_COST_CURSERELIC,
                'InitCostFunc': OptionInitCostAction311300,
                'RewardTips': 3726,
                'RewardType': NPC_OPTION_REWARD_GOLDENCUP,
                'InitRewardFunc': OptionInitRewardAction311300,
                'GainRewardTips': 3115,
                'RewardDelay': 37 } },
        2: { } }


class CNpcEventData3115(CCustom):
    m_SID = 3115
    m_Titles = {
        1: 3013,
        2: 3021 }
    m_Event = {
        1: {
            0: {
                'Title': 3160,
                'CostTips': 3408,
                'CostType': NPC_OPTION_COST_CURSERELIC,
                'InitCostFunc': OptionInitCostAction311500,
                'RewardTips': 3702,
                'RewardType': NPC_OPTION_REWARD_ATTR,
                'InitRewardFunc': OptionInitRewardAction311500,
                'GainRewardTips': 3145,
                'RewardDelay': 37 },
            1: {
                'Title': 3161,
                'CostTips': 3408,
                'CostType': NPC_OPTION_COST_CURSERELIC,
                'InitCostFunc': OptionInitCostAction311501,
                'RewardTips': 3703,
                'RewardType': NPC_OPTION_REWARD_ATTR,
                'InitRewardFunc': OptionInitRewardAction311501,
                'GainRewardTips': 3145,
                'RewardDelay': 37 },
            2: {
                'Title': 3159,
                'CostTips': 3408,
                'CostType': NPC_OPTION_COST_CURSERELIC,
                'InitCostFunc': OptionInitCostAction311502,
                'RewardTips': 3717,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction311502,
                'GainRewardTips': 7203,
                'RewardDelay': 37 } },
        2: { } }


class CNpcEventData3116(CCustom):
    m_SID = 3116
    m_Titles = {
        1: 3013,
        2: 3021 }
    m_Event = {
        1: {
            0: {
                'Title': 3162,
                'CostTips': 3408,
                'CostType': NPC_OPTION_COST_CURSERELIC,
                'InitCostFunc': OptionInitCostAction311600,
                'RewardTips': 3722,
                'RewardType': NPC_OPTION_REWARD_RELIC,
                'InitRewardFunc': OptionInitRewardAction311600,
                'GainRewardTips': 7202,
                'RewardDelay': 37 },
            1: {
                'Title': 3159,
                'CostTips': 3408,
                'CostType': NPC_OPTION_COST_CURSERELIC,
                'InitCostFunc': OptionInitCostAction311601,
                'RewardTips': 3717,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction311601,
                'GainRewardTips': 7203,
                'RewardDelay': 37 },
            2: {
                'Title': 3157,
                'CostTips': 3408,
                'CostType': NPC_OPTION_COST_CURSERELIC,
                'InitCostFunc': OptionInitCostAction311602,
                'RewardTips': 3723,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction311602,
                'GainRewardTips': 3144,
                'RewardDelay': 37 } },
        2: { } }


class CNpcEventData3117(CCustom):
    m_SID = 3117
    m_Titles = {
        1: 3008,
        2: 7182 }
    m_Event = {
        1: {
            0: {
                'Title': 3157,
                'CostTips': 3408,
                'CostType': NPC_OPTION_COST_CURSERELIC,
                'InitCostFunc': OptionInitCostAction311700,
                'RewardTips': 3723,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction311700,
                'GainRewardTips': 3144,
                'RewardDelay': 37 },
            1: {
                'Title': 3174,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction311701,
                'RewardTips': 3713,
                'RewardType': NPC_OPTION_REWARD_RELIC,
                'InitRewardFunc': OptionInitRewardAction311701,
                'GainRewardTips': 3103,
                'RewardDelay': 37 },
            2: {
                'Title': 3179,
                'CostTips': 3409,
                'CostType': NPC_OPTION_COST_HP,
                'InitCostFunc': OptionInitCostAction311702,
                'RewardTips': 3718,
                'RewardType': NPC_OPTION_REWARD_COSTRELIC,
                'InitRewardFunc': OptionInitRewardAction311702,
                'GainRewardTips': 3142,
                'RewardDelay': 37 } },
        2: { } }


class CNpcEventData3118(CCustom):
    m_SID = 3118
    m_Titles = {
        1: 3019,
        2: 3020 }
    m_Event = {
        1: {
            0: {
                'Title': 3167,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction311800,
                'RewardTips': 3717,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction311800,
                'GainRewardTips': 7176,
                'RewardDelay': 37 },
            1: {
                'Title': 3164,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction311801,
                'RewardTips': 3716,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction311801,
                'GainRewardTips': 3141,
                'RewardDelay': 37 },
            2: {
                'Title': 3165,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction311802,
                'RewardTips': 3712,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction311802,
                'GainRewardTips': 7180,
                'RewardDelay': 37 } },
        2: { } }


class CNpcEventData3119(CCustom):
    m_SID = 3119
    m_Titles = {
        1: 3019,
        2: 3020 }
    m_Event = {
        1: {
            0: {
                'Title': 7145,
                'CostTips': 7147,
                'CostType': NPC_OPTION_COST_SELECTRELIC,
                'InitCostFunc': OptionInitCostAction311900,
                'RewardTips': 3713,
                'RewardType': NPC_OPTION_REWARD_RELIC,
                'InitRewardFunc': OptionInitRewardAction311900,
                'GainRewardTips': 3103,
                'RewardDelay': 37 },
            1: {
                'Title': 3168,
                'CostTips': 7147,
                'CostType': NPC_OPTION_COST_SELECTRELIC,
                'InitCostFunc': OptionInitCostAction311901,
                'RewardTips': 3702,
                'RewardType': NPC_OPTION_REWARD_ATTR,
                'InitRewardFunc': OptionInitRewardAction311901,
                'GainRewardTips': 3130,
                'RewardDelay': 37 },
            2: {
                'Title': 3173,
                'CostTips': 7147,
                'CostType': NPC_OPTION_COST_SELECTRELIC,
                'InitCostFunc': OptionInitCostAction311902,
                'RewardTips': 3703,
                'RewardType': NPC_OPTION_REWARD_ATTR,
                'InitRewardFunc': OptionInitRewardAction311902,
                'GainRewardTips': 3130,
                'RewardDelay': 37 } },
        2: { } }


class CNpcEventData3121(CCustom):
    m_SID = 3121
    m_Titles = {
        1: 3019,
        2: 3020 }
    m_Event = {
        1: {
            0: {
                'Title': 3170,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction312100,
                'RewardTips': 3713,
                'RewardType': NPC_OPTION_REWARD_RELIC,
                'InitRewardFunc': OptionInitRewardAction312100,
                'GainRewardTips': 3103,
                'RewardDelay': 37 },
            1: {
                'Title': 3164,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction312101,
                'RewardTips': 3716,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction312101,
                'GainRewardTips': 3141,
                'RewardDelay': 37 },
            2: {
                'Title': 3165,
                'CostTips': 7179,
                'CostType': NPC_OPTION_COST_NONE,
                'InitCostFunc': None,
                'RewardTips': 3712,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction312102,
                'GainRewardTips': 7180,
                'RewardDelay': 37 } },
        2: { } }


class CNpcEventData3122(CCustom):
    m_SID = 3122
    m_Titles = {
        1: 3019,
        2: 3020 }
    m_Event = {
        1: {
            0: {
                'Title': 3169,
                'CostTips': 3408,
                'CostType': NPC_OPTION_COST_CURSERELIC,
                'InitCostFunc': OptionInitCostAction312200,
                'RewardTips': 3728,
                'RewardType': NPC_OPTION_REWARD_WEAPON,
                'InitRewardFunc': OptionInitRewardAction312200,
                'GainRewardTips': 3145,
                'RewardDelay': 37 },
            1: {
                'Title': 3167,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction312201,
                'RewardTips': 3717,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction312201,
                'GainRewardTips': 7176,
                'RewardDelay': 37 },
            2: {
                'Title': 3164,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction312202,
                'RewardTips': 3711,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction312202,
                'GainRewardTips': 7175,
                'RewardDelay': 37 } },
        2: { } }


class CNpcEventData3201(CCustom):
    m_SID = 3201
    m_Titles = {
        1: 3019,
        2: 3020 }
    m_Event = {
        1: {
            0: {
                'Title': 3163,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction320100,
                'RewardTips': 3707,
                'RewardType': NPC_OPTION_REWARD_WEAPON,
                'InitRewardFunc': OptionInitRewardAction320100,
                'GainRewardTips': 3131,
                'RewardDelay': 37 },
            1: {
                'Title': 3164,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction320101,
                'RewardTips': 3711,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction320101,
                'GainRewardTips': 7175,
                'RewardDelay': 37 },
            2: {
                'Title': 3165,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction320102,
                'RewardTips': 3712,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction320102,
                'GainRewardTips': 7180,
                'RewardDelay': 37 } },
        2: { } }


class CNpcEventData3202(CCustom):
    m_SID = 3202
    m_Titles = {
        1: 3015,
        2: 7156 }
    m_Event = {
        1: {
            0: {
                'Title': 3147,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction320200,
                'RewardTips': 3702,
                'RewardType': NPC_OPTION_REWARD_ATTR,
                'InitRewardFunc': OptionInitRewardAction320200,
                'GainRewardTips': 3184,
                'RewardDelay': 37 },
            1: {
                'Title': 3148,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction320201,
                'RewardTips': 3703,
                'RewardType': NPC_OPTION_REWARD_ATTR,
                'InitRewardFunc': OptionInitRewardAction320201,
                'GainRewardTips': 3184,
                'RewardDelay': 37 } },
        2: { } }


class CNpcEventData3203(CCustom):
    m_SID = 3203
    m_Titles = {
        1: 3008,
        2: 7182 }
    m_Event = {
        1: {
            0: {
                'Title': 3168,
                'CostTips': 3409,
                'CostType': NPC_OPTION_COST_HP,
                'InitCostFunc': OptionInitCostAction320300,
                'RewardTips': 3702,
                'RewardType': NPC_OPTION_REWARD_ATTR,
                'InitRewardFunc': OptionInitRewardAction320300,
                'GainRewardTips': 3130,
                'RewardDelay': 37 },
            1: {
                'Title': 3173,
                'CostTips': 3409,
                'CostType': NPC_OPTION_COST_HP,
                'InitCostFunc': OptionInitCostAction320301,
                'RewardTips': 3703,
                'RewardType': NPC_OPTION_REWARD_ATTR,
                'InitRewardFunc': OptionInitRewardAction320301,
                'GainRewardTips': 3130,
                'RewardDelay': 37 } },
        2: { } }


class CNpcEventData3205(CCustom):
    m_SID = 3205
    m_Titles = {
        1: 3016,
        2: 7156 }
    m_Event = {
        1: {
            0: {
                'Title': 3149,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction320500,
                'RewardTips': 3713,
                'RewardType': NPC_OPTION_REWARD_RELIC,
                'InitRewardFunc': OptionInitRewardAction320500,
                'GainRewardTips': 3103,
                'RewardDelay': 37 },
            1: {
                'Title': 3150,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction320501,
                'RewardTips': 3714,
                'RewardType': NPC_OPTION_REWARD_RELIC,
                'InitRewardFunc': OptionInitRewardAction320501,
                'GainRewardTips': 3103,
                'RewardDelay': 37 },
            2: {
                'Title': 3151,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction320502,
                'RewardTips': 3715,
                'RewardType': NPC_OPTION_REWARD_RELIC,
                'InitRewardFunc': OptionInitRewardAction320502,
                'GainRewardTips': 3103,
                'RewardDelay': 37 } },
        2: { } }


class CNpcEventData3212(CCustom):
    m_SID = 3212
    m_Titles = {
        1: 3017,
        2: 7156 }
    m_Event = {
        1: {
            0: {
                'Title': 3155,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction321200,
                'RewardTips': 3722,
                'RewardType': NPC_OPTION_REWARD_RELIC,
                'InitRewardFunc': OptionInitRewardAction321200,
                'GainRewardTips': 3103,
                'RewardDelay': 37 },
            1: {
                'Title': 3156,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction321201,
                'RewardTips': 3713,
                'RewardType': NPC_OPTION_REWARD_RELIC,
                'InitRewardFunc': OptionInitRewardAction321201,
                'GainRewardTips': 3103,
                'RewardDelay': 37 },
            2: {
                'Title': 3164,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction321202,
                'RewardTips': 3711,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction321202,
                'GainRewardTips': 7175,
                'RewardDelay': 37 } },
        2: { } }


class CNpcEventData3213(CCustom):
    m_SID = 3213
    m_Titles = {
        1: 3018,
        2: 3021 }
    m_Event = {
        1: {
            0: {
                'Title': 3101,
                'CostTips': 3729,
                'CostType': NPC_OPTION_COST_CURSERELIC,
                'InitCostFunc': OptionInitCostAction321300,
                'RewardTips': 3726,
                'RewardType': NPC_OPTION_REWARD_GOLDENCUP,
                'InitRewardFunc': OptionInitRewardAction321300,
                'GainRewardTips': 3115,
                'RewardDelay': 37 } },
        2: { } }


class CNpcEventData3215(CCustom):
    m_SID = 3215
    m_Titles = {
        1: 3013,
        2: 3021 }
    m_Event = {
        1: {
            0: {
                'Title': 3160,
                'CostTips': 3408,
                'CostType': NPC_OPTION_COST_CURSERELIC,
                'InitCostFunc': OptionInitCostAction321500,
                'RewardTips': 3702,
                'RewardType': NPC_OPTION_REWARD_ATTR,
                'InitRewardFunc': OptionInitRewardAction321500,
                'GainRewardTips': 3145,
                'RewardDelay': 37 },
            1: {
                'Title': 3161,
                'CostTips': 3408,
                'CostType': NPC_OPTION_COST_CURSERELIC,
                'InitCostFunc': OptionInitCostAction321501,
                'RewardTips': 3703,
                'RewardType': NPC_OPTION_REWARD_ATTR,
                'InitRewardFunc': OptionInitRewardAction321501,
                'GainRewardTips': 3145,
                'RewardDelay': 37 },
            2: {
                'Title': 3159,
                'CostTips': 3408,
                'CostType': NPC_OPTION_COST_CURSERELIC,
                'InitCostFunc': OptionInitCostAction321502,
                'RewardTips': 3717,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction321502,
                'GainRewardTips': 7203,
                'RewardDelay': 37 } },
        2: { } }


class CNpcEventData3216(CCustom):
    m_SID = 3216
    m_Titles = {
        1: 3013,
        2: 3021 }
    m_Event = {
        1: {
            0: {
                'Title': 3162,
                'CostTips': 3408,
                'CostType': NPC_OPTION_COST_CURSERELIC,
                'InitCostFunc': OptionInitCostAction321600,
                'RewardTips': 3722,
                'RewardType': NPC_OPTION_REWARD_RELIC,
                'InitRewardFunc': OptionInitRewardAction321600,
                'GainRewardTips': 7202,
                'RewardDelay': 37 },
            1: {
                'Title': 3159,
                'CostTips': 3408,
                'CostType': NPC_OPTION_COST_CURSERELIC,
                'InitCostFunc': OptionInitCostAction321601,
                'RewardTips': 3717,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction321601,
                'GainRewardTips': 7203,
                'RewardDelay': 37 },
            2: {
                'Title': 3157,
                'CostTips': 3408,
                'CostType': NPC_OPTION_COST_CURSERELIC,
                'InitCostFunc': OptionInitCostAction321602,
                'RewardTips': 3723,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction321602,
                'GainRewardTips': 3144,
                'RewardDelay': 37 } },
        2: { } }


class CNpcEventData3217(CCustom):
    m_SID = 3217
    m_Titles = {
        1: 3008,
        2: 7182 }
    m_Event = {
        1: {
            0: {
                'Title': 3157,
                'CostTips': 3408,
                'CostType': NPC_OPTION_COST_CURSERELIC,
                'InitCostFunc': OptionInitCostAction321700,
                'RewardTips': 3723,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction321700,
                'GainRewardTips': 3144,
                'RewardDelay': 37 },
            1: {
                'Title': 3174,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction321701,
                'RewardTips': 3713,
                'RewardType': NPC_OPTION_REWARD_RELIC,
                'InitRewardFunc': OptionInitRewardAction321701,
                'GainRewardTips': 3103,
                'RewardDelay': 37 },
            2: {
                'Title': 3179,
                'CostTips': 3409,
                'CostType': NPC_OPTION_COST_HP,
                'InitCostFunc': OptionInitCostAction321702,
                'RewardTips': 3718,
                'RewardType': NPC_OPTION_REWARD_COSTRELIC,
                'InitRewardFunc': OptionInitRewardAction321702,
                'GainRewardTips': 3142,
                'RewardDelay': 37 } },
        2: { } }


class CNpcEventData3218(CCustom):
    m_SID = 3218
    m_Titles = {
        1: 3019,
        2: 3020 }
    m_Event = {
        1: {
            0: {
                'Title': 3167,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction321800,
                'RewardTips': 3717,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction321800,
                'GainRewardTips': 7176,
                'RewardDelay': 37 },
            1: {
                'Title': 3164,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction321801,
                'RewardTips': 3716,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction321801,
                'GainRewardTips': 3141,
                'RewardDelay': 37 },
            2: {
                'Title': 3165,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction321802,
                'RewardTips': 3712,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction321802,
                'GainRewardTips': 7180,
                'RewardDelay': 37 } },
        2: { } }


class CNpcEventData3221(CCustom):
    m_SID = 3221
    m_Titles = {
        1: 3019,
        2: 3020 }
    m_Event = {
        1: {
            0: {
                'Title': 3170,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction322100,
                'RewardTips': 3713,
                'RewardType': NPC_OPTION_REWARD_RELIC,
                'InitRewardFunc': OptionInitRewardAction322100,
                'GainRewardTips': 3103,
                'RewardDelay': 37 },
            1: {
                'Title': 3164,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction322101,
                'RewardTips': 3716,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction322101,
                'GainRewardTips': 3141,
                'RewardDelay': 37 },
            2: {
                'Title': 3165,
                'CostTips': 7179,
                'CostType': NPC_OPTION_COST_NONE,
                'InitCostFunc': None,
                'RewardTips': 3712,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction322102,
                'GainRewardTips': 7180,
                'RewardDelay': 37 } },
        2: { } }


class CNpcEventData3222(CCustom):
    m_SID = 3222
    m_Titles = {
        1: 3019,
        2: 3020 }
    m_Event = {
        1: {
            0: {
                'Title': 3169,
                'CostTips': 3408,
                'CostType': NPC_OPTION_COST_CURSERELIC,
                'InitCostFunc': OptionInitCostAction322200,
                'RewardTips': 3728,
                'RewardType': NPC_OPTION_REWARD_WEAPON,
                'InitRewardFunc': OptionInitRewardAction322200,
                'GainRewardTips': 3145,
                'RewardDelay': 37 },
            1: {
                'Title': 3167,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction322201,
                'RewardTips': 3717,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction322201,
                'GainRewardTips': 7176,
                'RewardDelay': 37 },
            2: {
                'Title': 3164,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction322202,
                'RewardTips': 3711,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction322202,
                'GainRewardTips': 7175,
                'RewardDelay': 37 } },
        2: { } }


class CNpcEventData3223(CCustom):
    m_SID = 3223
    m_Titles = {
        1: 7125,
        2: 7151 }
    m_Event = {
        1: {
            0: {
                'Title': 3101,
                'CostTips': 3729,
                'CostType': NPC_OPTION_COST_CURSERELIC,
                'InitCostFunc': OptionInitCostAction322300,
                'RewardTips': 3730,
                'RewardType': NPC_OPTION_REWARD_RELIC,
                'InitRewardFunc': OptionInitRewardAction322300,
                'GainRewardTips': 9594,
                'RewardDelay': 37 },
            1: {
                'Title': 3101,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction322301,
                'RewardTips': 3731,
                'RewardType': NPC_OPTION_REWARD_UPGRADERELIC,
                'InitRewardFunc': OptionInitRewardAction322301,
                'GainRewardTips': 3191,
                'RewardDelay': 37 } },
        2: { } }


class CNpcEventData3224(CCustom):
    m_SID = 3224
    m_Titles = {
        1: 7128,
        2: 7154 }
    m_Event = {
        1: {
            0: {
                'Title': 3140,
                'CostTips': 3411,
                'CostType': NPC_OPTION_COST_SELECTRELIC,
                'InitCostFunc': OptionInitCostAction322400,
                'RewardTips': 3730,
                'RewardType': NPC_OPTION_REWARD_RELIC,
                'InitRewardFunc': OptionInitRewardAction322400,
                'GainRewardTips': 9594,
                'RewardDelay': 37 },
            1: {
                'Title': 3190,
                'CostTips': 3414,
                'CostType': NPC_OPTION_COST_SELECTRELIC,
                'InitCostFunc': OptionInitCostAction322401,
                'RewardTips': 3730,
                'RewardType': NPC_OPTION_REWARD_RELIC,
                'InitRewardFunc': OptionInitRewardAction322401,
                'GainRewardTips': 9594,
                'RewardDelay': 37 } },
        2: { } }


class CNpcEventData4001(CCustom):
    m_SID = 4001
    m_Titles = {
        1: 7131,
        2: 7156 }
    m_Event = {
        1: {
            0: {
                'Title': 7218,
                'CostTips': 3406,
                'CostType': NPC_OPTION_COST_RELIC,
                'InitCostFunc': OptionInitCostAction400100,
                'RewardTips': 3701,
                'RewardType': NPC_OPTION_REWARD_WARCASH,
                'InitRewardFunc': OptionInitRewardAction400100,
                'GainRewardTips': 7177,
                'RewardDelay': 37 } },
        2: { } }


class CNpcEventData4002(CCustom):
    m_SID = 4002
    m_Titles = {
        1: 7222,
        2: 7151 }
    m_Event = {
        1: {
            0: {
                'Title': 7219,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction400200,
                'RewardTips': 7220,
                'RewardType': NPC_OPTION_REWARD_COSTRELIC,
                'InitRewardFunc': OptionInitRewardAction400200,
                'GainRewardTips': 3135,
                'RewardDelay': 37 } },
        2: { } }


class CNpcEventData4003(CCustom):
    m_SID = 4003
    m_Titles = {
        1: 7129,
        2: 7152 }
    m_Event = {
        1: {
            0: {
                'Title': 7132,
                'CostTips': 7179,
                'CostType': NPC_OPTION_COST_NONE,
                'InitCostFunc': None,
                'RewardTips': 7221,
                'RewardType': NPC_OPTION_REWARD_RELIC,
                'InitRewardFunc': OptionInitRewardAction400300,
                'GainRewardTips': 3103,
                'RewardDelay': 37 } },
        2: { } }


class CNpcEventData4004(CCustom):
    m_SID = 4004
    m_Titles = {
        1: 3006 }
    m_Event = {
        1: {
            0: {
                'Title': 3113,
                'CostTips': 3409,
                'CostType': NPC_OPTION_COST_HP,
                'InitCostFunc': OptionInitCostAction400400,
                'RewardTips': 3701,
                'RewardType': NPC_OPTION_REWARD_WARCASH,
                'InitRewardFunc': OptionInitRewardAction400400,
                'GainRewardTips': 3110,
                'RewardDelay': 37 },
            1: {
                'Title': 3113,
                'CostTips': 3409,
                'CostType': NPC_OPTION_COST_HP,
                'InitCostFunc': OptionInitCostAction400401,
                'RewardTips': 3701,
                'RewardType': NPC_OPTION_REWARD_WARCASH,
                'InitRewardFunc': OptionInitRewardAction400401,
                'GainRewardTips': 3111,
                'RewardDelay': 37 },
            2: {
                'Title': 3113,
                'CostTips': 3409,
                'CostType': NPC_OPTION_COST_HP,
                'InitCostFunc': OptionInitCostAction400402,
                'RewardTips': 3701,
                'RewardType': NPC_OPTION_REWARD_WARCASH,
                'InitRewardFunc': OptionInitRewardAction400402,
                'GainRewardTips': 3112,
                'RewardDelay': 37 } } }


class CNpcEventData4005(CCustom):
    m_SID = 4005
    m_Titles = {
        1: 3008,
        2: 7182 }
    m_Event = {
        1: {
            0: {
                'Title': 3113,
                'CostTips': 3409,
                'CostType': NPC_OPTION_COST_HP,
                'InitCostFunc': OptionInitCostAction400500,
                'RewardTips': 3702,
                'RewardType': NPC_OPTION_REWARD_ATTR,
                'InitRewardFunc': OptionInitRewardAction400500,
                'GainRewardTips': 3130,
                'RewardDelay': 37 },
            1: {
                'Title': 3113,
                'CostTips': 3409,
                'CostType': NPC_OPTION_COST_HP,
                'InitCostFunc': OptionInitCostAction400501,
                'RewardTips': 3702,
                'RewardType': NPC_OPTION_REWARD_ATTR,
                'InitRewardFunc': OptionInitRewardAction400501,
                'GainRewardTips': 3130,
                'RewardDelay': 37 } },
        2: { } }


class CNpcEventData4006(CCustom):
    m_SID = 4006
    m_Titles = {
        1: 3008,
        2: 7182 }
    m_Event = {
        1: {
            0: {
                'Title': 3113,
                'CostTips': 3409,
                'CostType': NPC_OPTION_COST_HP,
                'InitCostFunc': OptionInitCostAction400600,
                'RewardTips': 3701,
                'RewardType': NPC_OPTION_REWARD_WARCASH,
                'InitRewardFunc': OptionInitRewardAction400600,
                'GainRewardTips': 3134,
                'RewardDelay': 37 },
            1: {
                'Title': 3113,
                'CostTips': 3409,
                'CostType': NPC_OPTION_COST_HP,
                'InitCostFunc': OptionInitCostAction400601,
                'RewardTips': 3704,
                'RewardType': NPC_OPTION_REWARD_RELIC,
                'InitRewardFunc': OptionInitRewardAction400601,
                'GainRewardTips': 3129,
                'RewardDelay': 37 },
            2: {
                'Title': 3113,
                'CostTips': 3409,
                'CostType': NPC_OPTION_COST_HP,
                'InitCostFunc': OptionInitCostAction400602,
                'RewardTips': 3707,
                'RewardType': NPC_OPTION_REWARD_WEAPON,
                'InitRewardFunc': OptionInitRewardAction400602,
                'GainRewardTips': 3129,
                'RewardDelay': 37 } },
        2: { } }


class CNpcEventData4007(CCustom):
    m_SID = 4007
    m_Titles = {
        1: 7128,
        2: 7154 }
    m_Event = {
        1: {
            0: {
                'Title': 7144,
                'CostTips': 3409,
                'CostType': NPC_OPTION_COST_HP,
                'InitCostFunc': OptionInitCostAction400700,
                'RewardTips': 7158,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction400700,
                'GainRewardTips': 7180,
                'RewardDelay': 37 },
            1: {
                'Title': 7144,
                'CostTips': 3409,
                'CostType': NPC_OPTION_COST_HP,
                'InitCostFunc': OptionInitCostAction400701,
                'RewardTips': 7158,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction400701,
                'GainRewardTips': 7180,
                'RewardDelay': 37 },
            2: {
                'Title': 7134,
                'CostTips': 3409,
                'CostType': NPC_OPTION_COST_HP,
                'InitCostFunc': OptionInitCostAction400702,
                'RewardTips': 7149,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction400702,
                'GainRewardTips': 7176,
                'RewardDelay': 37 },
            3: {
                'Title': 7134,
                'CostTips': 3409,
                'CostType': NPC_OPTION_COST_HP,
                'InitCostFunc': OptionInitCostAction400703,
                'RewardTips': 7149,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction400703,
                'GainRewardTips': 7176,
                'RewardDelay': 37 } },
        2: { } }


class CNpcEventData4008(CCustom):
    m_SID = 4008
    m_Titles = {
        1: 3006,
        2: 7151 }
    m_Event = {
        1: {
            0: {
                'Title': 7132,
                'CostTips': 3409,
                'CostType': NPC_OPTION_COST_HP,
                'InitCostFunc': OptionInitCostAction400800,
                'RewardTips': 7159,
                'RewardType': NPC_OPTION_REWARD_RELIC,
                'InitRewardFunc': OptionInitRewardAction400800,
                'GainRewardTips': 3103,
                'RewardDelay': 37 },
            1: {
                'Title': 7133,
                'CostTips': 3409,
                'CostType': NPC_OPTION_COST_HP,
                'InitCostFunc': OptionInitCostAction400801,
                'RewardTips': 7148,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction400801,
                'GainRewardTips': 7175,
                'RewardDelay': 37 },
            2: {
                'Title': 7133,
                'CostTips': 3409,
                'CostType': NPC_OPTION_COST_HP,
                'InitCostFunc': OptionInitCostAction400802,
                'RewardTips': 7148,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction400802,
                'GainRewardTips': 7175,
                'RewardDelay': 37 } },
        2: { } }


class CNpcEventData4010(CCustom):
    m_SID = 4010
    m_Titles = {
        1: 7127,
        2: 7153 }
    m_Event = {
        1: {
            0: {
                'Title': 7140,
                'CostTips': 3701,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction401000,
                'RewardTips': 7161,
                'RewardType': NPC_OPTION_REWARD_RELIC,
                'InitRewardFunc': OptionInitRewardAction401000,
                'GainRewardTips': 3103,
                'RewardDelay': 37 },
            1: {
                'Title': 7141,
                'CostTips': 3701,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction401001,
                'RewardTips': 7162,
                'RewardType': NPC_OPTION_REWARD_RELIC,
                'InitRewardFunc': OptionInitRewardAction401001,
                'GainRewardTips': 3103,
                'RewardDelay': 37 },
            2: {
                'Title': 7142,
                'CostTips': 3701,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction401002,
                'RewardTips': 7163,
                'RewardType': NPC_OPTION_REWARD_RELIC,
                'InitRewardFunc': OptionInitRewardAction401002,
                'GainRewardTips': 3103,
                'RewardDelay': 37 } },
        2: { } }


class CNpcEventData4011(CCustom):
    m_SID = 4011
    m_Titles = {
        1: 7131,
        2: 7156 }
    m_Event = {
        1: {
            0: {
                'Title': 7218,
                'CostTips': 3406,
                'CostType': NPC_OPTION_COST_RELIC,
                'InitCostFunc': OptionInitCostAction401100,
                'RewardTips': 3410,
                'RewardType': NPC_OPTION_REWARD_WARCASH,
                'InitRewardFunc': OptionInitRewardAction401100,
                'GainRewardTips': 3710,
                'RewardDelay': 37 } },
        2: { } }


class CNpcEventData4012(CCustom):
    m_SID = 4012
    m_Titles = {
        1: 3001 }
    m_Event = {
        1: {
            0: {
                'Title': 3123,
                'CostTips': 7179,
                'CostType': NPC_OPTION_COST_NONE,
                'InitCostFunc': None,
                'RewardTips': 3704,
                'RewardType': NPC_OPTION_REWARD_RELIC,
                'InitRewardFunc': OptionInitRewardAction401200,
                'GainRewardTips': 3103,
                'RewardDelay': 32 } } }


class CNpcEventData4013(CCustom):
    m_SID = 4013
    m_Titles = {
        1: 3008,
        2: 7182 }
    m_Event = {
        1: {
            0: {
                'Title': 3113,
                'CostTips': 3409,
                'CostType': NPC_OPTION_COST_HP,
                'InitCostFunc': OptionInitCostAction401300,
                'RewardTips': 3410,
                'RewardType': NPC_OPTION_REWARD_WARCASH,
                'InitRewardFunc': OptionInitRewardAction401300,
                'GainRewardTips': 0,
                'RewardDelay': 37 },
            1: {
                'Title': 3113,
                'CostTips': 3409,
                'CostType': NPC_OPTION_COST_HP,
                'InitCostFunc': OptionInitCostAction401301,
                'RewardTips': 3410,
                'RewardType': NPC_OPTION_REWARD_WARCASH,
                'InitRewardFunc': OptionInitRewardAction401301,
                'GainRewardTips': 0,
                'RewardDelay': 37 },
            2: {
                'Title': 3113,
                'CostTips': 3409,
                'CostType': NPC_OPTION_COST_HP,
                'InitCostFunc': OptionInitCostAction401302,
                'RewardTips': 3410,
                'RewardType': NPC_OPTION_REWARD_WARCASH,
                'InitRewardFunc': OptionInitRewardAction401302,
                'GainRewardTips': 0,
                'RewardDelay': 37 } },
        2: { } }


class CNpcEventData4014(CCustom):
    m_SID = 4014
    m_Titles = {
        1: 7126,
        2: 7152 }
    m_Event = {
        1: {
            0: {
                'Title': 7133,
                'CostTips': 3701,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction401400,
                'RewardTips': 7148,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction401400,
                'GainRewardTips': 7175,
                'RewardDelay': 37 },
            1: {
                'Title': 7133,
                'CostTips': 3701,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction401401,
                'RewardTips': 7148,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction401401,
                'GainRewardTips': 7175,
                'RewardDelay': 37 } },
        2: { } }


class CNpcEventData4015(CCustom):
    m_SID = 4015
    m_Titles = {
        1: 7126,
        2: 7152 }
    m_Event = {
        1: {
            0: {
                'Title': 7133,
                'CostTips': 3701,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction401500,
                'RewardTips': 7150,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction401500,
                'GainRewardTips': 7175,
                'RewardDelay': 37 },
            1: {
                'Title': 7133,
                'CostTips': 3701,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction401501,
                'RewardTips': 7150,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction401501,
                'GainRewardTips': 7175,
                'RewardDelay': 37 },
            2: {
                'Title': 7144,
                'CostTips': 3701,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction401502,
                'RewardTips': 7158,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction401502,
                'GainRewardTips': 7180,
                'RewardDelay': 37 },
            3: {
                'Title': 7144,
                'CostTips': 3701,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction401503,
                'RewardTips': 7158,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction401503,
                'GainRewardTips': 7180,
                'RewardDelay': 37 } },
        2: { } }


class CNpcEventData4101(CCustom):
    m_SID = 4101
    m_Titles = {
        1: 3008,
        2: 7182 }
    m_Event = {
        1: {
            0: {
                'Title': 3180,
                'CostTips': 3409,
                'CostType': NPC_OPTION_COST_HP,
                'InitCostFunc': OptionInitCostAction410100,
                'RewardTips': 3717,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction410100,
                'GainRewardTips': 7176,
                'RewardDelay': 37 },
            1: {
                'Title': 3181,
                'CostTips': 3409,
                'CostType': NPC_OPTION_COST_HP,
                'InitCostFunc': OptionInitCostAction410101,
                'RewardTips': 3711,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction410101,
                'GainRewardTips': 7175,
                'RewardDelay': 37 },
            2: {
                'Title': 3182,
                'CostTips': 3409,
                'CostType': NPC_OPTION_COST_HP,
                'InitCostFunc': OptionInitCostAction410102,
                'RewardTips': 3712,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction410102,
                'GainRewardTips': 7180,
                'RewardDelay': 37 } },
        2: { } }


class CNpcEventData4102(CCustom):
    m_SID = 4102
    m_Titles = {
        1: 3008,
        2: 7182 }
    m_Event = {
        1: {
            0: {
                'Title': 3177,
                'CostTips': 3409,
                'CostType': NPC_OPTION_COST_HP,
                'InitCostFunc': OptionInitCostAction410200,
                'RewardTips': 3713,
                'RewardType': NPC_OPTION_REWARD_RELIC,
                'InitRewardFunc': OptionInitRewardAction410200,
                'GainRewardTips': 3103,
                'RewardDelay': 37 },
            1: {
                'Title': 3177,
                'CostTips': 3409,
                'CostType': NPC_OPTION_COST_HP,
                'InitCostFunc': OptionInitCostAction410201,
                'RewardTips': 3725,
                'RewardType': NPC_OPTION_REWARD_RELIC,
                'InitRewardFunc': OptionInitRewardAction410201,
                'GainRewardTips': 3103,
                'RewardDelay': 37 },
            2: {
                'Title': 3181,
                'CostTips': 3409,
                'CostType': NPC_OPTION_COST_HP,
                'InitCostFunc': OptionInitCostAction410202,
                'RewardTips': 3716,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction410202,
                'GainRewardTips': 3141,
                'RewardDelay': 37 } },
        2: { } }


class CNpcEventData4103(CCustom):
    m_SID = 4103
    m_Titles = {
        1: 3016,
        2: 7156 }
    m_Event = {
        1: {
            0: {
                'Title': 3149,
                'CostTips': 3701,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction410300,
                'RewardTips': 3713,
                'RewardType': NPC_OPTION_REWARD_RELIC,
                'InitRewardFunc': OptionInitRewardAction410300,
                'GainRewardTips': 3103,
                'RewardDelay': 37 },
            1: {
                'Title': 3150,
                'CostTips': 3701,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction410301,
                'RewardTips': 3714,
                'RewardType': NPC_OPTION_REWARD_RELIC,
                'InitRewardFunc': OptionInitRewardAction410301,
                'GainRewardTips': 3103,
                'RewardDelay': 37 },
            2: {
                'Title': 3151,
                'CostTips': 3701,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction410302,
                'RewardTips': 3715,
                'RewardType': NPC_OPTION_REWARD_RELIC,
                'InitRewardFunc': OptionInitRewardAction410302,
                'GainRewardTips': 3103,
                'RewardDelay': 37 } },
        2: { } }


class CNpcEventData4104(CCustom):
    m_SID = 4104
    m_Titles = {
        1: 7126,
        2: 7152 }
    m_Event = {
        1: {
            0: {
                'Title': 3167,
                'CostTips': 3701,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction410400,
                'RewardTips': 3717,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction410400,
                'GainRewardTips': 7176,
                'RewardDelay': 37 },
            1: {
                'Title': 3164,
                'CostTips': 3701,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction410401,
                'RewardTips': 3716,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction410401,
                'GainRewardTips': 3141,
                'RewardDelay': 37 },
            2: {
                'Title': 3165,
                'CostTips': 3701,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction410402,
                'RewardTips': 3712,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction410402,
                'GainRewardTips': 7180,
                'RewardDelay': 37 } },
        2: { } }


class CNpcEventData4105(CCustom):
    m_SID = 4105
    m_Titles = {
        1: 7126,
        2: 7152 }
    m_Event = {
        1: {
            0: {
                'Title': 3167,
                'CostTips': 3701,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction410500,
                'RewardTips': 3707,
                'RewardType': NPC_OPTION_REWARD_WEAPON,
                'InitRewardFunc': OptionInitRewardAction410500,
                'GainRewardTips': 3131,
                'RewardDelay': 37 },
            1: {
                'Title': 3164,
                'CostTips': 3701,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction410501,
                'RewardTips': 3711,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction410501,
                'GainRewardTips': 7175,
                'RewardDelay': 37 },
            2: {
                'Title': 3165,
                'CostTips': 3701,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction410502,
                'RewardTips': 3712,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction410502,
                'GainRewardTips': 7180,
                'RewardDelay': 37 } },
        2: { } }


class CNpcEventData9001(CCustom):
    m_SID = 9001
    m_Titles = {
        1: 9002 }
    m_Event = {
        1: {
            0: {
                'Title': 3113,
                'CostTips': 3409,
                'CostType': NPC_OPTION_COST_HP,
                'InitCostFunc': OptionInitCostAction900100,
                'RewardTips': 3701,
                'RewardType': NPC_OPTION_REWARD_WARCASH,
                'InitRewardFunc': OptionInitRewardAction900100,
                'GainRewardTips': 3134,
                'RewardDelay': 37 },
            1: {
                'Title': 3113,
                'CostTips': 3409,
                'CostType': NPC_OPTION_COST_HP,
                'InitCostFunc': OptionInitCostAction900101,
                'RewardTips': 3704,
                'RewardType': NPC_OPTION_REWARD_WARCASH,
                'InitRewardFunc': OptionInitRewardAction900101,
                'GainRewardTips': 3134,
                'RewardDelay': 37 } } }


class CNpcEventData9002(CCustom):
    m_SID = 9002
    m_Titles = {
        1: 9003 }
    m_Event = {
        1: {
            0: {
                'Title': 9003,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction900200,
                'RewardTips': 7158,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction900200,
                'GainRewardTips': 7180,
                'RewardDelay': 37 },
            1: {
                'Title': 9003,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction900201,
                'RewardTips': 7158,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction900201,
                'GainRewardTips': 7180,
                'RewardDelay': 37 } } }


class CNpcEventData9003(CCustom):
    m_SID = 9003
    m_Titles = {
        1: 9004 }
    m_Event = {
        1: {
            0: {
                'Title': 9004,
                'CostTips': 3404,
                'CostType': NPC_OPTION_COST_ATTR,
                'InitCostFunc': OptionInitCostAction900300,
                'RewardTips': 3701,
                'RewardType': NPC_OPTION_REWARD_WARCASH,
                'InitRewardFunc': OptionInitRewardAction900300,
                'GainRewardTips': 0,
                'RewardDelay': 0 },
            1: {
                'Title': 9004,
                'CostTips': 3405,
                'CostType': NPC_OPTION_COST_RELIC,
                'InitCostFunc': OptionInitCostAction900301,
                'RewardTips': 3701,
                'RewardType': NPC_OPTION_REWARD_WARCASH,
                'InitRewardFunc': OptionInitRewardAction900301,
                'GainRewardTips': 0,
                'RewardDelay': 0 },
            2: {
                'Title': 9004,
                'CostTips': 3403,
                'CostType': NPC_OPTION_COST_ATTR,
                'InitCostFunc': OptionInitCostAction900302,
                'RewardTips': 3701,
                'RewardType': NPC_OPTION_REWARD_WARCASH,
                'InitRewardFunc': OptionInitRewardAction900302,
                'GainRewardTips': 0,
                'RewardDelay': 0 } } }


class CNpcEventData9004(CCustom):
    m_SID = 9004
    m_Titles = {
        1: 9005 }
    m_Event = {
        1: {
            0: {
                'Title': 7140,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction900400,
                'RewardTips': 7161,
                'RewardType': NPC_OPTION_REWARD_RELIC,
                'InitRewardFunc': OptionInitRewardAction900400,
                'GainRewardTips': 3103,
                'RewardDelay': 32 },
            1: {
                'Title': 7141,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction900401,
                'RewardTips': 9104,
                'RewardType': NPC_OPTION_REWARD_RELIC,
                'InitRewardFunc': OptionInitRewardAction900401,
                'GainRewardTips': 3103,
                'RewardDelay': 32 },
            2: {
                'Title': 7142,
                'CostTips': 3401,
                'CostType': NPC_OPTION_COST_WARCASH,
                'InitCostFunc': OptionInitCostAction900402,
                'RewardTips': 7163,
                'RewardType': NPC_OPTION_REWARD_RELIC,
                'InitRewardFunc': OptionInitRewardAction900402,
                'GainRewardTips': 3103,
                'RewardDelay': 32 } } }


class CNpcEventData9005(CCustom):
    m_SID = 9005
    m_Titles = {
        1: 9006 }
    m_Event = {
        1: {
            0: {
                'Title': 9006,
                'CostTips': 3406,
                'CostType': NPC_OPTION_COST_RELIC,
                'InitCostFunc': OptionInitCostAction900500,
                'RewardTips': 7167,
                'RewardType': NPC_OPTION_REWARD_HP,
                'InitRewardFunc': OptionInitRewardAction900500,
                'GainRewardTips': 7178,
                'RewardDelay': 32 },
            1: {
                'Title': 9006,
                'CostTips': 3408,
                'CostType': NPC_OPTION_COST_CURSERELIC,
                'InitCostFunc': OptionInitCostAction900501,
                'RewardTips': 7167,
                'RewardType': NPC_OPTION_REWARD_HP,
                'InitRewardFunc': OptionInitRewardAction900501,
                'GainRewardTips': 7178,
                'RewardDelay': 32 } } }


class CNpcEventData9006(CCustom):
    m_SID = 9006
    m_Titles = {
        1: 9007 }
    m_Event = {
        1: {
            0: {
                'Title': 9007,
                'CostTips': 7179,
                'CostType': NPC_OPTION_COST_NONE,
                'InitCostFunc': None,
                'RewardTips': 7167,
                'RewardType': NPC_OPTION_REWARD_HP,
                'InitRewardFunc': OptionInitRewardAction900600,
                'GainRewardTips': 7178,
                'RewardDelay': 0 },
            1: {
                'Title': 9007,
                'CostTips': 7179,
                'CostType': NPC_OPTION_COST_NONE,
                'InitCostFunc': None,
                'RewardTips': 3702,
                'RewardType': NPC_OPTION_REWARD_ATTR,
                'InitRewardFunc': OptionInitRewardAction900601,
                'GainRewardTips': 3130,
                'RewardDelay': 0 },
            2: {
                'Title': 9007,
                'CostTips': 7179,
                'CostType': NPC_OPTION_COST_NONE,
                'InitCostFunc': None,
                'RewardTips': 7148,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction900602,
                'GainRewardTips': 7201,
                'RewardDelay': 0 },
            3: {
                'Title': 9007,
                'CostTips': 7179,
                'CostType': NPC_OPTION_COST_NONE,
                'InitCostFunc': None,
                'RewardTips': 7148,
                'RewardType': NPC_OPTION_REWARD_WEAPONACTION,
                'InitRewardFunc': OptionInitRewardAction900603,
                'GainRewardTips': 7201,
                'RewardDelay': 0 } } }

g_AllEvent = {
    1001: CNpcEventData1001,
    1002: CNpcEventData1002,
    1003: CNpcEventData1003,
    1004: CNpcEventData1004,
    1005: CNpcEventData1005,
    1006: CNpcEventData1006,
    1007: CNpcEventData1007,
    1008: CNpcEventData1008,
    1009: CNpcEventData1009,
    1010: CNpcEventData1010,
    1011: CNpcEventData1011,
    1012: CNpcEventData1012,
    1013: CNpcEventData1013,
    1014: CNpcEventData1014,
    1015: CNpcEventData1015,
    1016: CNpcEventData1016,
    1017: CNpcEventData1017,
    1018: CNpcEventData1018,
    1019: CNpcEventData1019,
    1020: CNpcEventData1020,
    1021: CNpcEventData1021,
    1022: CNpcEventData1022,
    1023: CNpcEventData1023,
    1024: CNpcEventData1024,
    1101: CNpcEventData1101,
    1102: CNpcEventData1102,
    1103: CNpcEventData1103,
    1104: CNpcEventData1104,
    1105: CNpcEventData1105,
    1106: CNpcEventData1106,
    1107: CNpcEventData1107,
    1108: CNpcEventData1108,
    1109: CNpcEventData1109,
    1110: CNpcEventData1110,
    1111: CNpcEventData1111,
    1112: CNpcEventData1112,
    1113: CNpcEventData1113,
    2001: CNpcEventData2001,
    2002: CNpcEventData2002,
    2003: CNpcEventData2003,
    2004: CNpcEventData2004,
    2005: CNpcEventData2005,
    2006: CNpcEventData2006,
    2007: CNpcEventData2007,
    2008: CNpcEventData2008,
    2009: CNpcEventData2009,
    2010: CNpcEventData2010,
    2011: CNpcEventData2011,
    2012: CNpcEventData2012,
    2013: CNpcEventData2013,
    2014: CNpcEventData2014,
    2015: CNpcEventData2015,
    2101: CNpcEventData2101,
    2102: CNpcEventData2102,
    2103: CNpcEventData2103,
    2104: CNpcEventData2104,
    2105: CNpcEventData2105,
    2106: CNpcEventData2106,
    2107: CNpcEventData2107,
    2108: CNpcEventData2108,
    2110: CNpcEventData2110,
    2112: CNpcEventData2112,
    2113: CNpcEventData2113,
    2114: CNpcEventData2114,
    2115: CNpcEventData2115,
    2116: CNpcEventData2116,
    2117: CNpcEventData2117,
    2118: CNpcEventData2118,
    2119: CNpcEventData2119,
    2120: CNpcEventData2120,
    2121: CNpcEventData2121,
    2122: CNpcEventData2122,
    2123: CNpcEventData2123,
    2201: CNpcEventData2201,
    2202: CNpcEventData2202,
    2204: CNpcEventData2204,
    2205: CNpcEventData2205,
    2206: CNpcEventData2206,
    2301: CNpcEventData2301,
    2302: CNpcEventData2302,
    3101: CNpcEventData3101,
    3102: CNpcEventData3102,
    3103: CNpcEventData3103,
    3105: CNpcEventData3105,
    3112: CNpcEventData3112,
    3113: CNpcEventData3113,
    3115: CNpcEventData3115,
    3116: CNpcEventData3116,
    3117: CNpcEventData3117,
    3118: CNpcEventData3118,
    3119: CNpcEventData3119,
    3121: CNpcEventData3121,
    3122: CNpcEventData3122,
    3201: CNpcEventData3201,
    3202: CNpcEventData3202,
    3203: CNpcEventData3203,
    3205: CNpcEventData3205,
    3212: CNpcEventData3212,
    3213: CNpcEventData3213,
    3215: CNpcEventData3215,
    3216: CNpcEventData3216,
    3217: CNpcEventData3217,
    3218: CNpcEventData3218,
    3221: CNpcEventData3221,
    3222: CNpcEventData3222,
    3223: CNpcEventData3223,
    3224: CNpcEventData3224,
    4001: CNpcEventData4001,
    4002: CNpcEventData4002,
    4003: CNpcEventData4003,
    4004: CNpcEventData4004,
    4005: CNpcEventData4005,
    4006: CNpcEventData4006,
    4007: CNpcEventData4007,
    4008: CNpcEventData4008,
    4010: CNpcEventData4010,
    4011: CNpcEventData4011,
    4012: CNpcEventData4012,
    4013: CNpcEventData4013,
    4014: CNpcEventData4014,
    4015: CNpcEventData4015,
    4101: CNpcEventData4101,
    4102: CNpcEventData4102,
    4103: CNpcEventData4103,
    4104: CNpcEventData4104,
    4105: CNpcEventData4105,
    9001: CNpcEventData9001,
    9002: CNpcEventData9002,
    9003: CNpcEventData9003,
    9004: CNpcEventData9004,
    9005: CNpcEventData9005,
    9006: CNpcEventData9006 }
