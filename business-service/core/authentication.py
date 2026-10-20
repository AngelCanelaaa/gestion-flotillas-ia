from rest_framework_simplejwt.authentication import JWTAuthentication

class MicroserviceJWTAuthentication(JWTAuthentication):
    def get_user(self, validated_token):
        class MicroserviceUser:
            def __init__(self, user_id):
                self.id = user_id
                self.is_authenticated = True
                self.is_active = True
                self.is_anonymous = False

        user_id = validated_token.get('user_id')
        return MicroserviceUser(user_id)