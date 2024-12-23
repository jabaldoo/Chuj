import argparse
import random
import os

def print_ascii_art():
    """Displays ASCII art for 'chuj'."""
    ascii_art = r"""
    

    _______   .---.  .---.   ___    _      .-./`)   
   /   __  \  |   |  |_ _| .'   |  | |     \ '_ .') 
  | ,_/  \__) |   |  ( ' ) |   .'  | |    (_ (_) _) 
,-./  )       |   '-(_{;}_).'  '_  | |      / .  \  
\  '_ '`)     |      (_,_) '   ( \.-.| ___  |-'`|   
 > (_)  )  __ | _ _--.   | ' (`. _` /||   | |   '   
(  .  .-'_/  )|( ' ) |   | | (_ (_) _)|   `-'  /    
 `-'`-'     / (_{;}_)|   |  \ /  . \ / \      /     
   `._____.'  '(_,_) '---'   ``-'`-''   `-..-'      
                                                    


    print(ascii_art)

def show_random_line(database_path):
    """Displays a random line from the database file."""
    if not os.path.exists(database_path):
        print("Database file not found! Please create the file with your entries.")
        return

    with open(database_path, 'r') as file:
        lines = [line.strip() for line in file if line.strip()]

    if not lines:
        print("The database is empty! Add some lines to the file.")
        return

    print(random.choice(lines))

def main():
    # Hardcoded path for the database
    default_db_path = os.path.expanduser('~/Documents/data.txt')

    parser = argparse.ArgumentParser(description="The 'chuj' CLI app: Display a random line from your database.")
    parser.add_argument(
        '--db', 
        type=str, 
        default=default_db_path,
        help=f"Path to the database file (default: '{default_db_path}')."
    )
    parser.add_argument('--show-db', action='store_true', help="Print the default database path.")
    parser.add_argument('--view', action='store_true', help="Display all lines in the database file.")

    args = parser.parse_args()

    # Print ASCII art when the app runs
    print_ascii_art()

    if args.show_db:
        print(f"Default database path: {default_db_path}")
        return

    if args.view:
        if os.path.exists(args.db):
            with open(args.db, 'r') as file:
                print(file.read())
        else:
            print(f"Database file not found at '{args.db}'.")
        return

    show_random_line(args.db)

if __name__ == '__main__':
    main()
