def ageInSeconds():
    """
    Reads the age and converts to seconds.
    """
    ageYears = int(input("Tell me your age, please: "))
    seconds = ageYears * (365*24*60*60)
    print("\nBatman says you age in seconds is: " % seconds)