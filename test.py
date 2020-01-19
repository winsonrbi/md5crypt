word = "hi!"

encoded = word.encode("utf-8")
match = "ed7a5307588e49ed3a2777d926d62f96"
match2 = "ed7a5307588e49ed3a2777d926d62f96"
check = "ed7a5307588e49ed3a2777d926d62f96"

if match2 == check:
    print("good")
else:
    print("Bad")
print(encoded.decode())


