from random import choice

class ExpertSystem:
    def __init__(self, symptoms, diseases):
        self.symptoms = symptoms
        self.diseases = diseases
        self.current_symptom = None
        self.current_disease = None
    
    def start(self):
        self.current_symptom = choice(self.symptoms)
        n = int(input(f"What is severity of {self.current_symptom} (0-10) : "))
        self.current_disease = self.diseases[self.current_symptom]
        if n > 5:
            print(f"You may have {self.current_disease}")
        else:
            print(f"You don't have {self.current_disease}")
            
        self.askNextQuestion()
    
    def askNextQuestion(self):
        if self.current_disease is not None:
            n = input("Do you have any other symptoms (yes/no) : ")
            if n.lower() == "yes":
                self.start()
            else:
                print("Thank you for using our Expert System!")
        else:
            print("Sorry, I can't help you with disease diagnosis.")
            
if __name__=='__main__':
    symptoms = ["fever", "cough", "sore throat", "running nose", "headache"]
    disease = {
        "fever": "flu",
        "cough": "cold",
        "sore throat": "strep throat",
        "running nose": "allergies",
        "headache": "migraine"
    }
            
    es = ExpertSystem(symptoms, disease)
    es.start()
