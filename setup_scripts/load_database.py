import brewery_db_accessor as bda


def load():
    """Main script to check, create, and restore."""
    # Check if the database exists
    if bda.check_database_exists():
        print(f"Database '{bda.db_name}' already exists. Dropping and recreating.")
        bda.drop_database()
    else:
        print(f"Database '{bda.db_name}' does not exist. Creating...")

    bda.create_database()
    bda.restore_dump()


def main():
    load()


if __name__ == "__main__":
    main()
