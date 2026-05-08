# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/pfai/pfai31251.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/pfai/pfai31251.pyc
# Source Generated with Decompyle++
# File: pfai31251.pyc (Python 3.6)

import cl_betree.pfai.mobject as pfaiobj
import cl_condition
from cl_commondefines import MONSTER_PFAI_CATCH, MONSTER_PFAI_DODGE, PF_GROUP_CHECK_FIRST

class CPerformAI(pfaiobj.CBasePerformAI):
    m_SID = 31251
    m_Name = '【第二幕】精英中型盾兵'
    m_FillBulletData = ()
    m_UseBulletPF = ()
    m_PFGroup = {
        1001: {
            0: [
                31251,
                1,
                1,
                0] },
        1002: {
            0: [
                31252,
                1,
                1,
                0] },
        1003: {
            0: [
                31253,
                1,
                1,
                0] },
        1004: {
            0: [
                31254,
                1,
                1,
                0] },
        1005: {
            0: [
                31251,
                1,
                1,
                0],
            1: [
                31251,
                1,
                1,
                0] },
        1006: {
            0: [
                31251,
                1,
                1,
                0],
            1: [
                31251,
                1,
                1,
                0],
            2: [
                31251,
                1,
                1,
                0] } }
    m_GroupOfPF = {
        31251: [
            1001,
            1005,
            1006],
        31252: [
            1002],
        31253: [
            1003],
        31254: [
            1004] }
    m_ChoosePFInfo = {
        MONSTER_PFAI_DODGE: { },
        MONSTER_PFAI_CATCH: {
            (4, 8, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1003: 100,
                        1004: 150 } }],
            (15, 99, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1005: 30,
                        1004: 40,
                        1006: 30 } }],
            (8, 15, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1001: 15,
                        1004: 50,
                        1003: 15,
                        1005: 15 } }],
            (0, 4, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1003: 100,
                        1002: 10 } }] } }
    m_CheckPFCanUse = { }
    m_PFGroupCheck = {
        1001: PF_GROUP_CHECK_FIRST,
        1002: PF_GROUP_CHECK_FIRST,
        1003: PF_GROUP_CHECK_FIRST,
        1004: PF_GROUP_CHECK_FIRST,
        1005: PF_GROUP_CHECK_FIRST,
        1006: PF_GROUP_CHECK_FIRST }

