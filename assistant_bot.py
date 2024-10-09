def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def input_error(func):
    def validate(*args):
        params = args[0]
        contacts = args[1]
        func_name = func.__name__

        if func_name == "cmd_add_contact":
            if len(params) == 0:
                msg = "Please enter command in the format: add [username] [phone]"
                complete = False
                return (msg, complete)

            if len(params) == 1:
                msg = "Please enter a phone."
                complete = False
                return (msg, complete)

            name, phone = params
            if contacts.get(name):
                msg = "Contact already exists."
                complete = False
                return (msg, complete)

        if func_name == "cmd_change_contact":
            if len(params) == 0:
                msg = "Please enter command in the format: change [username] [phone]"
                complete = False
                return (msg, complete)

            if len(params) == 1:
                msg = "Please enter a phone."
                complete = False
                return (msg, complete)

            name, phone = params
            if not contacts.get(name):
                msg = "Contact not exist"
                complete = False
                return (msg, complete)

        if func_name == "cmd_phone":
            if len(params) == 0:
                msg = "Please enter command in the format: phone [username]"
                complete = False
                return (msg, complete)

            name = params[0]
            phone = contacts.get(name)
            if not phone:
                msg = "Contact not exist."
                complete = False
                return (msg, complete)

        if func_name == "cmd_all":
            if len(contacts) == 0:
                msg = "Contacts list is empty"
                complete = False
                return (msg, complete)

        return func(*args)

    return validate


def cmd_hello(*args):
    msg = "How can I help you?"
    complete = False
    return (msg, complete)


def cmd_exit(*args):
    msg = "Good bye!"
    complete = True
    return (msg, complete)


@input_error
def cmd_add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    msg = "Contact added."
    complete = False
    return (msg, complete)


@input_error
def cmd_change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    msg = "Contact changed."
    complete = False
    return (msg, complete)


@input_error
def cmd_phone(args, contacts):
    name = args[0]
    phone = contacts.get(name)
    msg = phone
    complete = False
    return (msg, complete)


@input_error
def cmd_all(args, contacts):
    msg = contacts
    complete = False
    return (msg, complete)


COMMANDS = {
    "hello": cmd_hello,
    "close": cmd_exit,
    "exit": cmd_exit,
    "add": cmd_add_contact,
    "change": cmd_change_contact,
    "phone": cmd_phone,
    "all": cmd_all
}


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        try:
            if not len(user_input.strip()):
                print("Please enter a command.")
                continue

            command, *args = parse_input(user_input)
            callback = COMMANDS.get(command)
            if callback:
                msg, complete = callback(args, contacts)
                if msg:
                    print(msg)
                if complete:
                    exit(0)
            else:
                print("Invalid command.")
        except Exception as e:
            print("Internal error", e)


if __name__ == "__main__":
    main()
