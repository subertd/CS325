class ConsoleReader:

    def get_user_input_file_name(self):

        user_input_file_name = ""

        prompt = "Name of file to open: "

        while len(user_input_file_name) == 0:
            user_input_file_name = raw_input(prompt)

        return user_input_file_name