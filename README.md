# DSP Simulation

## Project Overview
This project simulates digital signal processing (DSP) techniques using Python. It demonstrates the generation of composite signals, Fast Fourier Transform (FFT) analysis, and visualization of both time-domain and frequency-domain representations. The project highlights skills in Python programming, signal processing, and data visualization.

---

## Key Features
- **Sine Wave Generation:** Creates a composite signal with multiple frequencies.
- **Fast Fourier Transform (FFT):** Performs frequency domain analysis to extract signal components.
- **Signal Visualization:** Displays time-domain and frequency-domain representations of signals.
- **FIR/IIR Filtering**: Filters noisy signals using Finite and Infinite Impulse Response filters.
- **Extensible Design:** Prepared for enhancements like FIR/IIR filtering and machine learning-based analysis.

---

## Technologies Used
- **Languages:** Python
- **Libraries:** NumPy, SciPy, Matplotlib
- **Tools:** Visual Studio Code, Jupyter Notebook (optional)

---

## Setup Instructions
1. **Clone the Repository:**
```bash
git clone https://github.com/bryanmalak/DSP-Simulation.git
cd DSP-Simulation
```

2. **Install Dependencies:**
```bash
pip install numpy scipy matplotlib
```

3. **Run the Simulation:**
```bash
python3 dsp_simulation.py
```

---

## Screenshots
### Time Domain Signal
![Time Domain Signal](screenshots/time_domain_signal.png)

### Frequency Domain Signal (FFT)
![Frequency Domain Signal](screenshots/frequency_domain_signal.png)

Time Domain Signal with Filtering

This plot displays the noisy signal (blue) along with the FIR filtered (red) and IIR filtered (green) outputs. Both filters effectively smooth the noise while retaining key signal features.


Frequency Domain Signal (FFT)

The FFT of the original signal shows peaks at 50 Hz and 120 Hz, corresponding to the input frequencies.


FIR Filtered Signal (FFT)

The FIR filter reduces the 120 Hz component and preserves the 50 Hz component.


IIR Filtered Signal (FFT)

The IIR filter demonstrates similar performance, effectively reducing the 120 Hz component.


FIR Filter Frequency Response

The FIR filter shows a sharp cutoff at 50 Hz, effectively attenuating higher frequencies.


IIR Filter Frequency Response

The IIR filter displays a steeper roll-off, making it highly effective at suppressing high frequencies.
---

## Future Enhancements
- Add support for processing live data streams.
- Incorporate machine learning algorithms for predictive analysis.
- Develop a GUI interface for parameter selection and visualization.

---

## How to Contribute
1. Fork the repository.
2. Create a new branch:
```bash
git checkout -b feature-branch
```
3. Commit changes and push:
```bash
git commit -m "Feature: Add FIR filter"
git push origin feature-branch
```
4. Create a Pull Request.

---

## Contact Information
- **Author:** Bryan Malak
- **GitHub:** [bryanmalak](https://github.com/bryanmalak)
- **Email:** bvmalak@gmail.com

---


