#!/usr/bin/env python3
"""
Pull Request Title Checker

Validates pull request titles against a configurable regex pattern.
"""

import re
import sys
import os
from typing import Optional


def check_pr_title(
    title: str,
    pattern: str,
    expected_format: str,
    error_message: str = "Pull request title does not match required format",
    success_message: str = "Pull request title format is correct!"
) -> bool:
    """
    Check if the PR title matches the required pattern.
    
    Args:
        title: The PR title to validate
        pattern: Regex pattern to match against
        expected_format: Description of expected format for error messages
        error_message: Custom error message
        success_message: Custom success message
        
    Returns:
        True if title matches pattern, False otherwise
    """
    try:
        regex = re.compile(pattern)
        if regex.match(title):
            print(f"✅ {success_message}")
            return True
        else:
            error_msg = f"""❌ {error_message}.

Expected format: {expected_format}
Current title: {title}

Please update the title to follow the required pattern."""
            print(error_msg, file=sys.stderr)
            return False
    except re.error as e:
        print(f"❌ Invalid regex pattern: {e}", file=sys.stderr)
        return False


def main():
    """Main function to handle command line arguments and execute validation."""
    # Get inputs from environment variables (set by GitHub Actions)
    title = os.environ.get('PR_TITLE', '')
    pattern = os.environ.get('TITLE_PATTERN', '^FIX JIRA-\\d+: .+$')
    expected_format = os.environ.get('EXPECTED_FORMAT', 'FIX JIRA-123: Subject')
    error_message = os.environ.get('ERROR_MESSAGE', 'Pull request title does not match required format')
    success_message = os.environ.get('SUCCESS_MESSAGE', 'Pull request title format is correct!')
    
    if not title:
        print("❌ No PR title provided", file=sys.stderr)
        sys.exit(1)
    
    # Perform validation
    is_valid = check_pr_title(
        title=title,
        pattern=pattern,
        expected_format=expected_format,
        error_message=error_message,
        success_message=success_message
    )
    
    # Exit with appropriate code
    sys.exit(0 if is_valid else 1)


if __name__ == "__main__":
    main() 