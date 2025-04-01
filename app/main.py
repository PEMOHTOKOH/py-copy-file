def copy_file(command: str) -> None:
    cmd = command.split()
    if len(cmd) == 3:
        copy_command = cmd[0]
        file_name_to_copy = cmd[1]
        new_file_name = cmd[2]
    else:
        return

    if file_name_to_copy != new_file_name and copy_command == "cp":
        try:
            with (open(file_name_to_copy, "r") as file_in,
                  open(new_file_name, "w") as file_out):
                file_out.write(file_in.read())
        except FileNotFoundError:
            return
