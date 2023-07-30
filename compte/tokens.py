from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.translation import gettext_lazy as _

class TokenGenerator(PasswordResetTokenGenerator):  
    def _make_hash_value(self, user, timestamp):
        return str(user.pk) + str(timestamp) + str(user.is_active)

account_activation_token = TokenGenerator()
