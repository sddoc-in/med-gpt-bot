import openai

## API key
openai.api_key = "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"

flag = True

while flag:
  try:
    patient_age = int(input("Enter patient's age: "))
    if patient_age < 0:
        print("Age cannot be negative")
        continue
    print("Choose: \n1. Disease \n2. Symptoms \n3. Conditions")
    choice_type = int(input("Enter your choice: "))
    switcher = {
        1: "disease",
        2: "symptoms",
        3: "conditions"
    }
    choice = switcher.get(choice_type, "Invalid choice")
    if(choice == "Invalid choice"):
        print("Invalid choice")
        continue
    data = input("Enter the " + choice + " of the patient: ")
    print("Patient's age is " + str(patient_age) + " and " + choice + " is " + data)

    question = input("Enter your question: ")

    main_question_str = "I am a patient and I have a question about my health. My age is " + str(patient_age) + " and " + choice + " is " + data + ". My question is: " + question + " What is the answer?"

    print("\n\nLoading...\n\n")
    completion = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "system", "content": "You are a doctor and have to answer patient's question."},
        {"role": "user", "content": main_question_str}
      ]
    )

    print("Answer: \n")
    print(completion.choices[0].message["content"])
    print("\n\n")

    exit_flag = input("Do you want to exit? (y/n): ")
    if exit_flag == 'n':
        flag = False
        
    print("\n\n")
    

  except:
    print("Invalid input")
    continue