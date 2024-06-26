from nada_dsl import *


def nada_main():
    party1 = Party(name="Party1")
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))

    # Compute the sum and product of my_int1 and my_int2
    sum_result = my_int1 + my_int2
    product_result = my_int1 * my_int2

    # Return the sum and product as outputs
    return [
        Output(sum_result, "sum_output", party1),
        Output(product_result, "product_output", party1)
    ]
