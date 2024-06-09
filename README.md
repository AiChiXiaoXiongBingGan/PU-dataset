# 🌟 Introduction to the PU Dataset 🌟

The Paderborn University (PU) Bearing Fault Diagnosis Dataset from Germany provides a wealth of bearing fault signal data. This dataset encompasses various types of bearing faults, such as inner ring, outer ring, and rolling element faults. Compared to other datasets, the PU dataset is distinguished by its inclusion of extensive motor-driven system fault data, offering researchers a comprehensive experimental platform for bearing fault diagnosis.

## 📊 Dataset Overview

The PU dataset is divided into multiple subsets, each featuring different fault types and experimental conditions. The primary subsets are described as follows:

Component defects in the dataset arise from both artificial causes and accelerated life testing. The modular test bench consists of five main components: torque shaft, bearing test module, flywheel, motor, and load motor.

Experimental conditions, such as N15_M01_F10, indicate a bearing speed of 1500 rpm, a radial load of 1000 N, and a system load torque of 0.1 Nm. Each experimental condition is repeated 20 times, with a sampling frequency of 64 kHz and a collection duration of 4 seconds per sample. Data for experimental validation are selected from 13 non-artificial bearing damage samples generated from accelerated life tests.

### 📡 Data Collection Methods

Vibration signal data in the PU dataset are collected using high-precision accelerometers and recorded with a data acquisition system. During experiments, researchers set various operating conditions, including speed, load, lubrication, and temperature, to ensure the diversity and representativeness of the data. All data are preprocessed to remove noise and interference signals, ensuring data quality.

### 💾 Data Format

The PU dataset is typically stored in MAT file format, with each file containing vibration signal data for one or more channels. Each channel's data is a time series representing the amplitude of vibration signals collected by accelerometers over a specific time period. Additionally, each data file includes descriptions of the experimental conditions, such as fault type, speed, and load.

### 🚀 Application Scenarios

The PU dataset is widely used in fields such as rotating machinery fault diagnosis, condition monitoring, and predictive maintenance. Researchers analyze fault characteristics in vibration signals to develop efficient fault diagnosis algorithms, enhancing equipment reliability and safety. In recent years, the PU dataset has also been utilized for training and testing machine learning and deep learning algorithms, providing valuable experimental data for the advancement of intelligent fault diagnosis technologies.
