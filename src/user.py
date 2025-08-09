"""
User class - A main class for user management.
"""

from datetime import datetime
import re

class User:
    """A user management class with basic user operations."""
    
    def __init__(self, username, email, full_name=""):
        """Initialize a new user."""
        self.username = self._validate_username(username)
        self.email = self._validate_email(email)
        self.full_name = full_name
        self.created_at = datetime.now()
        self.is_active = True
        self.login_count = 0
        self.last_login = None
    
    def _validate_username(self, username):
        """Validate username format."""
        if not isinstance(username, str):
            raise TypeError("Username must be a string")
        if len(username) < 3:
            raise ValueError("Username must be at least 3 characters long")
        if len(username) > 20:
            raise ValueError("Username must be at most 20 characters long")
        if not re.match(r'^[a-zA-Z0-9_]+$', username):
            raise ValueError("Username can only contain letters, numbers, and underscores")
        return username
    
    def _validate_email(self, email):
        """Validate email format."""
        if not isinstance(email, str):
            raise TypeError("Email must be a string")
        # More strict email pattern that doesn't allow consecutive dots
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9]([a-zA-Z0-9-]*[a-zA-Z0-9])?(\.[a-zA-Z0-9]([a-zA-Z0-9-]*[a-zA-Z0-9])?)*\.[a-zA-Z]{2,}$'
        if not re.match(email_pattern, email):
            raise ValueError("Invalid email format")
        return email.lower()
    
    def login(self):
        """Record a user login."""
        if not self.is_active:
            raise ValueError("User account is deactivated")
        self.login_count += 1
        self.last_login = datetime.now()
        return True
    
    def deactivate(self):
        """Deactivate the user account."""
        self.is_active = False
    
    def activate(self):
        """Activate the user account."""
        self.is_active = True
    
    def update_email(self, new_email):
        """Update user email address."""
        self.email = self._validate_email(new_email)
    
    def update_full_name(self, new_full_name):
        """Update user full name."""
        if not isinstance(new_full_name, str):
            raise TypeError("Full name must be a string")
        self.full_name = new_full_name
    
    def get_user_info(self):
        """Get user information as a dictionary."""
        return {
            'username': self.username,
            'email': self.email,
            'full_name': self.full_name,
            'created_at': self.created_at,
            'is_active': self.is_active,
            'login_count': self.login_count,
            'last_login': self.last_login
        }
    
    def __str__(self):
        """String representation of the user."""
        return f"User(username='{self.username}', email='{self.email}', active={self.is_active})"
    
    def __repr__(self):
        """Detailed string representation of the user."""
        return f"User(username='{self.username}', email='{self.email}', full_name='{self.full_name}', is_active={self.is_active})"