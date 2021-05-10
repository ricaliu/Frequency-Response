import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

filter_size = eval( input( "Please enter the filter size: " ) )
filter_half = int( filter_size / 2 )
wc = np.pi / 2

na = np.arange( -filter_half, filter_half + 1 )	# 定義 n 陣列 
h = np.zeros( filter_size )						# 計算脈衝響應
for n in na:
	if n == 0: 
		h[n+filter_half] = 0.5
	else:
		h[n+filter_half] = np.sin( wc * n ) / ( np.pi * n )

w, H = signal.freqz( h )
mag = abs( H )

plt.plot( w, mag )
plt.xlabel( r'$\omega$' )
plt.ylabel( 'Magnitude' )

plt.show( )