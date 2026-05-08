# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/pfai/pfai32421.pyc
# RelativePath: clientlogic/cl_platformdata/pc/pfai/pfai32421.pyc
# Source Generated with Decompyle++
# File: pfai32421.pyc (Python 3.6)

import cl_betree.pfai.mobject as pfaiobj
import cl_condition
from cl_commondefines import MONSTER_PFAI_CATCH, MONSTER_PFAI_DODGE, PF_GROUP_CHECK_FIRST

class CPerformAI(pfaiobj.CBasePerformAI):
    m_SID = 32421
    m_Name = '【第二幕】投射怪-精英投射怪'
    m_FillBulletData = ()
    m_UseBulletPF = ()
    m_PFGroup = {
        1001: {
            0: [
                38028,
                1,
                1,
                0] },
        1002: {
            0: [
                38029,
                1,
                1,
                0] },
        1003: {
            0: [
                38030,
                1,
                1,
                0] },
        1101: {
            0: [
                32421,
                1,
                1,
                0] },
        1201: {
            0: [
                32422,
                1,
                1,
                0] },
        1202: {
            0: [
                32422,
                1,
                1,
                0],
            1: [
                32422,
                1,
                1,
                0] },
        1301: {
            0: [
                32423,
                1,
                1,
                0] },
        1302: {
            0: [
                32423,
                1,
                1,
                0],
            1: [
                32421,
                1,
                1,
                0] },
        1401: {
            0: [
                32424,
                1,
                1,
                0] },
        1402: {
            0: [
                32424,
                1,
                1,
                0],
            1: [
                32422,
                1,
                1,
                0] },
        1403: {
            0: [
                32424,
                1,
                1,
                0],
            1: [
                32424,
                1,
                1,
                50] } }
    m_GroupOfPF = {
        38028: [
            1001],
        38029: [
            1002],
        38030: [
            1003],
        32421: [
            1101,
            1302],
        32422: [
            1201,
            1202,
            1402],
        32423: [
            1301,
            1302],
        32424: [
            1401,
            1402,
            1403] }
    m_ChoosePFInfo = {
        MONSTER_PFAI_DODGE: {
            (0, 99, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1001: 10 },
                    'angle': (0, 135) },
                {
                    'choose': {
                        1002: 10 },
                    'angle': (-135, 0) },
                {
                    'choose': {
                        1003: 10 },
                    'angle': (135, 180) },
                {
                    'choose': {
                        1003: 10 },
                    'angle': (-180, -135) }] },
        MONSTER_PFAI_CATCH: {
            (15, 99, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1201: 25,
                        1202: 75,
                        1401: 25,
                        1402: 50,
                        1403: 25 } }],
            (10, 15, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1101: 10,
                        1201: 45,
                        1202: 15,
                        1401: 20,
                        1402: 5,
                        1403: 5 } }],
            (5, 10, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1101: 20,
                        1201: 10,
                        1302: 70 } }],
            (0, 5, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1301: 10 } }] } }
    m_CheckPFCanUse = { }
    m_PFGroupCheck = {
        1001: PF_GROUP_CHECK_FIRST,
        1002: PF_GROUP_CHECK_FIRST,
        1003: PF_GROUP_CHECK_FIRST,
        1101: PF_GROUP_CHECK_FIRST,
        1201: PF_GROUP_CHECK_FIRST,
        1202: PF_GROUP_CHECK_FIRST,
        1301: PF_GROUP_CHECK_FIRST,
        1302: PF_GROUP_CHECK_FIRST,
        1401: PF_GROUP_CHECK_FIRST,
        1402: PF_GROUP_CHECK_FIRST,
        1403: PF_GROUP_CHECK_FIRST }

