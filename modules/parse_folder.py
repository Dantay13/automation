def parse_log_file(log_file, target_directory):
    error_file = os.path.join(target_directory, "errors.log")
    warning_file = os.path.join(target_directory, "warnings.log")

    with open(log_file, "r") as file:
        error_lines = []
        warning_lines = []
        for line in file:
            if "ERROR" in line:
                error_lines.append(line)
            elif "WARNING" in line:
                warning_lines.append(line)

    with open(error_file, "w") as file:
        file.writelines(error_lines)

    with open(warning_file, "w") as file:
        file.writelines(warning_lines)

# Usage:
parse_log_file("logs_folder/log.txt", "target_directory")
