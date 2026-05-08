# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/pfai/pfai21631.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/pfai/pfai21631.pyc
# Source Generated with Decompyle++
# File: pfai21631.pyc (Python 3.6)

import cl_betree.pfai.mobject as pfaiobj
import cl_condition
from cl_commondefines import MONSTER_PFAI_CATCH, MONSTER_PFAI_DODGE, PF_GROUP_CHECK_FIRST

class CPerformAI(pfaiobj.CBasePerformAI):
    m_SID = 21631
    m_Name = '狙击怪-闪烁追踪怪'
    m_FillBulletData = (38015, 10, 20)
    m_UseBulletPF = (21631,)
    m_PFGroup = {
        1001: {
            0: [
                21631,
                2,
                2,
                0] },
        1002: {
            0: [
                21632,
                1,
                1,
                0] },
        1003: {
            0: [
                21621,
                1,
                1,
                0] },
        1004: {
            0: [
                21613,
                1,
                1,
                0] },
        1005: {
            0: [
                21614,
                1,
                1,
                0] },
        1006: {
            0: [
                21631,
                3,
                3,
                0] },
        1007: {
            0: [
                21631,
                4,
                4,
                0] },
        1008: {
            0: [
                21613,
                1,
                1,
                0] },
        1009: {
            0: [
                38015,
                1,
                1,
                0] },
        1010: {
            0: [
                7109,
                1,
                1,
                0] },
        1011: {
            0: [
                7110,
                1,
                1,
                0] } }
    m_GroupOfPF = {
        21631: [
            1001,
            1006,
            1007],
        21632: [
            1002],
        21621: [
            1003],
        21613: [
            1004,
            1008],
        21614: [
            1005],
        38015: [
            1009],
        7109: [
            1010],
        7110: [
            1011] }
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
            (20, 99, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1006: 40,
                        1007: 60 } }],
            (10, 20, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1001: 20,
                        1006: 50,
                        1007: 30 } }],
            (4, 10, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1001: 50,
                        1006: 40,
                        1007: 10 } }],
            (0, 4, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1002: 10 } }] } }
    m_CheckPFCanUse = { }
    m_PFGroupCheck = {
        1001: PF_GROUP_CHECK_FIRST,
        1002: PF_GROUP_CHECK_FIRST,
        1003: PF_GROUP_CHECK_FIRST,
        1004: PF_GROUP_CHECK_FIRST,
        1005: PF_GROUP_CHECK_FIRST,
        1006: PF_GROUP_CHECK_FIRST,
        1007: PF_GROUP_CHECK_FIRST,
        1008: PF_GROUP_CHECK_FIRST,
        1009: PF_GROUP_CHECK_FIRST,
        1010: PF_GROUP_CHECK_FIRST,
        1011: PF_GROUP_CHECK_FIRST }

