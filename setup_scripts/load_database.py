import brewery_db_accessor as bda


def main():
    """Main script to check, create, and restore."""
    # Check if the database exists
    if bda.check_database_exists():
        print(f"Database '{bda.db_name}' already exists.")
    else:
        print(f"Database '{bda.db_name}' does not exist. Creating...")
        bda.create_database()

    # Restore the dump file
    bda.restore_dump()


if __name__ == "__main__":
    main()
