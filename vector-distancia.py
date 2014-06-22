import copy
import os
inf=9999999 #definimos este valor como nuestro infinito
adyA=[0,1,inf,inf,inf,inf,4,inf,10]
adyB=[1,0,9,inf,8,inf,inf,inf,inf]
adyC=[inf,9,0,2,inf,inf,inf,inf,inf]
adyD=[inf,inf,2,0,9,4,inf,inf,2]
adyE=[inf,8,inf,9,0,2,inf,inf,1]
adyF=[inf,inf,inf,4,2,0,inf,6,inf]
adyG=[4,inf,inf,inf,inf,inf,0,7,inf]
adyH=[inf,inf,inf,inf,inf,6,7,0,3]
adyI=[10,inf,inf,2,1,inf,inf,3,0]
adyacentes=[adyA,adyB,adyC,adyD,adyE,adyF,adyG,adyH,adyI]
lista=[0,1,2,3,4,5,6,7,8]#variable auxiliar para mover los for
costosAct=[]
costosSig=[]
valor_act=[0,0,0,0,0,0,0,0,0]#vector usado para saber cuando se debe actualizar la tabla de costos de cada router
def init():#inicializa las tablas con los costos hacia los vecinos
    cpyAdy=copy.deepcopy(adyacentes)
    tcost=[[],[],[],[],[],[],[],[],[]]
    vector=[inf,inf,inf,inf,inf,inf,inf,inf,inf]#para crear cada tabla de costos inicial
    for i in lista:
        for j in lista:
            if i==j:
                tcost[j].append(cpyAdy[j])
            else:
                tcost[j].append(vector)
    return tcost



#obtiene el menor elemento de una lista de numeros
def menor_lista(lista):
    menor = 0 + lista[0]
    for valor in lista:
        if valor < menor:
            menor = 0 + valor
    return menor

#entrega el menor coste para ir de x a y al informarle una nueva tabla de costos
def dxy(x,y,costosAct):
    costosVecinos=[]
    vecinos=[]
    costo=0
    dvy=0
    for i in lista:#determinamos los vecinos a x
        if adyacentes[x][i]<inf:#si el elelemto es adyacente a x (<inf)
            vecinos.append(0+i)#guardamos los id de los vecinos de x
        for ady in vecinos:#determinamos los costos para ir a cada vecino
            costo=0 + adyacentes[x][ady]#guardamos el costo para ir a cada vecino directo
            dvy=0 + costosAct[ady][ady][y]
            costosVecinos.append(costo+dvy)
    return menor_lista(costosVecinos)


costosAct=copy.deepcopy(init())
costosSig=copy.deepcopy(init())

#suma los elementos en una lista numerica
def sumalist(lista):
    sum=0
    for i in lista:
        sum=sum+i
    return sum


def vectorDist(CA,CS,valor_act):
    vecinos=[]
    #primera actualizacion siempre se hace
    for i in range(9):#iteramos para los 9 routers
        for j in range(9):#actualizamos las dxy de x hacia todos los routers
            valor=dxy(i,j,CA)#para cada i-esimo router, actualiza todos los costos de ir a j segun los costos de las tablas de sus vecinos
            if valor<CA[i][i][j] and valor<CS[i][i][j]:#si el valor es menor lo reemplaza en costos siguientes
                CS[i][i][j]=valor
                valor_act[i]=1#indicamos que esta tabla se modifico
            for k in lista:#determinamos los vecinos a i
                if adyacentes[i][k]<inf and adyacentes[i][k]>0:#si el elelemto es adyacente a x (<inf)
                    vecinos.append(0+k)#guardamos los id de los vecinos de x
            for v in vecinos:#guardamos los dv de los vecinos en nuestra propia tabla de costos
                CS[i][v]=copy.deepcopy(CA[v][v])

    for l in lista:
        CA[l]=copy.deepcopy(CS[l])#actualizamos los costos actuales a los costos siguientes

    #ahora iteramos nuevamente
    continuar=sumalist(valor_act)#obtenemos la suma de los elementos en list
    aux=copy.deepcopy(valor_act)#copiamos la lista para usarla mas adelante y poder modificar la actual
    while(continuar>0):#si se modifico alguna tabla
        for i in lista:#para cada router
            v=[]#no hay vecinos
            valor_act[i]=0
            for k in lista:#determinamos los vecinos a i
                if adyacentes[i][k]<inf and adyacentes[i][k]>0:#si el elemento es adyacente a i (<inf)
                    vecinos.append(0+k)#guardamos los id de los vecinos de i
            for v in vecinos:#para cada vecino vemos si este se modifico
                if aux[v]>0:#si se modifico
                    CS[i][v]=copy.deepcopy(CA[v][v])#como se habia actualizado, actualizamos los costos con el valor del vecino
                    for j in lista:#actualizamos las dxy de i hacia todos los routers
                        valor=dxy(i,j,CA)#para cada i-esimo router, actualiza todos los costos de ir a j segun los costos de las tablas de sus vecinos
                        if valor<CA[i][i][j] and valor<CS[i][i][j]:#si el valor es menor lo reemplaza en costos siguientes
                            CS[i][i][j]=valor
                            valor_act[i]=valor_act[i]+1#indicamos que esta tabla se modifico
        for l in lista:
            CA[l]=copy.deepcopy(CS[l])#actualizamos los costos actuales a los costos siguientes
        continuar=sumalist(valor_act)#obtenemos la suma de los elementos en list
        aux=copy.deepcopy(valor_act)#copiamos la lista para usarla mas adelante y poder modificar la actual


def imprimeTablita(tablita,letra):
    listAlphabet = ['B','C','D','E','F','G','H','I','A']
    cadena=listAlphabet[8]+"\t\t\t"
    print("Router "+listAlphabet[letra-1]+"\tA\tB\tC\tD\tE\tF\tG\tH\tI")
    for i in lista:
        for j in lista:
            cadena=cadena+str(tablita[i][j])+"\t"
        print (cadena)
        cadena=listAlphabet[i]+"\t\t\t"


def vectorDistInt(CA,CS,valor_act):
    vecinos=[]
    CA[7][7][8]=inf
    CA[8][8][7]=inf
    CS[7][7][8]=inf
    CS[8][8][7]=inf
    adyH[8]=inf
    adyI[7]=inf
    adyacentes=[adyA,adyB,adyC,adyD,adyE,adyF,adyG,adyH,adyI]
    valor_act[7]=1
    valor_act[8]=1
    #ahora iteramos nuevamente
    continuar=sumalist(valor_act)#obtenemos la suma de los elementos en list
    aux=copy.deepcopy(valor_act)#copiamos la lista para usarla mas adelante y poder modificar la actual
    while(continuar>0):#si se modifico alguna tabla
        for i in lista:#para cada router
            v=[]#no hay vecinos
            valor_act[i]=0
            for k in lista:#determinamos los vecinos a i
                if adyacentes[i][k]<inf and adyacentes[i][k]>0:#si el elemento es adyacente a i (<inf)
                    vecinos.append(0+k)#guardamos los id de los vecinos de i
            for v in vecinos:#para cada vecino vemos si este se modifico
                if aux[v]>0:#si se modifico
                    CS[i][v]=copy.deepcopy(CA[v][v])#como se habia actualizado, actualizamos los costos con el valor del vecino
                    for j in lista:#actualizamos las dxy de i hacia todos los routers
                        valor=dxy(i,j,CA)#para cada i-esimo router, actualiza todos los costos de ir a j segun los costos de las tablas de sus vecinos
                        if valor<CA[i][i][j] and valor<CS[i][i][j]:#si el valor es menor lo reemplaza en costos siguientes
                            CS[i][i][j]=valor
                            valor_act[i]=valor_act[i]+1#indicamos que esta tabla se modifico
        for l in lista:
            CA[l]=copy.deepcopy(CS[l])#actualizamos los costos actuales a los costos siguientes
        continuar=sumalist(valor_act)#obtenemos la suma de los elementos en list
        aux=copy.deepcopy(valor_act)#copiamos la lista para usarla mas adelante y poder modificar la actual

if __name__ == '__main__':
    vectorDist(costosAct,costosSig,valor_act)
    print ("Con H e I conectados")
    for i in lista:
        imprimeTablita(costosAct[i],i)
        print("")
    vectorDistInt(costosAct,costosSig,valor_act)
    print ("Sin enlace entre H e I")
    for i in lista:
        imprimeTablita(costosAct[i],i)
        print("")




