#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
StructureTools Test Runner

Simple test runner script for StructureTools workbench.
Run this script to execute the test suite with proper configuration.
"""

import os
import sys
import subprocess
from pathlib import Path


def main():
    """Run the StructureTools test suite."""
    
    # Get project root directory
    script_dir = Path(__file__).parent
    os.chdir(script_dir)
    
    print("StructureTools Test Runner")
    print("=" * 50)
    print(f"Project Directory: {script_dir}")
    print(f"Python Version: {sys.version}")
    print()
    
    # Check if pytest is available
    try:
        import pytest
        print(f"[OK] Pytest version: {pytest.__version__}")
    except ImportError:
        print("[ERROR] Pytest not found. Installing...")
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements-test.txt"])
        import pytest
        print(f"[OK] Pytest installed: {pytest.__version__}")
    
    print()
    
    # Default test arguments
    test_args = [
        "--tb=short",           # Short traceback format
        "--strict-markers",     # Strict marker validation
        "--strict-config",      # Strict config validation
        "-v",                   # Verbose output
    ]
    
    # Parse command line arguments
    if len(sys.argv) > 1:
        if "--coverage" in sys.argv:
            test_args.extend([
                "--cov=freecad.StructureTools",
                "--cov-report=term-missing",
                "--cov-report=html:htmlcov"
            ])
            print("[INFO] Running tests with coverage analysis...")
        
        if "--performance" in sys.argv:
            test_args.extend([
                "-m", "performance",
                "--benchmark-only",
                "--benchmark-sort=mean"
            ])
            print("[INFO] Running performance benchmarks...")
        
        if "--unit" in sys.argv:
            test_args.extend(["-m", "unit"])
            print("[INFO] Running unit tests only...")
        
        if "--integration" in sys.argv:
            test_args.extend(["-m", "integration"])
            print("[INFO] Running integration tests only...")
    else:
        # Default: run unit tests only
        test_args.extend(["-m", "unit"])
        print("[INFO] Running unit tests (default)...")
    
    print()
    
    # Add test directory
    test_args.append("tests/")
    
    # Run tests
    print("Starting test execution...")
    print("-" * 30)
    
    try:
        exit_code = pytest.main(test_args)
        
        print("-" * 30)
        if exit_code == 0:
            print("[SUCCESS] All tests passed!")
        else:
            print(f"[FAIL] Tests failed with exit code: {exit_code}")
        
        return exit_code
        
    except Exception as e:
        print(f"[ERROR] Error running tests: {e}")
        return 1


if __name__ == "__main__":
    # Usage examples
    if len(sys.argv) > 1 and sys.argv[1] in ["--help", "-h"]:
        print("StructureTools Test Runner")
        print()
        print("Usage:")
        print("  python run_tests.py                    # Run unit tests")
        print("  python run_tests.py --coverage         # Run with coverage")
        print("  python run_tests.py --performance      # Run benchmarks")
        print("  python run_tests.py --unit             # Run unit tests only")
        print("  python run_tests.py --integration      # Run integration tests")
        print("  python run_tests.py --help             # Show this help")
        print()
        print("Examples:")
        print("  python run_tests.py --unit --coverage  # Unit tests with coverage")
        print("  python run_tests.py --performance      # Performance benchmarks")
        sys.exit(0)
    
    exit_code = main()
    sys.exit(exit_code)