import streamlit as st
import joblib
import pandas as pd
import plotly.graph_objects as go

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="Diabetes Risk Predictor",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- Custom CSS for Premium Design ----------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
    }
    
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Header styling */
    h1 {
        color: #ffffff;
        font-weight: 700;
        font-size: 3rem !important;
        text-align: center;
        margin-bottom: 0.5rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
        animation: fadeInDown 0.8s ease-in-out;
    }
    
    h2, h3 {
        color: #ffffff;
        font-weight: 600;
    }
    
    /* Card container */
    .card {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 2.5rem;
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
        margin: 1rem 0;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 25px 70px rgba(0, 0, 0, 0.4);
    }
    
    /* Input fields */
    .stNumberInput > div > div > input {
        border-radius: 12px;
        border: 2px solid #e0e0e0;
        padding: 12px;
        font-size: 16px;
        transition: all 0.3s ease;
        background: #ffffff;
    }
    
    .stNumberInput > div > div > input:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        font-weight: 600;
        font-size: 1.1rem;
        padding: 0.75rem 2rem;
        border-radius: 12px;
        border: none;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
        transition: all 0.3s ease;
        width: 100%;
        margin-top: 1rem;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.6);
    }
    
    /* Success/Warning boxes */
    .success-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 2rem;
        border-radius: 16px;
        text-align: center;
        margin: 2rem 0;
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);
        animation: slideIn 0.5s ease-out;
    }
    
    .warning-box {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
        padding: 2rem;
        border-radius: 16px;
        text-align: center;
        margin: 2rem 0;
        box-shadow: 0 10px 30px rgba(245, 87, 108, 0.3);
        animation: slideIn 0.5s ease-out;
    }
    
    .info-box {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
        box-shadow: 0 8px 20px rgba(79, 172, 254, 0.3);
    }
    
    /* Animations */
    @keyframes fadeInDown {
        from {
            opacity: 0;
            transform: translateY(-20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    @keyframes slideIn {
        from {
            opacity: 0;
            transform: translateX(-20px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    /* Sidebar styling */
    .css-1d391kg, [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Footer */
    .footer {
        text-align: center;
        color: #ffffff;
        padding: 2rem;
        margin-top: 3rem;
        font-size: 0.9rem;
    }
    
    /* Feature card */
    .feature-card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 12px;
        padding: 1.5rem;
        margin: 0.5rem 0;
        border: 1px solid rgba(255, 255, 255, 0.2);
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# ---------------- Header ----------------
st.markdown("<h1>🏥 Diabetes Risk Predictor</h1>", unsafe_allow_html=True)
st.markdown("""
    <div class='info-box'>
        <h3 style='margin: 0; font-size: 1.1rem;'>🎯 Advanced AI-Powered Health Assessment</h3>
        <p style='margin: 0.5rem 0 0 0; font-size: 0.95rem;'>
            Get instant diabetes risk prediction using state-of-the-art Gradient Boosting Machine Learning
        </p>
    </div>
""", unsafe_allow_html=True)

# ---------------- Sidebar Info ----------------
with st.sidebar:
    st.markdown("<h2 style='color: white;'>📊 About This Tool</h2>", unsafe_allow_html=True)
    st.markdown("""
        <div class='feature-card'>
            <h4>🤖 Machine Learning Model</h4>
            <p>Gradient Boosting Regressor trained on comprehensive diabetes dataset</p>
        </div>
        
        <div class='feature-card'>
            <h4>🎯 Accuracy</h4>
            <p>State-of-the-art prediction algorithm with validated results</p>
        </div>
        
        <div class='feature-card'>
            <h4>⚡ Instant Results</h4>
            <p>Get your diabetes risk assessment in seconds</p>
        </div>
        
        <div class='feature-card'>
            <h4>🔒 Privacy First</h4>
            <p>All data processing happens locally - your information stays private</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("""
        <p style='color: white; font-size: 0.85rem;'>
            ⚠️ <b>Medical Disclaimer:</b> This tool is for informational purposes only. 
            Always consult healthcare professionals for medical advice.
        </p>
    """, unsafe_allow_html=True)

# ---------------- Load Model ----------------
@st.cache_resource
def load_model():
    model = joblib.load("diabetes_gradient_boosting_model.pkl")
    feature_columns = joblib.load("diabetes_feature_columns.pkl")
    return model, feature_columns

model, feature_columns = load_model()

# ---------------- User Input Section ----------------
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown("<h2 style='color: #667eea; margin-bottom: 1.5rem;'>📝 Patient Health Metrics</h2>", unsafe_allow_html=True)

# Create columns for better layout
num_features = len(feature_columns)
cols_per_row = 3
input_data = {}

# Friendly names and descriptions for features
feature_info = {
    'BMI': ('Body Mass Index', 'Weight (kg) / Height² (m²)', 18.5, 35.0),
    'Age': ('Age', 'Age in years', 18, 100),
    'Glucose': ('Glucose Level', 'Blood glucose (mg/dL)', 70, 200),
    'BloodPressure': ('Blood Pressure', 'Diastolic BP (mm Hg)', 60, 120),
    'Insulin': ('Insulin Level', 'Serum insulin (μIU/mL)', 0, 300),
    'SkinThickness': ('Skin Thickness', 'Triceps skinfold (mm)', 10, 50),
    'Pregnancies': ('Pregnancies', 'Number of pregnancies', 0, 15),
    'DiabetesPedigreeFunction': ('Diabetes Pedigree', 'Genetic risk score', 0.0, 2.5),
}

# Create input fields in a grid layout
for i in range(0, num_features, cols_per_row):
    cols = st.columns(cols_per_row)
    for j, col in enumerate(cols):
        if i + j < num_features:
            feature = feature_columns[i + j]
            with col:
                if feature in feature_info:
                    label, desc, min_val, max_val = feature_info[feature]
                    st.markdown(f"**{label}**")
                    st.caption(desc)
                    input_data[feature] = st.number_input(
                        f"{feature}",
                        value=float(min_val),
                        min_value=float(min_val),
                        max_value=float(max_val),
                        label_visibility="collapsed",
                        key=feature
                    )
                else:
                    input_data[feature] = st.number_input(
                        f"{feature}",
                        value=0.0
                    )

# Convert input to DataFrame
input_df = pd.DataFrame([input_data])

st.markdown("</div>", unsafe_allow_html=True)

# ---------------- Prediction ----------------
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    predict_button = st.button("🔍 Analyze Health Metrics", use_container_width=True)

if predict_button:
    with st.spinner('🔄 Analyzing your health data...'):
        prediction = model.predict(input_df)[0]
        
        # Determine risk level
        if prediction < 0.3:
            risk_level = "Low"
            color = "#4ade80"
            message = "Great news! Your diabetes risk appears to be low."
            box_class = "success-box"
            emoji = "✅"
        elif prediction < 0.6:
            risk_level = "Moderate"
            color = "#fbbf24"
            message = "Your diabetes risk is moderate. Consider lifestyle adjustments."
            box_class = "warning-box"
            emoji = "⚠️"
        else:
            risk_level = "High"
            color = "#f87171"
            message = "Your diabetes risk is elevated. Please consult a healthcare provider."
            box_class = "warning-box"
            emoji = "🚨"
        
        # Display result
        st.markdown(f"""
            <div class='{box_class}'>
                <h2 style='margin: 0; font-size: 2rem;'>{emoji} Risk Assessment Complete</h2>
                <h1 style='margin: 1rem 0; font-size: 3.5rem;'>{prediction:.2f}</h1>
                <h3 style='margin: 0.5rem 0;'>Risk Level: {risk_level}</h3>
                <p style='font-size: 1.1rem; margin-top: 1rem;'>{message}</p>
            </div>
        """, unsafe_allow_html=True)
        
        # Create gauge chart
        fig = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = prediction,
            domain = {'x': [0, 1], 'y': [0, 1]},
            title = {'text': "Diabetes Risk Score", 'font': {'size': 24, 'color': '#667eea'}},
            gauge = {
                'axis': {'range': [0, 1], 'tickwidth': 1, 'tickcolor': "#667eea"},
                'bar': {'color': color},
                'bgcolor': "white",
                'borderwidth': 2,
                'bordercolor': "#667eea",
                'steps': [
                    {'range': [0, 0.3], 'color': 'rgba(74, 222, 128, 0.2)'},
                    {'range': [0.3, 0.6], 'color': 'rgba(251, 191, 36, 0.2)'},
                    {'range': [0.6, 1], 'color': 'rgba(248, 113, 113, 0.2)'}
                ],
                'threshold': {
                    'line': {'color': "red", 'width': 4},
                    'thickness': 0.75,
                    'value': 0.6
                }
            }
        ))
        
        fig.update_layout(
            paper_bgcolor = "rgba(0,0,0,0)",
            plot_bgcolor = "rgba(0,0,0,0)",
            font = {'color': "#667eea", 'family': "Inter"},
            height = 400
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Recommendations
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("<h3 style='color: #667eea;'>💡 Personalized Recommendations</h3>", unsafe_allow_html=True)
        
        recommendations = []
        if input_data.get('BMI', 0) > 25:
            recommendations.append("🏃‍♂️ Consider maintaining a healthy weight through balanced diet and regular exercise")
        if input_data.get('Glucose', 0) > 140:
            recommendations.append("🍎 Monitor your blood glucose levels regularly and reduce sugar intake")
        if input_data.get('BloodPressure', 0) > 90:
            recommendations.append("💊 Keep track of your blood pressure and consider consulting a doctor")
        if input_data.get('Age', 0) > 45:
            recommendations.append("👨‍⚕️ Regular health checkups are recommended for your age group")
        
        if recommendations:
            for rec in recommendations:
                st.markdown(f"- {rec}")
        else:
            st.markdown("✨ Keep up your healthy lifestyle! Continue regular checkups.")
        
        st.markdown("</div>", unsafe_allow_html=True)

# ---------------- Footer ----------------
st.markdown("""
    <div class='footer'>
        <p style='font-size: 1rem; font-weight: 600;'>🏥 Diabetes Risk Predictor</p>
        <p>Powered by Gradient Boosting ML | Built with ❤️ using Streamlit</p>
        <p style='font-size: 0.85rem; margin-top: 1rem;'>
            © 2026 | This tool uses machine learning for educational purposes only
        </p>
    </div>
""", unsafe_allow_html=True)