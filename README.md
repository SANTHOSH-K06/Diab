# 🏥 Diabetes Risk Predictor - Enhanced Version

An advanced, AI-powered diabetes risk assessment tool with a stunning modern interface. Built with Streamlit and powered by Gradient Boosting Machine Learning.

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Machine Learning](https://img.shields.io/badge/ML-Scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)

## ✨ Features

- 🎨 **Premium Modern UI** - Beautiful gradient design with glassmorphism effects
- 📊 **Interactive Visualizations** - Real-time gauge charts showing risk levels
- 🤖 **Advanced ML Model** - Gradient Boosting algorithm for accurate predictions
- 💡 **Personalized Recommendations** - Health tips based on your input data
- ⚡ **Instant Results** - Get your diabetes risk assessment in seconds
- 🔒 **Privacy First** - All processing happens locally
- 📱 **Responsive Design** - Works perfectly on all devices

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. Clone this repository:
```bash
git clone https://github.com/YOUR_USERNAME/diabetes-risk-predictor.git
cd diabetes-risk-predictor
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
streamlit run app.py
```

4. Open your browser and navigate to `http://localhost:8501`

## 📋 Usage

1. Enter patient health metrics in the input fields:
   - BMI (Body Mass Index)
   - Age
   - Glucose Level
   - Blood Pressure
   - Insulin Level
   - Skin Thickness
   - Number of Pregnancies
   - Diabetes Pedigree Function

2. Click "Analyze Health Metrics" to get instant predictions

3. Review your risk assessment with:
   - Numerical risk score
   - Visual gauge chart
   - Risk level categorization (Low/Moderate/High)
   - Personalized health recommendations

## 🎯 Model Information

- **Algorithm**: Gradient Boosting Regressor
- **Framework**: scikit-learn
- **Input Features**: 8 health metrics
- **Output**: Diabetes risk score (0-1 scale)

## 🛠️ Tech Stack

- **Frontend**: Streamlit with custom CSS
- **ML Framework**: scikit-learn
- **Visualization**: Plotly
- **Data Processing**: Pandas
- **Model Persistence**: Joblib

## ⚠️ Medical Disclaimer

This tool is for **informational and educational purposes only**. It should NOT be used as a substitute for professional medical advice, diagnosis, or treatment. Always consult qualified healthcare professionals for medical decisions.

## 📦 Project Structure

```
diabetes-risk-predictor/
├── app.py                                    # Main Streamlit application
├── diabetes_gradient_boosting_model.pkl      # Trained ML model
├── diabetes_feature_columns.pkl              # Feature columns
├── requirements.txt                          # Python dependencies
├── README.md                                 # Project documentation
└── .gitignore                               # Git ignore file
```

## 🤝 Contributing

Contributions are welcome! Feel free to:

- Report bugs
- Suggest new features
- Submit pull requests

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- Original repository: [diabetes-gradient-boosting-streamlit](https://github.com/Beni-18/diabetes-gradient-boosting-streamlit)
- Enhanced UI and features by Santhosh K

## 📞 Contact

For questions or feedback, please open an issue on GitHub.

---

**Made with ❤️ using Streamlit and Machine Learning**
