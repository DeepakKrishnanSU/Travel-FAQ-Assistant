from matcher import find_best_answer

def load_faq(file_path):
    faq = {}
    question = None

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()

            if line.startswith("Q:"):
                question = line[2:].strip()

            elif line.startswith("A:") and question:
                answer = line[2:].strip()
                faq[question] = answer
                question = None

    return faq


def main():
    faq_data = load_faq("faq.txt")

    print("Travel FAQ Assistant")
    print("Type 'exit' to quit\n")

    while True:
        user_input = input("Ask a travel question: ")
        if user_input.lower() == "exit":
            break

        answer = find_best_answer(user_input, faq_data)
        print("\nAnswer:", answer)
        print("-" * 40)


if __name__ == "__main__":
    main()