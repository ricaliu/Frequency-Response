import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

M = eval( input( "Please enter M for the Comb Filter: " ) )

b = np.zeros( M + 1 )			# 梳狀低通濾波器
b[0] = 0.5
b[M] = 0.5
w, H = signal.freqz( b, 1 )
H0 = abs( H )

b[M] = -0.5						# 梳狀高通濾波器
w, H = signal.freqz( b, 1 )
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