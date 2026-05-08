# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/pfai/pfai21123.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/pfai/pfai21123.pyc
# Source Generated with Decompyle++
# File: pfai21123.pyc (Python 3.6)

import cl_betree.pfai.mobject as pfaiobj
import cl_condition
from cl_commondefines import MONSTER_PFAI_CATCH, MONSTER_PFAI_DODGE, PF_GROUP_CHECK_FIRST

def Condition21122(oOwner, dInfo):
    return cl_condition.AICheckHasState(oOwner, dInfo, 8135) == 1


class CPerformAI(pfaiobj.CBasePerformAI):
    m_SID = 21123
    m_Name = '<三周目>【第三幕】小型远程-毒系持盾远程怪'
    m_FillBulletData = (38012, 4, 50)
    m_UseBulletPF = (21061, 21062)
    m_PFGroup = {
        1001: {
            0: [
                21121,
                1,
                2,
                12] },
        1002: {
            0: [
                21121,
                2,
                3,
                12] },
        1003: {
            0: [
                21121,
                3,
                4,
                12] },
        1004: {
            0: [
                38017,
                1,
                1,
                0] },
        1005: {
            0: [
                38031,
                1,
                1,
                0] },
        1006: {
            0: [
                38032,
                1,
                1,
                0] },
        1007: {
            0: [
                21122,
                1,
                1,
                0] },
        1008: {
            0: [
                21124,
                1,
                1,
                0] },
        1009: {
            0: [
                21123,
                1,
                1,
                0] } }
    m_GroupOfPF = {
        21121: [
            1001,
            1002,
            1003],
        38017: [
            1004],
        38031: [
            1005],
        38032: [
            1006],
        21122: [
            1007],
        21124: [
            1008],
        21123: [
            1009] }
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
            (10, 99, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1003: 10,
                        1007: 18 } }],
            (5, 10, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1002: 10,
                        1007: 18 } }],
            (0, 5, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1001: 10,
                        1007: 18,
                        1008: 0 } }] } }
    m_CheckPFCanUse = {
        21122: Condition21122 }
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

