import random


def random_int(min, max):
    """
    Random integer

    Args:
        min (int): minimum allowed integer
        max (int): maximum allowed integer

    Returns:
        int: random integer between (min,max)
    """
    return random.randint(min, max)


def random_operation():
    """
    Returns a random operator from ('+','-','*')
        
    Returns:
        string: operator
    """
    return random.choice(['+', '-', '*'])


def calculate_result(n1, n2, o):
    """
    Calculate the result of the operation

    Args:
        n1 (int): Operand-1
        n2 (int): Operand-2
        o (string): Operation

    Returns:
        p (string): problem statement
        a (int): final result of the operation
    """
    p = f"{n1} {o} {n2}"
    if o == '+': a = n1 + n2
    elif o == '-': a = n1 - n2
    else: a = n1 * n2
    return p, a

def math_quiz():
    """
    The `math_quiz` function generates math problems for the user to solve and keeps track of their
    score.
    """
    total_points = 0 # counter for points
    total_questions = 3 # total questions to be generated

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        n1 = random_int(1, 10); n2 = random_int(1, 5); o = random_operation()

        PROBLEM, ANSWER = calculate_result(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")
        
        # Check if useranswer is an integer
        try:
            useranswer = int(useranswer)
            if useranswer == ANSWER:
                print("Correct! You earned a point.")
                total_points += 1
            else:
                print(f"Wrong answer. The correct answer is {ANSWER}.")
        except ValueError:
            print("Please enter a number!")



    print(f"\nGame over! Your score is: {total_points}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
