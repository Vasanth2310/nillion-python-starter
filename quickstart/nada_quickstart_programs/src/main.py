#Nada Program for finding Haemoglobin level at the blood
from nada_dsl import *

def nada_main():

    # Define the party
    party1 = Party(name="Party1")

    # Define the input secret integers
    rbc_count = SecretInteger(Input(name="rbc_count", party=party1))  # RBC count in millions per microliter
    hct_value = SecretInteger(Input(name="hct_value", party=party1))  # Hematocrit value as a percentage

    # Initialize hemoglobin level
    hemoglobin_level = SecretInteger(0)

    # Assume the formula for hemoglobin level is: hemoglobin = (RBC count * Hematocrit value) / 100
    # This is a simplified formula for demonstration purposes
    temp_sum = Integer(0)
    for i in range(Integer(100)):
        temp_sum += (rbc_count * hct_value) / Integer(100)
    hemoglobin_level = temp_sum / Integer(100)

    # Classification of hemoglobin level
    # Assuming hemoglobin levels are considered low if < 12 g/dL, otherwise high
    low_threshold = Integer(12)
    is_low = hemoglobin_level < low_threshold

    # Define the outputs
    output_hemoglobin_level = Output(hemoglobin_level, "hemoglobin_level", party1)
    output_is_low = Output(is_low, "is_low", party1)

    return [output_hemoglobin_level, output_is_low]

# Call the main function to execute the program
nada_main()

