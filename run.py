import json
from datetime import datetime, timedelta

def check_capacity(max_capacity: int, guests: list) -> bool:

    format = '%Y-%m-%d'
    
    list_date = []
    for i in guests:
        list_date.append(i['check-in'])
        list_date.append(i['check-out'])

    list_date.sort()   

    current = datetime.strptime(list_date[0], format)
    last = datetime.strptime(list_date[-1], format)

    days =  last - current

    rooms = 0

    for i in range(days.days):
        for guest in guests:
            
            check_in = datetime.strptime(guest['check-in'], format)
            check_out = datetime.strptime(guest['check-out'], format)
       
            if current >= check_in and current < check_out:
                rooms += 1

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
