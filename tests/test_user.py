"""
Unit tests for the User class.
"""

import unittest
import sys
import os
from datetime import datetime
from unittest.mock import patch

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from user import User


class TestUser(unittest.TestCase):
    """Test cases for the User class."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.valid_username = "testuser123"
        self.valid_email = "test@example.com"
        self.valid_full_name = "Test User"
    
    def test_user_initialization_with_required_params(self):
        """Test user initialization with required parameters only."""
        user = User(self.valid_username, self.valid_email)
        
        self.assertEqual(user.username, self.valid_username)
        self.assertEqual(user.email, self.valid_email)
        self.assertEqual(user.full_name, "")
        self.assertIsInstance(user.created_at, datetime)
        self.assertTrue(user.is_active)
        self.assertEqual(user.login_count, 0)
        self.assertIsNone(user.last_login)
    
    def test_user_initialization_with_all_params(self):
        """Test user initialization with all parameters."""
        user = User(self.valid_username, self.valid_email, self.valid_full_name)
        
        self.assertEqual(user.username, self.valid_username)
        self.assertEqual(user.email, self.valid_email)
        self.assertEqual(user.full_name, self.valid_full_name)
        self.assertTrue(user.is_active)
    
    def test_username_validation_valid_usernames(self):
        """Test valid username formats."""
        valid_usernames = ["user123", "test_user", "ABC123", "a1b2c3", "user_name_123"]
        
        for username in valid_usernames:
            user = User(username, self.valid_email)
            self.assertEqual(user.username, username)
    
    def test_username_validation_invalid_type(self):
        """Test username validation with invalid types."""
        with self.assertRaises(TypeError) as context:
            User(123, self.valid_email)
        self.assertEqual(str(context.exception), "Username must be a string")
        
        with self.assertRaises(TypeError):
            User(None, self.valid_email)
        
        with self.assertRaises(TypeError):
            User([], self.valid_email)
    
    def test_username_validation_too_short(self):
        """Test username validation with too short usernames."""
        short_usernames = ["", "a", "ab"]
        
        for username in short_usernames:
            with self.assertRaises(ValueError) as context:
                User(username, self.valid_email)
            self.assertEqual(str(context.exception), "Username must be at least 3 characters long")
    
    def test_username_validation_too_long(self):
        """Test username validation with too long usernames."""
        long_username = "a" * 21  # 21 characters
        
        with self.assertRaises(ValueError) as context:
            User(long_username, self.valid_email)
        self.assertEqual(str(context.exception), "Username must be at most 20 characters long")
    
    def test_username_validation_invalid_characters(self):
        """Test username validation with invalid characters."""
        invalid_usernames = ["user-name", "user@name", "user name", "user.name", "user#name"]
        
        for username in invalid_usernames:
            with self.assertRaises(ValueError) as context:
                User(username, self.valid_email)
            self.assertEqual(str(context.exception), "Username can only contain letters, numbers, and underscores")
    
    def test_email_validation_valid_emails(self):
        """Test valid email formats."""
        valid_emails = [
            "test@example.com",
            "user.name@domain.org",
            "user+tag@company.co.uk",
            "123@numbers.com",
            "test_user@sub.domain.com"
        ]
        
        for email in valid_emails:
            user = User(self.valid_username, email)
            self.assertEqual(user.email, email.lower())
    
    def test_email_validation_invalid_type(self):
        """Test email validation with invalid types."""
        with self.assertRaises(TypeError) as context:
            User(self.valid_username, 123)
        self.assertEqual(str(context.exception), "Email must be a string")
        
        with self.assertRaises(TypeError):
            User(self.valid_username, None)
    
    def test_email_validation_invalid_format(self):
        """Test email validation with invalid formats."""
        invalid_emails = [
            "invalid-email",
            "@domain.com",
            "user@",
            "user@domain",
            "user.domain.com",
            "user@@domain.com",
            "user@domain..com",
            ""
        ]
        
        for email in invalid_emails:
            with self.assertRaises(ValueError) as context:
                User(self.valid_username, email)
            self.assertEqual(str(context.exception), "Invalid email format")
    
    def test_email_case_normalization(self):
        """Test that email addresses are normalized to lowercase."""
        email = "TEST@EXAMPLE.COM"
        user = User(self.valid_username, email)
        self.assertEqual(user.email, "test@example.com")
    
    def test_login_successful(self):
        """Test successful user login."""
        user = User(self.valid_username, self.valid_email)
        
        with patch('user.datetime') as mock_datetime:
            mock_now = datetime(2023, 1, 1, 12, 0, 0)
            mock_datetime.now.return_value = mock_now
            
            result = user.login()
            
            self.assertTrue(result)
            self.assertEqual(user.login_count, 1)
            self.assertEqual(user.last_login, mock_now)
    
    def test_login_multiple_times(self):
        """Test multiple user logins."""
        user = User(self.valid_username, self.valid_email)
        
        user.login()
        user.login()
        user.login()
        
        self.assertEqual(user.login_count, 3)
        self.assertIsInstance(user.last_login, datetime)
    
    def test_login_deactivated_user(self):
        """Test login attempt with deactivated user."""
        user = User(self.valid_username, self.valid_email)
        user.deactivate()
        
        with self.assertRaises(ValueError) as context:
            user.login()
        self.assertEqual(str(context.exception), "User account is deactivated")
        self.assertEqual(user.login_count, 0)
        self.assertIsNone(user.last_login)
    
    def test_user_deactivation(self):
        """Test user account deactivation."""
        user = User(self.valid_username, self.valid_email)
        self.assertTrue(user.is_active)
        
        user.deactivate()
        self.assertFalse(user.is_active)
    
    def test_user_activation(self):
        """Test user account activation."""
        user = User(self.valid_username, self.valid_email)
        user.deactivate()
        self.assertFalse(user.is_active)
        
        user.activate()
        self.assertTrue(user.is_active)
    
    def test_update_email_valid(self):
        """Test updating user email with valid email."""
        user = User(self.valid_username, self.valid_email)
        new_email = "newemail@example.com"
        
        user.update_email(new_email)
        self.assertEqual(user.email, new_email)
    
    def test_update_email_invalid(self):
        """Test updating user email with invalid email."""
        user = User(self.valid_username, self.valid_email)
        
        with self.assertRaises(ValueError):
            user.update_email("invalid-email")
        
        # Email should remain unchanged
        self.assertEqual(user.email, self.valid_email)
    
    def test_update_full_name_valid(self):
        """Test updating user full name with valid name."""
        user = User(self.valid_username, self.valid_email)
        new_name = "New Full Name"
        
        user.update_full_name(new_name)
        self.assertEqual(user.full_name, new_name)
    
    def test_update_full_name_invalid_type(self):
        """Test updating user full name with invalid type."""
        user = User(self.valid_username, self.valid_email, self.valid_full_name)
        
        with self.assertRaises(TypeError) as context:
            user.update_full_name(123)
        self.assertEqual(str(context.exception), "Full name must be a string")
        
        # Full name should remain unchanged
        self.assertEqual(user.full_name, self.valid_full_name)
    
    def test_get_user_info(self):
        """Test getting user information as dictionary."""
        user = User(self.valid_username, self.valid_email, self.valid_full_name)
        user.login()
        
        user_info = user.get_user_info()
        
        expected_keys = {'username', 'email', 'full_name', 'created_at', 'is_active', 'login_count', 'last_login'}
        self.assertEqual(set(user_info.keys()), expected_keys)
        
        self.assertEqual(user_info['username'], self.valid_username)
        self.assertEqual(user_info['email'], self.valid_email)
        self.assertEqual(user_info['full_name'], self.valid_full_name)
        self.assertTrue(user_info['is_active'])
        self.assertEqual(user_info['login_count'], 1)
        self.assertIsInstance(user_info['created_at'], datetime)
        self.assertIsInstance(user_info['last_login'], datetime)
    
    def test_str_representation(self):
        """Test string representation of user."""
        user = User(self.valid_username, self.valid_email)
        expected_str = f"User(username='{self.valid_username}', email='{self.valid_email}', active=True)"
        self.assertEqual(str(user), expected_str)
    
    def test_repr_representation(self):
        """Test detailed string representation of user."""
        user = User(self.valid_username, self.valid_email, self.valid_full_name)
        expected_repr = f"User(username='{self.valid_username}', email='{self.valid_email}', full_name='{self.valid_full_name}', is_active=True)"
        self.assertEqual(repr(user), expected_repr)
    
    def test_user_lifecycle(self):
        """Test complete user lifecycle."""
        # Create user
        user = User(self.valid_username, self.valid_email, self.valid_full_name)
        self.assertTrue(user.is_active)
        self.assertEqual(user.login_count, 0)
        
        # Login multiple times
        user.login()
        user.login()
        self.assertEqual(user.login_count, 2)
        
        # Update profile
        new_email = "updated@example.com"
        new_name = "Updated Name"
        user.update_email(new_email)
        user.update_full_name(new_name)
        
        self.assertEqual(user.email, new_email)
        self.assertEqual(user.full_name, new_name)
        
        # Deactivate and try to login
        user.deactivate()
        with self.assertRaises(ValueError):
            user.login()
        
        # Reactivate and login
        user.activate()
        user.login()
        self.assertEqual(user.login_count, 3)


if __name__ == '__main__':
    unittest.main()