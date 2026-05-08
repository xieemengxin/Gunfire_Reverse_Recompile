# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/pfai/pfai21022.pyc
# RelativePath: clientlogic/cl_platformdata/pc/pfai/pfai21022.pyc
# Source Generated with Decompyle++
# File: pfai21022.pyc (Python 3.6)

import cl_betree.pfai.mobject as pfaiobj
import cl_condition
from cl_commondefines import MONSTER_PFAI_CATCH, MONSTER_PFAI_DODGE, PF_GROUP_CHECK_FIRST

def Condition38012(oOwner, dInfo):
    return cl_condition.AICheckHasState(oOwner, dInfo, 7013)


def Condition21021(oOwner, dInfo):
    return cl_condition.AICheckHasState(oOwner, dInfo, 7012) == 1


def Condition21022(oOwner, dInfo):
    return cl_condition.AICheckHasState(oOwner, dInfo, 7012) == 1


def Condition21023(oOwner, dInfo):
    return cl_condition.AICheckHasState(oOwner, dInfo, 7013) == 1


def Condition21024(oOwner, dInfo):
    return cl_condition.AICheckHasState(oOwner, dInfo, 7013) == 1


class CPerformAI(pfaiobj.CBasePerformAI):
    m_SID = 21022
    m_Name = '<二周目>小型远程-小型盾兵'
    m_FillBulletData = (38012, 4, 50)
    m_UseBulletPF = (21021, 21022, 21023, 21024)
    m_PFGroup = {
        1001: {
            0: [
                21021,
                1,
                1,
                0] },
        1002: {
            0: [
                38012,
                1,
                1,
                0] },
        1003: {
            0: [
                21022,
                1,
                1,
                0] },
        1004: {
            0: [
                21023,
                1,
                1,
                0] },
        1005: {
            0: [
                21024,
                1,
                1,
                0] } }
    m_GroupOfPF = {
        21021: [
            1001],
        38012: [
            1002],
        21022: [
            1003],
        21023: [
            1004],
        21024: [
            1005] }
    m_ChoosePFInfo = {
        MONSTER_PFAI_DODGE: { },
        MONSTER_PFAI_CATCH: {
            (0, 99, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1001: 10,
                        1003: 10,
                        1004: 15,
                        1005: 15 } }] } }
    m_CheckPFCanUse = {
        38012: Condition38012,
        21021: Condition21021,
        21022: Condition21022,
        21023: Condition21023,
        21024: Condition21024 }
    m_PFGroupCheck = {
        1001: PF_GROUP_CHECK_FIRST,
        1002: PF_GROUP_CHECK_FIRST,
        1003: PF_GROUP_CHECK_FIRST,
        1004: PF_GROUP_CHECK_FIRST,
        1005: PF_GROUP_CHECK_FIRST }

