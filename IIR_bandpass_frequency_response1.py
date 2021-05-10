import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

alpha = 0.5
beta = 0.2
b = np.array( [ 1 - alpha, 0, -( 1 - alpha ) ] )
a = np.array( [ 2, -2 * beta * ( 1 + alpha ), 2 * alpha ] )
w, H = signal.freqz( b, a )
H1 = abs( H )

alpha = 0.5
beta = 0.5
b = np.array( [ 1 - alpha, 0, -( 1 - alpha ) ] )
a = np.array( [ 2, -2 * beta * ( 1 + alpha ), 2 * alpha ] )
w, H = signal.freqz( b, a )
H2 = abs( H )

alpha = 0.5
beta = 0.8
b = np.array( [ 1 - alpha, 0, -( 1 - alpha ) ] )
a = np.array( [ 2, -2 * beta * ( 1 + alpha ), 2 * alpha ] )
w, H = signal.freqz( b, a )
H3 = abs( H )

plt.plot( w, H1, '-', label = r'$\beta$ = 0.2' )
plt.plot( w, H2, '--', label = r'$\beta$ = 0.5' )
plt.plot( w, H3, '-.', label = r'$\beta$ = 0.8' )

plt.legend( loc = 'upper right' )
plt.xlabel( r'$\omega$' )
plt.ylabel( 'Magnitude' )

plt.show( )