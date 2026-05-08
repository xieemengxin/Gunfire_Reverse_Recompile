# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/pfai/pfai20221.pyc
# RelativePath: clientlogic/cl_platformdata/pc/pfai/pfai20221.pyc
# Source Generated with Decompyle++
# File: pfai20221.pyc (Python 3.6)

import cl_betree.pfai.mobject as pfaiobj
import cl_condition
from cl_commondefines import MONSTER_PFAI_CATCH, MONSTER_PFAI_DODGE, PF_GROUP_CHECK_FIRST

def Condition20225(oOwner, dInfo):
    return oOwner.Phase() == 1


def Condition7109(oOwner, dInfo):
    return oOwner.Phase() == 1


def Condition7110(oOwner, dInfo):
    return oOwner.Phase() == 1


def Condition38018(oOwner, dInfo):
    return oOwner.Phase() == 1


class CPerformAI(pfaiobj.CBasePerformAI):
    m_SID = 20221
    m_Name = '召唤四足兽'
    m_FillBulletData = ()
    m_UseBulletPF = ()
    m_PFGroup = {
        1001: {
            0: [
                20221,
                1,
                1,
                0] },
        1002: {
            0: [
                20222,
                1,
                1,
                0] },
        1003: {
            0: [
                20223,
                1,
                1,
                0] },
        1004: {
            0: [
                38028,
                1,
                1,
                0] },
        1005: {
            0: [
                38029,
                1,
                1,
                0] },
        1006: {
            0: [
                20221,
                1,
                1,
                0],
            1: [
                20221,
                1,
                1,
                0] },
        1007: {
            0: [
                20221,
                1,
                1,
                0],
            1: [
                20221,
                1,
                1,
                0],
            2: [
                20221,
                1,
                1,
                0] },
        1008: {
            0: [
                20222,
                1,
                1,
                0],
            1: [
                20223,
                1,
                1,
                0] },
        1009: {
            0: [
                20225,
                1,
                1,
                0] } }
    m_GroupOfPF = {
        20221: [
            1001,
            1006,
            1007],
        20222: [
            1002,
            1008],
        20223: [
            1003,
            1008],
        38028: [
            1004],
        38029: [
            1005],
        20225: [
            1009] }
    m_ChoosePFInfo = {
        MONSTER_PFAI_DODGE: {
            (0, 99, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1004: 10 },
                    'angle': (0, 180) },
                {
                    'choose': {
                        1005: 10 },
                    'angle': (-180, 0) }] },
        MONSTER_PFAI_CATCH: {
            (0, 4, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1003: 100,
                        1006: 10 } }],
            (4, 8, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1008: 60,
                        1003: 40,
                        1006: 10 } }],
            (8, 12, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1001: 35,
                        1006: 65 } }],
            (12, 99, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1006: 55,
                        1007: 45 } }] } }
    m_CheckPFCanUse = {
        20225: Condition20225,
        7109: Condition7109,
        7110: Condition7110,
        38018: Condition38018 }
    m_PFGroupCheck = {
        1001: PF_GROUP_CHECK_FIRST,
        1002: PF_GROUP_CHECK_FIRST,
        1003: PF_GROUP_CHECK_FIRST,
        1004: PF_GROUP_CHECK_FIRST,
        1005: PF_GROUP_CHECK_FIRST,
        1006: PF_GROUP_CHECK_FIRST,
        1007: PF_GROUP_CHECK_FIRST,
        1008: PF_GROUP_CHECK_FIRST,
        1009: PF_GROUP_CHECK_FIRST }

