#!/usr/bin/env python3
"""
Test runner script for the project.
"""

import sys
import subprocess

def run_tests():
    """Run all unit tests."""
    try:
        # Run tests with unittest
        result = subprocess.run([
            sys.executable, '-m', 'unittest', 'discover', 
            '-s', 'tests', '-p', 'test_*.py', '-v'
        ], cwd='.')
        return result.returncode == 0
    except Exception as e:
        print(f"Error running tests: {e}")
        return False

def run_tests_with_coverage():
    """Run tests with coverage report."""
    try:
        # Install coverage if not available
        subprocess.run([sys.executable, '-m', 'pip', 'install', 'coverage'], check=True)
        
        # Run tests with coverage
        subprocess.run([
            sys.executable, '-m', 'coverage', 'run', '-m', 'unittest', 
            'discover', '-s', 'tests', '-p', 'test_*.py'
        ], cwd='.', check=True)
        
        # Generate coverage report
        subprocess.run([sys.executable, '-m', 'coverage', 'report'], cwd='.', check=True)
        
        return True
    except Exception as e:
        print(f"Error running tests with coverage: {e}")
        return False

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Run project tests')
    parser.add_argument('--coverage', action='store_true', help='Run tests with coverage')
    args = parser.parse_args()
    
    if args.coverage:
        success = run_tests_with_coverage()
    else:
        success = run_tests()
    
    sys.exit(0 if success else 1)