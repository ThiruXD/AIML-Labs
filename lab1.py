def generate_valid_pins_loop():
    even = [0, 2, 4, 6, 8]
    pins = []
    
    for a in even:
        for b in even:
            for c in even:
                for d in even:
                    if a + b + c + d == 16:
                        pins.append(f"{a}{b}{c}{d}")
    
   # pins.sort()
    return pins

print(generate_valid_pins_loop())
