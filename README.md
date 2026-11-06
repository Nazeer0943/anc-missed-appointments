# ANC Missed Appointments: Data Analysis and Prediction

**Capstone Project | eHealth Africa (eHA) First Data Science Cohort — Group 2**

**Live Application:** <a href=https://anc-missed-appointments-huc5petjhmw4zst6s8ae3y.streamlit.app/ target="_blank">ANC Missed Appointments Dashboard</a> <br />
**Project Slide:** <a href= "https://docs.google.com/presentation/d/1yScVlJ3MSmToZw21XSjMdjKrl1Tbpb-zeiWj0FnIxeY/edit?slide=id.p1#slide=id.p1" target="_blank">Click Here</a>

## 1. Project Overview

Missed antenatal care appointments may interrupt continuity of monitoring, counselling and follow-up. This capstone demonstrates an end-to-end data science workflow: inspect and prepare an appointment dataset, explore attendance patterns, examine statistical associations, compare machine learning classifiers and deploy an interactive prediction dashboard.

The ANC Missed Appointments project explores patterns associated with missed antenatal care (ANC) appointments using a synthetic dataset. It combines exploratory data analysis, data visualization, summary statistics, and a machine-learning prediction interface in an interactive Streamlit application.

This project was developed as a capstone submission for the eHealth Africa (eHA) First Data Science Cohort, Group 2, demonstrating the application of data science techniques to a maternal healthcare attendance scenario.

## 2. Project Objectives

- Explore patterns in missed and attended ANC appointments.
- Examine missed-appointment rates across selected demographic, socioeconomic, and appointment-related characteristics.
- Present findings through interactive visualizations and summary tables.
- Integrate a trained machine-learning model into a Streamlit application.
- Demonstrate how data analysis and machine learning can support the exploration of healthcare attendance patterns.

- Aim
To determine the prevalence and factors associated with missed antenatal care appointments in an AI generated dataset.

Specific objectives
1.To determine the prevalence of missed ANC appointments.
2.To assess the pattern of missed ANC appointments.
3.To identify the factors associated with missed ANC appointments. 

Research questions
1.What is the prevalence of missed ANC appointments?
2.What is the pattern of missing ANC appointments among women?
3.What are the factors associated with missing ANC appointments?

## 3. Group members and contributions

| Member | Group role / workstream | Contribution to the capstone |
|---|---|---|
| **Sadika Ali Abarshi** | **Group Lead; end-to-end project documentation and presentation** | Led and coordinated the group; Consolidated the team's work into the overall capstone documentation and prepared the full PowerPoint presentation to showcase all workstreams. Oversaw integration and final presentation of deliverables. |
| **Carol Namutenda** | Data Management and Cleaning | Worked on dataset inspection, preparation, data-quality checks, documenting anomalies and producing clean-data outputs and preparation notes. |
| **Laura Domiah Chalansi** | Statistical Analysis and Visualisation | Worked on descriptive statistical analysis, exploring appointment attendance patterns, charts and interpretation of findings. |
| **Abba Daniel** | Machine Learning and Model Evaluation | Worked on predictive modelling, feature preprocessing, patient-grouped validation, model comparison, evaluation and model handoff documentation. |
| **Nazir Sani** | Streamlit Application and GitHub | Worked on the interactive Streamlit application, integration of the saved model into the user interface and the GitHub/deployment workstream. |

## 4. Data source, unit of analysis and preparation

The supplied file, `synthetic_anc_missed_appointments.csv`, is an **artificial appointment-level dataset**; its generation process, real clinical setting and observation dates are not verifiable from the provided material.
The project uses a synthetic ANC dataset containing 1,800 valid records, as reported in the exploratory analysis findings.
The dataset supports demonstration and educational analysis. Its results should not be interpreted as representative of actual patients, healthcare facilities, or populations.

| Property | Value |
|---|---|
| Scheduled appointment records | **1,800** |
| Distinct synthetic patient identifiers | **574** |
| Dataset columns | **25** |
| Missing values reported | **0** |
| Target | `missed_appointment`: **1 = missed; 0 = not missed** |
| Unit of analysis | **One scheduled appointment, not one unique woman** |

Variables include residence, insurance, reminder status, phone access, partner support, history of missed appointments, travel distance, waiting time, age and appointment type. The preparation work found no missing cells, exact duplicate rows or duplicate appointment IDs. No source rows were deleted or imputed. **558 records** in repeated patient-ID/appointment-number groups were flagged for review but retained because their appointment IDs differed and pregnancy-episode definitions were unavailable. Missing-data checks and duplicate checks are distinct from proof that all source definitions are valid.

## 5. Main findings

**Descriptive results (synthetic appointment records):**

- **1,092 of 1,800 appointments (60.7%)** were labelled missed; **708 (39.3%)** were not missed.
- Recorded missed-appointment shares were **64.2%** for rural, **61.1%** for peri-urban and **56.5%** for urban appointments.
- Records without reliable phone access had a **74.5%** missed share; records with a reminder sent had **57.6%**, versus **65.6%** where no reminder was sent.
- These comparisons are descriptive; they do not demonstrate that any specific intervention caused better attendance.

**Held-out predictive performance** (352 appointment records):

| Model | Accuracy | ROC-AUC |
|---|---:|---:|
| Always-missed baseline | 62.5% | 0.500 |
| **Tuned logistic regression — selected** | **68.5%** | **0.729** |
| Tuned random forest | 68.5% | 0.725 |
| Untuned XGBoost | 61.9% | 0.639 |

The selected tuned logistic regression offered the highest reported ROC-AUC among these candidates and an interpretable, deployable pipeline. For the missed class, the reported recall was **81.8% (180/220)**. The confusion matrix also showed **71 false-positive missed flags** and **40 missed-class false negatives**. Results apply only to the simulated test sample and are not evidence of operational effectiveness in real ANC settings.

The project's separate exploratory regression report describes positive adjusted associations for previous missed appointments, distance to facility and low/absent partner support, and inverse associations for health insurance and reliable phone access. Because the dataset is synthetic, these estimates must not be generalised to real patients.

## 6. Application Features

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

## 7. Technologies Used

- **Python** — data processing and application development
- **pandas** — data manipulation and analysis
- **NumPy** — numerical operations
- **scikit-learn** — machine-learning model development and prediction
- **joblib** — saving and loading the trained model
- **Streamlit** — interactive web application
- **Matplotlib** — data visualization
- **openpyxl** — Excel file support

## 8. Repository Structure

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

## 9. Running the Application Locally

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

## 11. Limitations, ethics and future work

- **Synthetic data:** Dataset patterns reflect an artificial generation process; they cannot establish real ANC prevalence, causal effects or clinical risk.
- **Repeated observations:** Multiple appointments per patient require patient-grouped validation and appropriate handling of within-patient correlation.
- **Unresolved source definitions:** Pregnancy episode boundaries, appointment chronology and transport-cost currency were not confirmed.
- **Outcome scope:** The dataset has no maternal complication, birth-outcome or neonatal endpoints.
- **Model validation:** Real-world deployment would require representative clinical data, external validation, calibration and fairness assessment, data privacy safeguards, ethical and institutional approvals, and clinical governance.

Potential extensions include evaluating routinely collected, appropriately governed ANC attendance records; confirming a prospective prediction time point; measuring calibration and subgroup performance; and assessing reminder workflows only after appropriate evaluation. **No findings from the synthetic dataset should be used to target or deny care.**

## 12. References and acknowledgements

1. World Health Organization. *WHO recommendations on antenatal care for a positive pregnancy experience*. Geneva: WHO; 2016. https://www.who.int/publications/i/item/9789241549912
