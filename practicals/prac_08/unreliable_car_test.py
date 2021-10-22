from practicals.prac_08.unreliable_car import UnreliableCar

good_car = UnreliableCar(100, 'Good Car', 95)
bad_car = UnreliableCar(100, 'Bad Car', 15)
print(f"Attempting to drive 40km, {good_car.name} drove {good_car.drive(40)}km")
print(f"Attempting to drive 40km, {bad_car.name} drove {bad_car.drive(40)}km")
print(good_car)
print(bad_car)