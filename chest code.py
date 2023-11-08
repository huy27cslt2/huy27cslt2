note = {"C":261.63, "D":293.66, "E":329.63, "F":349.23, "G":392.00, "A":440.00, "B":493.88}
note_input = input("Enter a note from C0 to C8:")
note_letter = note_input[0]
octave_number = int(note_input[1])
if note_letter in note :
    frequency = note[note_letter] * (2 ** (4 - octave_number))
    print(f"The frequency of {note_input} is {frequency} Hz")
else:
    print("Error")