class Task:
    def __init__(self, description, due_date, status=False):
        self.description = description
        self.due_date = due_date
        self.status = status  # False означает "не выполнено", True означает "выполнено"

    def mark_as_done(self):
        self.status = True

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date):
        task = Task(description, due_date)
        self.tasks.append(task)

    def mark_task_as_done(self, description):
        for task in self.tasks:
            if task.description == description:
                task.mark_as_done()
                return f"Задача '{description}' отмечена как выполненная."
        return f"Задача '{description}' не найдена."

    def get_current_tasks(self):
        return [task for task in self.tasks if not task.status]

# Пример использования
task_manager = TaskManager()

# Добавляем задачи
task_manager.add_task("Задача 1", "2023-04-15")
task_manager.add_task("Задача 2", "2023-05-01")

# Отмечаем задачу как выполненную
print(task_manager.mark_task_as_done("Задача 1"))

# Получаем список текущих задач
current_tasks = task_manager.get_current_tasks()
for task in current_tasks:
    print(f"Описание: {task.description}, Срок: {task.due_date}, Статус: {'Выполнено' if task.status else 'Не выполнено'}")