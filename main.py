import matplotlib.pyplot as plt 
import matplotlib.animation as am 
from linnierReg import data, regression , Opened 


def main(): 
    fig = plt.figure(figsize=(10,8), layout="constrained")
    Data = Opened
    scatx = list(Data["x"])
    scaty = list(Data["y"])
    scatter = plt.scatter(scatx, scaty, s=10)  

    def update(frame): 
        m = regression(0, 0, l=0.001, itterations=frame)[0]
        b = regression(0, 0, l=0.001, itterations=frame)[1]
        line = plt.plot(list(range(0,len(scatx))), [m * x + b for x in range(0,len(scatx))], color="r")  
        return line 

    ani = am.FuncAnimation(fig=fig, func=update, frames=100, interval=40, blit=True) 
    plt.grid() 
    plt.show()  

if __name__ == "__main__": 
    main() 