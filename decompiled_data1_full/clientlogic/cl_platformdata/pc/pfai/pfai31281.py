# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/pfai/pfai31281.pyc
# RelativePath: clientlogic/cl_platformdata/pc/pfai/pfai31281.pyc
# Source Generated with Decompyle++
# File: pfai31281.pyc (Python 3.6)

import cl_betree.pfai.mobject as pfaiobj
import cl_condition
from cl_commondefines import MONSTER_PFAI_CATCH, MONSTER_PFAI_DODGE, PF_GROUP_CHECK_FIRST

class CPerformAI(pfaiobj.CBasePerformAI):
    m_SID = 31281
    m_Name = '【第四幕】精英弱点怪'
    m_FillBulletData = ()
    m_UseBulletPF = ()
    m_PFGroup = {
        1001: {
            0: [
                31281,
                1,
                1,
                0] },
        1002: {
            0: [
                31282,
                1,
                1,
                0],
            1: [
                31284,
                1,
                1,
                0] },
        1003: {
            0: [
                31285,
                1,
                1,
                0],
            1: [
                31283,
                1,
                1,
                0] },
        1006: {
            0: [
                31284,
                1,
                1,
                0],
            1: [
                31286,
                1,
                1,
                0] },
        1007: {
            0: [
                31282,
                1,
                1,
                0],
            1: [
                31286,
                1,
                1,
                0] },
        1008: {
            0: [
                31286,
                1,
                1,
                0],
            1: [
                31287,
                1,
                1,
                0] },
        1009: {
            0: [
                31285,
                1,
                1,
                0],
            1: [
                31287,
                1,
                1,
                0],
            2: [
                31283,
                1,
                1,
                0] },
        1010: {
            0: [
                31283,
                1,
                1,
                0],
            1: [
                31287,
                1,
                1,
                0] },
        1011: {
            0: [
                38039,
                1,
                1,
                0] },
        1012: {
            0: [
                38040,
                1,
                1,
                0] } }
    m_GroupOfPF = {
        31281: [
            1001],
        31282: [
            1002,
            1007],
        31284: [
            1002,
            1006],
        31285: [
            1003,
            1009],
        31283: [
            1003,
            1009,
            1010],
        31286: [
            1006,
            1007,
            1008],
        31287: [
            1008,
            1009,
            1010],
        38039: [
            1011],
        38040: [
            1012] }
    m_ChoosePFInfo = {
        MONSTER_PFAI_DODGE: {
            (0, 99, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1011: 10 },
                    'angle': (0, 180) },
                {
                    'choose': {
                        1012: 10 },
                    'angle': (-180, 0) }] },
        MONSTER_PFAI_CATCH: {
            (4, 99, -1, 100, -1, 50, 0): [
                {
                    'choose': {
                        1008: 10,
                        1009: 20 } }],
            (0, 4, -1, 100, -1, 50, 0): [
                {
                    'choose': {
                        1003: 20,
                        1010: 10 } }],
            (4, 99, -1, 100, 50, 100, 0): [
                {
                    'choose': {
                        1006: 20,
                        1007: 10 } }],
            (0, 4, -1, 100, 50, 100, 0): [
                {
                    'choose': {
                        1001: 20,
                        1002: 10 } }] } }
    m_CheckPFCanUse = { }
    m_PFGroupCheck = {
        1001: PF_GROUP_CHECK_FIRST,
        1002: PF_GROUP_CHECK_FIRST,
        1003: PF_GROUP_CHECK_FIRST,
        1006: PF_GROUP_CHECK_FIRST,
        1007: PF_GROUP_CHECK_FIRST,
        1008: PF_GROUP_CHECK_FIRST,
        1009: PF_GROUP_CHECK_FIRST,
        1010: PF_GROUP_CHECK_FIRST,
        1011: PF_GROUP_CHECK_FIRST,
        1012: PF_GROUP_CHECK_FIRST }

