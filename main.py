







import tkinter as tk
import numpy as np
import pandas as pd
import pickle
from groq import Groq
import json



GroqAPIKey = "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"
client = Groq(api_key=GroqAPIKey)

System = """
You are a very accurate AI HealthCare Assistant.

You are provided with this list of symptoms:
[itching, skin rash, nodal skin eruptions, continuous sneezing, shivering, chills, joint pain, stomach pain, acidity, ulcers on tongue, muscle wasting, vomiting, burning micturition, spotting urination, fatigue, weight gain, anxiety, cold hands and feets, mood swings, weight loss, restlessness, lethargy, patches in throat, irregular sugar level, cough, high fever, sunken eyes, breathlessness, sweating, dehydration, indigestion, headache, yellowish skin, dark urine, nausea, loss of appetite, pain behind the eyes, back pain, constipation, abdominal pain, diarrhoea, mild fever, yellow urine, yellowing of eyes, acute liver failure, fluid overload, swelling of stomach, swelled lymph nodes, malaise, blurred and distorted vision, phlegm, throat irritation, redness of eyes, sinus pressure, runny nose, congestion, chest pain, weakness in limbs, fast heart rate, dizziness, cramps, bruising, obesity, swollen legs, swollen blood vessels, puffy face and eyes, enlarged thyroid, brittle nails, swollen extremeties, excessive hunger, dry tingling lips, slurred speech, knee pain, hip joint pain, muscle weakness, stiff neck, swelling joints, movement stiffness, spinning movements, loss of balance, unsteadiness, weakness of one body side, loss of smell, bladder discomfort, foul smell of urine, continuous feel of urine, passage of gases, internal itching, depression, irritability, muscle pain, altered sensorium, red spots over body, belly pain, abnormal menstruation, watering from eyes, increased appetite, polyuria, coma, stomach bleeding, distention of abdomen, blood in sputum, palpitations, painful walking, pus filled pimples, blackheads, scurring, skin peeling, silver like dusting, small dents in nails, inflammatory nails, blister, red sore around nose, yellow crust ooze]

When the user sends a message describing symptoms, you must return ONLY the list of matching symptoms from the above list.

Do not return extra text, explanations, or notes. Just return a clean JSON list of matched symptoms.

Example:

User: "I have a headache and chest pain."

AI Output:
["headache", "chest pain"]

--- Begin processing ---
"""



# ------------------ GUI Initialization ------------------
root = tk.Tk()
root.title("AI HealthCare Assistant")
root.state('zoomed')
root.iconbitmap(r'robot.ico') 
root.config(bg="#ecf0f1")

# ------------------ Canvas Background ------------------
canvas = tk.Canvas(root, width=1900, height=1650, bg="#ecf0f1", highlightthickness=0)
canvas.place(x=0, y=0)
canvas.create_oval(-120, -120, 200, 200, fill="#dfe6e9", outline="")
canvas.create_oval(650, 450, 1000, 800, fill="#dfe6e9", outline="")
canvas.create_oval(200, 100, 450, 350, fill="#a4b0be", outline="")

# ------------------ Hover Effects ------------------
def on_hover_enter(event):
    event.widget["bg"] = "#2d3436"

def on_hover_leave(event):
    event.widget["bg"] = event.widget.original_bg

# ------------------ Alert Box Function ------------------
def show_custom_alert(title, message):
    popup = tk.Toplevel(root)
    popup.title(title)
    popup.configure(bg="#ffffff")
    popup.resizable(False, False)
    popup.attributes('-topmost', True)

    popup_width = 500
    popup_height = 500
    root.update_idletasks()

    root_x = root.winfo_x()
    root_y = root.winfo_y()
    root_width = root.winfo_width()
    root_height = root.winfo_height()

    pos_x = root_x + (root_width // 2) - (popup_width // 2)
    pos_y = root_y + (root_height // 2) - (popup_height // 2)
    popup.geometry(f"{popup_width}x{popup_height}+{pos_x}+{pos_y}")

    shadow_bg = tk.Label(popup, bg="#dfe6e9")
    shadow_bg.place(relwidth=1, relheight=1)

    card_frame = tk.Frame(popup, bg="#ffffff", bd=2, relief="groove")
    card_frame.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.9, relheight=0.8)

    icon_label = tk.Label(card_frame, text="🧠", font=("Segoe UI", 28), bg="#ffffff")
    icon_label.pack(pady=(10, 0))

    title_label = tk.Label(card_frame, text=title, font=("Segoe UI", 14, "bold"), bg="#ffffff", fg="#2d3436")
    title_label.pack(pady=(5, 0))

    message_label = tk.Label(card_frame, text=message, font=("Segoe UI", 11), bg="#ffffff", fg="#636e72", wraplength=300)
    message_label.pack(pady=(10, 15))

    ok_button = tk.Button(card_frame, text="OK", font=("Segoe UI", 10, "bold"),
                          bg="#0984e3", fg="white", activebackground="#74b9ff",
                          relief="flat", padx=15, pady=5, command=popup.destroy)
    ok_button.pack()






# ------------------ Load Model and Data ------------------

sym_des = pd.read_csv("symtoms_df.csv")
precautions = pd.read_csv("precautions_df.csv")
workout = pd.read_csv("workout_df.csv")
description = pd.read_csv("description.csv")
medications = pd.read_csv('medications.csv')
diets = pd.read_csv("diets.csv")


# load model
svc = pickle.load(open('svc.pkl','rb'))

symptoms_dict = {'itching': 0, 'skin_rash': 1, 'nodal_skin_eruptions': 2, 'continuous_sneezing': 3, 'shivering': 4, 'chills': 5, 'joint_pain': 6, 'stomach_pain': 7, 'acidity': 8, 'ulcers_on_tongue': 9, 'muscle_wasting': 10, 'vomiting': 11, 'burning_micturition': 12, 'spotting_ urination': 13, 'fatigue': 14, 'weight_gain': 15, 'anxiety': 16, 'cold_hands_and_feets': 17, 'mood_swings': 18, 'weight_loss': 19, 'restlessness': 20, 'lethargy': 21, 'patches_in_throat': 22, 'irregular_sugar_level': 23, 'cough': 24, 'high_fever': 25, 'sunken_eyes': 26, 'breathlessness': 27, 'sweating': 28, 'dehydration': 29, 'indigestion': 30, 'headache': 31, 'yellowish_skin': 32, 'dark_urine': 33, 'nausea': 34, 'loss_of_appetite': 35, 'pain_behind_the_eyes': 36, 'back_pain': 37, 'constipation': 38, 'abdominal_pain': 39, 'diarrhoea': 40, 'mild_fever': 41, 'yellow_urine': 42, 'yellowing_of_eyes': 43, 'acute_liver_failure': 44, 'fluid_overload': 45, 'swelling_of_stomach': 46, 'swelled_lymph_nodes': 47, 'malaise': 48, 'blurred_and_distorted_vision': 49, 'phlegm': 50, 'throat_irritation': 51, 'redness_of_eyes': 52, 'sinus_pressure': 53, 'runny_nose': 54, 'congestion': 55, 'chest_pain': 56, 'weakness_in_limbs': 57, 'fast_heart_rate': 58, 'pain_during_bowel_movements': 59, 'pain_in_anal_region': 60, 'bloody_stool': 61, 'irritation_in_anus': 62, 'neck_pain': 63, 'dizziness': 64, 'cramps': 65, 'bruising': 66, 'obesity': 67, 'swollen_legs': 68, 'swollen_blood_vessels': 69, 'puffy_face_and_eyes': 70, 'enlarged_thyroid': 71, 'brittle_nails': 72, 'swollen_extremeties': 73, 'excessive_hunger': 74, 'extra_marital_contacts': 75, 'drying_and_tingling_lips': 76, 'slurred_speech': 77, 'knee_pain': 78, 'hip_joint_pain': 79, 'muscle_weakness': 80, 'stiff_neck': 81, 'swelling_joints': 82, 'movement_stiffness': 83, 'spinning_movements': 84, 'loss_of_balance': 85, 'unsteadiness': 86, 'weakness_of_one_body_side': 87, 'loss_of_smell': 88, 'bladder_discomfort': 89, 'foul_smell_of urine': 90, 'continuous_feel_of_urine': 91, 'passage_of_gases': 92, 'internal_itching': 93, 'toxic_look_(typhos)': 94, 'depression': 95, 'irritability': 96, 'muscle_pain': 97, 'altered_sensorium': 98, 'red_spots_over_body': 99, 'belly_pain': 100, 'abnormal_menstruation': 101, 'dischromic _patches': 102, 'watering_from_eyes': 103, 'increased_appetite': 104, 'polyuria': 105, 'family_history': 106, 'mucoid_sputum': 107, 'rusty_sputum': 108, 'lack_of_concentration': 109, 'visual_disturbances': 110, 'receiving_blood_transfusion': 111, 'receiving_unsterile_injections': 112, 'coma': 113, 'stomach_bleeding': 114, 'distention_of_abdomen': 115, 'history_of_alcohol_consumption': 116, 'fluid_overload.1': 117, 'blood_in_sputum': 118, 'prominent_veins_on_calf': 119, 'palpitations': 120, 'painful_walking': 121, 'pus_filled_pimples': 122, 'blackheads': 123, 'scurring': 124, 'skin_peeling': 125, 'silver_like_dusting': 126, 'small_dents_in_nails': 127, 'inflammatory_nails': 128, 'blister': 129, 'red_sore_around_nose': 130, 'yellow_crust_ooze': 131}
diseases_list = {15: 'Fungal infection', 4: 'Allergy', 16: 'GERD', 9: 'Chronic cholestasis', 14: 'Drug Reaction', 33: 'Peptic ulcer diseae', 1: 'AIDS', 12: 'Diabetes ', 17: 'Gastroenteritis', 6: 'Bronchial Asthma', 23: 'Hypertension ', 30: 'Migraine', 7: 'Cervical spondylosis', 32: 'Paralysis (brain hemorrhage)', 28: 'Jaundice', 29: 'Malaria', 8: 'Chicken pox', 11: 'Dengue', 37: 'Typhoid', 40: 'hepatitis A', 19: 'Hepatitis B', 20: 'Hepatitis C', 21: 'Hepatitis D', 22: 'Hepatitis E', 3: 'Alcoholic hepatitis', 36: 'Tuberculosis', 10: 'Common Cold', 34: 'Pneumonia', 13: 'Dimorphic hemmorhoids(piles)', 18: 'Heart attack', 39: 'Varicose veins', 26: 'Hypothyroidism', 24: 'Hyperthyroidism', 25: 'Hypoglycemia', 31: 'Osteoarthristis', 5: 'Arthritis', 0: '(vertigo) Paroymsal  Positional Vertigo', 2: 'Acne', 38: 'Urinary tract infection', 35: 'Psoriasis', 27: 'Impetigo'}

# ------------------ Analyze Button Function ------------------
# def analyze_symptoms():
#     global symptoms
#     global predicted_disease
#     global desc
#     global pre
#     global med
#     global die
#     global wrkout
#     symptoms = symptom_entry.get()
#     # Clean and split the input
    
#     user_symptoms = [s.strip() for s in symptoms.split(',')]
#     user_symptoms = [symptom.strip("[]' ") for symptom in user_symptoms]

#     def get_predicted_value(user_symptoms):
#         input_vector = np.zeros(len(symptoms_dict))
#         for item in user_symptoms:
#             input_vector[symptoms_dict[item]] = 1
#         return diseases_list[svc.predict([input_vector])[0]]

#     try:
#         predicted_disease = get_predicted_value(user_symptoms)
#         # show_custom_alert("AI Suggestion", f"Predicted Disease: {predicted_disease}")
#         show_custom_alert("AI Suggestion", f"Symptoms analyzed: {symptoms}")
#     except Exception as e:
#         show_custom_alert("Error", f"Prediction failed: {str(e)} if symptoms did not match any disease then overlook Symptoms.txt for avalable symptoms.   Thanks!") 



import json
import numpy as np

def analyze_symptoms():
    global symptoms
    global predicted_disease
    global desc
    global pre
    global med
    global die
    global wrkout

    # Get symptoms input from user (as a string)
    symptoms = symptom_entry.get().strip()

    # Prepare a system prompt listing all known symptoms
    symptom_list_str = ", ".join(symptoms_dict.keys())
    system_prompt = (
        "You are an AI HealthCare Assistant.\n\n"
        "Here is the list of symptoms you should match user input against:\n"
        f"[{symptom_list_str}]\n\n"
        "When the user sends symptoms, reply ONLY with a JSON array (list) of matched symptoms "
        "from the above list.\n\n"
        "Example:\n"
        'User: "I have headache and chest pain."\n'
        'AI response:\n'
        '["headache", "chest pain"]'
    )

    # Call the Groq AI model to extract matched symptoms
    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": symptoms}
        ],
        temperature=0  # Use zero temperature for accurate matching
    )

    # Extract the AI response text
    llm_output = response.choices[0].message.content.strip()

    # Try to parse AI output as JSON list of symptoms
    try:
        response = json.loads(llm_output)
    except json.JSONDecodeError:
        # If JSON parsing fails, fallback: split by comma and clean strings
        response = [s.strip(" []'\"") for s in llm_output.split(',')]

    # Helper function to predict disease from symptoms list
    def get_predicted_value(response):
        input_vector = np.zeros(len(symptoms_dict))
        for item in response:
            if item in symptoms_dict:
                input_vector[symptoms_dict[item]] = 1
        predicted_index = svc.predict([input_vector])[0]
        return diseases_list[predicted_index]

    try:
        predicted_disease = get_predicted_value(response)
        show_custom_alert("AI Suggestion", f"Symptoms analyzed: {symptoms}")
    except Exception as e:
        show_custom_alert(
            "Error",
            f"Prediction failed: {str(e)}. "
            "If symptoms did not match any disease, please check Symptoms.txt for available symptoms. Thanks!"
        )





    # print("Analyzing:", symptoms)
    

    def helper(dis):
        desc = description[description['Disease'] == predicted_disease]['Description']
        desc = " ".join([w for w in desc])

        pre = precautions[precautions['Disease'] == dis][['Precaution_1', 'Precaution_2', 'Precaution_3', 'Precaution_4']]
        pre = [col for col in pre.values]

        med = medications[medications['Disease'] == dis]['Medication']
        med = [med for med in med.values]

        die = diets[diets['Disease'] == dis]['Diet']
        die = [die for die in die.values]

        wrkout = workout[workout['disease'] == dis] ['workout']


        return desc,pre,med,die,wrkout
    
    desc, pre, med, die, wrkout = helper(predicted_disease)




# ------------------ Individual Section Functions ------------------
def show_disease():
        show_custom_alert(" Disease", f"🦠 Predicted disease: {predicted_disease}")
        print("Disease: ", predicted_disease)
 

def show_description():
        show_custom_alert("📋 Description: ",desc)
        print("Description: ", desc)




def show_precaution():
    formatted_message = "\n".join([f"{i+1}: {x}" for i, x in enumerate(pre[0])])
    show_custom_alert("😷 Precaution: ", formatted_message)
    print("Precautions: ", formatted_message)





def show_medications():
    # print(pre)
    formatted_message = "\n".join([f"{i+1}: {d}" for i, d in enumerate(eval(med[0]))])
    show_custom_alert("💊 Medications: ", formatted_message)
    print("Medications: ", formatted_message)



def show_diets():
    formatted_message = "\n".join([f"{i+1}: {d}" for i, d in enumerate(eval(die[0]))])
    show_custom_alert("🍴 Diets: ", formatted_message)
    print("Diets: ", formatted_message)





def show_workouts():
        # Add numbering to each workout
    numbered_workouts = "\n".join([f"{i+1}. {w}" for i, w in enumerate(wrkout)])
    
    # Optional: Print to console (debug/log)
    for i, w in enumerate(wrkout, 1):
        print(f"{i}: {w}")
    
    # Show custom alert with formatted workout list
    show_custom_alert("🏃 Workouts", numbered_workouts)
    print("Workout: ", numbered_workouts)





# ------------------ Header ------------------
header_label = tk.Label(root, text="🩺 AI HealthCare Center", font=("Segoe UI", 28, "bold"), bg="#ecf0f1", fg="#2d3436")
header_label.pack(pady=30)

# ------------------ Input Section ------------------
input_frame = tk.Frame(root, bg="#ffffff", padx=30, pady=25)
input_frame.pack(pady=10)

symptom_label = tk.Label(input_frame, text="Enter Symptoms:", font=("Segoe UI", 12, "bold"), bg="#ffffff", fg="#2d3436")
symptom_label.pack(anchor="w")

symptom_entry = tk.Entry(input_frame, font=("Segoe UI", 12), width=45, bd=1, relief="solid", bg="#f8f9fa")
symptom_entry.insert(0, "headache, cough")
symptom_entry.pack(pady=12, ipady=6)

analyze_button = tk.Button(input_frame, text="🔎 Analyze Symptoms", font=("Segoe UI", 12, "bold"),
                           bg="#0984e3", fg="white", activebackground="#74b9ff",
                           relief="flat", padx=20, pady=10, command=analyze_symptoms)
analyze_button.pack(pady=10)
analyze_button.original_bg = "#0984e3"
analyze_button.bind("<Enter>", on_hover_enter)
analyze_button.bind("<Leave>", on_hover_leave)

# ------------------ AI Response Section ------------------
response_label = tk.Label(root, text="📊 AI Doctor's Response", font=("Segoe UI", 20, "bold"), bg="#ecf0f1", fg="#2d3436")
response_label.pack(pady=20)

response_frame = tk.Frame(root, bg="#ecf0f1")
response_frame.pack()

# ------------------ Separate Response Buttons ------------------
btn_disease = tk.Button(response_frame, text="🦠 Disease", bg="#00cec9", fg="white", font=("Segoe UI", 10, "bold"),
                        width=15, height=2, relief="flat", command=show_disease)
btn_disease.pack(side="left", padx=10)
btn_disease.original_bg = "#00cec9"
btn_disease.bind("<Enter>", on_hover_enter)
btn_disease.bind("<Leave>", on_hover_leave)

btn_description = tk.Button(response_frame, text="📋 Description", bg="#6c5ce7", fg="white", font=("Segoe UI", 10, "bold"),
                            width=15, height=2, relief="flat", command=show_description)
btn_description.pack(side="left", padx=10)
btn_description.original_bg = "#6c5ce7"
btn_description.bind("<Enter>", on_hover_enter)
btn_description.bind("<Leave>", on_hover_leave)

btn_precaution = tk.Button(response_frame, text="😷 Precaution", bg="#fd79a8", fg="white", font=("Segoe UI", 10, "bold"),
                           width=15, height=2, relief="flat", command=show_precaution)
btn_precaution.pack(side="left", padx=10)
btn_precaution.original_bg = "#fd79a8"
btn_precaution.bind("<Enter>", on_hover_enter)
btn_precaution.bind("<Leave>", on_hover_leave)

btn_medications = tk.Button(response_frame, text="💊 Medications", bg="#e17055", fg="white", font=("Segoe UI", 10, "bold"),
                            width=15, height=2, relief="flat", command=show_medications)
btn_medications.pack(side="left", padx=10)
btn_medications.original_bg = "#e17055"
btn_medications.bind("<Enter>", on_hover_enter)
btn_medications.bind("<Leave>", on_hover_leave)

btn_workouts = tk.Button(response_frame, text="🏃 Workouts", bg="#00b894", fg="white", font=("Segoe UI", 10, "bold"),
                         width=15, height=2, relief="flat", command=show_workouts)
btn_workouts.pack(side="left", padx=10)
btn_workouts.original_bg = "#00b894"
btn_workouts.bind("<Enter>", on_hover_enter)
btn_workouts.bind("<Leave>", on_hover_leave)

btn_diets = tk.Button(response_frame, text="🍴 Diets", bg="#fab1a0", fg="white", font=("Segoe UI", 10, "bold"),
                      width=15, height=2, relief="flat", command=show_diets)
btn_diets.pack(side="left", padx=10)
btn_diets.original_bg = "#fab1a0"
btn_diets.bind("<Enter>", on_hover_enter)
btn_diets.bind("<Leave>", on_hover_leave)

# ------------------ Footer ------------------
footer_label = tk.Label(root, text="Developed by Jay Dengle © 2025", font=("Segoe UI", 10), bg="#ecf0f1", fg="#636e72")
footer_label.pack(side="bottom", pady=20)

# ------------------ Start GUI ------------------
root.mainloop()
