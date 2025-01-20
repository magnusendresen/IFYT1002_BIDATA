
import numpy as np
import matplotlib.pyplot as plt
# Replace 'your_file.csv' with the path to your CSV file
#filnavn='C:\\Users\\trotho\\OD\\fag\\IFYT1001\\programmering\\øvinger\\Raw Data_u1_5.csv' # ligger på et annet sted
filnavn='Raw Data_1.csv' # ligger samme sted som jupyter notebook fila
data = np.genfromtxt(filnavn, delimiter=';', skip_header=1)  # Use skip_header=1 to skip the header row if there is one

plt.scatter(data[:,0] , data[:,1] , color='blue', marker='s', label='x-retning',s=10)
plt.scatter(data[:,0] , data[:,2] , color='red', marker='^', label='y-retning',s=10)
plt.scatter(data[:,0] , data[:,3] , color='black', marker='o', label='z-retning',s=10)

plt.xlabel('Tid [sekunder]')
plt.ylabel('Akselerasjon [m/s**2]')
plt.title('Akselerasjonsmålingene')
 
# Add a legend

 
# Show the plot
plt.show()

# Søker opp intervallet mellom 5.4 til 6.3 sekunder
intervallA = (data[:,0] >= 5.4) & (data[:,0] <= 6.3) 
intervallB = (data[:,0] >= 12.5) & (data[:,0] <= 13.25) 
plt.scatter(data[intervallB,0] , data[intervallB,3] , color='red', marker='o', label='Data points')
plt.scatter(data[intervallA,0] , data[intervallA,3] , color='red', marker='o', label='z-retning')
plt.scatter(data[:,0] , data[:,3] , color='black', marker='.', label='Data points',s=20)
#

# Add labels and a title

x1=[4, 8]
y1=[np.mean(data[intervallA,3]), np.mean(data[intervallA,3])]
yp1=[np.mean(data[intervallA,3])+np.std(data[intervallA,3]), np.mean(data[intervallA,3])+np.std(data[intervallA,3])]
ym1=[np.mean(data[intervallA,3])-np.std(data[intervallA,3]), np.mean(data[intervallA,3])-np.std(data[intervallA,3])]

x2=[11, 15]
y2=[np.mean(data[intervallB,3]), np.mean(data[intervallB,3])]
yp2=[np.mean(data[intervallB,3])+np.std(data[intervallB,3]), np.mean(data[intervallB,3])+np.std(data[intervallB,3])]
ym2=[np.mean(data[intervallB,3])-np.std(data[intervallB,3]), np.mean(data[intervallB,3])-np.std(data[intervallB,3])]




plt.plot(x1,y1,'k-')
plt.plot(x1,yp1,'b-')
plt.plot(x1,ym1,'b-')
plt.plot(x2,y2,'k-')
plt.plot(x2,yp2,'b-')
plt.plot(x2,ym2,'b-')
plt.xlabel('Tid [sekunder]')
plt.ylabel('Akselerasjon [m/s**2]')
plt.title('Akselerasjonsmålingene')
 
 
# Show the plot

plt.show()