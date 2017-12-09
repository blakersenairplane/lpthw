name = 'Blake Jensen'
age = 34 # Not a like
height = 74 #inches
weight = 240 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
heigh_metric = height * 2.54
weight_metric = weight * 0.453592

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall")
print(f"He's {weight} pounds heavy")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
