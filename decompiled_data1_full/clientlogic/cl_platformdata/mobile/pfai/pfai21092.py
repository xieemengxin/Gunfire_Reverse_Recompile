# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/pfai/pfai21092.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/pfai/pfai21092.pyc
# Source Generated with Decompyle++
# File: pfai21092.pyc (Python 3.6)

import cl_betree.pfai.mobject as pfaiobj
import cl_condition
from cl_commondefines import MONSTER_PFAI_CATCH, MONSTER_PFAI_DODGE, PF_GROUP_CHECK_FIRST

class CPerformAI(pfaiobj.CBasePerformAI):
    m_SID = 21092
    m_Name = '<二周目>【第四幕】小型远程-电系基础远程怪'
    m_FillBulletData = (38020, 15, 3)
    m_UseBulletPF = (21091,)
    m_PFGroup = {
        1001: {
            0: [
                21091,
                2,
                4,
                0] },
        1004: {
            0: [
                38020,
                1,
                1,
                0] },
        1005: {
            0: [
                21091,
                3,
                6,
                0] },
        1006: {
            0: [
                21091,
                5,
                9,
                0] },
        1002: {
            0: [
                38036,
                1,
                1,
                0] },
        1003: {
            0: [
                38037,
                1,
                1,
                0] } }
    m_GroupOfPF = {
        21091: [
            1001,
            1005,
            1006],
        38020: [
            1004],
        38036: [
            1002],
        38037: [
            1003] }
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
            (10, 99, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1006: 10 } }],
            (5, 10, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1005: 10 } }],
            (0, 5, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1001: 10 } }] } }
    m_CheckPFCanUse = { }
    m_PFGroupCheck = {
        1001: PF_GROUP_CHECK_FIRST,
        1004: PF_GROUP_CHECK_FIRST,
        1005: PF_GROUP_CHECK_FIRST,
        1006: PF_GROUP_CHECK_FIRST,
        1002: PF_GROUP_CHECK_FIRST,
        1003: PF_GROUP_CHECK_FIRST }

