import sys
def mru():
  while(True):
    print("Ingrese 1(v), 2(t), 3(m) de lo que quiera calcular: ")
    v, t, m = 0, 0, 0
    i = int(input())
    if( 1 > i or i > 3):
      print("Opción no válida.")
      continue
    if(i != 1):
      print("Velocidad:")
      v = float(input())
    if(i != 2):
      print("Tiempo: ")
      t = float(input())
    if(i != 3):
      print("Distancia:")
      m = float(input())
    
    mru_calc(i, [v, t, m])
    break

def mru_calc(i, param):
  v, t, m = param
  match i:
    case 1:
      if(t == 0):
        print("No se puede calcular")
      else:
        v = m / t; 
        print("La velocidad es:", v, "m/s")
    case 2:
      if(v == 0):
        print("No se puede calcular")
      else:
        t = m / v;
        print("El tiempo es:", t, "s")
    case 3:
      m = v * t
      print("La distancia es:", m, "m")

def mruv_options():
  print("Ingrese 1 para calcular la distancia, 2 para calular la velocidad final")
  i = int(input())
  if( 1 > i or i > 2):
    print("Opción no válida.")
    return
  print("Velocida Inicial:")
  v0 = float(input())
  print("Aceleración:")
  a = float(input())
  print("Tiempo:")
  t = float(input())

  if(i == 1):
    mruv_form1(v0, a, t)
  elif(i == 2):
    mruv_form2(v0, a, t)

def mruv_form1(v0, a, t):
  d = v0 * t + 0.5 * a * t**2
  print("La distancia es:", d, "m")

def mruv_form2(v0, a, t):
  vf = v0 + a * t
  print("La velocidad final es:", vf, "m/s")

print("Ingrese 1 para MRU, 2 para MRUV")
i = int(input())
if(i == 1):
  mru()
elif(i == 2):
  mruv_options()
else:
  print("Opción no válida.")
