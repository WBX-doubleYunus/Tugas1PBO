import wx
import kalkulator1

class kalkulator123(kalkulator1.MyFrame1):
    def __init__(self,parent):
        kalkulator1.MyFrame1.__init__(self,parent)

    def tambahkan(self,event):
        a = int(self.m_textCtrl1.GetValue())
        b = int(self.m_textCtrl2.GetValue())
        c = a + b
        self.m_textCtrl3.SetValue(str(c))

    def kurangkan(self,event):
        a = int(self.m_textCtrl1.GetValue())
        b = int(self.m_textCtrl2.GetValue())
        c = a - b
        self.m_textCtrl3.SetValue(str(c))

    def kalikan(self,event):
        a = int(self.m_textCtrl1.GetValue())
        b = int(self.m_textCtrl2.GetValue())
        c = a * b
        self.m_textCtrl3.SetValue(str(c))

    def bagikan(self,event):
        a = int(self.m_textCtrl1.GetValue())
        b = int(self.m_textCtrl2.GetValue())
        c = a / b
        self.m_textCtrl3.SetValue(str(c))

if __name__ == "__main__":
    app = wx.App(False)
    frame = kalkulator123(None)
    frame.Show(True)
    app.MainLoop()
    