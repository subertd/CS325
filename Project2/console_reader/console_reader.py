class ConsoleReader:

    def get_user_input_file_name(self):

        user_input_file_name = ""

        prompt = "What file would you like me to inspect for you, Dave?\n"

        while len(user_input_file_name) == 0:
            raw_input(prompt)

        return user_input_file_name