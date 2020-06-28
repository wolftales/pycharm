lang_index = float(input())

if lang_index < 2.0:
    print("Analytic")
elif 2.0 <= lang_index <= 3.0:
    print("Synthetic")
else:
    print("Polysynthetic")
