# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/pfai/pfai30211.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/pfai/pfai30211.pyc
# Source Generated with Decompyle++
# File: pfai30211.pyc (Python 3.6)

import cl_betree.pfai.mobject as pfaiobj
import cl_condition
from cl_commondefines import MONSTER_PFAI_CATCH, MONSTER_PFAI_DODGE, PF_GROUP_CHECK_FIRST

class CPerformAI(pfaiobj.CBasePerformAI):
    m_SID = 30211
    m_Name = '四足怪-精英四足怪'
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
        1101: {
            0: [
                30211,
                1,
                1,
                0] },
        1201: {
            0: [
                30212,
                1,
                1,
                0] },
        1301: {
            0: [
                30213,
                1,
                1,
                0] },
        1401: {
            0: [
                30214,
                1,
                1,
                0] },
        1402: {
            0: [
                30214,
                1,
                1,
                0],
            1: [
                30212,
                1,
                1,
                0] },
        1403: {
            0: [
                30214,
                1,
                1,
                0],
            1: [
                30211,
                1,
                1,
                0] },
        1405: {
            0: [
                30211,
                1,
                1,
                0],
            1: [
                30212,
                1,
                1,
                0] },
        1601: {
            0: [
                30216,
                1,
                1,
                0] },
        1602: {
            0: [
                30216,
                1,
                1,
                0],
            1: [
                30214,
                1,
                1,
                0],
            2: [
                30214,
                2,
                2,
                0] },
        1603: {
            0: [
                30216,
                1,
                1,
                0],
            1: [
                30211,
                1,
                1,
                0] },
        1406: {
            0: [
                30214,
                1,
                1,
                0],
            1: [
                30216,
                1,
                1,
                0] } }
    m_GroupOfPF = {
        38028: [
            1001],
        38029: [
            1002],
        30211: [
            1101,
            1403,
            1405,
            1603],
        30212: [
            1201,
            1402,
            1405],
        30213: [
            1301],
        30214: [
            1401,
            1402,
            1403,
            1602,
            1406],
        30216: [
            1601,
            1602,
            1603,
            1406] }
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
            (0, 4, -1, 100, -1, 100, 2): [
                {
                    'choose': {
                        1301: 10 } }],
            (4, 8, -1, 100, -1, 100, 2): [
                {
                    'choose': {
                        1603: 10,
                        1602: 10,
                        1406: 20 } }],
            (8, 15, -1, 100, -1, 100, 2): [
                {
                    'choose': {
                        1601: 10,
                        1602: 10,
                        1603: 10,
                        1406: 10 } }],
            (15, 99, -1, 100, -1, 100, 2): [
                {
                    'choose': {
                        1403: 10 } }],
            (0, 4, -1, 100, -1, 100, 1): [
                {
                    'choose': {
                        1301: 10 } }],
            (4, 8, -1, 100, -1, 100, 1): [
                {
                    'choose': {
                        1201: 10,
                        1301: 5 } }],
            (8, 12, -1, 100, -1, 100, 1): [
                {
                    'choose': {
                        1402: 10,
                        1403: 5 } }],
            (12, 99, -1, 100, -1, 100, 1): [
                {
                    'choose': {
                        1402: 5,
                        1403: 10 } }] } }
    m_CheckPFCanUse = { }
    m_PFGroupCheck = {
        1001: PF_GROUP_CHECK_FIRST,
        1002: PF_GROUP_CHECK_FIRST,
        1101: PF_GROUP_CHECK_FIRST,
        1201: PF_GROUP_CHECK_FIRST,
        1301: PF_GROUP_CHECK_FIRST,
        1401: PF_GROUP_CHECK_FIRST,
        1402: PF_GROUP_CHECK_FIRST,
        1403: PF_GROUP_CHECK_FIRST,
        1405: PF_GROUP_CHECK_FIRST,
        1601: PF_GROUP_CHECK_FIRST,
        1602: PF_GROUP_CHECK_FIRST,
        1603: PF_GROUP_CHECK_FIRST,
        1406: PF_GROUP_CHECK_FIRST }

