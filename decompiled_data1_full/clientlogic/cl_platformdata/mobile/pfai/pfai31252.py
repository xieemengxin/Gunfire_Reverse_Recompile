# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/pfai/pfai31252.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/pfai/pfai31252.pyc
# Source Generated with Decompyle++
# File: pfai31252.pyc (Python 3.6)

import cl_betree.pfai.mobject as pfaiobj
import cl_condition
from cl_commondefines import MONSTER_PFAI_CATCH, MONSTER_PFAI_DODGE, PF_GROUP_CHECK_FIRST

class CPerformAI(pfaiobj.CBasePerformAI):
    m_SID = 31252
    m_Name = '【第二幕】精英中型盾兵（迭代）'
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
                31255,
                1,
                1,
                0] },
        1004: {
            0: [
                31256,
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
        31255: [
            1003],
        31256: [
            1004] }
    m_ChoosePFInfo = {
        MONSTER_PFAI_DODGE: { },
        MONSTER_PFAI_CATCH: {
            (15, 99, -1, 30, -1, 100, 0): [
                {
                    'choose': {
                        1003: 50,
                        1006: 50 } }],
            (8, 15, -1, 30, -1, 100, 0): [
                {
                    'choose': {
                        1003: 20,
                        1004: 80 } }],
            (4, 8, -1, 30, -1, 100, 0): [
                {
                    'choose': {
                        1005: 20,
                        1004: 80 } }],
            (0, 4, -1, 30, -1, 100, 0): [
                {
                    'choose': {
                        1002: 50,
                        1004: 50 } }],
            (15, 99, 30, 60, -1, 100, 0): [
                {
                    'choose': {
                        1005: 10,
                        1003: 50,
                        1006: 40 } }],
            (8, 15, 30, 60, -1, 100, 0): [
                {
                    'choose': {
                        1003: 45,
                        1004: 35,
                        1005: 20 } }],
            (4, 8, 30, 60, -1, 100, 0): [
                {
                    'choose': {
                        1005: 20,
                        1003: 45,
                        1004: 35 } }],
            (0, 4, 30, 60, -1, 100, 0): [
                {
                    'choose': {
                        1002: 75,
                        1004: 25 } }],
            (15, 99, 60, 100, -1, 100, 0): [
                {
                    'choose': {
                        1005: 25,
                        1003: 50,
                        1006: 25 } }],
            (8, 15, 60, 100, -1, 100, 0): [
                {
                    'choose': {
                        1001: 20,
                        1003: 40,
                        1005: 40 } }],
            (4, 8, 60, 100, -1, 100, 0): [
                {
                    'choose': {
                        1001: 50,
                        1003: 50 } }],
            (0, 4, 60, 100, -1, 100, 0): [
                {
                    'choose': {
                        1002: 100 } }] } }
    m_CheckPFCanUse = { }
    m_PFGroupCheck = {
        1001: PF_GROUP_CHECK_FIRST,
        1002: PF_GROUP_CHECK_FIRST,
        1003: PF_GROUP_CHECK_FIRST,
        1004: PF_GROUP_CHECK_FIRST,
        1005: PF_GROUP_CHECK_FIRST,
        1006: PF_GROUP_CHECK_FIRST }

