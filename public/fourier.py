import numpy as np
import matplotlib.pyplot as plt
from js import document, window

def plotar():
    termos = int(document.getElementById("termos").value)
    ganho = int(document.getElementById("ganho").value)
    document.getElementById("valTermo").innerHTML = termos
    document.getElementById("valGanho").innerHTML = ganho
    tela = document.getElementById("bode")
    px = 1/plt.rcParams['figure.dpi']
    tamanho = (int(window.innerHeight*px*3/4), int(window.innerHeight*px*3/4))
    
    def fourier(x:np.float64, termos:int =1, k:int =1):
        res = 0
        for n in range(1, termos+1):
            if n == 0: continue
            res += ((1 - np.cos(n*np.pi))*np.sin(n*np.pi*x)/n)
        res *= 4*k/np.pi
        return res
    
    plt.close('all') #limpeza
    fig, ax = plt.subplots(figsize=tamanho)
    t = np.linspace(-1, 1, 100, dtype=np.float64)
    y = fourier(x=t, termos=termos, k=ganho)
    ax.plot(t, y, "b.-")
    ax.set_aspect('auto')

    Element("plote").clear()
    display(fig, target="plote", append=True) #workaround

plotar()

document.getElementById("bode").style.visibility = "visible"