#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Comprehensive Test Runner for StructureTools
Runs all test suites for BIM Integration, Material Database, and Load Generator
"""

import os
import sys
import unittest
import time
from io import StringIO

def setup_test_environment():
    """Setup test environment and paths"""
    # Get the repository root
    current_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.abspath(os.path.join(current_dir, '..', '..'))
    
    # Add freecad directory to path
    freecad_dir = os.path.join(repo_root, 'freecad')
    if freecad_dir not in sys.path:
        sys.path.insert(0, freecad_dir)
    
    # Add tests directory to path
    tests_dir = os.path.join(repo_root, 'tests')
    if tests_dir not in sys.path:
        sys.path.insert(0, tests_dir)
    
    return repo_root

def run_test_suite(test_module_name, suite_name):
    """Run a specific test suite and return results"""
    print(f"\n{'='*60}")
    print(f"Running {suite_name} Tests")
    print(f"{'='*60}")
    
    try:
        # Import the test module
        test_module = __import__(f'integration.{test_module_name}', fromlist=[''])
        
        # Create test suite
        loader = unittest.TestLoader()
        suite = loader.loadTestsFromModule(test_module)
        
        # Capture output
        output_buffer = StringIO()
        runner = unittest.TextTestRunner(
            stream=output_buffer,
            verbosity=2,
            buffer=True
        )
        
        # Run tests
        start_time = time.time()
        result = runner.run(suite)
        end_time = time.time()
        
        # Get output
        test_output = output_buffer.getvalue()
        
        return {
            'name': suite_name,
            'result': result,
            'output': test_output,
            'duration': end_time - start_time,
            'success': result.wasSuccessful()
        }
        
    except ImportError as e:
        print(f"Failed to import {test_module_name}: {e}")
        return {
            'name': suite_name,
            'result': None,
            'output': f"Import error: {e}",
            'duration': 0,
            'success': False,
            'error': str(e)
        }
    except Exception as e:
        print(f"Unexpected error running {suite_name}: {e}")
        return {
            'name': suite_name,
            'result': None,
            'output': f"Unexpected error: {e}",
            'duration': 0,
            'success': False,
            'error': str(e)
        }

def print_test_summary(results):
    """Print comprehensive test summary"""
    print(f"\n{'='*80}")
    print("COMPREHENSIVE TEST SUMMARY")
    print(f"{'='*80}")
    
    total_tests = 0
    total_failures = 0
    total_errors = 0
    total_duration = 0
    successful_suites = 0
    
    for suite_result in results:
        print(f"\n{'-'*50}")
        print(f"Test Suite: {suite_result['name']}")
        print(f"{'-'*50}")
        
        if suite_result['success'] and suite_result['result']:
            result = suite_result['result']
            tests_run = result.testsRun
            failures = len(result.failures)
            errors = len(result.errors)
            
            total_tests += tests_run
            total_failures += failures
            total_errors += errors
            total_duration += suite_result['duration']
            successful_suites += 1
            
            success_rate = ((tests_run - failures - errors) / tests_run * 100) if tests_run > 0 else 0
            
            print(f"Status: {'✅ PASSED' if result.wasSuccessful() else '❌ FAILED'}")
            print(f"Tests Run: {tests_run}")
            print(f"Failures: {failures}")
            print(f"Errors: {errors}")
            print(f"Success Rate: {success_rate:.1f}%")
            print(f"Duration: {suite_result['duration']:.3f} seconds")
            
            # Print failure details
            if failures > 0:
                print(f"\nFailures in {suite_result['name']}:")
                for test, traceback in result.failures:
                    print(f"  - {test}")
                    print(f"    {traceback.split(chr(10))[-2] if chr(10) in traceback else traceback}")
            
            if errors > 0:
                print(f"\nErrors in {suite_result['name']}:")
                for test, traceback in result.errors:
                    print(f"  - {test}")
                    print(f"    {traceback.split(chr(10))[-2] if chr(10) in traceback else traceback}")
                    
        else:
            print(f"Status: ❌ FAILED TO RUN")
            if 'error' in suite_result:
                print(f"Error: {suite_result['error']}")
            print(f"Output: {suite_result['output']}")
    
    # Overall summary
    print(f"\n{'='*80}")
    print("OVERALL RESULTS")
    print(f"{'='*80}")
    print(f"Test Suites Run: {len(results)}")
    print(f"Successful Suites: {successful_suites}")
    print(f"Failed Suites: {len(results) - successful_suites}")
    print(f"Total Tests: {total_tests}")
    print(f"Total Failures: {total_failures}")
    print(f"Total Errors: {total_errors}")
    print(f"Overall Success Rate: {((total_tests - total_failures - total_errors) / total_tests * 100) if total_tests > 0 else 0:.1f}%")
    print(f"Total Duration: {total_duration:.3f} seconds")
    
    # Final verdict
    overall_success = successful_suites == len(results) and total_failures == 0 and total_errors == 0
    print(f"\nFinal Verdict: {'🎉 ALL TESTS PASSED!' if overall_success else '⚠️  SOME TESTS FAILED'}")
    
    return overall_success

def main():
    """Main test runner"""
    print("StructureTools Comprehensive Test Suite")
    print("Testing: BIM Integration, Material Database, Load Generator")
    
    # Setup environment
    repo_root = setup_test_environment()
    print(f"Repository root: {repo_root}")
    
    # Test suites to run
    test_suites = [
        ('test_bim_integration', 'BIM Integration'),
        ('test_material_database', 'Material Database'),
        ('test_load_generator', 'Load Generator')
    ]
    
    # Run all test suites
    results = []
    start_time = time.time()
    
    for test_module, suite_name in test_suites:
        result = run_test_suite(test_module, suite_name)
        results.append(result)
        
        # Print immediate feedback
        status = "✅ PASSED" if result['success'] else "❌ FAILED"
        print(f"{suite_name}: {status} ({result['duration']:.3f}s)")
    
    total_time = time.time() - start_time
    
    # Print comprehensive summary
    overall_success = print_test_summary(results)
    
    print(f"\nTotal execution time: {total_time:.3f} seconds")
    
    # Return appropriate exit code
    return 0 if overall_success else 1

if __name__ == '__main__':
    sys.exit(main())
