# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/pfai/pfai39244.pyc
# RelativePath: clientlogic/cl_platformdata/pc/pfai/pfai39244.pyc
# Source Generated with Decompyle++
# File: pfai39244.pyc (Python 3.6)

import cl_betree.pfai.mobject as pfaiobj
import cl_condition
from cl_commondefines import MONSTER_PFAI_CATCH, MONSTER_PFAI_DODGE, PF_GROUP_CHECK_ALL, PF_GROUP_CHECK_ALLCD

class CPerformAI(pfaiobj.CBasePerformAI):
    m_SID = 39244
    m_Name = '<三周目>【诡谲雪山】boss-妖王分身'
    m_FillBulletData = ()
    m_UseBulletPF = ()
    m_PFGroup = {
        1001: {
            0: [
                39244,
                1,
                1,
                0] },
        1002: {
            0: [
                39245,
                1,
                1,
                0],
            1: [
                39244,
                1,
                1,
                0] },
        1101: {
            0: [
                39242,
                1,
                1,
                0] },
        1102: {
            0: [
                39245,
                1,
                1,
                0],
            1: [
                39242,
                1,
                1,
                0] },
        1201: {
            0: [
                39242,
                1,
                1,
                0],
            1: [
                39244,
                1,
                1,
                0] },
        1202: {
            0: [
                39245,
                1,
                1,
                0],
            1: [
                39242,
                1,
                1,
                0],
            2: [
                39244,
                1,
                1,
                0] },
        1203: {
            0: [
                39244,
                1,
                1,
                0],
            1: [
                39245,
                1,
                1,
                0],
            2: [
                39242,
                1,
                1,
                0] } }
    m_GroupOfPF = {
        39244: [
            1001,
            1002,
            1201,
            1202,
            1203],
        39245: [
            1002,
            1102,
            1202,
            1203],
        39242: [
            1101,
            1102,
            1201,
            1202,
            1203] }
    m_ChoosePFInfo = {
        MONSTER_PFAI_DODGE: { },
        MONSTER_PFAI_CATCH: {
            (0, 10, -1, 100, -1, 100, 1): [
                {
                    'choose': {
                        1101: 10,
                        1201: 6 } }],
            (10, 20, -1, 100, -1, 100, 1): [
                {
                    'choose': {
                        1202: 10,
                        1002: 8,
                        1102: 18 } }],
            (20, 99, -1, 100, -1, 100, 1): [
                {
                    'choose': {
                        1001: 5,
                        1002: 12,
                        1202: 6,
                        1203: 14 } }] } }
    m_CheckPFCanUse = { }
    m_PFGroupCheck = {
        1001: PF_GROUP_CHECK_ALL | PF_GROUP_CHECK_ALLCD,
        1002: PF_GROUP_CHECK_ALL | PF_GROUP_CHECK_ALLCD,
        1101: PF_GROUP_CHECK_ALL | PF_GROUP_CHECK_ALLCD,
        1102: PF_GROUP_CHECK_ALL | PF_GROUP_CHECK_ALLCD,
        1201: PF_GROUP_CHECK_ALL | PF_GROUP_CHECK_ALLCD,
        1202: PF_GROUP_CHECK_ALL | PF_GROUP_CHECK_ALLCD,
        1203: PF_GROUP_CHECK_ALL | PF_GROUP_CHECK_ALLCD }

