def main():
    present_value = 1
    interest_rate = input("Enter the Interest Rate: ")  #
    years = 0
    future_value = present_value

    while future_value < present_value * 2:
        future_value = future_value + future_value * (
            (float(interest_rate) / 100))
        years = years + 1
    future = future_value % 2
    print("It takes approximately", round(years - future, 1),
          "years to double investment.")


main()
