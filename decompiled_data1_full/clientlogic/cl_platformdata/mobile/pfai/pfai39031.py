# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/pfai/pfai39031.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/pfai/pfai39031.pyc
# Source Generated with Decompyle++
# File: pfai39031.pyc (Python 3.6)

import cl_betree.pfai.mobject as pfaiobj
import cl_condition
from cl_commondefines import MONSTER_PFAI_CATCH, MONSTER_PFAI_DODGE, PF_GROUP_CHECK_FIRST

def Condition39033(oOwner, dInfo):
    return oOwner.Phase() == 1


def Condition39034(oOwner, dInfo):
    return oOwner.Phase() == 1


def Condition39035(oOwner, dInfo):
    return oOwner.Phase() == 1


def Condition39036(oOwner, dInfo):
    return oOwner.Phase() == 2


def Condition39037(oOwner, dInfo):
    return oOwner.Phase() == 2


def Condition39038(oOwner, dInfo):
    return oOwner.Phase() == 2


class CPerformAI(pfaiobj.CBasePerformAI):
    m_SID = 39031
    m_Name = 'boss-第二幕'
    m_FillBulletData = ()
    m_UseBulletPF = ()
    m_PFGroup = {
        1003: {
            0: [
                39033,
                1,
                1,
                0] },
        1004: {
            0: [
                39034,
                1,
                1,
                0] },
        1005: {
            0: [
                39035,
                1,
                1,
                0] },
        1006: {
            0: [
                39036,
                1,
                1,
                0] },
        1007: {
            0: [
                39037,
                1,
                1,
                0] },
        1008: {
            0: [
                39038,
                1,
                1,
                0] },
        1009: {
            0: [
                39039,
                1,
                1,
                0] },
        1010: {
            0: [
                39040,
                1,
                1,
                0] },
        1011: {
            0: [
                39041,
                1,
                1,
                0] },
        1012: {
            0: [
                39034,
                1,
                1,
                0],
            1: [
                39035,
                1,
                1,
                50] },
        1013: {
            0: [
                39035,
                1,
                1,
                0],
            1: [
                39034,
                1,
                1,
                50] } }
    m_GroupOfPF = {
        39033: [
            1003],
        39034: [
            1004,
            1012,
            1013],
        39035: [
            1005,
            1012,
            1013],
        39036: [
            1006],
        39037: [
            1007],
        39038: [
            1008],
        39039: [
            1009],
        39040: [
            1010],
        39041: [
            1011] }
    m_ChoosePFInfo = {
        MONSTER_PFAI_DODGE: { },
        MONSTER_PFAI_CATCH: {
            (12, 99, -1, 100, -1, 35, 0): [
                {
                    'choose': {
                        1008: 10,
                        1007: 10,
                        1004: 10,
                        1005: 10 } }],
            (12, 99, -1, 100, 35, 65, 0): [
                {
                    'choose': {
                        1004: 10,
                        1008: 10,
                        1007: 10,
                        1005: 10,
                        1012: 10,
                        1013: 10 } }],
            (0, 12, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1003: 10,
                        1008: 10 } }],
            (12, 99, -1, 100, 65, 100, 0): [
                {
                    'choose': {
                        1012: 10,
                        1008: 5,
                        1007: 5,
                        1013: 10 } }] } }
    m_CheckPFCanUse = {
        39033: Condition39033,
        39034: Condition39034,
        39035: Condition39035,
        39036: Condition39036,
        39037: Condition39037,
        39038: Condition39038 }
    m_PFGroupCheck = {
        1003: PF_GROUP_CHECK_FIRST,
        1004: PF_GROUP_CHECK_FIRST,
        1005: PF_GROUP_CHECK_FIRST,
        1006: PF_GROUP_CHECK_FIRST,
        1007: PF_GROUP_CHECK_FIRST,
        1008: PF_GROUP_CHECK_FIRST,
        1009: PF_GROUP_CHECK_FIRST,
        1010: PF_GROUP_CHECK_FIRST,
        1011: PF_GROUP_CHECK_FIRST,
        1012: PF_GROUP_CHECK_FIRST,
        1013: PF_GROUP_CHECK_FIRST }

