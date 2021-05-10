import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

sigma = eval( input( "Please enter sigma: " ) )

filter_size = int( 6 * sigma + 1 )				# 濾波器大小
gauss = signal.gaussian( filter_size, sigma )	# 濾波器係數
sum = np.sum( gauss )                   		# 正規化
gauss = gauss / sum

w, H = signal.freqz( gauss )
mag = abs( H )

plt.plot( w, mag )
plt.xlabel( r'$\omega$' )
plt.ylabel( 'Magnitude' )

plt.show( )