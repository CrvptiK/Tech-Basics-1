#%%
#hours (and tears) reeee: 2 (wow, new record)

#im sick as all heck so this will be fun... headache yayy (っ◞‸◟ c)
#lets first import what we need

import csv
import random
import sys
import time

#name the files

input_file = 'Technical Basics I_2025 - Sheet1.csv'
output_file = 'updated.csv'

#typewriter effect for later
def typewriter(text, delay=0.03):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

#now for the main loop
#to be totally honest, a good portion of this was done with chatgpt bc im sick off my rocker and cant focus at all
#i did however not give chatgpt the google sheet file (a bc i dont want to give personal data to it and b bc i wanted to at least do some part of this assignment myself, even tho im sick)
#i mainly put in the correct numbers (i hope theyre correct at least) and fixed the code, for example with the sixth week being skipped and with 7 being in the file but empty score wise
try:
    with open(input_file, newline='') as csvfile:
        reader = list(csv.reader(csvfile))
        header = reader[0]
        data = reader[1:]

        weeks = [f"Week {i}" for i in range(1, 7) if i != 6] + [f"Week {i}" for i in range(7, 14)]
        existing_weeks = header[4:]
        new_weeks = weeks[len(existing_weeks):]
        header += new_weeks + ["Total Points", "Average Points"]

    for row in data:
        grades = []
#now to populate the empty slots (side note, week7 was funny to figure out since it existed but was not populated, so its a kinda special case
        for i in range(len(existing_weeks)):
            week_num = i + 1 if i < 5 else i + 2
            if week_num == 7:
                grade = random.randint(0, 3)
                grades.append(grade)
                row[4 + i] = str(grade)
            else:
                val = row[4 + i].strip()
                grades.append(int(val) if val.isdigit() else 0)

            for _ in new_weeks:
                grade = random.randint(0, 3)
                grades.append(grade)
                row.append(str(grade))
#now this here i do not quite understand yet, so i googled for like 15 minutes before giving up and looking back at chatgpts suggestion
            top_10 = sorted(grades, reverse=True)[:10]
            total = min(sum(top_10), 30)
            avg = round(sum(grades) / len(grades), 2) if grades else 0
            row.append(str(total))
            row.append(str(avg))
#this i took from our in-class exercise and changed to fit this file
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)
        writer.writerows(data)

    print("\nAnd the weekly Averages are coming in live 🔴")
    for i in range(4, 4 + len(weeks)):
        week_vals = [int(r[i]) if r[i].strip().isdigit() else 0 for r in data]
        avg = sum(week_vals) / len(week_vals)
        typewriter(f"{header[i]}: {avg:.2f}")

    stream_a = [float(r[-1]) for r in data if r[1].strip().upper() == 'A']
    stream_b = [float(r[-1]) for r in data if r[1].strip().upper() == 'B']
    print("\n⚔️Battle of the Streams!")
    typewriter(f"In the left corner: Stream A with a breathtaking average of {sum(stream_a)/len(stream_a):.2f} points!")
    typewriter(f"And in the right corner: Stream B with a stunning average of {sum(stream_b)/len(stream_b):.2f} points!")
#small addon by yours truly (and google)
    def compare_streams(stream_a, stream_b):
        avg_a = sum(stream_a) / len(stream_a) if stream_a else 0
        avg_b = sum(stream_b) / len(stream_b) if stream_b else 0

        typewriter("\nAnd today's winner is...   ")
        if avg_a > avg_b:
            typewriter(f"Stream A! Well done! 🏆")
        elif avg_b > avg_a:
            typewriter(f"Stream B! Great performance! 🏆")
        else:
            typewriter(f"It's a tie! No loosers today! No winners either...")

    compare_streams(stream_a, stream_b)

except FileNotFoundError:
    print("The file was not found. Please check the file name or path.")

#now i thought i could add a function to look up specific students, created by me and a bit of searching in our exercise notebooks)
def lookup_student(data, header):
    name = input("\nEnter student name to look up: ").strip().lower()
    found = False
    for row in data:
        if row[0].strip().lower() == name:
            found = True
            typewriter("\nYour Scores coming in hotttt!")
            typewriter(f"Name: {row[0]}")
            typewriter(f"Stream: {row[1]}")
            for i in range(4, len(header)):
                typewriter(f"{header[i]}: {row[i]}")
                total_points_index = header.index("Total Points")
            if row[total_points_index].isdigit() and int(row[total_points_index]) == 30:
                print("((ヽ(๑╹◡╹๑)ﾉ))♬")
                typewriter("Wow! You reached the maximum score! Congrats!")
            break
    if not found:
        print("Student not found.")

while True:
    lookup_student(data, header)
    again = input("Look up another? (y/n): ").strip().lower()
    if again != 'y':
        break

#enough for today, im going to bed (it might be 11 am right now, dont tell anyone) i will revisit this at some point and replace/revise some code but for now, lets get healthy again first