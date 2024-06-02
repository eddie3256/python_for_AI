import tools
from tools import Student

def main():
    print(tools.PI)
    s1:Students = tools.get_student(name="摳呆", chinese=89, english=92, math=91)
    print(f"name = {s1.name}")
    print(f"chinese = {s1.chinese}")
    print(f"english = {s1.english}")
    print(f"math = {s1.math}")
    print(f"total: {s1.sum()}")
    print(f"avetage: {s1.average()}")

if __name__ == "__main__":
    main()