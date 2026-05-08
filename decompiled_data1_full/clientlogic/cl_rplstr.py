# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_rplstr.pyc
# RelativePath: clientlogic/cl_rplstr.pyc
# Source Generated with Decompyle++
# File: cl_rplstr.pyc (Python 3.6)


class CRplStr(object):
    
    def __init__(self, sText, dReplaceInfo = None):
        self.m_Text = sText
        self.m_ReplaceInfo = dReplaceInfo
        self.m_ReplacedText = None

    
    def __repr__(self):
        return self.GetString()

    
    def __str__(self):
        return self.GetString()

    
    def GetRawString(self):
        return self.m_Text

    
    def GetString(self):
        if self.m_ReplacedText is not None:
            return self.m_ReplacedText
        sText = self.m_Text
        if self.m_ReplaceInfo:
            for sPara, sReplace in self.m_ReplaceInfo.items():
                sReplace = sReplace.replace(',', '，')
                sText = sText.replace(sPara, sReplace)
            
        self.m_ReplacedText = sText
        return sText

    
    def GetPacketInfo(self):
        return (self.m_Text, self.m_ReplaceInfo)


