def array_of_names(name_dict):
    full_names = []
    for first, last in name_dict.items():
       
        full_name = f"{first.capitalize()} {last.capitalize()}"
        full_names.append(full_name)
    return full_names


if __name__ == "__main__":
    example_dict = {
        "john": "doe",
        "jane": "smith",
        "alice": "johnson"
    }

    names = array_of_names(example_dict)
    print(names)