# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/pfai/pfai21341.pyc
# RelativePath: clientlogic/cl_platformdata/pc/pfai/pfai21341.pyc
# Source Generated with Decompyle++
# File: pfai21341.pyc (Python 3.6)

import cl_betree.pfai.mobject as pfaiobj
import cl_condition
from cl_commondefines import MONSTER_PFAI_CATCH, MONSTER_PFAI_DODGE, PF_GROUP_CHECK_FIRST

class CPerformAI(pfaiobj.CBasePerformAI):
    m_SID = 21341
    m_Name = '<一周目>【新一幕】中型近战-冲锋兵'
    m_FillBulletData = ()
    m_UseBulletPF = ()
    m_PFGroup = {
        1101: {
            0: [
                21341,
                1,
                1,
                0] },
        1102: {
            0: [
                21342,
                1,
                1,
                0] },
        1303: {
            0: [
                21342,
                1,
                1,
                0],
            1: [
                21341,
                1,
                1,
                0] } }
    m_GroupOfPF = {
        21341: [
            1101,
            1303],
        21342: [
            1102,
            1303] }
    m_ChoosePFInfo = {
        MONSTER_PFAI_DODGE: { },
        MONSTER_PFAI_CATCH: {
            (16, 99, -1, 100, -1, 100, 2): [
                {
                    'choose': {
                        1102: 10 } }],
            (12, 16, -1, 100, -1, 100, 2): [
                {
                    'choose': {
                        1101: 60,
                        1102: 40 } }],
            (8, 12, -1, 100, -1, 100, 2): [
                {
                    'choose': {
                        1102: 70,
                        1101: 30 } }],
            (0, 8, -1, 100, -1, 100, 2): [
                {
                    'choose': {
                        1101: 10 } }],
            (16, 99, -1, 100, -1, 100, 1): [
                {
                    'choose': {
                        1102: 10 } }],
            (12, 16, -1, 100, -1, 100, 1): [
                {
                    'choose': {
                        1101: 20,
                        1102: 80 } }],
            (8, 12, -1, 100, -1, 100, 1): [
                {
                    'choose': {
                        1102: 10,
                        1101: 10 } }],
            (0, 8, -1, 100, -1, 100, 1): [
                {
                    'choose': {
                        1101: 10 } }] } }
    m_CheckPFCanUse = { }
    m_PFGroupCheck = {
        1101: PF_GROUP_CHECK_FIRST,
        1102: PF_GROUP_CHECK_FIRST,
        1303: PF_GROUP_CHECK_FIRST }

