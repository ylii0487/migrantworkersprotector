import re


class Security:
    def is_xss(self, input):
        matches = re.search(r"\<.*\>.*\<.*\>", input)
        if matches:
            return True

        return False

    def is_sql_injection(self, input):
        """check sql injection

        Args:
            data (str): data is user input string
        """
        regexes = [
            r"(.*) [oO][rR] (.*)=(.*)",  # 105 or 1 = 1
            r"(.*)DROP TABLE(.*)",  #
            r"(.*)delete from(.*)",
            r"(.*)update(.*)set(.*)",
            r"(.*)insert(.*)values(.*)",
        ]
        for regex in regexes:
            matches = re.search(regex, input, re.IGNORECASE)
            if matches:
                print("{} match sql injection rule {}".format(input, regex))
                return True

        return False
