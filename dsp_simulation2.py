import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft
from scipy import signal

# Generate a sample signal
fs = 1000  # Sampling frequency (Hz)
t = np.arange(0, 1, 1/fs)  # Time vector - 1 second duration
freq1, freq2 = 50, 120  # Frequencies of signals
signal_input = np.sin(2 * np.pi * freq1 * t) + 0.5 * np.sin(2 * np.pi * freq2 * t)

# Add noise to the signal
noisy_signal = signal_input + 0.02 * np.random.normal(0, 1, len(signal_input))

# FIR Filter (Low-pass)
numtaps = 201  # Increased filter order for better smoothing
cutoff = 40  # Lower cutoff frequency for noise reduction
fir_coeff = signal.firwin(numtaps, cutoff, fs=fs)
filtered_fir = signal.lfilter(fir_coeff, 1.0, noisy_signal)

# IIR Filter (Low-pass)
sos = signal.butter(20, 40, 'low', fs=fs, output='sos')
filtered_iir = signal.sosfilt(sos, noisy_signal)

# Plot the time-domain signal with filtering
plt.figure(figsize=(10, 4))
plt.plot(t, noisy_signal, label='Noisy Signal', color='orange')
plt.plot(t, filtered_fir, label='FIR Filtered', color='red')
plt.plot(t, filtered_iir, label='IIR Filtered', color='green')
plt.title('Time Domain Signal with Filtering')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.savefig('screenshots/filtered_signals.png')
plt.show()

# FIR Filter Frequency Response
w, h = signal.freqz(fir_coeff, worN=8000)
plt.figure(figsize=(10, 4))
plt.plot(0.5 * fs * w / np.pi, np.abs(h))
plt.title('FIR Filter Frequency Response')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Gain')
plt.grid(True)
plt.savefig('screenshots/fir_response.png')
plt.show()

# IIR Filter Frequency Response
w, h = signal.sosfreqz(sos, worN=8000, fs=fs)
plt.figure(figsize=(10, 4))
plt.plot(w, np.abs(h))
plt.title('IIR Filter Frequency Response')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Gain')
plt.grid(True)
plt.savefig('screenshots/iir_response.png')
plt.show()

# Perform FFT on original signal
N = len(signal_input)
fft_output = fft(signal_input)
frequencies = np.fft.fftfreq(N, 1/fs)

# Plot the frequency-domain signal
plt.figure(figsize=(10, 4))
plt.plot(frequencies[:N//2], 2/N * np.abs(fft_output[:N//2]))
plt.title('Frequency Domain Signal (FFT)')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.grid(True)
plt.savefig('screenshots/frequency_domain_signal.png')
plt.show()

# Perform FFT on FIR filtered signal
fft_fir = fft(filtered_fir)
plt.figure(figsize=(10, 4))
plt.plot(frequencies[:N//2], 2/N * np.abs(fft_fir[:N//2]))
plt.title('FIR Filtered Signal (FFT)')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.grid(True)
plt.savefig('screenshots/fir_filtered_fft.png')
plt.show()

# Perform FFT on IIR filtered signal
fft_iir = fft(filtered_iir)
plt.figure(figsize=(10, 4))
plt.plot(frequencies[:N//2], 2/N * np.abs(fft_iir[:N//2]))
plt.title('IIR Filtered Signal (FFT)')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.grid(True)
plt.savefig('screenshots/iir_filtered_fft.png')
plt.show()

# Script Features:
# - Generates a composite sine wave with two frequencies and adds noise.
# - Implements FIR and IIR filters with optimized parameters to clean the noisy signal.
# - Visualizes the noisy and filtered signals in the time domain.
# - Computes and plots FFT to show frequency components before and after filtering.
# - Visualizes filter frequency responses for FIR and IIR filters.
# - Saves all plots in the 'screenshots' folder for documentation.
# - Suitable for academic reports, portfolio projects, and engineering documentation.

