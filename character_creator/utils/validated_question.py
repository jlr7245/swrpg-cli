import PyInquirer

def validated_question(question, validator):
    """Validator function in PyInquirer is broken;
    this won't let matters proceed until the validator
    says everything is the correct format."""
    has_been_validated = False
    while not has_been_validated:
        answer = PyInquirer.prompt(question)
        is_valid = validator(answer)
        if is_valid != True:
            print(is_valid)
        else:
            has_been_validated = True
            return answer
