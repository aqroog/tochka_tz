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

    # Перебираем всю карту и находим позиции элементов
    for x in range(rows):
        for y in range(cols):
            cell = data[x][y]
            if cell == '@':
                robot_position.append((x, y))
            elif cell in keys_char:
                key_position[cell] = (x, y)
            elif cell in doors_char:
                door_position[cell] = (x, y)

    direction = [(-1,0), (1,0), (0,-1), (0,1)] # Направление робота
    
    
    state = collections.deque([(tuple(robot_position), tuple())])
    # Сохраняем начальное положение роботов и ключи, как посещенные места и подобранные (в начале пустые)
    visited_position = {(tuple(robot_position), tuple())}
    
    steps = 0

    while state:
        
        for _ in range(len(state)):
            current_robot_positions, collected_keys = state.popleft()

            # Сравниваем кол-во собранных и созданных ключей
            if len(collected_keys) == len(key_position):
                return steps
            
            # Перебираем всех роботов
            for i in range(len(current_robot_positions)):
                robot_x, robot_y = current_robot_positions[i]

                # Перебираем все возможные направления
                for dx, dy in direction:
                    # Создаем новые точки, в которые пошли роботы
                    nx, ny = robot_x + dx, robot_y + dy

                    # Проверяем точки на выход из поля
                    if 0 <= nx < rows and 0 <= ny < cols and data[nx][ny] != '#':
                        cell = data[nx][ny]

                        # Если встретил дверь, то проверь, собран ли ключ и есть ли он
                        if cell in doors_char:
                            key = cell.lower()
                            if key not in collected_keys:
                                continue

                        # Обновление позиции робота, после всех проверок
                        new_robot_positions = list(current_robot_positions)
                        new_robot_positions[i] = (nx, ny)
                        new_collected_keys = list(collected_keys)

                        # Если встретил ключ, собери и занеси значение
                        if cell in keys_char:
                            if cell not in new_collected_keys:
                                new_collected_keys.append(cell)
                                new_collected_keys.sort()                            

                        next_step = (tuple(new_robot_positions), tuple(new_collected_keys))
                        
                        # Записываем точку, как пройденную, если в ней еще не были
                        if next_step not in visited_position:
                            visited_position.add(next_step)
                            state.append(next_step)

        steps += 1

def main():
    data = get_input()
    result = solve(data)
    print(result)

if __name__ == '__main__':
    main()
