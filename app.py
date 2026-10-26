
# Danh sách công việc
tasks = [
    {"name": "Học Python", "completed": False},
    {"name": "Làm bài tập GitHub", "completed": False},
    {"name": "Ôn bài", "completed": False}
]


def add_task(task_name):
    """Thêm một công việc mới."""
    tasks.append({"name": task_name, "completed": False})
    print(f"Đã thêm công việc: {task_name}")


def list_tasks():
    """Hiển thị danh sách công việc."""
    if not tasks:
        print("Danh sách công việc trống.")
        return

    print("\nDanh sách công việc:")
    for index, task in enumerate(tasks, start=1):
        status = "[x]" if task["completed"] else "[ ]"
        print(f"{index}. {status} {task['name']}")


def complete_task(task_index):
    """Đánh dấu công việc đã hoàn thành."""
    if 1 <= task_index <= len(tasks):
        tasks[task_index - 1]["completed"] = True
        print(f"Đã hoàn thành: {tasks[task_index - 1]['name']}")
    else:
        print("Chỉ số công việc không hợp lệ.")


if __name__ == "__main__":
    list_tasks()
    complete_task(1)
    list_tasks()
