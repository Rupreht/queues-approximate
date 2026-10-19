# Алгоритм такой, есть 6 fifo очереди, индексы 0-4, проходим в одном цикле,
# берем первый элемент из очереди, записываем в конец рабочей очереди
# с индексом 5.
# Условия для очередей:
# индекс 0 - каждый проход,
# индекс 1 - каждый второй проход,
# индекс 2 - каждый третий,
# индекс 3 - каждый четвертый,
# индекс 4 - каждый пятый,
# индекс 5 - рабочая очередь

from collections import deque


def process_queues(queues, max_passes=20):
    """
    queues: список из 6 deque.
    Индексы 0-4 — исходные FIFO-очереди.
    Индекс 5 — рабочая очередь, куда записываются элементы.
    """
    if len(queues) != 6:
        raise ValueError("Нужно ровно 6 очередей: индексы 0-5")

    # Очередь 0 — каждый проход,
    # 1 — каждый второй, 2 — каждый третий и т.д.
    intervals = {0: 1, 1: 2, 2: 3, 3: 4, 4: 5}

    for pass_number in range(1, max_passes + 1):
        for queue_index, interval in intervals.items():
            # Например, очередь 1 обрабатывается на проходах 2, 4, 6...
            if pass_number % interval == 0 and queues[queue_index]:
                item = queues[queue_index].popleft()
                queues[5].append(item)

    return queues[5]


# Пример использования
queues = [deque() for _ in range(6)]

# Заполняем исходные очереди
for i in range(5):
    for value in range(1, 6):
        queues[i].append(f"Q{i}-{value}")

print(list(process_queues(queues, max_passes=25)))
