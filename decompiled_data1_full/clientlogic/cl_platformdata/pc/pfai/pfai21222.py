# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/pfai/pfai21222.pyc
# RelativePath: clientlogic/cl_platformdata/pc/pfai/pfai21222.pyc
# Source Generated with Decompyle++
# File: pfai21222.pyc (Python 3.6)

import cl_betree.pfai.mobject as pfaiobj
import cl_condition
from cl_commondefines import MONSTER_PFAI_CATCH, MONSTER_PFAI_DODGE, PF_GROUP_CHECK_FIRST

class CPerformAI(pfaiobj.CBasePerformAI):
    m_SID = 21222
    m_Name = '<二周目>中型近战-重甲突击怪'
    m_FillBulletData = ()
    m_UseBulletPF = ()
    m_PFGroup = {
        1101: {
            0: [
                21222,
                1,
                1,
                0] },
        1102: {
            0: [
                21222,
                1,
                1,
                0],
            1: [
                21221,
                1,
                1,
                0] },
        1201: {
            0: [
                21221,
                1,
                1,
                0] },
        1301: {
            0: [
                21223,
                1,
                1,
                0] },
        1302: {
            0: [
                21223,
                1,
                1,
                0],
            1: [
                21223,
                1,
                1,
                25] },
        1303: {
            0: [
                21223,
                1,
                1,
                0],
            1: [
                21221,
                1,
                1,
                0] } }
    m_GroupOfPF = {
        21222: [
            1101,
            1102],
        21221: [
            1102,
            1201,
            1303],
        21223: [
            1301,
            1302,
            1303] }
    m_ChoosePFInfo = {
        MONSTER_PFAI_DODGE: { },
        MONSTER_PFAI_CATCH: {
            (15, 99, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1302: 50,
                        1201: 50,
                        1101: 1 } }],
            (10, 15, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1301: 40,
                        1303: 40,
                        1201: 20,
                        1101: 1 } }],
            (5, 10, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1201: 100,
                        1101: 1 } }],
            (0, 5, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1101: 20,
                        1102: 40,
                        1201: 40 } }] } }
    m_CheckPFCanUse = { }
    m_PFGroupCheck = {
        1101: PF_GROUP_CHECK_FIRST,
        1102: PF_GROUP_CHECK_FIRST,
        1201: PF_GROUP_CHECK_FIRST,
        1301: PF_GROUP_CHECK_FIRST,
        1302: PF_GROUP_CHECK_FIRST,
        1303: PF_GROUP_CHECK_FIRST }

