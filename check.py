from info import nums

to_check = """
""" # long python text to check converstion between E.164 and other formats

for n in nums:
    if  str(n)[2:] not in to_check:
        print("number not in list: ", str(n))
