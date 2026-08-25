class Employee:

    # Base/minimum salary for each level
    _base_salaries = {
        'trainee': 1000,
        'junior': 2000,
        'mid-level': 3000,
        'senior': 4000,
    }

    def __init__(self, name, level):
        self.name = name
        self.level = level

        # Set the starting salary based on the employee's level
        self.salary = Employee._base_salaries[level]

    # Controls how the Employee object looks when printed
    def __str__(self):
        return f'{self.name}: {self.level}'

    # Gives a developer-friendly representation of the object
    def __repr__(self):
        return f"Employee('{self.name}', '{self.level}')"

    # ---------------- NAME ----------------

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):

        # Name must be a string
        if not isinstance(new_name, str):
            raise TypeError("'name' must be a string.")

        self._name = new_name
        print(f"'name' updated to '{self.name}'.")

    # ---------------- LEVEL ----------------

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, new_level):

        # Level must be a string
        if not isinstance(new_level, str):
            raise TypeError("'level' must be a string.")

        # Level must exist in the base salaries dictionary
        if new_level not in Employee._base_salaries:
            raise ValueError(
                f"Invalid value '{new_level}' for 'level' attribute."
            )

        # Prevent selecting the same level again
        if hasattr(self, '_level') and new_level == self.level:
            raise ValueError(
                f"'{self.level}' is already the selected level."
            )

        # Prevent an employee from being demoted
        if hasattr(self, '_level') and Employee._base_salaries[new_level] < Employee._base_salaries[self.level]:
            raise ValueError("Cannot change to lower level.")

        print(f"'{self.name}' promoted to '{new_level}'.")

        # Use the salary setter instead of changing _salary directly
        self.salary = Employee._base_salaries[new_level]

        self._level = new_level

    # ---------------- SALARY ----------------

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, new_salary):

        # Salary must be an integer or a float
        if not isinstance(new_salary, (int, float)):
            raise TypeError("'salary' must be a number.")

        # Salary cannot be lower than the minimum salary
        # for the employee's current level
        if hasattr(self, '_level') and new_salary < Employee._base_salaries[self.level]:
            raise ValueError(
                f"Salary must be higher than minimum salary ${Employee._base_salaries[self.level]}."
            )

        self._salary = new_salary
        print(f'Salary updated to ${self.salary}.')


# ---------------- TESTING THE CLASS ----------------

# Create an Employee object
# Create an Employee object
gebremariam_godad = Employee('Gebremariam Godad', 'trainee')

# __str__() is called here
print(gebremariam_godad)

# Access the salary through the salary property
print(f'Base salary: ${gebremariam_godad.salary}')

# Promote Gebremariam from trainee to junior
gebremariam_godad.level = 'junior'