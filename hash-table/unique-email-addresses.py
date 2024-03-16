class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        valid = []
        for email in emails:
            if '@' not in email:
                continue
            else:
                local = email[:email.index('@')]
                domain = email[email.index('@'):]
                local = local.replace('.', '')
                if '+' in local:
                    local = local[:local.index('+')]
                if local+domain not in valid:
                    valid.append(local+domain)

        return len(valid)
        