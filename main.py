def write_question(filename, surname, question):
    """Function to write a question to a file."""
    try:
        with open(filename, 'w') as file:
            file.write(f"{surname}\n")
            file.write(f"Question: {question}\n")
    except IOError as e:
        print(f"Error writing to file: {e}")

def append_answer_and_question(filename, surname, answer, new_question):
    """Function to append an answer and a new question to the file."""
    try:
        with open(filename, 'a') as file:
            file.write(f"{surname}\n")
            file.write(f"Answer: {answer}\n")
            file.write(f"New question: {new_question}\n")
    except IOError as e:
        print(f"Error adding information: {e}")


write_question('programming_questions.txt', 'Koshman', 'How to use list comprehension in Python?')

append_answer_and_question('programming_questions.txt', 'Ruban', 'Honestly speaking, i don`t know?','Python or c++')
