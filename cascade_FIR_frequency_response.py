import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

order = eval( input( "Enter number of cascade FIR filters: " ) )

b = np.array( [ 0.5, 0.5 ] )
w, H = signal.freqz( b )

for i in range( order - 1 ):
	H *= H

H0 = abs( H )
	
plt.plot( w, H0 )
plt.xlabel( r'$\omega$' )
plt.ylabel( 'Magnitude' )

plt.show( )