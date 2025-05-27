import pandas as pd

# Step 1: Load Data
df = pd.read_csv('insurance_claims_dataset.csv', header=1)

# Step 2: Convert Dates to datetime
df['Claim_Date'] = pd.to_datetime(df['Claim_Date'])
df['Processed_Date'] = pd.to_datetime(df['Processed_Date'])

# Step 3: Calculate Days to Settle
df['Days_To_Settle'] = (df['Processed_Date'] - df['Claim_Date']).dt.days

# Step 4: KPI Calculations
total_claims = df.shape[0]
total_claim_amount = df['Claim_Amount'].sum()
average_claim_amount = df['Claim_Amount'].mean()
claim_status_counts = df['Claim_Status'].value_counts()
insurance_type_counts = df['Insurance_Type'].value_counts()
top_hospitals = df['Hospital_Name'].value_counts().head(5)
common_diagnoses = df['Diagnosis'].value_counts().head(5)
average_settlement_time = df['Days_To_Settle'].mean()
fraudulent_claims_percent = (df['Fraud_Flag'].str.lower() == 'yes').mean() * 100

# Step 5: Display Results
print("📊 Insurance Claims Dashboard KPIs")
print("----------------------------------")
print(f"Total Claims: {total_claims}")
print(f"Total Claim Amount: ₹{total_claim_amount:,.2f}")
print(f"Average Claim Amount: ₹{average_claim_amount:,.2f}")
print(f"Average Settlement Time (days): {average_settlement_time:.2f}")
print(f"Fraudulent Claims (%): {fraudulent_claims_percent:.2f}%")
print("\nClaim Status Distribution:")
print(claim_status_counts)
print("\nInsurance Type Breakdown:")
print(insurance_type_counts)
print("\nTop 5 Hospitals by Claims:")
print(top_hospitals)
print("\nMost Common Diagnoses:")
print(common_diagnoses)

import matplotlib.pyplot as plt

# Bar chart for claim status
claim_status_counts.plot(kind='bar', title='Claim Status Distribution', color='skyblue')
plt.xlabel("Status")
plt.ylabel("Number of Claims")
plt.tight_layout()
plt.show()

summary = {
    'Total Claims': [total_claims],
    'Total Claim Amount': [total_claim_amount],
    'Average Claim Amount': [average_claim_amount],
    'Average Settlement Time': [average_settlement_time],
    'Fraudulent Claims (%)': [fraudulent_claims_percent]
}
pd.DataFrame(summary).to_csv('insurance_kpis_summary.csv', index=False)

import streamlit as st
import pandas as pd

# Load the dataset
df = pd.read_csv('insurance_claims_dataset.csv', header=1)

# Convert date columns
df['Claim_Date'] = pd.to_datetime(df['Claim_Date'])
df['Processed_Date'] = pd.to_datetime(df['Processed_Date'])

# Calculate days to settle
df['Days_To_Settle'] = (df['Processed_Date'] - df['Claim_Date']).dt.days

# Calculate KPIs
total_claims = df.shape[0]
total_claim_amount = df['Claim_Amount'].sum()
average_claim_amount = df['Claim_Amount'].mean()
average_settlement_time = df['Days_To_Settle'].mean()
fraudulent_claims_percent = (df['Fraud_Flag'].str.lower() == 'yes').mean() * 100

# Page title
st.title("🩺 Insurance Claim Analysis Dashboard")

# KPI cards
col1, col2, col3 = st.columns(3)
col1.metric("Total Claims", total_claims)
col2.metric("Total Claim Amount", f"₹{total_claim_amount:,.2f}")
col3.metric("Avg. Claim Amount", f"₹{average_claim_amount:,.2f}")

col4, col5 = st.columns(2)
col4.metric("Avg. Settlement Time (Days)", f"{average_settlement_time:.2f}")
col5.metric("Fraudulent Claims (%)", f"{fraudulent_claims_percent:.2f}%")

# Visuals
st.subheader("📌 Claim Status Distribution")
st.bar_chart(df['Claim_Status'].value_counts())

st.subheader("📌 Insurance Type Breakdown")
st.bar_chart(df['Insurance_Type'].value_counts())

st.subheader("📌 Top 5 Hospitals by Claims")
st.bar_chart(df['Hospital_Name'].value_counts().head(5))

st.subheader("📌 Most Common Diagnoses")
st.bar_chart(df['Diagnosis'].value_counts().head(5))

import plotly.express as px


# 📌 Claim Status Distribution
st.subheader("📌 Claim Status Distribution")
claim_status_data = df['Claim_Status'].value_counts().reset_index()
claim_status_data.columns = ['Claim Status', 'Count']
fig1 = px.bar(claim_status_data,
              x='Claim Status', y='Count',
              color='Claim Status',
              color_discrete_sequence=['#4CAF50', '#FF9800', '#F44336'])  # green, orange, red
st.plotly_chart(fig1, use_container_width=True, key="claim_status_chart")

# 📌 Insurance Type Breakdown
st.subheader("📌 Insurance Type Breakdown")
insurance_type_data = df['Insurance_Type'].value_counts().reset_index()
insurance_type_data.columns = ['Insurance Type', 'Count']
fig2 = px.bar(insurance_type_data,
              x='Insurance Type', y='Count',
              color='Insurance Type',
              color_discrete_sequence=px.colors.qualitative.Set3)
st.plotly_chart(fig2, use_container_width=True, key="insurance_type_chart")

# 📌 Top 5 Hospitals by Claims
st.subheader("📌 Top 5 Hospitals by Claims")
hospital_data = df['Hospital_Name'].value_counts().head(5).reset_index()
hospital_data.columns = ['Hospital', 'Count']
fig3 = px.bar(hospital_data,
              x='Hospital', y='Count',
              color='Hospital',
              color_discrete_sequence=px.colors.sequential.Bluered)
st.plotly_chart(fig3, use_container_width=True, key="top_hospitals_chart")

# 📌 Most Common Diagnoses
st.subheader("📌 Most Common Diagnoses")
diagnosis_data = df['Diagnosis'].value_counts().head(5).reset_index()
diagnosis_data.columns = ['Diagnosis', 'Count']
fig4 = px.bar(diagnosis_data,
              x='Diagnosis', y='Count',
              color='Diagnosis',
              color_discrete_sequence=px.colors.qualitative.Pastel)
st.plotly_chart(fig4, use_container_width=True, key="common_diagnosis_chart")

# 📌 Insurance Type Breakdown
st.subheader("📌 Insurance Type Breakdown")
insurance_type_data = df['Insurance_Type'].value_counts().reset_index()
insurance_type_data.columns = ['Insurance Type', 'Count']
fig5 = px.bar(insurance_type_data,
              x='Insurance Type', y='Count',
              color='Insurance Type',
              color_discrete_sequence=px.colors.qualitative.Set3)
st.plotly_chart(fig5, use_container_width=True, key="insurance_type_chart_v2")

# 📌 Top 5 Hospitals by Claims
st.subheader("📌 Top 5 Hospitals by Claims")
hospital_data = df['Hospital_Name'].value_counts().head(5).reset_index()
hospital_data.columns = ['Hospital', 'Count']
fig6 = px.bar(hospital_data,
              x='Hospital', y='Count',
              color='Hospital',
              color_discrete_sequence=px.colors.sequential.Bluered)
st.plotly_chart(fig6, use_container_width=True, key="top_hospitals_chart_v2")

# 📌 Most Common Diagnoses
st.subheader("📌 Most Common Diagnoses")
diagnosis_data = df['Diagnosis'].value_counts().head(5).reset_index()
diagnosis_data.columns = ['Diagnosis', 'Count']
fig7 = px.bar(diagnosis_data,
              x='Diagnosis', y='Count',
              color='Diagnosis',
              color_discrete_sequence=px.colors.qualitative.Pastel)
st.plotly_chart(fig7, use_container_width=True, key="common_diagnosis_chart_v2")