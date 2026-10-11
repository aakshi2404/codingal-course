name = "aakshi"
steps = 7500
target = 10000
calories_per_1000_steps = 40
calories = (steps / 1000) * calories_per_1000_steps
percentage = (steps / target) * 100
remaining = max(0, target - steps)
print("Name:", name)
print("Steps taken:", steps)
print("calories burned:", calories)
print("target completed:", percentage, "%")
print("remaining steps to reach target:", remaining)
print("Is target achieved?", steps >= target)