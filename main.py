def choose_practicum():
    practicum = input("select practicum")
    name = input("select name ")
    
    # or
    # and
    # ==
    # !=
    if practicum != "costume" and "scenery" and \
        "lighting" and "sound":
        print("invalid choice")
    else:
        print(f"congrats {name}, you are now in {practicum}")
    
choose_practicum()