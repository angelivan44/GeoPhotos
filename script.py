from PIL import Image
import simplekml
import os

class Foto():
    def __init__(self,dirFotos, dirSave):
        self.rutaFotos = dirFotos
        self.rutaDir = dirSave
        self.documents = os.listdir(dirFotos)

    def DMS2DD(self,data, direction):
        print(data)
        dd = float(data[0][0]) + float(data[1][0]/60) + float(data[2][0]/3600);
        if (direction == "S" or direction == "W") :
            dd = dd * -1; 
        return dd;

    def Write(self):
        kml = simplekml.Kml()
        folder = kml.newfolder(name="Fotos")
        for index, picture in enumerate(self.documents):
            image_path = self.rutaFotos+"\\"+picture
            try:
                image = Image.open(image_path)
                metada = image._getexif()
            except:
                image = None
                metada = {}
            try:
                ubication = metada[34853]
                print(ubication)
            except:
                ubication = "none"
            if(ubication != "none"):
                file = """file:///"""
                este = self.DMS2DD(ubication[4],ubication[3])
                norte = self.DMS2DD(ubication[2],ubication[1])
                descripcion =  f"""<html> 
                                    <div style="width: 550px;height: 600px;"><h3 style="font-size:22px;color:white;background-color: red;text-align: center;">Foto {index}</h3>
                                    <table style="border:1px solid black;width: 550px;height: 600px; cellspacing:0;" >
                                        <tr>
                                        <td style="border:1px solid">
                                                <img style="width:550; height:420; border:1; bordercolor:blue; transform: rotate(90deg); -webkit-transform: rotate(90deg);" src="{file}{image_path}">
                                        </td>
                                        </tr>
                                    </table >
                                    </div>
                                    </html>
                                        """
                pto = folder.newpoint(name=index, coords=[(este,norte)], description=descripcion)
            return True
        
            
        kml.save(self.rutaDir+"\\"+"exp.kml")



