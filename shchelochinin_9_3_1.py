import sys
import os
import glob


class Student:
    TYPES = ("humanitarian", "natural", "natural-humanitarian")

    def __init__(self, student_type: str, credits_required: int, money: float):
        if student_type not in self.TYPES:
            raise ValueError(f"Невідомий тип студента: {student_type}")
        self.student_type = student_type
        self.credits_required = credits_required
        self.money = money
        self.credits_earned = 0
        self.expelled = False

    def teach(self, discipline_type: str, credits: int) -> bool:
        if self.student_type == "humanitarian":
            can_learn = (discipline_type == "humanitarian")
        elif self.student_type == "natural":
            can_learn = (discipline_type == "natural")
        else:
            can_learn = True
        if can_learn:
            self.credits_earned += credits
        return can_learn

    def obtain_scholarship(self, amount: float):
        self.money += amount

    def obtain_help(self, amount: float):
        self.money += amount

    def pay_hostel(self, amount: float) -> bool:
        if self.money >= amount:
            self.money -= amount
            return True
        self.expelled = True
        return False

    def pay_canteen(self, amount: float) -> bool:
        if self.money >= amount:
            self.money -= amount
            return True
        self.expelled = True
        return False

    @property
    def has_diploma(self) -> bool:
        return not self.expelled and self.credits_earned >= self.credits_required


class Visitor:
    def visit(self, student: Student, steps: list[tuple]) -> bool:
        for step in steps:
            if student.expelled:
                break
            action = step[0]
            if action == "teach":
                student.teach(step[1], int(float(step[2])))
            elif action == "obtain":
                amount = float(step[2])
                if step[1] == "scholarship":
                    student.obtain_scholarship(amount)
                elif step[1] == "help":
                    student.obtain_help(amount)
            elif action == "pay":
                amount = float(step[2])
                if step[1] == "hostel":
                    student.pay_hostel(amount)
                elif step[1] == "canteen":
                    student.pay_canteen(amount)
        return student.has_diploma


def parse_number(s: str) -> float:
    s = s.strip()
    if '/' in s:
        a, b = s.split('/', 1)
        return float(a) / float(b)
    return float(s)


def parse_input_file(filepath: str) -> tuple[Student, list[tuple]]:
    with open(filepath, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]

    student_type = lines[0]

    # Рядки 2 і 3 можуть містити кілька токенів — беремо перший
    credits_required = int(parse_number(lines[1].split()[0]))
    money = parse_number(lines[2].split()[0])

    steps = []
    for line in lines[3:]:
        parts = line.split()
        if len(parts) >= 3:
            steps.append(tuple(parts))

    return Student(student_type, credits_required, money), steps


def process_file(filepath: str) -> str:
    student, steps = parse_input_file(filepath)
    got_diploma = Visitor().visit(student, steps)
    filename = os.path.basename(filepath)
    result = "отримав диплом" if got_diploma else "НЕ отримав диплом"
    return f"{filename}: студент {result}"


def main():
    if len(sys.argv) > 1:
        filepaths = sys.argv[1:]
    else:
        filepaths = sorted(glob.glob("input*.txt"))
        if not filepaths:
            print("Не знайдено жодного файлу input*.txt у поточній папці.")
            sys.exit(1)

    for fp in filepaths:
        if not os.path.exists(fp):
            print(f"Файл не знайдено: {fp}")
            continue
        try:
            print(process_file(fp))
        except Exception as e:
            print(f"{fp}: помилка — {e}")


if __name__ == "__main__":
    main()
