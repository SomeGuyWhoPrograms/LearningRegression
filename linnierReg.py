import pandas as pd 

def data(file:str)->pd.DataFrame| Exception: 
    if (isinstance(file, str) == False):
        raise Exception("file path is not a valid string")
    #elif file[-2::].lower != "csv": 
        #raise Exception("file path requires a valid csv")

    df = pd.read_csv(file)
    df.dropna() 
    # note the file uses x and y as the axis but stdard wont exept that i have to convert x-y for model 

    return df 

Opened = data("test.csv") 

def L_one_loss(m:int, b:int, points:pd.DataFrame): 
    # mean squered error
    # # this is the error function total_error / float(len(points)) sum((y[i] - (m * x +b))**2 ) 
    total_error = 0 
    for i in range(0, len(points)): 
        x = points.iloc[i].x 
        y = points.iloc[i].y
        total_error += (y - (m * x +b))**2  # reminder y=mx+b is slope intercept and y -(mx+b) at point 0 = 0 

    val = total_error / float(len(points))
    return val 

def graidient_decent (m_now, b_now, points, l_rate:float): 
    m_gradient = 0
    b_gradient = 0 

    n = len(points) 

    for i in range(0, n): 
        x = points.iloc[i].x 
        y = points.iloc[i].y 

        # Thees are the partial derivitives taken from the error function with respect to to x - y 
        m_gradient += -(2/n) * x * (y-(m_now * x + b_now))
        b_gradient += -(2/n) * (y-(m_now * x + b_now)) 

    m = m_now - m_gradient * l_rate
    b = m = b_now - b_gradient * l_rate 

    return m, b 

def regression(m, b, l:float, itterations:int):
    # iterations is also called epochs 
    for i in range(0,itterations): 
        m , b = graidient_decent(m ,b ,data("test.csv"), l) 

    return m , b  




"""
def generatecsv(numitems: int , xlable="x" , ylable="y"): 
    lables = ""
    def gen(): 
        val = list(range(0, 200))
        val_2 = list(range(0, 200 , 2))
        
        return val , val_2 
    
    lables += f"{xlable},{ylable}\n"
    for i in range(numitems):
        lables += f"{gen()[0][i]},{gen()[1][i]}\n" 

    return lables 

print(generatecsv(100))
""" 
