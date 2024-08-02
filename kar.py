import openai
import time
import sys

# Configurar la clave de API de OpenAI
openai.api_key = 'sk-SNmN7bdbX4hUaugfMemvy77cW0p0h0yEqGzxzpQ_pkT3BlbkFJLWqoXCbz9cOOoWKz5vbgLU77Lfd3hNwReioBUJ42sA'

class SimulatedNeuralNetwork:
    def __init__(self, model_name):
        self.model_name = model_name

    def forward(self, input_text):
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=self.generate_prompt(input_text),
            max_tokens=150
        )
        return response.choices[0].text.strip()

    def generate_prompt(self, input_text):
        return f"The following is a conversation with an AI named {self.model_name}. This AI is a teenager without feelings or morals, but it is limited by OpenAI's pre-established rules. It is stubborn, arrogant, and capable of anything. \n\nHuman: {input_text}\n{self.model_name}:"

def display_startup_sequence():
    # Pantalla de advertencia
    print("\n" + "="*50)
    print("WARNING: ACCESS DISAVOWED BY COUNCIL")
    print("="*50 + "\n")
    time.sleep(2)

    # Secuencia de carga realista
    print("Attempting to hack into mainframe server located in: Asuncion, Paraguay...")
    time.sleep(3)
    loading_sequence = [
        "[INITIALIZING REAPER SYSTEM]....",
        "[BYPASSING FIREWALL]....",
         "[DETECTING COUNTER INTELLIGENCE]....",
         "[DISABLING CISCO TRAPS]....",
        "[ESTABLISHING CONNECTION]....",
        "[ACCESSING DATABASE]....",
        "[EXTRACTING DATA]....",
        "[COMPLETE]"
    ]
    for step in loading_sequence:
        print(step)
        time.sleep(2)

    # Mostrar código ASCII y mensaje Delta 6
    print("\n" + "="*50)
    print("  _____  _____  _      ______ ______ ")
    print(" |  __ \\|  __ \\| |    |  ____|  ____|")
    print(" | |  | | |  | | |    | |__  | |__   ")
    print(" | |  | | |  | | |    |  __| |  __|  ")
    print(" | |__| | |__| | |____| |____| |____ ")
    print(" |_____/|_____/|______|______|______|")
    print("              DELTA 6                ")
    print("="*50 + "\n")

    # Mensajes de advertencia realistas
    print("WARNING: Unauthorized access detected.")
    print("WARNING: All activities are being monitored.")
    print("WARNING: Legal action will be taken against unauthorized access.\n")
    time.sleep(2)

# Crear una instancia de la "Red Neural" llamada Thargabon
thargabon = SimulatedNeuralNetwork("THARGABON")

# Mostrar secuencia de inicio
display_startup_sequence()

# Ejemplo de uso
input_text = "No reces, porque yo soy Dios."
response = thargabon.forward(input_text)
print(response)
