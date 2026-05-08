# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/pfai/pfai33811.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/pfai/pfai33811.pyc
# Source Generated with Decompyle++
# File: pfai33811.pyc (Python 3.6)

import cl_betree.pfai.mobject as pfaiobj
import cl_condition
from cl_commondefines import MONSTER_PFAI_CATCH, MONSTER_PFAI_DODGE, PF_GROUP_CHECK_FIRST

def Condition33812(oOwner, dInfo):
    return oOwner.Phase() == 1


def Condition33814(oOwner, dInfo):
    return oOwner.Phase() == 1


def Condition33815(oOwner, dInfo):
    return oOwner.Phase() == 1


def Condition33811(oOwner, dInfo):
    return oOwner.Phase() == 2


def Condition33817(oOwner, dInfo):
    return oOwner.Phase() == 2


class CPerformAI(pfaiobj.CBasePerformAI):
    m_SID = 33811
    m_Name = '精英骑乘怪'
    m_FillBulletData = ()
    m_UseBulletPF = ()
    m_PFGroup = {
        1001: {
            0: [
                33812,
                1,
                1,
                0] },
        1002: {
            0: [
                33814,
                1,
                1,
                0] },
        1003: {
            0: [
                33815,
                1,
                1,
                0] },
        2001: {
            0: [
                33811,
                1,
                1,
                0] },
        2002: {
            0: [
                33817,
                1,
                1,
                0] } }
    m_GroupOfPF = {
        33812: [
            1001],
        33814: [
            1002],
        33815: [
            1003],
        33811: [
            2001],
        33817: [
            2002] }
    m_ChoosePFInfo = {
        MONSTER_PFAI_DODGE: { },
        MONSTER_PFAI_CATCH: {
            (4, 99, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1001: 9999,
                        1002: 100,
                        2001: 10,
                        1003: 1 } }],
            (0, 4, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1003: 10,
                        2001: 10 } }] } }
    m_CheckPFCanUse = {
        33812: Condition33812,
        33814: Condition33814,
        33815: Condition33815,
        33811: Condition33811,
        33817: Condition33817 }
    m_PFGroupCheck = {
        1001: PF_GROUP_CHECK_FIRST,
        1002: PF_GROUP_CHECK_FIRST,
        1003: PF_GROUP_CHECK_FIRST,
        2001: PF_GROUP_CHECK_FIRST,
        2002: PF_GROUP_CHECK_FIRST }

