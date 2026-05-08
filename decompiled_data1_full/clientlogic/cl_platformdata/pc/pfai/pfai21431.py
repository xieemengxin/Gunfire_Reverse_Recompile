# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/pfai/pfai21431.pyc
# RelativePath: clientlogic/cl_platformdata/pc/pfai/pfai21431.pyc
# Source Generated with Decompyle++
# File: pfai21431.pyc (Python 3.6)

import cl_betree.pfai.mobject as pfaiobj
import cl_condition
from cl_commondefines import MONSTER_PFAI_CATCH, MONSTER_PFAI_DODGE, PF_GROUP_CHECK_FIRST

class CPerformAI(pfaiobj.CBasePerformAI):
    m_SID = 21431
    m_Name = '【第三幕】中型远程'
    m_FillBulletData = ()
    m_UseBulletPF = ()
    m_PFGroup = {
        1001: {
            0: [
                38033,
                1,
                1,
                0] },
        1002: {
            0: [
                38034,
                1,
                1,
                0] },
        1003: {
            0: [
                38012,
                1,
                1,
                0] },
        1101: {
            0: [
                21431,
                1,
                2,
                0] },
        1102: {
            0: [
                21431,
                1,
                2,
                0],
            1: [
                21431,
                1,
                2,
                30] },
        1103: {
            0: [
                21431,
                3,
                3,
                0] },
        1104: {
            0: [
                21431,
                2,
                3,
                0],
            1: [
                21431,
                2,
                3,
                30] },
        1105: {
            0: [
                21431,
                2,
                3,
                0],
            1: [
                21431,
                1,
                4,
                30],
            2: [
                21431,
                2,
                3,
                30] },
        1106: {
            0: [
                21431,
                5,
                5,
                0] },
        1201: {
            0: [
                21432,
                1,
                1,
                0] },
        1301: {
            0: [
                21435,
                1,
                1,
                0] },
        1401: {
            0: [
                21436,
                1,
                1,
                0] } }
    m_GroupOfPF = {
        38033: [
            1001],
        38034: [
            1002],
        38012: [
            1003],
        21431: [
            1101,
            1102,
            1103,
            1104,
            1105,
            1106],
        21432: [
            1201],
        21435: [
            1301],
        21436: [
            1401] }
    m_ChoosePFInfo = {
        MONSTER_PFAI_DODGE: {
            (0, 99, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1001: 10 },
                    'angle': (0, 180) },
                {
                    'choose': {
                        1002: 10 },
                    'angle': (-180, 0) }] },
        MONSTER_PFAI_CATCH: {
            (12, 99, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1106: 40,
                        1401: 40,
                        1104: 20 } }],
            (8, 12, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1103: 50,
                        1401: 25,
                        1104: 25 } }],
            (5, 8, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1101: 40,
                        1301: 40,
                        1102: 20 } }],
            (0, 5, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1201: 10 } }] } }
    m_CheckPFCanUse = { }
    m_PFGroupCheck = {
        1001: PF_GROUP_CHECK_FIRST,
        1002: PF_GROUP_CHECK_FIRST,
        1003: PF_GROUP_CHECK_FIRST,
        1101: PF_GROUP_CHECK_FIRST,
        1102: PF_GROUP_CHECK_FIRST,
        1103: PF_GROUP_CHECK_FIRST,
        1104: PF_GROUP_CHECK_FIRST,
        1105: PF_GROUP_CHECK_FIRST,
        1106: PF_GROUP_CHECK_FIRST,
        1201: PF_GROUP_CHECK_FIRST,
        1301: PF_GROUP_CHECK_FIRST,
        1401: PF_GROUP_CHECK_FIRST }

