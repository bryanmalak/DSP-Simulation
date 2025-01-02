import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft

# Generate a sample signal
fs = 1000  # Sampling frequency (Hz)
t = np.arange(0, 1, 1/fs)  # Time vector - 1 second duration
freq1, freq2 = 50, 120  # Frequencies of signals
signal = np.sin(2 * np.pi * freq1 * t) + 0.5 * np.sin(2 * np.pi * freq2 * t)

# Plot the time-domain signal
plt.figure(figsize=(10, 4))
plt.plot(t, signal)
plt.title('Time Domain Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.savefig('screenshots/time_domain_signal.png')  # Save the plot
plt.show()

# Perform FFT
N = len(signal)
fft_output = fft(signal)
frequencies = np.fft.fftfreq(N, 1/fs)

# Plot the frequency-domain signal
plt.figure(figsize=(10, 4))
plt.plot(frequencies[:N//2], 2/N * np.abs(fft_output[:N//2]))  # Single-sided amplitude spectrum
plt.title('Frequency Domain Signal (FFT)')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.grid(True)
plt.savefig('screenshots/frequency_domain_signal.png')  # Save the plot
plt.show()


#This code Generates a composite sine wave with two frequencies.
#Visualizes the signal in the time domain.
#Computes and plots the FFT to show frequency components.