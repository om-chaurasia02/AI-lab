# Vacuum Cleaner Agent
# Simple Reflex Agent

# --------------------------------------------------
# Display the current state
# --------------------------------------------------
def display(room, position):
    print()
    print("Room A :", room["A"])
    print("Room B :", room["B"])
    print("Vacuum Position :", position)
    print()


# --------------------------------------------------
# Vacuum Cleaner Agent
# --------------------------------------------------
def vacuum_cleaner(room, position):

    print("===================================")
    print("       VACUUM CLEANER AGENT")
    print("===================================")

    display(room, position)

    # Continue until both rooms are clean
    while room["A"] == "Dirty" or room["B"] == "Dirty":

        # ------------------------------------------
        # If current room is dirty
        # ------------------------------------------
        if room[position] == "Dirty":

            print("Current Room :", position)
            print("Action        : SUCK")

            # Clean the room
            room[position] = "Clean"

        # ------------------------------------------
        # If current room is clean
        # ------------------------------------------
        else:

            if position == "A":

                print("Current Room : A")
                print("Action        : MOVE RIGHT")

                position = "B"

            else:

                print("Current Room : B")
                print("Action        : MOVE LEFT")

                position = "A"

        display(room, position)

    # ------------------------------------------
    # All rooms are clean
    # ------------------------------------------
    print("All rooms are clean!")
    print("Vacuum Cleaner Task Completed.")


# --------------------------------------------------
# MAIN PROGRAM
# --------------------------------------------------

# Initial condition
room = {
    "A": "Dirty",
    "B": "Dirty"
}

# Initial vacuum position
position = "A"

vacuum_cleaner(room, position)
