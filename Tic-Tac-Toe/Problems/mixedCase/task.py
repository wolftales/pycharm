intp = input()

tmp = intp.title().replace(" ", "")

print(tmp[0].lower() + "".join(tmp[1:]))

# if len(intp) <= 1:
#     print("".join(intp).lower())
# else:
#     print(intp[0].lower() + "".join(intp[1:]))
