# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/clinterface/clclient/clc_version.pyc
# RelativePath: clientlogic/clinterface/clclient/clc_version.pyc
# Source Generated with Decompyle++
# File: clc_version.pyc (Python 3.6)

from cl_only import PythonError
from myutil.cipher import Decrypt
import base64
import marshal
ENCRYPT_KEY_LIST = [
    81,
    72,
    67,
    77,
    67,
    77,
    83,
    72]

def UpdateLogicScript(sCodeList):
    for sCode in sCodeList:
        
        try:
            exec(sCode)
        except:
            PythonError()

        codeList = sCode.split('\n')
        if codeList:
            print('update: ', codeList[0], codeList[len(codeList) - 1])
    


def GetEncryptKey():
    sKey = ''
    for i, iValue in enumerate(ENCRYPT_KEY_LIST):
        sKey += chr(i ^ iValue)
    
    return sKey


def UpdateLogicEncryptScript(sEncryptCodeList):
    sKey = GetEncryptKey()
    lstCode = []
    for sEnCode in sEncryptCodeList:
        sEnCode = base64.b64decode(sEnCode)
        lstCode.append(Decrypt(sEnCode, sKey))
    
    UpdateLogicScript(lstCode)


def UpdateLogicScriptByteCode(sCode):
    sCode = base64.b64decode(sCode)
    sCode = marshal.loads(sCode)
    
    try:
        exec(sCode)
        print('update done')
    except:
        PythonError()


