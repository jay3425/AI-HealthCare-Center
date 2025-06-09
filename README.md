# 🩺 AI HealthCare Assistant

![](https://github.com/jay3425/AI-HealthCare-Center/blob/main/MainImg.png)

An interactive, AI-powered healthcare assistant built with Python and Tkinter.  
This system predicts diseases based on user symptoms using a trained ML model, and provides personalized recommendations including precautions, medications, diets, and workout routines — all powered by an enhanced **AI chatbot (Groq Llama3)** for natural language symptom parsing.

---

## 🚀 Features

### 🤖 AI-Powered Symptom Analysis (Groq Llama3)
- Uses **Groq Llama3-70B** model to intelligently extract valid symptoms from free-form user input.
- Flexible natural language understanding — no need for perfect input formatting.
- Returns a clean list of matched symptoms for ML model prediction.

### 🧠 Disease Prediction
- ML-based **disease prediction** using an SVC model.
- Over **130+ symptoms** mapped to **40+ possible diseases**.
- Displays the most probable disease based on user input.

### 📋 Comprehensive Recommendations
- **Description** of the disease.
- **Precautions** to follow.
- **Medications** typically prescribed.
- **Diet** suggestions to aid recovery.
- **Workout** recommendations for wellness support.

### 🖥️ Interactive GUI
- Built with **Tkinter** — clean and responsive.
- Hover effects on buttons.
- Fully interactive response section.
- Custom popup alerts with clean UI for displaying each category of information.
- Easy-to-use buttons to display:
  - 🦠 Disease name
  - 📋 Description
  - 😷 Precaution
  - 💊 Medications
  - 🍴 Diets
  - 🏃 Workouts

---

## 🧠 Technologies Used

- **Python 3**
- **Tkinter** – for the GUI.
- **Scikit-learn** – SVC model for disease prediction.
- **Pandas** – for handling symptom, description, precaution, medication, and diet data.
- **NumPy** – for model input processing.
- **Pickle** – for loading trained models.
- **Groq API** — for LLM-based symptom extraction
---

## 📂 File Structure

```plaintext
├── main.py                     # Main app GUI and logic
├── svc.pkl                     # Trained SVC model
├── symtoms_df.csv              # Symptoms dataset
├── precautions_df.csv          # Precautions dataset
├── workout_df.csv              # Workouts dataset
├── description.csv             # Disease descriptions
├── medications.csv              # Medications dataset
├── diets.csv                   # Diet plans dataset
└── README.md                   # Project documentation
````

---

## 💡 How to Run

1. **Install Dependencies**:

   ```bash
   pip install numpy pandas scikit-learn groq json pickle
   ```

2. **Run the App**:

   ```bash
   python main.py
   ```

---

## 📸 Screenshots
Main App Dashboard
>  ![](https://github.com/jay3425/AI-HealthCare-Center/blob/main/Screenshot%20(471).png)

Symptom Input → Disease Prediction
>  ![](https://github.com/jay3425/AI-HealthCare-Center/blob/main/Screenshot%20(481).png)

Description Popups
>  ![](https://github.com/jay3425/AI-HealthCare-Center/blob/main/Screenshot%20(476).png)

Precautions Recommendations
>  ![](https://github.com/jay3425/AI-HealthCare-Center/blob/main/Screenshot%20(477).png)

Medications Recommendations
>  ![](https://github.com/jay3425/AI-HealthCare-Center/blob/main/Screenshot%20(478).png)

Diet Recommendations
>  ![](https://github.com/jay3425/AI-HealthCare-Center/blob/main/Screenshot%20(480).png)

Workout Recommendations
>  ![](https://github.com/jay3425/AI-HealthCare-Center/blob/main/Screenshot%20(479).png)

---

## 👨‍💻 Author

**Jay Dengle** – *Aspiring Data Analyst / ML Engineer*
📧 [jaydengle2005@gmail.com](mailto:jaydengle2005@gmail.com)
🌐 [LinkedIn](https://www.linkedin.com/in/jay-anil-dengle-049952337/) | [GitHub](https://github.com/jay3425)

---

## 📃 License

This project is for **educational and demonstration** purposes.
Feel free to fork, modify, and build upon it.

---

If you like this project, give it a ⭐ and share it with others!

---
