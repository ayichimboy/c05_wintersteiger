############################################################
#-------------------------------Import Libraries----------##
############################################################

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import smartsheet
import streamlit as st

###############################################################
##-------------------------import the smartsheet ----------####
###############################################################
API_TOKEN  = "4jPmJP29lZilsAf60FllSXAeX4A0uR29MXaSc"
smartsheet_client = smartsheet.Smartsheet(API_TOKEN)


##############################################################
##-------ooo--CONTROL SAMPLE OIL ANALYSIS--ooo--------------##
##############################################################


##--------------------New Wintersteiger Combine Harvester ---------
c05_oil = "4062998129758084"
sheet_c05oil = smartsheet_client.Sheets.get_sheet(c05_oil)

# Extract data and column names
columns_c05oil = [col.title for col in sheet_c05oil.columns]
data_c05oil = []

for row in sheet_c05oil.rows:
    row_data = {}
    for cell, col in zip(row.cells, columns_c05oil):
        row_data[col] = cell.value
    data_c05oil.append(row_data)

# Convert to DataFrame
df_c05oil = pd.DataFrame(data_c05oil)
df_c05oil = df_c05oil.dropna(subset = ['Measured Oil'])
df_c05oil["Date Created"] = pd.to_datetime(df_c05oil["Date Created"])
df_c05oil = df_c05oil.sort_values("Date Created")



##--------------------Old Wintersteiger Combine Harvester --------------
c01_oil = "7751120906571652"
sheet_c01oil = smartsheet_client.Sheets.get_sheet(c01_oil)

# Extract data and column names
columns_c01oil = [col.title for col in sheet_c01oil.columns]
data_c01oil = []

for row in sheet_c01oil.rows:
    row_data = {}
    for cell, col in zip(row.cells, columns_c01oil):
        row_data[col] = cell.value
    data_c01oil.append(row_data)

# Convert to DataFrame
df_c01oil = pd.DataFrame(data_c01oil)

df_c01oil = df_c01oil.dropna(subset = ['Measured Oil'])
df_c01oil["Date Created"] = pd.to_datetime(df_c01oil["Date Created"])
df_c01oil = df_c01oil.sort_values("Date Created")



##-------------------ALMACO R1 COMBINE HARVESTER --------------

c02_oil =  "7534664352747396"
sheet_c02oil = smartsheet_client.Sheets.get_sheet(c02_oil)

# Extract data and column names
columns_c02oil = [col.title for col in sheet_c02oil.columns]
data_c02oil = []

for row in sheet_c02oil.rows:
    row_data = {}
    for cell, col in zip(row.cells, columns_c02oil):
        row_data[col] = cell.value
    data_c02oil.append(row_data)

# Convert to DataFrame
df_c02oil = pd.DataFrame(data_c02oil)

df_c02oil = df_c02oil.dropna(subset = ['Measured Oil'])
df_c02oil["Date Created"] = pd.to_datetime(df_c02oil["Date Created"])
df_c02oil = df_c02oil.sort_values("Date Created")

############################################################
##---------------CONTROL SAMPLE PROTEIN ANALYSIS----------##
############################################################


##-------------New Wintersteiger Combine Harvester ---------

c05_protein = "6368329476296580"
sheet_c05protein = smartsheet_client.Sheets.get_sheet(c05_protein)

# Extract data and column names
columns_c05protein = [col.title for col in sheet_c05protein.columns]
data_c05protein = []

for row in sheet_c05protein.rows:
    row_data = {}
    for cell, col in zip(row.cells, columns_c05protein):
        row_data[col] = cell.value
    data_c05protein.append(row_data)
    
# Convert to DataFrame
df_c05protein = pd.DataFrame(data_c05protein)
df_c05protein['Measured Protein'] = df_c05protein['Measured Protein'].replace(['N/A', 'NA'], pd.NA)
df_c05protein = df_c05protein.dropna(subset=['Measured Protein'])
#df_c05protein = df_c05protein[df_c05protein['Date'].dt.year == 2024]
df_c05protein = df_c05protein[df_c05protein["Measured Protein"] > 35]
df_c05protein["Date Created"] = pd.to_datetime(df_c05protein["Date Created"])
df_c05protein = df_c05protein.sort_values("Date Created")

# Convert to DataFrame
#df_c05protein = pd.DataFrame(data_c05protein)
#df_c05protein = df_c05protein.dropna(subset = ['Measured Protein'])
#df_c05protein["Date Created"] = pd.to_datetime(df_c05protein["Date Created"])
#df_c05protein = df_c05protein.sort_values("Date Created")



##--------------------Old Wintersteiger Combine Harvester --------------
c01_protein = "8313891545108356"
sheet_c01protein = smartsheet_client.Sheets.get_sheet(c01_protein)

# Extract data and column names
columns_c01protein = [col.title for col in sheet_c01protein.columns]
data_c01protein = []

for row in sheet_c01protein.rows:
    row_data = {}
    for cell, col in zip(row.cells, columns_c01protein):
        row_data[col] = cell.value
    data_c01protein.append(row_data)

# Convert to DataFrame
#df_c01protein = pd.DataFrame(data_c01protein)
#df_c01protein = df_c01protein.dropna(subset = ['Measured Protein'])
#df_c01protein["Date Created"] = pd.to_datetime(df_c01protein["Date Created"])
#df_c01protein = df_c01protein.sort_values("Date Created")


# Convert to DataFrame
df_c01protein = pd.DataFrame(data_c01protein)
df_c01protein['Measured Protein'] = df_c01protein['Measured Protein'].replace(['N/A', 'NA'], pd.NA)
df_c01protein = df_c01protein.dropna(subset=['Measured Protein'])
#df_c05protein = df_c05protein[df_c05protein['Date'].dt.year == 2024]
df_c01protein = df_c01protein[df_c01protein["Measured Protein"] > 35]
df_c01protein["Date Created"] = pd.to_datetime(df_c01protein["Date Created"])
df_c01protein = df_c01protein.sort_values("Date Created")

##-------------------ALMACO R1 COMBINE HARVESTER --------------

c02_protein =  "5100572034158468"
sheet_c02protein = smartsheet_client.Sheets.get_sheet(c02_protein)

# Extract data and column names
columns_c02protein = [col.title for col in sheet_c02protein.columns]
data_c02protein = []

for row in sheet_c02protein.rows:
    row_data = {}
    for cell, col in zip(row.cells, columns_c02protein):
        row_data[col] = cell.value
    data_c02protein.append(row_data)

# Convert to DataFrame
#df_c02protein = pd.DataFrame(data_c02protein)
#df_c02protein = df_c02protein.dropna(subset = ['Measured Protein'])
#df_c02protein["Date Created"] = pd.to_datetime(df_c02oil["Date Created"])
#df_c02protein = df_c02protein.sort_values("Date Created")

# Convert to DataFrame
df_c02protein = pd.DataFrame(data_c02protein)
df_c02protein['Measured Protein'] = df_c02protein['Measured Protein'].replace(['N/A', 'NA'], pd.NA)
df_c02protein = df_c02protein.dropna(subset=['Measured Protein'])
#df_c02protein = df_c02protein[df_c02protein['Date'].dt.year == 2024]
df_c02protein = df_c02protein[df_c02protein["Measured Protein"] > 35]
df_c02protein["Date Created"] = pd.to_datetime(df_c02protein["Date Created"])
df_c02protein = df_c02protein.sort_values("Date Created")

###---------------------------PLOT THE DATA-------------------------------

#####################################################################
#########--------------------------- PLOT OIL--------------------####
#####################################################################

##--------------------New Wintestersteiger Oil -----------------------
#print(df.head())
# Streamlit app title
st.title('Measured Oil Over Time')
# Display the DataFrame
#st.write('### Data', df_oil)

# Plot the data
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(df_c05oil['Date Created'], df_c05oil['Measured Oil'], marker='o', linestyle='-', color='g')

#mean
ax.axhline(y=19.028, color='black', linestyle='--', linewidth=1)
#2SD+
ax.axhline(y=19.605739, color='orange', linestyle='-.', linewidth=1)
#3SD+
ax.axhline(y=19.894609, color='r', linestyle='-.', linewidth=1)
#2SD-
ax.axhline(y=18.450261, color='orange', linestyle='-.', linewidth=1)
#3SD-
ax.axhline(y=18.161391, color='r', linestyle='-.', linewidth=1)

ax.set_title('Oil - C05 Wintersteiger [New]', fontsize = 16)
ax.set_xlabel('Date Analyzed', fontsize = 16)
ax.set_ylabel('Measured Oil', fontsize = 16)
#ax.plt.grid(False)
ax.grid(False)
#ax.tick_params(axis='x', rotation=45, labelsize=16)
# Set x-ticks to match the dates in the data

ax.set_xticks(df_c05oil['Date Created'])
ax.set_xticklabels(df_c05oil['Date Created'].dt.strftime("%Y-%m-%d"), rotation=90)
#ax.xticks(rotation = 90,ticks = df_c05oil['Date Created'],labels = df_c05oil['Date Created'].dt.strftime("%Y-%m-%d"))

ax.tick_params(axis='y', labelsize=16)
#ax.legend(fontsize=16)
st.pyplot(fig)


##----------------------------Old Wintersteiger Oil -------------------

#print(df.head())
# Streamlit app title
st.title('Measured Oil Over Time')

# Display the DataFrame
#st.write('### Data', df_oil)
# Plot the data
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(df_c01oil['Date Created'], df_c01oil['Measured Oil'], marker='o', linestyle='-', color='g')

#mean
ax.axhline(y=19.028, color='black', linestyle='--', linewidth=1)
#2SD+
ax.axhline(y=19.605739, color='orange', linestyle='-.', linewidth=1)
#3SD+
ax.axhline(y=19.894609, color='r', linestyle='-.', linewidth=1)
#2SD-
ax.axhline(y=18.450261, color='orange', linestyle='-.', linewidth=1)
#3SD-
ax.axhline(y=18.161391, color='r', linestyle='-.', linewidth=1)

ax.set_title('Oil - C01 Wintersteiger [Old]', fontsize = 16)
ax.set_xlabel('Date Analyzed', fontsize = 16)
ax.set_ylabel('Measured Oil', fontsize = 16)
#ax.plt.grid(False)
ax.grid(False)
#ax.tick_params(axis='x', rotation=45, labelsize=16)
ax.set_xticks(df_c01oil['Date Created'])
ax.set_xticklabels(df_c01oil['Date Created'].dt.strftime("%Y-%m-%d"), rotation=90)
#ax.xticks(rotation = 90,ticks = df_c01oil['Date Created'],labels = df_c01oil['Date Created'].dt.strftime("%Y-%m-%d"))
ax.tick_params(axis='y', labelsize=16)
#ax.legend(fontsize=16)
st.pyplot(fig)


##-----------------------ALMACO R1 OIL------------------
#print(df.head())
# Streamlit app title
st.title('Measured Oil Over Time')

# Display the DataFrame
#st.write('### Data', df_oil)

# Plot the data
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(df_c02oil['Date Created'], df_c02oil['Measured Oil'], marker='o', linestyle='-', color='g')


#mean
ax.axhline(y=19.33614, color='black', linestyle='--', linewidth=1)
#2SD+
ax.axhline(y=19.66411, color='orange', linestyle='-.', linewidth=1)
#3SD+
ax.axhline(y=19.8281, color='r', linestyle='-.', linewidth=1)
#2SD-
ax.axhline(y=19.00816, color='orange', linestyle='-.', linewidth=1)
#3SD-
ax.axhline(y=18.84417, color='r', linestyle='-.', linewidth=1)



ax.set_title('Oil - C01 Almaco R1', fontsize = 16)
ax.set_xlabel('Date Analyzed', fontsize = 16)
ax.set_ylabel('Measured Oil', fontsize = 16)
#ax.plt.grid(False)
ax.grid(False)
#ax.tick_params(axis='x', rotation=45, labelsize=16)
ax.set_xticks(df_c02oil['Date Created'])
ax.set_xticklabels(df_c02oil['Date Created'].dt.strftime("%Y-%m-%d"), rotation=90)
#ax.xticks(rotation = 90,ticks = df_c02oil['Date Created'],labels = df_c02oil['Date Created'].dt.strftime("%Y-%m-%d"))
ax.tick_params(axis='y', labelsize=16)
#ax.legend(fontsize=16)
st.pyplot(fig)



################################################################
####-----------------------PLOT PROTEIN-----------------------##
################################################################


##--------------------New Wintestersteiger Protein ------------------
#print(df.head())
# Streamlit app title
st.title('Measured Protein Over Time')
# Display the DataFrame
#st.write('### Data', df_oil)

# Plot the data
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(df_c05protein['Date Created'], df_c05protein['Measured Protein'], marker='o', linestyle='-', color='g')

#mean
ax.axhline(y=44.74867, color='black', linestyle='--', linewidth=1)
#2SD+
ax.axhline(y=45.69376, color='orange', linestyle='-.', linewidth=1)
#3SD+
ax.axhline(y=46.1663, color='r', linestyle='-.', linewidth=1)
#2SD-
ax.axhline(y=43.80358, color='orange', linestyle='-.', linewidth=1)
#3SD-
ax.axhline(y=43.33103, color='r', linestyle='-.', linewidth=1)


ax.set_title('Protein - C05 Wintersteiger [New]', fontsize = 16)
ax.set_xlabel('Date Analyzed', fontsize = 16)
ax.set_ylabel('Measured Protein', fontsize = 16)
#ax.plt.grid(False)
ax.grid(False)
#ax.tick_params(axis='x', rotation=45, labelsize=16)
ax.set_xticks(df_c05protein['Date Created'])
ax.set_xticklabels(df_c05protein['Date Created'].dt.strftime("%Y-%m-%d"), rotation=90)
#ax.xticks(rotation = 90,ticks = df_c05protein['Date Created'],labels = df_c05protein['Date Created'].dt.strftime("%Y-%m-%d"))
ax.tick_params(axis='y', labelsize=16)
#ax.legend(fontsize=16)
st.pyplot(fig)


##----------------------------Old Wintersteiger Protein -------------------

#print(df.head())
# Streamlit app title
st.title('Measured Protein Over Time')

# Display the DataFrame
#st.write('### Data', df_oil)
# Plot the data
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(df_c01protein['Date Created'], df_c01protein['Measured Protein'], marker='o', linestyle='-', color='g')

#mean
ax.axhline(y=44.62272, color='black', linestyle='--', linewidth=1)
#2SD+
ax.axhline(y=46.94681, color='orange', linestyle='-.', linewidth=1)
#3SD+
ax.axhline(y=48.10886, color='r', linestyle='-.', linewidth=1)
#2SD-
ax.axhline(y=42.298636, color='orange', linestyle='-.', linewidth=1)
#3SD-
ax.axhline(y=41.13658, color='r', linestyle='-.', linewidth=1)


ax.set_title('Protein - C01 Wintersteiger [Old]', fontsize = 16)
ax.set_xlabel('Date Analyzed', fontsize = 16)
ax.set_ylabel('Measured Protein', fontsize = 16)
#ax.plt.grid(False)
ax.grid(False)
#ax.tick_params(axis='x', rotation=45, labelsize=16)
ax.set_xticks(df_c01protein['Date Created'])
ax.set_xticklabels(df_c01protein['Date Created'].dt.strftime("%Y-%m-%d"), rotation=90)
#ax.xticks(rotation = 90,ticks = df_c01protein['Date Created'],labels = df_c01protein['Date Created'].dt.strftime("%Y-%m-%d"))
ax.tick_params(axis='y', labelsize=16)
#ax.legend(fontsize=16)
st.pyplot(fig)



##-----------------------ALMACO R1 Protein--------------------------------
#print(df.head())
# Streamlit app title
st.title('Measured Protein Over Time')

# Display the DataFrame
#st.write('### Data', df_oil)

# Plot the data
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(df_c02protein['Date Created'], df_c02protein['Measured Protein'], marker='o', linestyle='-', color='g')


#mean
#mean
ax.axhline(y=43.8499, color='black', linestyle='--', linewidth=1)
#2SD+
ax.axhline(y=44.94593, color='orange', linestyle='-.', linewidth=1)
#3SD+
ax.axhline(y=45.49395, color='r', linestyle='-.', linewidth=1)
#2SD-
ax.axhline(y=42.75387, color='orange', linestyle='-.', linewidth=1)
#3SD-
ax.axhline(y=42.20585, color='r', linestyle='-.', linewidth=1)



ax.set_title('Protein - C01 Almaco R1', fontsize = 16)
ax.set_xlabel('Date Analyzed', fontsize = 16)
ax.set_ylabel('Measured Protein', fontsize = 16)
#ax.plt.grid(False)
ax.grid(False)
#ax.tick_params(axis='x', rotation=45, labelsize=16)
ax.set_xticks(df_c02protein['Date Created'])
ax.set_xticklabels(df_c02protein['Date Created'].dt.strftime("%Y-%m-%d"), rotation=90)
#ax.xticks(rotation = 90,ticks = df_c02protein['Date Created'],labels = df_c02protein['Date Created'].dt.strftime("%Y-%m-%d"))
ax.tick_params(axis='y', labelsize=16)
#ax.legend(fontsize=16)
st.pyplot(fig)



###---------------------ooo----END------ooo---------------------------------------###
