import json
from datetime import datetime, timedelta

def check_capacity(max_capacity: int, guests: list) -> bool:

    format = '%Y-%m-%d'
    current = datetime.strptime(guests[0]['check-in'], format) 

    day = datetime.strptime(guests[-1]['check-out'], format).day
    month = datetime.strptime(guests[-1]['check-out'], format).month

    rooms = 0

    for i in range(day * month):
        print("Текущий день", current)
        for guest in guests:
            
            check_in = datetime.strptime(guest['check-in'], format)
            check_out = datetime.strptime(guest['check-out'], format)
       
            if current >= check_in and current < check_out:
                rooms += 1
                
        print("Кол-во занятых комнат", rooms)

        if max_capacity < rooms:
            return False

        rooms = 0
        current += timedelta(days=1) 
    
    return True

if __name__ == "__main__":
    # Чтение входных данных
    max_capacity = int(input())
    n = int(input())

    guests = []
    
    for _ in range(n):
        guest_json = input()
        guest_data = json.loads(guest_json)
        guests.append(guest_data)

    result = check_capacity(max_capacity, guests)
    print(result)

