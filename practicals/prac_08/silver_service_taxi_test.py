from practicals.prac_08.silver_service_taxi import SilverServiceTaxi

hummer = SilverServiceTaxi('Hummer', 200, 4)
tesla = SilverServiceTaxi('Tesla', 100, 2)
hummer.drive(35)
tesla.drive(18)

print(f"{hummer.name}, for 35km trip Expect fare of $176.70, Current Fare: ${hummer.get_fare():.2f}")
print(hummer)
print(f"{tesla.name}, for 18km trip Expect fare of $48.80, Current Fare: ${tesla.get_fare():.2f}")
print(tesla)