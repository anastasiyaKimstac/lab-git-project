# main.py
from utils import add_num, multiply_num

def main():
    result_add = add_num(5, 3)
    result_multiply = multiply_num(5, 3)
    print(f"Addition Result: {result_add}")
    print(f"Multiplication Result: {result_multiply}")

if __name__ == "__main__":
    main()
