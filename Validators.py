def check_price(user_input):
    # Check if user input is a valid number
    try:
        price = float(user_input)
    except ValueError:
        return None, "That is not a valid number. Please type a number like 10 or 15.50."

    # Check if number is zero or negative
    if price <= 0:
        return None, "Price must be more than 0!"

    return price, None


def check_text(user_input, label_name):
    # Remove extra spaces
    clean_input = user_input.strip()

    # Check if user left it blank
    if len(clean_input) == 0:
        return None, label_name + " cannot be left blank."

    return clean_input, None