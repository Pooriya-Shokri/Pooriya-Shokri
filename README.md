# Pooriya Shokri's Repository

👋 Hi, I'm @Pooriya-Shokri  
📫 Contact: pooriya(dot)shokri(at)gmail.com

## Project Structure

This repository contains example Python classes with comprehensive unit tests demonstrating best practices for software testing.

### Main Classes

- **Calculator** (`src/calculator.py`): A robust calculator class supporting basic arithmetic operations with history tracking
- **User** (`src/user.py`): A user management class with validation, authentication, and profile management features

### Features

#### Calculator Class
- Basic arithmetic operations (add, subtract, multiply, divide, power)
- Operation history tracking
- Input validation and error handling
- Support for integers and floating-point numbers

#### User Class
- User registration with validation
- Email format validation with strict rules
- Username validation (3-20 chars, alphanumeric + underscore)
- Login tracking and account management
- Profile updates and user lifecycle management

## Testing

The project includes comprehensive unit tests covering:

- **54 test cases** across both main classes
- Edge cases and error conditions
- Input validation testing
- State management verification
- Complete code coverage of public methods

### Running Tests

```bash
# Run tests using unittest
python -m unittest discover -s tests -p "test_*.py" -v

# Or use the test runner script
python run_tests.py

# Run tests with coverage (installs coverage automatically)
python run_tests.py --coverage
```

### Test Coverage

- **Calculator tests** (`tests/test_calculator.py`): 30 test cases
- **User tests** (`tests/test_user.py`): 24 test cases
- All tests validate both happy path and error conditions
- Comprehensive input validation testing
- Mock usage for datetime testing

## Project Structure

```
├── src/                    # Source code
│   ├── __init__.py
│   ├── calculator.py       # Calculator class
│   └── user.py            # User management class
├── tests/                  # Unit tests
│   ├── __init__.py
│   ├── test_calculator.py  # Calculator tests
│   └── test_user.py       # User tests
├── requirements.txt        # Dependencies
├── setup.cfg              # Test configuration
├── run_tests.py           # Test runner script
└── README.md              # This file
```

## Dependencies

- Python 3.6+
- No external dependencies for main classes
- Optional: `pytest` and `coverage` for enhanced testing

## Example Usage

```python
from src.calculator import Calculator
from src.user import User

# Calculator example
calc = Calculator()
result = calc.add(10, 5)        # Returns 15
result = calc.multiply(3, 4)    # Returns 12
history = calc.get_history()    # Get operation history

# User example
user = User("john_doe", "john@example.com", "John Doe")
user.login()                    # Record login
user.update_email("newemail@example.com")
info = user.get_user_info()     # Get user details
```

This project demonstrates professional Python development practices including proper code organization, comprehensive testing, input validation, and documentation.