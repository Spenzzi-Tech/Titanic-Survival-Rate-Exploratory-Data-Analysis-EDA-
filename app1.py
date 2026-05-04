import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt
import base64

st.markdown("""
<style>
.block-container { padding-top: 1.5rem; }

/* KPI polish */
.metric-card h2 {
    font-size: 40px;
    margin-top: 8px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
div[data-testid="stContainer"] {
    background: black;
    border: 4px solid black;
    border-radius: 35px;
    padding: 20px;
    height: 420px;
    overflow: hidden;
    border-color: #ddd !important
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
   # st.markdown(
   # "<style>body { background-color: #FFFF00; }</style>", unsafe_allow_html=True)

# Add some content here...

    layout="wide"
                   )

def get_base64_of_file(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            return base64.b64encode(f.read()).decode()
    except Exception as e:
        st.error("Error reading file: " + str(e))
        return None

try:
    img_base64 = get_base64_of_file('image.jpg')
    if img_base64 is not None:
        st.markdown(
            f"""
            <style>
            /* Main background */
            .stApp {{
                #--background-image: url("data:image/jpeg;base64,{img_base64}");--#
                background-color:  #FFFF00;
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
                color: white;
            }}

            /* Text */
            h1, h4, h5, h6, p, span, label {{
                color: black !important;
            }}
            h2, h3, label {{
                color: white !important;
            }}

            /* Sidebar */
            section[data-testid="stSidebar"] {{
                background-color: #003262 !important;
            }}

            /* Input fields */
            input, textarea, select {{
                background-color: white !important;
                color: black !important;
                border: 1px solid #ccc;
            }}

            /* Buttons */
            button {{
                background-color: #f0f0f0 !important;
                color: black !important;
                border: 1px solid #ccc;
            }}

            </style>
            """,
            unsafe_allow_html=True
        )
    else:
        st.write("Failed to read image file.")
except FileNotFoundError:
    st.error("image.jpg not found. Make sure it is in the same folder")


# Inject CSS
st.markdown("""
<style>
/* Blue title-style filter label */
.filter-title {
    background-color: #003262;
    color: white;
    font-size: 13px;
    font-weight: 700;
    padding: 6px 10px;
    border-radius: 6px;
    margin-bottom: 4px;
    max-width: 200px;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)


# -----------------------------
# CSS
# -----------------------------
st.markdown("""
<style>

/* Target your specific container by its key */
.st-key-my_white_container {
    background-color: white !important;   /* pure white */
/* Optional extras for better look */
    border-radius: 10px;                  /* rounded corners */
    padding: 15px;                        /* inner spacing */
    box-shadow: 0 4px 8px rgba(0,0,0,0.1); /* subtle shadow */
}
/* If you want the border to be more visible or styled */
.st-key-my_white_container [data-testid="stDecoration"] {
    border-color: #ddd !important;        /* light gray border */
}

.title-box {
    border: 4px solid black;
    border-radius: 30px;
    padding: 20px;
    text-align: center;
    font-size: 34px;
    font-weight: bold;
    margin-bottom: 30px;
    background-color: #003262 !important;
}

.filter-box {
    border: 3px solid black;
    border-radius: 12px;
    padding: 10px;
    margin-bottom: 12px;
    text-align: center;
    font-weight: bold;
}

.panel {{
    border: 4px solid black;
    border-radius: 35px;
    height: 420px;
    padding: 20px;
    overflow: hidden;
    background-color:#003262 ;
    margin-buttom:20px:
    display block
}}
.metric-card {
    border: 2px solid black;
    border-radius: 20px;
    padding: 15px;
    text-align: center;
    background-color: #003262 !important;
}
.card {
    border: 2px solid black;
    border-radius: 25px;
    padding: 20px;
    margin-bottom: 20px;
    text-color: black !important;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# DATA
# -----------------------------
df = pd.read_csv("titanic.csv")

# -----------------------------
# TITLE
# -----------------------------
st.markdown(
    "<div class='title-box'>Titanic Survival Rate Exploratory Data Analysis (EDA)</div>",
    unsafe_allow_html=True
)

 #gender_ratio= [[df('sex').unique]/ len[df('sex')]] * 100

df = df.dropna(subset=['Age'])

# -----------------------------
# KPI METRICS
# -----------------------------
sidebar,kpi1, kpi2, kpi3 = st.columns(4)
with sidebar:
    st.markdown("""
<style>
/* 🔵 Blue filter title */
.filter-title {
    background-color: #003262;
    color: white;
    font-size: 17px;
    font-weight: 700;
    padding: 6px 10px;
    border-radius: 6px;
    margin-bottom: 6px;
    max-width: 400px;
    align-self: center;
    justify-content: space-between
    body-align: center;
}

/* ⬜ OUTER select container */
div[data-baseweb="select"] {
    max-width: 400px;
}

/* ⬜ ACTUAL input box */
div[role="combobox"] {
    background-color: white !important;
    border: 1px solid #e5e7eb !important;
    border-radius: 6px !important;
    min-height: 34px !important;
    margin-bottom: 10px !important;
}

/* ⬜ Text inside input */
div[role="combobox"] * {
    color: #111827 !important;
    font-size: 12px !important;
}

/* ⬜ Selected value chips */
div[data-baseweb="tag"] {
    background-color: #f3f4f6 !important;
    color: #111827 !important;
    height: 20px !important;
    font-size: 11px !important;
    padding: 0px 6px !important;
    margin: 2px !important;
    border-radius: 4px !important;
}

/* ⬜ Dropdown arrow */
div[role="combobox"] svg {
    fill: #374151 !important;
    width: 14px !important;
    height: 14px !important;
}

/* ⬜ Dropdown list */
div[data-baseweb="menu"] {
    background-color: white !important;
    border-radius: 6px !important;
}
</style>
""", unsafe_allow_html=True)


    # Gender
    st.markdown("<div class='filter-title'>Gender</div>", unsafe_allow_html=True)
    sex = st.multiselect(
        label="",
        options=df["Sex"].unique(),
        label_visibility="collapsed"
    )
    # Class
    st.markdown("<div class='filter-title'>Class</div>", unsafe_allow_html=True)
    pclass = st.multiselect(
        label="",
        options=df["Pclass"].unique(),
        label_visibility="collapsed"
    )

    # Embarked
    st.markdown("<div class='filter-title'>Embarked</div>", unsafe_allow_html=True)
    embarked = st.multiselect(
        label="",
        options=df["Embarked"].dropna().unique(),
        label_visibility="collapsed"
    )
    # Age
    min_age = int(df["Age"].min())
    max_age = int(df["Age"].max())
    st.markdown("<div class='filter-title'>Select Age Range</div>", unsafe_allow_html=True)
    age_range = st.slider(
        label="",
        min_value=min_age,
        max_value=max_age,
        value=(min_age, max_age)
    )
df = df[(df['Sex'].isin(sex))&(df['Pclass'].isin(pclass)) &
        ((df['Age'] >= age_range[0]) & (df['Age'] <= age_range[1])) |
        (df['Embarked'].isin(embarked))]


Adult = (df["Age"] >= 18).sum()
Children = (df['Age'] < 18).sum()
with kpi1:
    st.markdown(
        f"<div class='metric-card'><h3>Total Passengers</h3><h2>{len(df)}</h2></div>",
        unsafe_allow_html=True
    )
    st.write("")
    st.markdown(
        f"<div class='metric-card'><h3>Survived</h3><h2>{(df['Survived']==1).sum()}</h2></div>",
        unsafe_allow_html=True
    )

with kpi2:
    survival_rate = round(df["Survived"].mean() * 100, 2)
    st.markdown(
        f"<div class='metric-card'><h3>Survival Rate</h3><h2>{survival_rate}%</h2></div>",
        unsafe_allow_html=True
    )
    st.write("")
    st.markdown(
        f"<div class='metric-card'><h3>Adult</h3><h2>{Adult}</h2></div>",
        unsafe_allow_html=True
    )

with kpi3:
    st.markdown(
        f"<div class='metric-card'><h3>Deaths</h3><h2>{(df['Survived']==0).sum()}</h2></div>",
        unsafe_allow_html=True
    )
    st.write("")
    st.markdown(
        f"<div class='metric-card'><h3>Children</h3><h2>{Children}</h2></div>",
        unsafe_allow_html=True
    )

st.write("")
# -----------------------------
# LAYOUT
# -----------------------------

# ----
# Filter data


left_panel, spacer, right_panel = st.columns([1, 0.05, 1])

with left_panel:
    sex_survival = (
df.groupby("Sex")["Survived"].mean().reset_index()
)

    fig = px.bar(
        sex_survival,
        x="Sex",
        y="Survived",
        title="<b>Survival Rate By Sex</b>",
        labels={"Survived": "Survival Rate"}
    )

    fig.update_layout(
        paper_bgcolor="#ffffff",
        plot_bgcolor="#003262",
        margin=dict(l=10, r=10, t=50, b=10),

        title_font=dict(size=31, color="black", family="Copperplate Gothic Bold"),
        font=dict(color="black", size=13, family="Copperplate Gothic Bold")
    )

    fig.update_xaxes(
        title_font=dict(color="black", size=14, family="Arial Black"),
        tickfont=dict(color="black", size=12, family="Arial Black")
    )

    fig.update_yaxes(
        title_font=dict(color="black", size=14, family="Arial Black"),
        tickfont=dict(color="black", size=12, family="Arial Black")
    )
    with st.container(border=True):
        st.plotly_chart(fig, width="stretch")
st.markdown("</div>", unsafe_allow_html=True)



with right_panel:
   # st.container(key='my_white_container',border=True)
    class_survival = (
        df.groupby("Pclass")["Survived"].mean().reset_index()
    )

    fig = px.bar(
        class_survival,
        x="Pclass",
        y="Survived",
        title="Survival Rate By Class",
        labels={"Survived": "Survival Rate"}
    )
    fig.update_layout(
    paper_bgcolor="#ffffff",
    plot_bgcolor="#003262",
    margin=dict(l=10, r=10, t=50, b=10),

    title_font=dict(size=31, color="black", family="Copperplate Gothic Bold"),
    font=dict(color="white", size=13, family="Copperplate Gothic Bold")
)

    fig.update_xaxes(
    title_font=dict(color="black", size=14, family="Arial Black"),
    tickfont=dict(color="black", size=12, family="Arial Black")
)

    fig.update_yaxes(
    title_font=dict(color="black", size=14, family="Arial Black"),
    tickfont=dict(color="black", size=12, family="Arial Black")
)
    with st.container(border=True):
        st.plotly_chart(fig, use_container_width=True)
        

# -----------------------------
left2, spacer, right2 = st.columns([1, 0.05, 1])

with left2:
    st.markdown('')
    fig = px.histogram(
        df,
        x="Age",
        y="Survived",
        title = "Age Distribution By Survival",
        nbins=30
    )
    fig.update_layout(
    paper_bgcolor="#ffffff",
    plot_bgcolor="#003262",
    margin=dict(l=10, r=10, t=50, b=10),

    title_font=dict(size=31, color="black", family="Copperplate Gothic Bold"),
    font=dict(color="white", size=13, family="Copperplate Gothic Bold"))

    fig.update_xaxes(
    title_font=dict(color="black", size=14, family="Arial Black"),
    tickfont=dict(color="black", size=12, family="Arial Black")
)

    fig.update_yaxes(
    title_font=dict(color="black", size=14, family="Arial Black"),
    tickfont=dict(color="black", size=12, family="Arial Black")
    )

    with st.container(border=True):    
        st.plotly_chart(fig, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

with right2:
    st.markdown('')
    fig = px.box(
        df,
        x="Survived",
        y="Fare",
        title="Fare vs Survival"
    )
    fig.update_layout(
    paper_bgcolor="#ffffff",
    plot_bgcolor="#003262",
    margin=dict(l=10, r=10, t=50, b=10),

    title_font=dict(size=31, color="black", family="Copperplate Gothic Bold"),
    font=dict(color="white", size=13, family="Copperplate Gothic Bold"))

    fig.update_xaxes(
    title_font=dict(color="black", size=14, family="Arial Black"),
    tickfont=dict(color="black", size=12, family="Arial Black")
)

    fig.update_yaxes(
    title_font=dict(color="black", size=14, family="Arial Black"),
    tickfont=dict(color="black", size=12, family="Arial Black")
    )
    with st.container(border=True):
        st.plotly_chart(fig, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)
st.markdown("---")
st.markdown(
"""
<div style ="
    backgroud-color:#00B9E8;
    padding:25px;
    border-radius:12px;
    margin-top:20px;
">
<h2 style="
    color:white;
    text-align:center;"
    > Key Insights</h2>
<ul style="
    color:#E5E7EB;
    font-size:18px;
    line-height:1.8;">
    <li><b>Females had higher survival rate than males.</b></li>
    <li><b>Higher class passengers survived more than the others.</b></li>
    <li><b>Fare correlates with survival.</b></li>
</ul>
</div>
""",unsafe_allow_html=True)


# -----------------------------
# DATA PREVIEW
# -----------------------------
st.markdown('')
st.markdown("### 📄 Dataset Preview")
st.dataframe(df)
st.markdown("</div>", unsafe_allow_html=True)

