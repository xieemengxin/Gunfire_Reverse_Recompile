# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/pfai/pfai21351.pyc
# RelativePath: clientlogic/cl_platformdata/pc/pfai/pfai21351.pyc
# Source Generated with Decompyle++
# File: pfai21351.pyc (Python 3.6)

import cl_betree.pfai.mobject as pfaiobj
import cl_condition
from cl_commondefines import MONSTER_PFAI_CATCH, MONSTER_PFAI_DODGE, PF_GROUP_CHECK_FIRST

class CPerformAI(pfaiobj.CBasePerformAI):
    m_SID = 21351
    m_Name = '【新四幕】中型钩爪怪'
    m_FillBulletData = ()
    m_UseBulletPF = ()
    m_PFGroup = {
        1001: {
            0: [
                21351,
                1,
                1,
                0] },
        1002: {
            0: [
                21352,
                1,
                1,
                0] },
        1003: {
            0: [
                38039,
                1,
                1,
                0] },
        1004: {
            0: [
                38040,
                1,
                1,
                0] },
        1005: {
            0: [
                21353,
                1,
                1,
                0] },
        1007: {
            0: [
                21355,
                1,
                1,
                0] },
        1008: {
            0: [
                21353,
                1,
                1,
                0],
            1: [
                21355,
                1,
                1,
                0] } }
    m_GroupOfPF = {
        21351: [
            1001],
        21352: [
            1002],
        38039: [
            1003],
        38040: [
            1004],
        21353: [
            1005,
            1008],
        21355: [
            1007,
            1008] }
    m_ChoosePFInfo = {
        MONSTER_PFAI_DODGE: {
            (0, 99, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1003: 10 },
                    'angle': (0, 180) },
                {
                    'choose': {
                        1004: 10 },
                    'angle': (-180, 0) }] },
        MONSTER_PFAI_CATCH: {
            (17, 99, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1007: 10,
                        1008: 10 } }],
            (8, 17, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1002: 60,
                        1005: 10 } }],
            (0, 8, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1001: 30 } }] } }
    m_CheckPFCanUse = { }
    m_PFGroupCheck = {
        1001: PF_GROUP_CHECK_FIRST,
        1002: PF_GROUP_CHECK_FIRST,
        1003: PF_GROUP_CHECK_FIRST,
        1004: PF_GROUP_CHECK_FIRST,
        1005: PF_GROUP_CHECK_FIRST,
        1007: PF_GROUP_CHECK_FIRST,
        1008: PF_GROUP_CHECK_FIRST }

