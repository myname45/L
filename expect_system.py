class ExpertSystem:
    def __init__(self):
        self.rules = {}  # Dictionary to store rules

    def add_rule(self, condition, action):
        self.rules[condition] = action

    def infer(self, symptoms):
        for condition, action in self.rules.items():
            if all(symptom in symptoms for symptom in condition):
                return action
        return "No action specified for given symptoms"

# Example usage
expert_system = ExpertSystem()

# Adding rules to the system
expert_system.add_rule(["fever", "cough"], "Take a flu test")
expert_system.add_rule(["fever", "rash"], "Consult a dermatologist")
expert_system.add_rule(["headache", "nausea"], "Consider migraines")

# Inferring actions based on symptoms
patient_symptoms = ["fever", "cough"]
action = expert_system.infer(patient_symptoms)
print("Patient should:", action)

patient_symptoms = ["fever", "rash"]
action = expert_system.infer(patient_symptoms)
print("Patient should:", action)

patient_symptoms = ["headache", "nausea"]
action = expert_system.infer(patient_symptoms)
print("Patient should:", action)

patient_symptoms = ["cough"]
action = expert_system.infer(patient_symptoms)
print("Patient should:", action)
