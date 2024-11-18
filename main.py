def choose_practicum():
    practicum = input("select practicum ")
    
    # or
    # and
    # ==
    # !=
    if practicum != "costume" and practicum != "lighting" \
        and practicum != "sound" and practicum != "scenery":
        print ("invalid choice")
        return choose_practicum()

    else:
        return practicum
    
name = input("select name ")
practicum = choose_practicum()
print(f"congrats {name}, you are now in {practicum}")