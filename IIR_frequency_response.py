import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

alpha = eval( input( "Please enter alpha (< 1): " ) )

b = np.array( [ 1 - alpha, 1 - alpha ] )
a = np.array( [ 2, -2 * alpha ] )
w, H = signal.freqz( b, a )
H0 = abs( H )

b = np.array( [ 1 + alpha, - ( 1 + alpha ) ] )
a = np.array( [ 2, -2 * alpha ] )
w, H = signal.freqz( b, a )
H1 = abs( H )

plt.figure( 1 )
plt.plot( w, H0 )
plt.xlabel( r'$\omega$' )
plt.ylabel( 'Magnitude' )

plt.figure( 2 )
plt.plot( w, H1 )
plt.xlabel( r'$\omega$' )
plt.ylabel( 'Magnitude' )

plt.show( )