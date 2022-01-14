def calculo_conversion(moneda1,valor_ref,nombremoneda):
        moneda1 = float(moneda1)
        valor_ref = float(valor_ref)
        result = moneda1/ valor_ref
        result = round(result,2) #redondear a dos decimales
        result = str(result)
        print("El resultado de la conversion es $" + result + nombremoneda)
        
tipo_moneda1=int(input('''
Escoje la moneda con la realizaras la operación:
1.  Colombiana 😎
2.  Chilena    🤔
3.  Mexicana   😏
4.  Peruana    😶
5.  Dolar      🤑
'''))
tipo_moneda2=int(input('''
Escoje la moneda a la  que deseas convertir tu dinero
1.  Colombiana 😎
2.  Chilena    🤔
3.  Mexicana   😏
4.  Peruana    😶
5.  Dolar      🤑
'''))
cantidad= int(input(''' Cuanta cantidad de dinero deseas convertir: '''))
if tipo_moneda1 == tipo_moneda2:
        print("No es posible realizar la conversion con la misma moneda")
elif (tipo_moneda1 == 1 and tipo_moneda2==2):
    ref1 = 4.78
    calculo_conversion(cantidad,ref1," pesos chilenos.💰") 
    
elif (tipo_moneda1 == 1 and tipo_moneda2==3):
    ref2 = 176.29
    calculo_conversion(cantidad,ref2," pesos mexicanos.💰") 

elif (tipo_moneda1 == 1 and tipo_moneda2==4):    
    ref3 = 962.61
    calculo_conversion(cantidad, ref3, " soles peruanos.💰") 

elif (tipo_moneda1 == 1 and tipo_moneda2==5):
    ref4 = 3875
    calculo_conversion(cantidad,ref4, " dolares.💰")    

elif (tipo_moneda1 == 2 and tipo_moneda2==1):
    ref5 = 0.21
    calculo_conversion(cantidad,ref5, "pesos colombianos💰") 

elif (tipo_moneda1 == 2 and tipo_moneda2==3):
    ref6 = 0.027
    calculo_conversion(cantidad,ref6, " pesos mexicanos.💰") 

elif (tipo_moneda1 == 2 and tipo_moneda2==4):
    ref7 = 201.39
    calculo_conversion(cantidad,ref7, " soles peruanos.💰") 

elif (tipo_moneda1 == 2 and tipo_moneda2==5):
    ref8 = 727.30
    calculo_conversion(cantidad,ref8, " dolares.💰") 

elif (tipo_moneda1 == 3 and tipo_moneda2==1):
    ref9 = 0.0057
    calculo_conversion(cantidad,ref9, " pesos colombianos💰") 

elif (tipo_moneda1 == 3 and tipo_moneda2==2):
    ref10 = 0.027
    calculo_conversion(cantidad,ref10, " pesos chilenos.💰")

elif (tipo_moneda1 == 3 and tipo_moneda2==4):
    ref11 = 5.46
    calculo_conversion(cantidad,ref11," soles peruanos.💰") 

elif (tipo_moneda1 == 3 and tipo_moneda2==5):
    ref12 = 19.72
    calculo_conversion(cantidad,ref12, " dolares.💰")  

elif (tipo_moneda1 == 4 and tipo_moneda2==1):
    ref13 = 0.0010
    calculo_conversion(cantidad,ref13," pesos colombianos💰") 

elif (tipo_moneda1 == 4 and tipo_moneda2==2):
    ref14 = 0.0050
    calculo_conversion(cantidad,ref14, " pesos chilenos.💰") 

elif (tipo_moneda1 == 4 and tipo_moneda2==3):
    ref14 = 0.18
    calculo_conversion(cantidad,ref14," pesos mexicanos.💰")

elif (tipo_moneda1 == 4 and tipo_moneda2==5):
    ref15 = 3.61
    calculo_conversion(cantidad,ref15, " dolares.💰")  

elif (tipo_moneda1 == 5 and tipo_moneda2==1):
    ref16 = 0.00029
    calculo_conversion(cantidad,ref16, " pesos colombianos💰") 

elif (tipo_moneda1 == 5 and tipo_moneda2==2):
    ref17 = 0.0014
    calculo_conversion(cantidad,ref17, " pesos chilenos.💰") 

elif (tipo_moneda1 == 5 and tipo_moneda2==3):
    ref18 = 0.051
    calculo_conversion(cantidad,ref18," pesos mexicanos.💰") 

elif (tipo_moneda1 == 5 and tipo_moneda2==4):
    ref19 = 0.28
    calculo_conversion(cantidad,ref19, " soles peruanos.💰") 

else:
    exit 
