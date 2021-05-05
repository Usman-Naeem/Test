import time

t = time.localtime()
current_time_1 = time.strftime("%H", t)
current_time_2 = time.strftime("%M", t)
current_time_3 = time.strftime("%S", t)

with open("test.txt", "w") as file:
    file.write("Time:\n")
    file.write(current_time_1 + "\n")
    file.write(current_time_2 + "\n")
    file.write(current_time_3 + "\n")
    file.write("\nConverted to integer:\n")
    file.write(str(int(current_time_1)) + "\n")
    file.write(str(int(current_time_2)) + "\n")
    file.write(str(int(current_time_3)) + "\n")
    if int(current_time_1) % 2 == 0:
        file.write("\nEven Time\n")
    else:
        file.write("\nOdd Time\n")
