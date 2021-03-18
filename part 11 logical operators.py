# and : both
# or : one of the condition
# not : true to false

has_good_credit = True
has_criminal_record = True
if has_good_credit and not has_criminal_record:
    print("Eligibile for loan")
elif has_good_credit and has_criminal_record:
    print("Uneligible for loan")
