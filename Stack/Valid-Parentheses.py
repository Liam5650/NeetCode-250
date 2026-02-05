class Solution:
    def isValid(self, s: str) -> bool:

        # Use list as stack, matching left brackets to right brackets
        stack = []

        for val in s:
            if val in "[{(":
                stack.append(val)

            else:
                # Early exit
                if len(stack) == 0: return False


                if (
                    (val == "]" and stack[-1] != "[") or
                    (val == "}" and stack[-1] != "{") or
                    (val == ")" and stack[-1] != "(")
                    ):
                        return False

                stack.pop()
        
        return len(stack) == 0