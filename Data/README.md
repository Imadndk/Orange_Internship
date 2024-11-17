# **DATA Folder Overview**

This folder contains resources and methods for data processing used in the project. It includes solutions for leveraging the MIMIC-III dataset for medical research and machine learning tasks and generating synthetic datasets.

---
### **Solution 1: MIMIC-III Dataset**

The **MIMIC-III** dataset is a rich, publicly available dataset that captures high-resolution longitudinal health data. It supports advanced machine learning research and clinical decision-making improvements.

#### **Dataset Features**:
- Contains de-identified patient data, including:
  - Vital signs, medications, laboratory measurements, clinical notes, fluid balance, procedural and diagnostic codes, imaging reports, and survival outcomes.
- Covers approximately **60,000 ICU admissions** at the Beth Israel Deaconess Medical Center between 2001 and 2012.
- Features high-resolution temporal data, including bedside monitor trends and waveform data.

#### **Access via AWS**:
- Hosted on **AWS Public Datasets**.
- Accessed directly through Amazon S3 without the need for downloading, copying, or storage fees.

---

## **Contents**
- **Synthetic_Data/**: Scripts and CSV files for the synthetic dataset.
- **MIMIC-III_Access/**: Configuration files and scripts for accessing MIMIC-III via AWS. [https://aws.amazon.com/blogs/big-data/perform-biomedical-informatics-without-a-database-using-mimic-iii-data-and-amazon-athena/]

---

## **Applications**
1. **Synthetic Data**: Used for training machine learning models to simulate various medical conditions.
2. **MIMIC-III**: Serves as a high-fidelity dataset for validating models and conducting in-depth clinical research.

---

## **. Data Collection Process**

### **Solution 2: Synthetic Data Generation**

After multiple meetings with a doctor, a custom script was developed to simulate realistic health data for a population of patients. This simulation integrates statistical distributions and realistic correlations between vital signs, mimicking various medical scenarios such as heart attacks, hyperglycemia, and hypoglycemia.

#### **Steps in the Process**:
1. **Configuration of Basic Parameters**:
   - Defined mean values and standard deviations for six key health variables: heart rate, oxygen saturation, body temperature, respiratory rate, systolic blood pressure, and diastolic blood pressure.
   - Specified a correlation matrix to simulate realistic interrelations between variables (e.g., increased heart rate correlates with higher respiratory rates).

2. **Data Creation**:
   - Used a multivariate normal distribution to generate baseline health data for each patient, accounting for statistical averages, variability, and correlations.

3. **Simulation of Medical Emergencies**:
   - Incorporated random emergency events into patient time series to simulate:
     - **Heart Attacks**: Drops in oxygen saturation, unstable blood pressure, and variable heart rates.
     - **Hyperglycemia**: Elevated heart rate, increased respiratory rate, and lowered blood pressure.
     - **Hypoglycemia**: High or low respiratory rate, elevated heart rate, and unstable blood pressure.

4. **Data Generation and Export**:
   - Generated data for 5,000 patients with 3-second intervals between time points, simulating real-time IoT sensor data.
   - Exported the data to CSV files with timestamps for each observation, enabling temporal analysis.

---


## **License**
Refer to the respective licensing terms for the synthetic dataset and the MIMIC-III dataset.

---


