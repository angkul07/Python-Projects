tasklist = []
print("Enter your TO-DO list: ")
serial_number = 1

while True:
    task = input()

    if(task == 'q'):
        break
    tasklist.append(f"{task}")
    # serial_number += 1

for i, task in enumerate(tasklist, start=1):
    print(f"{i}. {task}")
# print(*tasklist, sep='\n')
