
from pathlib import Path

import joblib
import pandas as pd
import streamlit as st

# --------------------------------------------------
# 1. Application configuration
# --------------------------------------------------
BASE_DIR = Path(__file__).parent
MODEL_PATH = BASE_DIR / "anc_missed_appointment_model.joblib"

st.set_page_config(
    page_title="ANC Missed Appointment Dashboard",
    page_icon="📋",
    layout="wide"
)

st.title("ANC Missed Appointment Dashboard")
st.caption(
    "Machine-learning demonstration using a synthetic ANC dataset. "
    "Not for clinical or real-patient decisions."
)

# --------------------------------------------------
# 2. Load the trained model
# --------------------------------------------------
@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)


# --------------------------------------------------
# 3. Dashboard
# --------------------------------------------------
dashboard_tab, prediction_tab, about_tab = st.tabs(
    ["📊 Dashboard", "🔮 Predict", "ℹ️ About"]
)

with dashboard_tab:
    st.header("Exploratory Analysis")

    st.info(
        "The charts and summaries below are generated from the "
        "team's synthetic-data analysis."
    )

    chart_files = sorted(BASE_DIR.glob("*_chart.png"))

    if chart_files:
        for start in range(0, len(chart_files), 2):
            cols = st.columns(2)

            for col, chart_path in zip(
                cols, chart_files[start:start + 2]
            ):
                with col:
                    st.subheader(
                        chart_path.stem.replace("_", " ").title()
                    )
                    st.image(
                        str(chart_path),
                        use_container_width=True
                    )
    else:
        st.warning(
            "No chart images were found. Upload the analysis "
            "PNG files to the repository's root folder."
        )

    with st.expander("View analysis summary tables"):
        summary_files = sorted(BASE_DIR.glob("*_summary.csv"))

        if summary_files:
            for csv_path in summary_files:
                st.subheader(
                    csv_path.stem.replace("_", " ").title()
                )
                try:
                    summary = pd.read_csv(csv_path)
                    st.dataframe(summary, use_container_width=True)
                except Exception as exc:
                    st.error(
                        f"Could not read {csv_path.name}: {exc}"
                    )
        else:
            st.info("No summary CSV files were found.")

    findings_path = BASE_DIR / "draft_findings.md"
    if findings_path.exists():
        with st.expander("Read draft findings"):
            st.markdown(
                findings_path.read_text(encoding="utf-8")
            )


# --------------------------------------------------
# 4. Prediction form
# --------------------------------------------------
with prediction_tab:
    st.header("Missed Appointment Prediction")

    st.write(
        "Enter the characteristics of one appointment. "
        "The model returns an estimated probability that "
        "the appointment will be missed."
    )

    with st.form("anc_prediction_form"):

        st.subheader("Patient and appointment characteristics")

        c1, c2, c3 = st.columns(3)

        with c1:
            maternal_age_years = st.number_input(
                "Maternal age (years)", 16, 45, 28
            )
            parity = st.number_input(
                "Parity", 0, 5, 1
            )
            appointment_number = st.number_input(
                "Appointment number", 1, 8, 1
            )

        with c2:
            gestational_age_weeks = st.number_input(
                "Gestational age (weeks)", 6, 42, 20
            )
            distance_to_facility_km = st.number_input(
                "Distance to facility (km)",
                min_value=0.3,
                max_value=35.0,
                value=5.0,
                step=0.1
            )
            estimated_round_trip_transport_cost = st.number_input(
                "Estimated round-trip transport cost",
                min_value=0,
                max_value=5247,
                value=500
            )

        with c3:
            usual_wait_time_minutes = st.number_input(
                "Usual waiting time (minutes)", 15, 205, 60
            )
            previous_missed_appointments = st.number_input(
                "Previous missed appointments", 0, 3, 0
            )
            days_between_booking_and_visit = st.number_input(
                "Days between booking and visit", 1, 21, 7
            )

        st.subheader("Social and service characteristics")

        categorical_options = {
            "residence": [
                "Peri-urban", "Rural", "Urban"
            ],
            "education_level": [
                "No formal education", "Primary",
                "Secondary", "Tertiary"
            ],
            "employment_status": [
                "Formal employment",
                "Informal/self-employed",
                "Student", "Unemployed"
            ],
            "health_insurance": ["No", "Yes"],
            "partner_support": [
                "High", "Low/None", "Moderate"
            ],
            "phone_access": [
                "No reliable phone", "Personal phone",
                "Shared phone"
            ],
            "chronic_condition_reported": ["No", "Yes"],
            "reminder_sent": ["No", "Yes"],
            "usual_transport_mode": [
                "Motorcycle/tricycle", "Private vehicle",
                "Public transport", "Walking"
            ],
            "appointment_day": [
                "Friday", "Monday", "Saturday",
                "Thursday", "Tuesday", "Wednesday"
            ],
            "season": ["Dry season", "Rainy season"],
            "appointment_type": [
                "Follow-up", "High-risk review", "Routine ANC"
            ],
            "barrier_reported_at_booking": [
                "Feeling unwell", "Forgot appointment",
                "Long waiting time", "None reported",
                "Transport cost", "Work/family duties"
            ]
        }

        # Arrange the categorical inputs in three columns.
        cat_columns = st.columns(3)
        categorical_values = {}

        for index, (feature, options) in enumerate(
            categorical_options.items()
        ):
            with cat_columns[index % 3]:
                categorical_values[feature] = st.selectbox(
                    feature.replace("_", " ").title(),
                    options,
                    key=f"input_{feature}"
                )

        submitted = st.form_submit_button(
            "Predict Missed Appointment",
            type="primary",
            use_container_width=True
        )

    if submitted:
        # Column names must match the model documentation exactly.
        input_data = {
            "residence": categorical_values["residence"],
            "education_level": categorical_values["education_level"],
            "employment_status": categorical_values["employment_status"],
            "health_insurance": categorical_values["health_insurance"],
            "partner_support": categorical_values["partner_support"],
            "phone_access": categorical_values["phone_access"],
            "chronic_condition_reported": categorical_values[
                "chronic_condition_reported"
            ],
            "reminder_sent": categorical_values["reminder_sent"],
            "usual_transport_mode": categorical_values[
                "usual_transport_mode"
            ],
            "appointment_day": categorical_values["appointment_day"],
            "season": categorical_values["season"],
            "appointment_type": categorical_values["appointment_type"],
            "barrier_reported_at_booking": categorical_values[
                "barrier_reported_at_booking"
            ],
            "maternal_age_years": maternal_age_years,
            "parity": parity,
            "appointment_number": appointment_number,
            "gestational_age_weeks": gestational_age_weeks,
            "distance_to_facility_km": distance_to_facility_km,
            "estimated_round_trip_transport_cost":
                estimated_round_trip_transport_cost,
            "usual_wait_time_minutes": usual_wait_time_minutes,
            "previous_missed_appointments":
                previous_missed_appointments,
            "days_between_booking_and_visit":
                days_between_booking_and_visit
        }

        try:
            model = load_model()
            input_df = pd.DataFrame([input_data])

            probability = float(
                model.predict_proba(input_df)[0, 1]
            )
            predicted_class = int(model.predict(input_df)[0])

            st.subheader("Prediction Result")

            st.metric(
                "Estimated missed-appointment probability",
                f"{probability:.1%}"
            )

            st.progress(probability)

            if predicted_class == 1:
                st.warning(
                    "Model output: missed appointment predicted "
                    "at the default 0.5 threshold."
                )
            else:
                st.success(
                    "Model output: not-missed class predicted "
                    "at the default 0.5 threshold."
                )

            st.caption(
                "This is an experimental model prediction, not a "
                "validated clinical risk estimate. Do not use it "
                "to make decisions about real patients."
            )

        except Exception as exc:
            st.error(
                "The prediction could not be generated. "
                "Please check the model file, input columns, "
                "and compatible package versions."
            )
            st.exception(exc)


# --------------------------------------------------
# 5. Project information
# --------------------------------------------------
with about_tab:
    st.header("About this project")

    st.write(
        "This project demonstrates how a trained logistic "
        "regression pipeline can be integrated into a Streamlit "
        "application for exploring missed ANC appointments."
    )

    st.markdown("""
    **Model reference performance**

    - Test accuracy: 0.685 (68.5%)
    - Test ROC-AUC: 0.729
    - Baseline accuracy: 0.625 (62.5%)

    These results are from the team's held-out synthetic dataset.
    They are not evidence of performance on real patients.

    **Important limitations**

    - The dataset is synthetic.
    - The model has not been clinically validated.
    - Predictions must not be used for real-patient decisions.
    """)
