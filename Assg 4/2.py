class UserProfile:
    def __init__(self, username, email, password, security_question):
        self._username = username  # Public attribute
        self._email = email  # Public attribute
        self.__password = password  # Private attribute
        self.__security_question = security_question  # Private attribute

    # Getter method for username
    def get_username(self):
        return self._username

    # Setter method for username with validation
    def set_username(self, new_username):
        if isinstance(new_username, str):
            self._username = new_username
        else:
            print("Invalid username. Please provide a valid string.")

    # Getter method for email
    def get_email(self):
        return self._email

    # Setter method for email with validation
    def set_email(self, new_email):
        if isinstance(new_email, str):
            self._email = new_email
        else:
            print("Invalid email. Please provide a valid string.")

    # Getter method for security_question
    def get_security_question(self):
        return self.__security_question

    # Setter method for security_question with validation
    def set_security_question(self, new_security_question):
        if isinstance(new_security_question, str):
            self.__security_question = new_security_question
        else:
            print("Invalid security question. Please provide a valid string.")

    # Getter method for password (returns a masked version for security)
    def get_password(self):
        return "****"

    # Setter method for password with validation
    def set_password(self, new_password):
        if isinstance(new_password, str):
            self.__password = new_password
        else:
            print("Invalid password. Please provide a valid string.")

# Example usage
user_profile = UserProfile(username="john_doe", email="john@example.com", password="secretpassword", security_question="Favorite color?")

# Accessing public attributes
print("Username:", user_profile._username)
print("Email:", user_profile._email)

# Accessing private attributes using getter methods
print("Security Question:", user_profile.get_security_question())
print("Password:", user_profile.get_password())

# Modifying private attributes using setter methods
user_profile.set_username("jane_doe")
user_profile.set_email("jane@example.com")
user_profile.set_security_question("Favorite movie?")
user_profile.set_password("newsecretpassword")

# Displaying updated information
print("Updated Username:", user_profile._username)
print("Updated Email:", user_profile._email)
print("Updated Security Question:", user_profile.get_security_question())
print("Updated Password:", user_profile.get_password())
