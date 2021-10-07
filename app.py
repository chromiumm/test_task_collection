# coding=utf-8
import argparse
import tasks


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("task", help="Название задачи для запуска")
    task = parser.parse_args().task
    task_func = getattr(tasks, task)
    task_func()


if __name__ == "__main__":  # проверка, что файл запускается, а не импортируется
    main()
