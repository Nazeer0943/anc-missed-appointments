# ANC Missed Appointments: Data Analysis and Prediction

**Capstone Project | eHealth Africa (eHA) First Data Science Cohort — Group 2**

**Live Application:** [ANC Missed Appointments Dashboard](https://anc-missed-appointments-huc5petjhmw4zst6s8ae3y.streamlit.app/)

## 1. Project Overview

The ANC Missed Appointments project explores patterns associated with missed antenatal care (ANC) appointments using a synthetic dataset. It combines exploratory data analysis, data visualization, summary statistics, and a machine-learning prediction interface in an interactive Streamlit application.

This project was developed as a capstone submission for the eHealth Africa (eHA) First Data Science Cohort, Group 2, demonstrating the application of data science techniques to a maternal healthcare attendance scenario.

## 2. Project Objectives

- Explore patterns in missed and attended ANC appointments.
- Examine missed-appointment rates across selected demographic, socioeconomic, and appointment-related characteristics.
- Present findings through interactive visualizations and summary tables.
- Integrate a trained machine-learning model into a Streamlit application.
- Demonstrate how data analysis and machine learning can support the exploration of healthcare attendance patterns.

## 3. Application Features

### Exploratory Analysis Dashboard

The dashboard presents charts and summary tables generated from the project's synthetic dataset. The analysis covers variables including:

- Residence
- Education level
- Employment status
- Parity
- Health insurance
- Partner support
- Phone access
- Appointment type
- Barriers reported at booking
- Previous missed appointments

The dashboard includes comparisons of missed-appointment rates across selected groups.

### Prediction Interface

The prediction page allows users to select appointment-related characteristics and obtain a model-generated estimate of the probability of a missed ANC appointment.

The application also includes an About section providing project information.

**Important:** The prediction is an experimental output based on synthetic data. It is not a validated clinical risk estimate and must not be used to make decisions about real patients.

## 4. Dataset

The project uses a synthetic ANC dataset containing 1,800 valid records, as reported in the exploratory analysis findings.

The dataset supports demonstration and educational analysis. Its results should not be interpreted as representative of actual patients, healthcare facilities, or populations.

## 5. Technologies Used

- **Python** — data processing and application development
- **pandas** — data manipulation and analysis
- **NumPy** — numerical operations
- **scikit-learn** — machine-learning model development and prediction
- **joblib** — saving and loading the trained model
- **Streamlit** — interactive web application
- **Matplotlib** — data visualization
- **openpyxl** — Excel file support

## 6. Repository Structure

| File or folder | Purpose |
|---|---|
| `app.py` | Main Streamlit application |
| `anc_cleaned.xlsx` | Cleaned synthetic ANC dataset |
| `anc_missed_appointment_model.joblib` | Saved trained machine-learning model |
| `requirements.txt` | Python package dependencies |
| `README.md` | Project documentation |
| `*_chart.png` | Exploratory analysis charts |
| `*_summary.csv` | Summary tables for individual variables |
| `comparison_summary.csv` | Comparison of missed-appointment rates across selected variables |
| `draft_findings.md` | Draft findings from the exploratory analysis |
| `.gitignore` | Specifies files to exclude from Git version control |

## 7. Running the Application Locally

### Prerequisites

- Python installed on your computer
- pip, the Python package installer
- Git, if you want to clone the repository

### Step 1: Clone the repository

```bash
git clone https://github.com/Nazeer0943/anc-missed-appointments.git
cd anc-missed-appointments
```

Alternatively, download the repository as a ZIP file from GitHub and extract it.

### Step 2: Create a virtual environment

```bash
python -m venv .venv
```

Activate the environment on Windows:

```bash
.venv\Scripts\activate
```

On macOS or Linux:

```bash
source .venv/bin/activate
```

### Step 3: Install dependencies

```bash
python -m pip install -r requirements.txt
```

### Step 4: Launch the application

```bash
streamlit run app.py
```

After Streamlit starts, open the local URL displayed in the terminal, usually `http://localhost:8501`.

Ensure that the dataset and saved model are available at the file paths expected by `app.py`.

## 8. Live Deployment

The application is hosted on Streamlit Community Cloud.

**Access the application:** [https://anc-missed-appointments-huc5petjhmw4zst6s8ae3y.streamlit.app/](https://anc-missed-appointments-huc5petjhmw4zst6s8ae3y.streamlit.app/)

## 9. Limitations and Responsible Use

This project uses synthetic data and is intended for educational demonstration. The exploratory findings describe patterns within the dataset and do not establish causation or prove that the same patterns occur in real-world healthcare settings.

Model predictions should not be interpreted as validated clinical assessments. Further validation using appropriate real-world data and relevant ethical and governance safeguards would be required before considering any real-world healthcare application.

## 10. Capstone Submission

**Programme:** eHealth Africa (eHA) First Data Science Cohort  
**Cohort:** Group 2  
**Project:** ANC Missed Appointments — Data Analysis and Prediction  
**Deliverables:** Exploratory analysis, data visualizations, summary tables, trained model integration, Streamlit dashboard, and project documentation.

This project demonstrates the use of data science tools to explore a healthcare-related problem and communicate analytical findings through an interactive application.
