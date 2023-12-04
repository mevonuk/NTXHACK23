This repository includes the files relivent to the entry of Team 43: TheHappyLie for NTXHACK23.

The directory raw_data contains the unprocessed datafiles. The data files are named such that the emotional state is listed first, followed by its index if repeated, and then the time stamp, and the datafile type (eeg or imu). Only the eeg data are used here. All data files are from the same female individual, except those prefixed with "s" which are for a second male individual.

The images directory contains two folders with animal photos from the internet (cute_animals and ugly_animals) that were viewed by the primary subject for the cute and ugly states.

The waves and waves_bars directories contain sample graphs of the data.

The states-waves.png and tests.png files are the images used in the presentation.

Back in the main directory, process.py contains the python code used to filter the raw data and output the average amplitude of five bands based on frequency: delta, theta, alpha, beta, and gamma.

The excel file, data_ave.xlsx, contains the averaged values of the various bands and their weighted average. These values are used to graph the data.

Finally, the presentation of the project is included. 
