import sys
import collections

# Константы для символов ключей и дверей
keys_char = [chr(i) for i in range(ord('a'), ord('z') + 1)]
doors_char = [k.upper() for k in keys_char]

def get_input():
    """Чтение данных из стандартного ввода."""
    return [list(line.strip()) for line in sys.stdin]

def solve(data):
    rows = len(data) # Строки
    cols = len(data[0]) # Ячейки

    robot_position = [] # Положение роботов
    key_position = {} # Положение ключей
    door_position = {} # Положение дверей

    start_position = [] # Начальные точки

    pickUp_key = {} # Подобраные ключи
    
    robots = 0
    doors = 0
    steps = 0

    # Перебираем всю карту и находим позиции элементов
    for x in range(rows):
        for y in range(cols):
            cell = data[x][y]
            if cell == '@':
                robot_position.append((x, y))
                start_position.append([x,y])
                robots += 1
            elif cell in keys_char:
                key_position[cell] = [(x, y)]
            elif cell in doors_char:
                door_position[cell] = [(x, y)]
                doors += 1

    direction = [(-1,0), (1,0), (0,-1), (0,1)] # Направление робота
    
    visited_position = set(robot_position)

    while doors > 0:

        # Перебираем всех роботов
        for i in range(robots):
            # Перебираем все возможные направления
            for dx, dy in direction:
                # Создаем новые точки, в которые пошли роботы
                nx, ny = start_position[i][0] + dx, start_position[i][1] + dy
                 # Проверяем точки на выход из поля
                if 0 <= nx < rows and 0 <= ny < cols:
                    cell = data[nx][ny]
                    # Если встретили стену, продолжаем
                    if cell == "#":
                        continue
                    # Если встретил дверь, то проверь, собран ли ключ
                    if cell in doors_char:
                        key = cell.lower()
                        if key in pickUp_key:
                            doors -= 1
                        else:
                            continue
                    # Если встретил ключ, собери и занеси значение
                    if cell in keys_char:
                        if cell not in pickUp_key:
                            pickUp_key[cell] = [(nx, ny)]
                        else:
                            continue
                    # Если встретил путь, то иди на него
                    if cell == ".":
                        start_position[i][0] = nx
                        start_position[i][1] = ny
                    
                    # Записываем точку, как пройденную
                    visited_position.add((nx, ny))
                    steps += 1

    return steps

def main():
    data = get_input()
    result = solve(data)
    print(result)

if __name__ == '__main__':
    main()