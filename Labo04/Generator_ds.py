import random

def Generacion_dataset(num_datos, porc_error_calculo):
    duracion = [20, 40, 60]
    for i in range(num_datos):
        cb1 = 0
        cb = 0
        tipo = random.randint(1, 3)
        calidad = random.randint(1, 3)
        duracion_max = random.sample(duracion, 1)[0]
        sonido = random.randint(0,2)
        num_revisiones = random.randint(1, 9)
        dias_trabajo = tipo + calidad + duracion_max/20 + sonido + 1#Añadir a codigo jupiter

        error = random.random()
        if tipo == 1:
            cb1 = random.randint(25, 60)
            cb = cb1
            cb += cb1 * calidad/10
            cb += cb1 * duracion_max/200
            cb += cb1 * sonido/10
            cb += num_revisiones * random.randint(3, 4)
        if tipo == 2:
            cb1 = random.randint(85, 135)
            cb = cb1
            cb += cb1 * calidad / 10
            cb += cb1 * duracion_max / 200
            cb += cb1 * sonido / 10
            cb += num_revisiones * random.randint(3, 4)
        if tipo == 3:
            cb1 = random.randint(175, 215)
            cb = cb1
            cb += cb1 * calidad / 10
            cb += cb1 * duracion_max / 200
            cb += cb1 * sonido / 10
            cb += num_revisiones * random.randint(3, 4)
        if error < porc_error_calculo:
            sum_res = random.randint(0, 1)
            if sum_res == 1:
                cb += cb1 * 0.2
            else:
                cb -= cb1 * 0.2
        cf = round(cb, 2)

        print(f'{tipo},{calidad},{duracion_max},{sonido},{num_revisiones},{cf}')


Generacion_dataset(150, 0.1)