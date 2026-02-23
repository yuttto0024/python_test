file_name = "config.txt"

with open(file_name, "r") as f:
    raw_config_data = f.read()
    # image: "WIDTH=20\nHEIGHT=15\n\n# comment\nENTRY=0,0\n"
    config_line = raw_config_data.split("\n")
    print(f"{file_all_data}")
