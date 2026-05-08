# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/pfai/pfai21061.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/pfai/pfai21061.pyc
# Source Generated with Decompyle++
# File: pfai21061.pyc (Python 3.6)

import cl_betree.pfai.mobject as pfaiobj
import cl_condition
from cl_commondefines import MONSTER_PFAI_CATCH, MONSTER_PFAI_DODGE, PF_GROUP_CHECK_FIRST

class CPerformAI(pfaiobj.CBasePerformAI):
    m_SID = 21061
    m_Name = '【第三幕】小型远程-持盾远程怪'
    m_FillBulletData = (38012, 4, 50)
    m_UseBulletPF = (21061, 21062)
    m_PFGroup = {
        1001: {
            0: [
                21061,
                1,
                1,
                0] },
        1002: {
            0: [
                21061,
                2,
                3,
                0] },
        1003: {
            0: [
                21061,
                2,
                4,
                0] },
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
                21062,
                1,
                1,
                0] } }
    m_GroupOfPF = {
        21061: [
            1001,
            1002,
            1003],
        38017: [
            1004],
        38031: [
            1005],
        38032: [
            1006],
        21062: [
            1007] }
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
            (12, 99, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1003: 10,
                        1002: 10,
                        1007: 20 } }],
            (5, 12, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1002: 10,
                        1007: 10 } }],
            (0, 5, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1001: 10,
                        1002: 10,
                        1007: 20 } }] } }
    m_CheckPFCanUse = { }
    m_PFGroupCheck = {
        1001: PF_GROUP_CHECK_FIRST,
        1002: PF_GROUP_CHECK_FIRST,
        1003: PF_GROUP_CHECK_FIRST,
        1004: PF_GROUP_CHECK_FIRST,
        1005: PF_GROUP_CHECK_FIRST,
        1006: PF_GROUP_CHECK_FIRST,
        1007: PF_GROUP_CHECK_FIRST }

