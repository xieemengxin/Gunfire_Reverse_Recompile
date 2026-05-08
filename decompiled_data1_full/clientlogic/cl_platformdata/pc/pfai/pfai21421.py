# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/pfai/pfai21421.pyc
# RelativePath: clientlogic/cl_platformdata/pc/pfai/pfai21421.pyc
# Source Generated with Decompyle++
# File: pfai21421.pyc (Python 3.6)

import cl_betree.pfai.mobject as pfaiobj
import cl_condition
from cl_commondefines import MONSTER_PFAI_CATCH, MONSTER_PFAI_DODGE, PF_GROUP_CHECK_FIRST

def Condition21423(oOwner, dInfo):
    return oOwner.Phase() == 1


def Condition7109(oOwner, dInfo):
    return oOwner.Phase() == 1


def Condition7110(oOwner, dInfo):
    return oOwner.Phase() == 1


def Condition38018(oOwner, dInfo):
    return oOwner.Phase() == 1


class CPerformAI(pfaiobj.CBasePerformAI):
    m_SID = 21421
    m_Name = '中型远程-隐身远程怪'
    m_FillBulletData = (38018, 15, 3)
    m_UseBulletPF = (21421,)
    m_PFGroup = {
        1001: {
            0: [
                21421,
                1,
                1,
                0] },
        1002: {
            0: [
                38018,
                1,
                1,
                0] },
        1003: {
            0: [
                21422,
                1,
                1,
                0] },
        1004: {
            0: [
                21423,
                1,
                1,
                0] },
        1005: {
            0: [
                38028,
                1,
                1,
                0] },
        1006: {
            0: [
                38029,
                1,
                1,
                0] } }
    m_GroupOfPF = {
        21421: [
            1001],
        38018: [
            1002],
        21422: [
            1003],
        21423: [
            1004],
        38028: [
            1005],
        38029: [
            1006] }
    m_ChoosePFInfo = {
        MONSTER_PFAI_DODGE: {
            (0, 99, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1005: 10 },
                    'angle': (0, 180) },
                {
                    'choose': {
                        1006: 10 },
                    'angle': (-180, 0) }] },
        MONSTER_PFAI_CATCH: {
            (5, 45, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1001: 10 } }],
            (0, 5, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1003: 10 } }] } }
    m_CheckPFCanUse = {
        21423: Condition21423,
        7109: Condition7109,
        7110: Condition7110,
        38018: Condition38018 }
    m_PFGroupCheck = {
        1001: PF_GROUP_CHECK_FIRST,
        1002: PF_GROUP_CHECK_FIRST,
        1003: PF_GROUP_CHECK_FIRST,
        1004: PF_GROUP_CHECK_FIRST,
        1005: PF_GROUP_CHECK_FIRST,
        1006: PF_GROUP_CHECK_FIRST }

