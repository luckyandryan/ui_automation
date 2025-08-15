import logging
import re


class AssertionHelper:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def assert_in(self, member, container):
        self.logger.info(f"[Asserting] '{member}' in '{container}'")

        assert member in container, f"Expected '{member}' to be in '{container}'"

    def assert_not_in(self, member, container):
        self.logger.info(f"[Asserting] '{member}' not in '{container}'")

        assert member not in container, f"Expected '{member}' to be not in '{container}'"

    def assert_equal(self, actual, expected):
        self.logger.info(f"[Asserting] {actual} == {expected}")

        assert actual == expected, f"Expected {expected}, but got {actual}"

    def assert_key_exists(self, key, dictionary):
        self.logger.info(f"[Asserting] key '{key}' exists in dictionary")

        assert key in dictionary, f"Expected key '{key}' not found in {dictionary}"

    def assert_startswith(self, actual_str, prefix):
        self.logger.info(f"[Asserting] '{actual_str}' starts with '{prefix}'")

        assert actual_str.startswith(
            prefix
        ), f"Expected '{actual_str}' to start with '{prefix}'"

    def assert_valid_email(self, email):
        self.logger.info(f"[Asserting] valid email format for: '{email}'")

        pattern = r"^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

        assert re.match(pattern, email), f"Invalid email format: {email}"

    def assert_data_type(self, data, expected_type):
        self.logger.info(f"[Asserting] data type of {data} is {expected_type}")

        assert isinstance(data, expected_type), f"Expected type {expected_type}, but got {type(data)}"