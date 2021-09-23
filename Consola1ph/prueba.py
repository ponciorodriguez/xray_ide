from PIL import Image
 
foto = Image.open('/home/poncio/proyectos_python/xray_ide/Consola1ph/captura_1.png')
 
datos = list(foto.getdata())

 
'''la linea anterior tambien podria escribirse como:
 
datos = list(Image.Image.getdata(foto))'''
 
#al finalizar cerramos el objeto instanciado
 
foto.close()
print(datos)
