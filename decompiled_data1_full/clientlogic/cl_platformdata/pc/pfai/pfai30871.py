# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/pfai/pfai30871.pyc
# RelativePath: clientlogic/cl_platformdata/pc/pfai/pfai30871.pyc
# Source Generated with Decompyle++
# File: pfai30871.pyc (Python 3.6)

import cl_betree.pfai.mobject as pfaiobj
import cl_condition
from cl_commondefines import MONSTER_PFAI_CATCH, MONSTER_PFAI_DODGE, PF_GROUP_CHECK_FIRST

class CPerformAI(pfaiobj.CBasePerformAI):
    m_SID = 30871
    m_Name = '【第三幕】精英小型近战'
    m_FillBulletData = ()
    m_UseBulletPF = ()
    m_PFGroup = {
        1001: {
            0: [
                30871,
                1,
                1,
                0] },
        1101: {
            0: [
                38031,
                1,
                1,
                0] },
        1102: {
            0: [
                38032,
                1,
                1,
                0] },
        1002: {
            0: [
                30872,
                1,
                1,
                0] },
        1103: {
            0: [
                38035,
                1,
                1,
                0] },
        1003: {
            0: [
                30871,
                1,
                1,
                0],
            1: [
                30872,
                1,
                1,
                0] },
        1004: {
            0: [
                30873,
                1,
                1,
                0] } }
    m_GroupOfPF = {
        30871: [
            1001,
            1003],
        38031: [
            1101],
        38032: [
            1102],
        30872: [
            1002,
            1003],
        38035: [
            1103],
        30873: [
            1004] }
    m_ChoosePFInfo = {
        MONSTER_PFAI_DODGE: {
            (0, 99, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1101: 10 },
                    'angle': (0, 135) },
                {
                    'choose': {
                        1102: 10 },
                    'angle': (-135, 0) },
                {
                    'choose': {
                        1103: 10 },
                    'angle': (135, 180) },
                {
                    'choose': {
                        1103: 10 },
                    'angle': (-180, -135) }] },
        MONSTER_PFAI_CATCH: {
            (5, 99, 0, 100, -1, 100, 0): [
                {
                    'choose': {
                        1001: 10,
                        1004: 10 } }],
            (0, 5, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1002: 10 } }] } }
    m_CheckPFCanUse = { }
    m_PFGroupCheck = {
        1001: PF_GROUP_CHECK_FIRST,
        1101: PF_GROUP_CHECK_FIRST,
        1102: PF_GROUP_CHECK_FIRST,
        1002: PF_GROUP_CHECK_FIRST,
        1103: PF_GROUP_CHECK_FIRST,
        1003: PF_GROUP_CHECK_FIRST,
        1004: PF_GROUP_CHECK_FIRST }

