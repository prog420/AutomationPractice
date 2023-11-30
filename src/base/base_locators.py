from typing import Tuple


class BasePageLocators:
    @staticmethod
    def format_locator(
        locator: Tuple[str, str], *args, **kwargs
    ) -> Tuple[str, str]:
        """
        Format **selector** part of the locator.

            Example:
        `format((By.XPATH, '//td[parent::tr/td/text()="{}"]'), 'Chrome')`

            Output:
        `(By.XPATH, '//td[parent::tr/td/text()="Chrome"]')`
        """
        by, value = locator
        formatted_value = value.format(*args, **kwargs)
        return by, formatted_value
