# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/pfai/pfai31421.pyc
# RelativePath: clientlogic/cl_platformdata/pc/pfai/pfai31421.pyc
# Source Generated with Decompyle++
# File: pfai31421.pyc (Python 3.6)

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


def Condition31424(oOwner, dInfo):
    return cl_condition.GetSceneAliveMonsterCnt(oOwner, dInfo, 20221) <= 2


class CPerformAI(pfaiobj.CBasePerformAI):
    m_SID = 31421
    m_Name = '【第二幕】精英中型远程'
    m_FillBulletData = ()
    m_UseBulletPF = ()
    m_PFGroup = {
        1001: {
            0: [
                31421,
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
                31422,
                1,
                1,
                0] },
        1004: {
            0: [
                31423,
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
                0] },
        1007: {
            0: [
                31424,
                3,
                3,
                0] },
        1008: {
            0: [
                31424,
                2,
                2,
                0] },
        1010: {
            0: [
                31425,
                1,
                1,
                0] },
        1011: {
            0: [
                31422,
                1,
                1,
                0],
            1: [
                31424,
                2,
                2,
                0] },
        1012: {
            0: [
                31425,
                1,
                1,
                0],
            1: [
                31424,
                2,
                2,
                0] },
        1013: {
            0: [
                31425,
                1,
                1,
                0],
            1: [
                31421,
                1,
                1,
                0] } }
    m_GroupOfPF = {
        31421: [
            1001,
            1013],
        38018: [
            1002],
        31422: [
            1003,
            1011],
        31423: [
            1004],
        38028: [
            1005],
        38029: [
            1006],
        31424: [
            1007,
            1008,
            1011,
            1012],
        31425: [
            1010,
            1012,
            1013] }
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
            (10, 99, -1, 100, -1, 50, 0): [
                {
                    'choose': {
                        1001: 5,
                        1010: 15,
                        1012: 25,
                        1013: 25,
                        1007: 10 } }],
            (10, 99, -1, 100, 50, 100, 0): [
                {
                    'choose': {
                        1001: 20,
                        1010: 25,
                        1012: 10,
                        1013: 10,
                        1008: 5 } }],
            (5, 10, -1, 100, -1, 50, 0): [
                {
                    'choose': {
                        1007: 20,
                        1011: 15,
                        1012: 10 } }],
            (5, 10, -1, 100, 50, 100, 0): [
                {
                    'choose': {
                        1003: 3,
                        1007: 10,
                        1008: 15,
                        1010: 15 } }],
            (0, 5, -1, 100, -1, 50, 0): [
                {
                    'choose': {
                        1003: 15,
                        1011: 25 } }],
            (0, 5, -1, 100, 50, 100, 0): [
                {
                    'choose': {
                        1003: 20,
                        1011: 15 } }] } }
    m_CheckPFCanUse = {
        21423: Condition21423,
        7109: Condition7109,
        7110: Condition7110,
        38018: Condition38018,
        31424: Condition31424 }
    m_PFGroupCheck = {
        1001: PF_GROUP_CHECK_FIRST,
        1002: PF_GROUP_CHECK_FIRST,
        1003: PF_GROUP_CHECK_FIRST,
        1004: PF_GROUP_CHECK_FIRST,
        1005: PF_GROUP_CHECK_FIRST,
        1006: PF_GROUP_CHECK_FIRST,
        1007: PF_GROUP_CHECK_FIRST,
        1008: PF_GROUP_CHECK_FIRST,
        1010: PF_GROUP_CHECK_FIRST,
        1011: PF_GROUP_CHECK_FIRST,
        1012: PF_GROUP_CHECK_FIRST,
        1013: PF_GROUP_CHECK_FIRST }

