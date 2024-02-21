def print_color_chars(text: str, definition_of_colors: dict[str, str]) -> None:
    reset = "\033[0m"
    colors = {
        "black": "\033[30m",
        "red": "\033[31m",
        "green": "\033[32m",
        "yellow": "\033[33m",
        "blue": "\033[34m",
        "magenta": "\033[35m",
        "cyan": "\033[36m",
        "white": "\033[37m",
    }
    colored_text = ""
    for char in text:
        if char in definition_of_colors:
            color_code = colors[definition_of_colors[char]]
            colored_text += f"{color_code}{char}{reset}"
        else:
            colored_text += char

    print(colored_text)
