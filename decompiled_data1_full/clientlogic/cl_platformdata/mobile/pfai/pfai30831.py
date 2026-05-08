# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/pfai/pfai30831.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/pfai/pfai30831.pyc
# Source Generated with Decompyle++
# File: pfai30831.pyc (Python 3.6)

import cl_betree.pfai.mobject as pfaiobj
import cl_condition
from cl_commondefines import MONSTER_PFAI_CATCH, MONSTER_PFAI_DODGE, PF_GROUP_CHECK_FIRST

def Condition30831(oOwner, dInfo):
    return cl_condition.GetWinkDisSubTargetDis(oOwner, dInfo) <= 0.5


def Condition30834(oOwner, dInfo):
    return oOwner.Phase() == 2


class CPerformAI(pfaiobj.CBasePerformAI):
    m_SID = 30831
    m_Name = '【第一幕】精英持矛近战怪'
    m_FillBulletData = ()
    m_UseBulletPF = ()
    m_PFGroup = {
        1001: {
            0: [
                30832,
                1,
                1,
                0] },
        1002: {
            0: [
                38021,
                1,
                1,
                0] },
        1003: {
            0: [
                38022,
                1,
                1,
                0] },
        1004: {
            0: [
                30835,
                1,
                1,
                0] },
        1005: {
            0: [
                30833,
                1,
                1,
                0] },
        1006: {
            0: [
                30834,
                1,
                1,
                0] },
        1007: {
            0: [
                30832,
                1,
                1,
                0],
            1: [
                30835,
                1,
                1,
                0] } }
    m_GroupOfPF = {
        30832: [
            1001,
            1007],
        38021: [
            1002],
        38022: [
            1003],
        30835: [
            1004,
            1007],
        30833: [
            1005],
        30834: [
            1006] }
    m_ChoosePFInfo = {
        MONSTER_PFAI_DODGE: {
            (0, 99, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1002: 10 },
                    'angle': (0, 180) },
                {
                    'choose': {
                        1003: 10 },
                    'angle': (-180, 0) }] },
        MONSTER_PFAI_CATCH: {
            (0, 8, -1, 100, -1, 50, 0): [
                {
                    'choose': {
                        1007: 20,
                        1005: 15,
                        1006: 9999,
                        1004: 5 } }],
            (8, 99, -1, 100, -1, 50, 0): [
                {
                    'choose': {
                        1004: 15,
                        1005: 15,
                        1006: 9999 } }],
            (0, 8, -1, 100, 50, 100, 0): [
                {
                    'choose': {
                        1001: 15,
                        1005: 15,
                        1006: 9999 } }],
            (8, 99, -1, 100, 50, 100, 0): [
                {
                    'choose': {
                        1004: 15,
                        1005: 15,
                        1006: 9999 } }] } }
    m_CheckPFCanUse = {
        30831: Condition30831,
        30834: Condition30834 }
    m_PFGroupCheck = {
        1001: PF_GROUP_CHECK_FIRST,
        1002: PF_GROUP_CHECK_FIRST,
        1003: PF_GROUP_CHECK_FIRST,
        1004: PF_GROUP_CHECK_FIRST,
        1005: PF_GROUP_CHECK_FIRST,
        1006: PF_GROUP_CHECK_FIRST,
        1007: PF_GROUP_CHECK_FIRST }

