# %%
from pathlib import Path
import re
def main():
    user_input_dir = FileArrange.getUserInputs()


class FileArrange:
    def __init__(self, main_dir, new_folder_name):
        self.main_dir = main_dir
        self.new_folder_name = new_folder_name
        # creating Path object
        self.new_folder_dir = Path(self.main_dir / self.new_folder_name)

    @classmethod
    def getUserInputs(cls):
        main_dir = input("Insert the dir").strip()
        new_folder_name = "Arranged_Files"
        # validation
        if re.match(r"^[A-Za-z]:\\(?:[^\\/:*?\"<>|\r\n]+\\)*$", main_dir):
            return cls(main_dir, new_folder_name)
        else:
            print(f"{main_dir} is not a valid dir")
            return None

    def __str__(self):
        print(self.new_folder_dir)

if __name__ == "__main__":
    main()

# %%
