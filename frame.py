import wx
from script import Foto

class Frame(wx.Frame):
    def __init__(self, parent):
        self.frame = wx.Frame.__init__(self,parent,-1,'Programa Georeferenciacion de Fotos en kml',size=(300,200))
        self.panel = panel(self)
        self.panel.Show()
        
class panel(wx.Panel):
    def __init__(self,parent):
        wx.Panel.__init__(self,parent=parent)
        self.SetBackgroundColour(wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ))
        self.malla = wx.BoxSizer(orient=wx.VERTICAL)
        boton4 = wx.Button(self, -1, 'Directorio Fotos',pos=wx.DefaultPosition,size=(300,30))
        boton3= wx.Button(self, -1, 'Directorio a Guardar',pos=wx.DefaultPosition,size=(300,30))
        self.boton2= wx.Button(self, -1, "Start",pos=wx.DefaultPosition,size=(300,30))
        self.rutaDir = ""
        self.rutaFoto = ""
        self.malla.Add(boton4,1,wx.ALIGN_CENTER,5)
        self.malla.Add(boton3,1,wx.ALIGN_CENTER,5)
        self.malla.Add(self.boton2,1,wx.ALIGN_CENTER,5)
        self.SetSizer(self.malla)
       
        self.Bind(wx.EVT_BUTTON,self.RutaFoto,boton4)
        self.Bind(wx.EVT_BUTTON,self.Dir,boton3)
        self.Bind(wx.EVT_BUTTON,self.onStart,self.boton2)
        
        self.Layout()

            
    def Dir(self,event):
            diaFolder = wx.DirDialog(self,"Abrir Directorio de Guardado")
            diaFolder.ShowModal()
           
            self.rutaDir = diaFolder.GetPath()
    def RutaFoto(self,event):
            diaFoto = wx.DirDialog(self,"Abrir Directorio de Fotos")
            diaFoto.ShowModal()
           
            self.rutaFoto = diaFoto.GetPath()

    def onStart(self,event):
        ex = Foto(self.rutaFoto,self.rutaDir)
        eje = ex.Write()
        if(eje):
            self.boton2.SetLabel("Finish")
            self.boton2.SetBackgroundColour(colour=(0,255,0))
            

        

app = wx.App()
frame = Frame(None)
frame.Show()
frame.Centre()
app.MainLoop()
   