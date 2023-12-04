from scipy import signal
import pandas as pd
import matplotlib.pyplot as plt

# notch filter to remove powerline noise
dataset_path = "raw_data/calm3eyesopen202312021438_eeg.csv"
dataset = pd.read_csv(dataset_path)

notch_freq = 50 # set to 50 in Europe, 60 in North America
numerator, denominator = signal.iirnotch(notch_freq, 20, 250)
filtered_notch_data = signal.filtfilt(b=numerator, a=denominator, x=dataset.ch1, padtype=None)

# bandpass filter to remove common artefacts during resting state recordings
high_pass_freq = 1
low_pass_freq = 35
denom, nom = signal.iirfilter(int(3), [1, 35], btype="bandpass", ftype="butter", fs=float(250), output="ba")
filtered_bp_data = signal.filtfilt(b=denom, a=nom, x=filtered_notch_data, padtype=None)

plt.plot(filtered_bp_data)
plt.show()

import numpy as np
import matplotlib.pyplot as plt

fs = 512
# Define EEG bands
eeg_bands = {'Delta': (0, 4),
             'Theta': (4, 8),
             'Alpha': (8, 12),
             'Beta': (12, 30),
             'Gamma': (30, 45)}

data = filtered_bp_data

# Get real amplitudes of FFT (only in postive frequencies)
fft_vals = np.absolute(np.fft.rfft(data))

# Get frequencies for amplitudes in Hz
fft_freq = np.fft.rfftfreq(len(data), 1.0/fs)

# Take the mean of the fft amplitude for each EEG band
eeg_band_fft = dict()
for band in eeg_bands:  
    freq_ix = np.where((fft_freq >= eeg_bands[band][0]) & 
                        (fft_freq <= eeg_bands[band][1]))[0]
    eeg_band_fft[band] = np.mean(fft_vals[freq_ix])

for band in eeg_bands:  
    print(band, eeg_band_fft[band])

# Plot the data (using pandas here cause it's easy)
df = pd.DataFrame(columns=['band', 'val'])
df['band'] = eeg_bands.keys()
df['val'] = [eeg_band_fft[band] for band in eeg_bands]
ax = df.plot.bar(x='band', y='val', legend=False)
ax.set_xlabel("EEG band")
ax.set_ylabel("Mean band Amplitude")

plt.show()