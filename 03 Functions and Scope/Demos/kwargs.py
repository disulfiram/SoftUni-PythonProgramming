def pretty_print_record(**kwargs):   # във функцията kwargs ще бъде обикновен dict
    print("Record:")
    for k, v in kwargs.items():
        print("\t", k, "= ", v)

pretty_print_record(name="Mercury", distance_au=0.387, diameter_km=4878)
pretty_print_record(name="Venus", distance_au=0.723, diameter_km=12104)
pretty_print_record(name="Earth", distance_au=1, diameter_km=12742, average_temp_c=7.2, atmosphere=["nitrogen", "oxygen", "argon"])
pretty_print_record()